import csv
import codecs
import pprint
import re
import xml.etree.cElementTree as ET
import cerberus
import schema
from collections import defaultdict


OSM_PATH = "sample.osm"
OSM_PATH_2 = 'sacramento.osm'

NODES_PATH = "nodes.csv"
NODE_TAGS_PATH = "nodes_tags.csv"
WAYS_PATH = "ways.csv"
WAY_NODES_PATH = "ways_nodes.csv"
WAY_TAGS_PATH = "ways_tags.csv"

LOWER_COLON = re.compile(r'^([a-z]|_)+:([a-z]|_)+')
PROBLEMCHARS = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


SCHEMA = schema.schema

# Make sure the fields order in the csvs matches the column order in the sql table schema
NODE_FIELDS = ['id', 'lat', 'lon', 'user', 'uid', 'version', 'changeset', 'timestamp']
NODE_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_FIELDS = ['id', 'user', 'uid', 'version', 'changeset', 'timestamp']
WAY_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_NODES_FIELDS = ['id', 'node_id', 'position']


def shape_element(element, node_attr_fields=NODE_FIELDS, way_attr_fields=WAY_FIELDS,
                  problem_chars=PROBLEMCHARS, default_tag_type='regular'):
    """Clean and shape node or way XML element to Python dict"""
    
    tags = []  # Handle secondary tags the same way for both node and way elements
    if element.tag == 'node':
        nodes = {}
        for item in NODE_FIELDS: #Under Node item insert everything into nodes
            nodes[item] = element.attrib[item] 
        for tag in element.iter("tag"):  #I ran tags in nodes independently.
            nodes_tags={} #Creating Names of the dictionary and 
            nodes_tags['id'] = element.attrib['id']
            
            if is_street_name(tag): 
                nodes_tags['value'] = update_name(tag.attrib['v'],mapping) #update the mapping for street names
            else: 
                nodes_tags['value'] = tag.attrib['v']

            if is_post_code(tag): 
                if 'CA' in tag.attrib['v']:
                    split = tag.attrib['v'].split(' ') #split where it has space 'CA _ 95 . . . '
                    nodes_tags['value'] = split[1] #give me only the zip code '95...'
                elif '-' in tag.attrib['v']: 
                    split = tag.attrib['v'].split('-') #split where it says '-'
                    nodes_tags['value'] = split[0] #give me the first part of the zip '95...'

            else: 
                nodes_tags['value'] = tag.attrib['v']

            m = LOWER_COLON.search(tag.attrib['k'])#We try to find out if the key is made with " : " format or only word.
            if not m:
                nodes_tags['type'] = 'regular'
                nodes_tags['key'] = tag.attrib['k']
            else:
                K_front = re.findall('(.+):', tag.attrib['k']) #before ":" appears.
                K_back = re.findall(':(.+)', tag.attrib['k'])
                nodes_tags['type'] = K_front[0]
                nodes_tags['key'] = K_back[0]
            tags.append(nodes_tags)          
        return {'node': nodes, 'node_tags': tags}
    elif element.tag == 'way':  # Logic is similary to 'node' tags and attributes
        ways = {}
        way_nodes = []
        count = 0
        for item in WAY_FIELDS: 
            ways[item] = element.attrib[item]
        for nd in element.iter('nd'): 
            way_node = {}
            way_node['id'] = ways['id']
            way_node['node_id'] = nd.attrib['ref']
            way_node['position'] = count # count the reference position within the 'nd' tags. 
            count += 1
            way_nodes.append(way_node)
    
        for tag in element.iter('tag'): 
            way_tags = {}
            way_tags['id'] = ways['id']
            if is_street_name(tag): 
                way_tags['value'] = update_name(tag.attrib['v'],mapping) #update the mapping for street names
            else: 
                way_tags['value'] = tag.attrib['v']
            
            if is_post_code(tag): 
                if 'CA' in tag.attrib['v']: #split where it has space 'CA _ 95 . . . '
                    split = tag.attrib['v'].split(' ') #give me only the zip code '95...'
                    way_tags['value'] = split[1]
                elif '-' in tag.attrib['v']: 
                    split = tag.attrib['v'].split('-')  #split where it says '-'
                    way_tags['value'] = split[0] #give me the first part of the zip '95...'
            else: 
                way_tags['value'] = tag.attrib['v']

            m = LOWER_COLON.search(tag.attrib['k'])
            if not m: 
                way_tags['type'] = 'regular'
                way_tags['key'] = tag.attrib['k']
            else: 
                K_front = re.findall('(.+):', tag.attrib['k'])
                K_back = re.findall(':(.+)', tag.attrib['k'])
                way_tags['type'] = K_front[0]
                way_tags['key'] = K_back[0]
                way_tags['type'] = way_tags['type'].replace('addr:street','addr')

            tags.append(way_tags)
        return {'way': ways, 'way_nodes': way_nodes, 'way_tags': tags}


