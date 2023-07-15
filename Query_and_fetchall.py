import sqlite3

# connecting to the database
conn = sqlite3.connect('Abhishek.db')

# creating the cursur
c = conn.cursor()

# Query the database
c.execute("select * from customers")

# printing the output on the screen
"""
fetchone() is used to fetch the first element from the database
fetchmany(2) is used to fetch many data from the database here 2 is representing how many data we want for exapmle 3 or 4 
fetchall() will print all the data from the database 
"""
print(c.fetchall())
# commit our commands
conn.commit()
conn.close()