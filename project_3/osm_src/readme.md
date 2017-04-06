# OpenStreetMap Case Study 
:tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: 

### Map Area 

Sacramento, CA, United States 
* https://www.openstreetmap.org/way/33135846
* https://mapzen.com/data/metro-extracts/
* http://www.zipmap.net/California/Sacramento_County.htm

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

## Postal Codes
After I was able to clean the postal codes I began to look at the results within the county the zip were provided. Above I provided a link to the Sacramento county boundy map to see if it's consistent to the Open Street Map data provided. I still hadn't fixed the ``tiger`` gps ``tags`` for the ``zip_left`` and ``zip_right`` because that was a problem I didn't want to explore. I figured I would get enough data within the ``postcode`` key. Regardless, of fixing this I was able to aggregate postals codes and its results by adding an or statement to ``zip_left``. I'm not sure if this caused for over counting within the data set but here are the ruslts below:

```sql
SELECT tags.value, COUNT(*) as count 
FROM (SELECT * FROM nodes_tags 
      UNION ALL 
      SELECT * FROM ways_tags) tags
WHERE tags.key='postcode' or tags.key='zip_left'
GROUP BY tags.value
ORDER BY count DESC;
```


```sql
value|count
95691|15341
95605|5216
95828|768
95823|724
95831|648
95758|560
95822|527
95624|498
95821|474
95608|429
95826|416
95838|415
95820|385
95833|371
95818|369
95841|367
95864|358
95829|304
95660|293
95815|291
95842|277
95825|276
95819|264
95835|257
95817|242
95824|238
95834|195
95814|183
95816|183
95673|135
95827|89
95832|68
95843|49
95811|38
95626|14
95652|11
95742|7
95612|6
95837|6
96816|5
95830|4
95683|3
95820:95826|3
95628|2
95817:95820|2
95818:95819|2
2557|1
85834|1
95605:95691|1
95621|1
95670|1
95757|1
95820:95823|1
98584|1

``` 

As you can see above ``95691`` is the highest count which is JUSTTTTTTT outside the boundry line in ``West Sacramento``. I don't know if they redrew the boundry lines, but it seems interesting that this was included into the ``Open Street Map`` dataset. 