# ================================================== #
#               Street Name Function                 #
# ================================================== #
expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons", 'Terrace', 'Ingoglia','Broadway','Circle','Way'] #place holder

# Create a mapping of desired stree names
mapping = { "St"  : "Street",
            "St." : "Street",
            'ST'  : 'Street',
            "Ave" : "Avenue",
            "Ave.": "Avenue",
            "Rd." : "Road",
            'Rd'  : 'Road',
            'Ct'  : 'Court',
            'Ct.' : 'Court', 
            'Blvd': 'Boulevard', 
            'Blvd.' : 'Boulevard',
            'Dr'  : 'Drive', 
            'Dr.' : 'Drive',
            'PlaceZ': 'Plaza',
            'Ln.' : 'Lane',
            'PKWY': 'Parkway'}


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types


def update_name(name, mapping):
    
        m = street_type_re.search(name)
        if m not in expected:
            if m.group() in mapping.keys(): 
                name = re.sub(m.group(), mapping[m.group()], name)
    
        return name


# ================================================== #
#               Postal Code Functions                #
# ================================================== #


def is_post_code(elem):  # check the 'addr:postcode' in osm file
    return (elem.attrib['k'] == 'addr:postcode')


# ================================================== #
#               Helper Functions                     #
# ================================================== #
def get_element(osm_file, tags=('node', 'way', 'relation')):
    """Yield element if it is the right type of tag"""

    context = ET.iterparse(osm_file, events=('start', 'end'))
    _, root = next(context)
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            yield elem
            root.clear()


def validate_element(element, validator, schema=SCHEMA):
    """Raise ValidationError if element does not match schema"""
    if validator.validate(element, schema) is not True:
        field, errors = next(validator.errors.iteritems())
        message_string = "\nElement of type '{0}' has the following errors:\n{1}"
        error_string = pprint.pformat(errors)
        
        raise Exception(message_string.format(field, error_string))


class UnicodeDictWriter(csv.DictWriter, object):
    """Extend csv.DictWriter to handle Unicode input"""

    def writerow(self, row):
        super(UnicodeDictWriter, self).writerow({
            k: (v.encode('utf-8') if isinstance(v, unicode) else v) for k, v in row.iteritems()
        })

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


# ================================================== #
#               Main Function                        #
# ================================================== #
def process_map(file_in, validate):
    """Iteratively process each XML element and write to csv(s)"""

    with codecs.open(NODES_PATH, 'w') as nodes_file, \
         codecs.open(NODE_TAGS_PATH, 'w') as nodes_tags_file, \
         codecs.open(WAYS_PATH, 'w') as ways_file, \
         codecs.open(WAY_NODES_PATH, 'w') as way_nodes_file, \
         codecs.open(WAY_TAGS_PATH, 'w') as way_tags_file:

        nodes_writer = UnicodeDictWriter(nodes_file, NODE_FIELDS)
        node_tags_writer = UnicodeDictWriter(nodes_tags_file, NODE_TAGS_FIELDS)
        ways_writer = UnicodeDictWriter(ways_file, WAY_FIELDS)
        way_nodes_writer = UnicodeDictWriter(way_nodes_file, WAY_NODES_FIELDS)
        way_tags_writer = UnicodeDictWriter(way_tags_file, WAY_TAGS_FIELDS)

        nodes_writer.writeheader()
        node_tags_writer.writeheader()
        ways_writer.writeheader()
        way_nodes_writer.writeheader()
        way_tags_writer.writeheader()

        validator = cerberus.Validator()

        for element in get_element(file_in, tags=('node', 'way')):
            el = shape_element(element)
            if el:
                if validate is True:
                    validate_element(el, validator)

                if element.tag == 'node':
                    nodes_writer.writerow(el['node'])
                    node_tags_writer.writerows(el['node_tags'])
                elif element.tag == 'way':
                    ways_writer.writerow(el['way'])
                    way_nodes_writer.writerows(el['way_nodes'])
                    way_tags_writer.writerows(el['way_tags'])


def test():
    st_types = audit(OSM_PATH)
    # pprint.pprint(dict(st_types))

    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            print name, "=>", better_name
if __name__ == '__main__':
    # Note: Validation is ~ 10X slower. For the project consider using a small
    # sample of the map when validating.
    process_map(OSM_PATH_2, validate=True)
    # test() 
