# Work with an in-memory SQLite database again
import sqlite3
#first the connection
connection = sqlite3.connect(':memory:')
table = 'CREATE TABLE files (id integer primary key, path TEXT, bytes INTEGER)'
#second the cursor connection
cursor = connection.cursor()
#third the query saved in table variable
cursor.execute(table)
#fourth the commit
connection.commit()
from my_files import files

for metadata in files:
#special SQL syntax in SQLite to insert values from Python into the SQL query
    query = 'INSERT INTO files(path, bytes) VALUES(?, ?)'
    # the execute() method accepts a query and optionally a tuple with values 
    # corresponding to the question marks in VALUES
    cursor.execute(query, metadata)
    connection.commit()
    #finding files to end in .pdf

query = """
SELECT path,bytes FROM files 
    WHERE path LIKE '%pdf%'
"""
for i in cursor.execute(query):
    print(i)
