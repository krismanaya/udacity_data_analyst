# OpenStreetMap Case Study 
:tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: 

### Map Area 

Sacramento, CA, United States 
* https://www.openstreetmap.org/way/33135846
* https://mapzen.com/data/metro-extracts/

Sacramento is where I spend most of my time, so I'm very interested to see what queries I may find regarding my city. 


## Problems Encountered in the Map 

Finding problems within the data and correcting them seemed like a streneous task. I created a sample ``.osm`` file and was able to find certain problems contained within the data that I could correct. However, I went ahead and skipped certain areas that needed correcting. 

* Overabbreviated street names ("_2108 Riverside Blvd._") 
* Inconsistent postal codes ("_95819-6055_","_CA 95834_")
* Incorrect postal codes "_85834_". Some of these were outside the county region like "_Charmichale,CA_". 
* "_Zip Left_" and "_Zip Right_" postal codes that wee included into the ``'k'`` tags for the ``Tiger`` GPS data. This data was devided into segmants 
* Words like ``sacramento`` were written like ``Sacramento`` and ``american`` like ``American``. 

```XML
		<tag k="tiger:reviewed" v="no" />
		<tag k="tiger:zip_left" v="95831" />
		<tag k="tiger:name_base" v="Joy River" />
		<tag k="tiger:name_type" v="Ct" />
		<tag k="tiger:separated" v="no" />
		<tag k="tiger:zip_right" v="95831" />
```

## Overabbreviated street names
Essentially, this was an exercise we had to perform using regular expression and grouping to essentially look for any problems like 
``St.`` or ``Blvd.`` and make each word consistent like ``Street`` or ``Boulevard``. There was problems with the ``update_name()`` function which was finding extra special words like ``Plaza`` and throwing a ``KeyError``, so I had to fix this probelm by asking the could to only choose groupings which we in my ``mapping`` dictionary. This solved the problem and was able to correct my street names: 

```python 

def update_name(name, mapping):
    
        m = street_type_re.search(name)
        if m not in expected:
            if m.group() in mapping.keys(): 
                name = re.sub(m.group(), mapping[m.group()], name)
    
        return name
```

I tacked my ``update_name()`` function onto the ``shape_element()`` function so everything would be written into the ``.csv`` file nicely. I called the ``is_street_nam()`` function which checks attributes addresses and then updated the mapping as shown below:

```python 

            if is_street_name(tag): 
                nodes_tags['value'] = update_name(tag.attrib['v'],mapping) 
            else: 
                nodes_tags['value'] = tag.attrib['v']
```

### Inconsistent postal codes
I found regular expression to be a challenge and couldn't quite get my handle on it for the postal codes. I spent about four hours trying to figure out how to fix them using the regular expression grouping technique. I failed, but with coding there is always another way. I figured I would use the split method and split the postal codes that have ``"CA"`` or ``"-"`` characters in them :thumbsup:. I placed my logic within the ``shape_element()`` function and I used the ``is_post_code()`` function too look for all post codes and if ``"CA"`` or ``"-"``  was inside the inconsistent zip, I split them up and pulled out what I needed. 

```python 

            if is_post_code(tag): 
                if 'CA' in tag.attrib['v']:
                    split = tag.attrib['v'].split(' ') 
                    nodes_tags['value'] = split[1] 
                elif '-' in tag.attrib['v']: 
                    split = tag.attrib['v'].split('-') 
                    nodes_tags['value'] = split[0] 
``` 


