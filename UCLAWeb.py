# (silverstein) file should have the .py suffix. Leaving it out makes it hard to understand what language its written in, and what its purpose is.

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
start_time = time.time() # move this below the sqlite3 import. All imports should be grouped together to improve readability.
import sqlite3

#1b) Create database
conn = sqlite3.connect("file.sqlite")
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Pages (
            url TEXT UNIQUE,visit INTEGER)''')
conn.close() # You still need to be connected later in your script. Don't close the connection, reuse it.


#2) Define initial URL, add into database with visit column value set to 0
url = "http://www.ucla.edu/"

conn = sqlite3.connect("file.sqlite") # do not need to reconnect
cur = conn.cursor()
cur.execute('INSERT OR IGNORE INTO Pages (url, visit) VALUES (?,?)', (url,0))
conn.commit()


#3 and #5) Need to read line from database where visit = 0, change visit to 1 then loop through step #4 until the program pulls and visits all ucla.edu links





#4)) Scrape all urls from html, add to database with visits set to 0
#4a) select only html sites
doc = urllib.request.urlopen(url) # Use more descriptive names for your variables. I should be able to infer its value by reading the name.
content_type = doc.info().get_content_type()

if content_type != 'text/html':
    pass

else: # the page is of "text/html" type
    html = doc.read().decode()

#4b) find the ucla.edu links and add into database with visits set to 0
    links = re.findall('href="(http://.*?ucla.edu/)"', html) # This regex will only look for http sites you're leaving out all https sites. A regex looking for just anything containing ucla.edu would be much more effective.

    #print only the first few
    # Why only print the first few?
    for link in links[0:5]:
        idx = link.find("#") # What is this line supposed to do?
        print(link)
        link = link[:idx]
        conn = sqlite3.connect("file.sqlite") # do not need to reconnect to DB conn variable from above is available in this scope.
        cur = conn.cursor()
        cur.execute('INSERT OR IGNORE INTO Pages (url, visit) VALUES (?,?)', (link,0))
        conn.commit()




#Print database
conn = sqlite3.connect("file.sqlite") # Do not need to reconnect
cur = conn.cursor()

cur.execute('SELECT * from Pages')
for row in cur:
    print(row)

cur.close()


#Timer output
print("My program took", time.time() - start_time, "seconds to run")
