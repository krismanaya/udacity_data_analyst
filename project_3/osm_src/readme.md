# OpenStreetMap Case Study 
:tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: 

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

```XML
		<tag k="tiger:reviewed" v="no" />
		<tag k="tiger:zip_left" v="95831" />
		<tag k="tiger:name_base" v="Joy River" />
		<tag k="tiger:name_type" v="Ct" />
		<tag k="tiger:separated" v="no" />
		<tag k="tiger:zip_right" v="95831" />
```

### Overabbreviated street names
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

I think tacked my ``update_name()`` function onto the ``shape_element()`` function so everything would be written into the ``.csv`` file nicely. I called the ``is_street_nam()`` function which checks attributes addresses and then updated the mapping as shown below:

```python 

            if is_street_name(tag): 
                nodes_tags['value'] = update_name(tag.attrib['v'],mapping) #update the mapping for street names
            else: 
                nodes_tags['value'] = tag.attrib['v']
```



