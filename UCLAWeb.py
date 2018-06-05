


#To Do- Need to complete items #3 and #5
    #1) Import libraries, add timer, create SQL database (Done)
    
    #2) Define initial URL, add into database with visit column value set to 0 (Done)
    
    #*3) Read line from database, change value from 0 to 1. Loop:
    
        #4) Scrape all urls from html, add to database with visits set to 0 (Done)
        
        #*5) Repeat until no rows are set to 0
       

#1) Import libraries, add timer, create SQL database
    
#1a) Import libraries
import urllib.request
import re
import time
start_time = time.time()
import sqlite3

#1b) Create database
conn = sqlite3.connect("file.sqlite")
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Pages (
            url TEXT UNIQUE,visit INTEGER)''')
conn.close()


#2) Define initial URL, add into database with visit column value set to 0
url = "http://www.ucla.edu/"

conn = sqlite3.connect("file.sqlite")
cur = conn.cursor()
cur.execute('INSERT OR IGNORE INTO Pages (url, visit) VALUES (?,?)', (url,0))
conn.commit()


#3 and #5) Need to read line from database where visit = 0, change visit to 1 then loop through step #4 until the program pulls and visits all ucla.edu links





#4)) Scrape all urls from html, add to database with visits set to 0
#4a) select only html sites
doc = urllib.request.urlopen(url)
content_type = doc.info().get_content_type()

if content_type != 'text/html':
    pass

else: # the page is of "text/html" type
    html = doc.read().decode()

#4b) find the ucla.edu links and add into database with visits set to 0
    links = re.findall('href="(http://.*?ucla.edu/)"', html)
    #print only the first few
    for link in links[0:5]: 
        idx = link.find("#")
        link = link[:idx]
        conn = sqlite3.connect("file.sqlite")
        cur = conn.cursor()
        cur.execute('INSERT OR IGNORE INTO Pages (url, visit) VALUES (?,?)', (link,0))
        conn.commit()




#Print database
conn = sqlite3.connect("file.sqlite")
cur = conn.cursor()

cur.execute('SELECT * from Pages')
for row in cur:
    print(row)

cur.close()
    

#Timer output
print("My program took", time.time() - start_time, "seconds to run")
