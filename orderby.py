import sqlite3
# connecting to the database
conn = sqlite3.connect('data.db')
# creating cursor
c = conn.cursor()
# executing command of order by
items = c.execute("select * from data where rowid = 3")
print(items.fetchall())
conn.commit()
conn.close()
"""
we can also use (like,order by and =,>,<)
"""