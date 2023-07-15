import sqlite3

#connecting to the database
conn = sqlite3.connect('Abhishek.db')

# creating a cursor
c = conn.cursor()
"""
        DATA TYPES
NULL MEANS IT IS NOT THEIR
INTEGER MEANS IT IS A NUMBER
REAL DECIMAL NUMBER LIKE 10.5 ETC
TEXT MEANS STRING VALUE
BLOB MEANS IMAGE, MP4 FILES

"""
# dropping the table if it exists
c.execute("""drop table if exists customers""")


# creating a table
c.execute("""
          
          create table customers(
          first_name text,
          last_name text,
          email varchar
) """)

c.execute("""
          insert into customers(first_name,last_name,email) values ('Abhishek','chauhan','abhi28c@gmail.com')
          """)

# insert many records into the table
many_data = [('Abhinav','chauhan','Abhinav21@gmail.com'),
              ('Aditya','chauhan','Aditya17aprl@gmail.com'),
              ('Naveen','kumar','naveenkumar28@gmail.com')]
c.executemany("insert into customers values(?,?,?)",many_data)
# commit our commands
conn.commit()
a1 = c.execute("select * from customers")
print(a1.fetchall())
# closing the connection
conn.close()