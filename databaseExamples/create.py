
import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

# Fetch table or create it

# Create table
c.execute('''
	CREATE TABLE Students (
		ID int,
		LastName varchar(255),
		FirstName varchar(255),
		Address varchar(255),
		Gender int
	);''')

# Insert a Students
c.execute('''INSERT INTO Students VALUES (10, "Anderson", "Alice", "101 Post Street", 0);''')

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

