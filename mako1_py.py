import sqlite3
import urllib.parse
import mako.template as mk
conn = sqlite3.connect('places.sqlite')
c = conn.cursor()
req = '''SELECT url, title, datetime(last_visit_date/1000000, 'unixepoch', 'localtime')FROM moz_places ORDER BY last_visit_date DESC limit 13;'''



d = []
for i in c.execute(req).fetchall():
    o = urllib.parse.urlparse(i[0]).netloc
    if i not in d:
        d.append(i)
    time = i[2]
    url=i[0]
    title=i[1]
   
  
t = mk.Template(filename='templ1.htm')
f=open('new1.html','w', encoding='utf-8')
f.write(t.render(val=d))
f.close
f.flush
conn.commit()
