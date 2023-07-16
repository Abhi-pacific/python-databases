import sqlite3

# connect to the database
conn = sqlite3.connect('data.db')
# creating cursor
c =conn.cursor()
# executing commands
c.execute("""
drop table if exists data
""")
c.execute("""
create table data (name text,id integer)
""")

# inserting into table
var_data = [('Abhishek chauhan',2254),('Aditya chauhan',2255),('Naveen kumar',2256)]
c.executemany("insert into data values(?,?)",var_data)
d = c.execute('select * from data')
# loops to print specific data
for item in d:
    print(f' Your name {item[0]} and your id is {item[1]}')
conn.commit()
conn.close()