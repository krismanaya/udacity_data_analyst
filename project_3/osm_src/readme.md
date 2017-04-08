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

I tacked my ``update_name()`` function onto the ``shape_element()`` function so everything would be written into the ``.csv`` file nicely. I called the ``is_street_name()`` function which checks attributes addresses and then updated the mapping as shown below:

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
ORDER BY count DESC
LIMIT 10;
```
Here are my top 10 zips:

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

``` 

As you can see above ``95691`` is the highest count which is JUSTTTTTTT outside the boundry line in ``West Sacramento``. I don't know if they redrew the boundry lines, but it seems interesting that this was included into the ``Open Street Map`` dataset. This presents a problem trying to analyze Sacramento county when a majority of zip codes are outside the boundry lines. It will not be a true representation of my fair city. I then thought maybe, there might be some other counties listed in this data set, so I look for key words like ``'%county'`` into ``sql`` and looked at the first two: 

```sql
SELECT tags.value, COUNT(*) as count
FROM (SELECT * FROM nodes_tags UNION ALL 
      SELECT * FROM ways_tags) tags 
WHERE tags.key LIKE '%county'
GROUP BY tags.value
ORDER BY count DESC
LIMIT 2;  
```
Top two counties: 

```sql 
Sacramento, CA|13957
Yolo, CA|750

```
As you can see a whole other county is included in the data set. This makes the data very problematic because it doesn't show a full representation of Sacramento County as a whole. 

## Data Overview and Additional Idea. 

For this section I'm going to give the reader basic statistics about the dataset, the SQL queries and additional explination.

### File sizes
```
sacramento.osm ......... 76.7 MB
sacramento.db .......... 50.9 MB
nodes.csv ............. 26.7 MB
nodes_tags.csv ........  4.4 MB
ways.csv ..............  2.1 MB
ways_tags.csv .........  7.7 MB
ways_nodes.cv .........  2.1 MB  
```  

### Number of nodes
```
sqlite> SELECT COUNT(*) FROM nodes;
```
318441

### Number of ways
```
sqlite> SELECT COUNT(*) FROM ways;
```
35541

### Number of unique users
```sql
sqlite> SELECT COUNT(DISTINCT(e.uid))          
FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways) e;
```
536

### Top 10 contributing users
```sql
sqlite> SELECT e.user, COUNT(*) as num
FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e
GROUP BY e.user
ORDER BY num DESC
LIMIT 10;
```

```sql
woodpeck_fixbot|91108
nmixter|56917
balcoath|26647
jraller|24285
tkmedia|18443
animeigo|14271
Eureka gold|9160
balrog-kun|6568
Charles_Smothers|6412
TheOutpost|6092 
```

### Number of unique :coffee::coffee:s
```sql 
SELECT COUNT(DISTINCT(e.id))     
FROM (SELECT id FROM nodes_tags WHERE value LIKE '%cafe' 
      UNION ALL SELECT id FROM ways_tags WHERE value LIKE '%cafe') e;
```
81 (Not accurate)

### Number of unique :beers::beers:s
```sql 
SELECT COUNT(DISTINCT(e.id))     
FROM (SELECT id FROM nodes_tags WHERE key == 'amenity' and (value == 'bar' or value == 'pub')
      UNION ALL SELECT id FROM ways_tags WHERE key == 'amenity' and (value == 'bar' or value == 'pub')) e;
```
24 (Not accurate)


## Additional Ideas 

### Statistics Contribution

 * Thigs go here 


 ### Additional Data Exploration 

 #### :beers::beers:s in Sacramento 
```sql 
SELECT nodes_tags.value as name
FROM nodes_tags 
     JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value='bar' or value == 'pub') i
     ON nodes_tags.id = i.id
WHERE nodes_tags.key = 'name'
GROUP BY nodes_tags.value
UNION ALL 
SELECT ways_tags.value as name
FROM ways_tags
     JOIN (SELECT DISTINCT(id) FROM ways_tags WHERE value='bar' or value == 'pub') i
     ON ways_tags.id = i.id
WHERE ways_tags.key = 'name'
GROUP BY ways_tags.value
ORDER BY name ASC;  
```
My :girl::heart_eyes: works at one of these bars. :raised_hands:
```sql 
Alley Katz
Bike Dog Brewing Co.
Bonn Lair
Burgers and Brew
Der Biergarten
Fox and Goose Public House
Fugu Lounge
Harry's Lounge
Joe Marty's
Kupros Craft House
Mix
New Helvetia Brewing
O'Mally's Irish Pub
Old Ironsides
Streets of London Pub
Tank House
The Golden Bear
The Grand Wine Bar
The O Club
The Trap
Torch Club
Uncle Vito's Midtown
University of Beer
XO Lounge

```

