** 1. How do we model a many-to-many relationship between two database tables?**

    1) We use a BLOB column in both tables
    2) We use the ARRAY column type in both of the tables
    3) We add 10 foreign keys to each table with names like artict_id_1, artist_id2, etc.
    4) We add a table with two foreign keys

_Answer is 4) We add a table with two foreign keys_

** 2. In Python, what is a database "cursor" most like?**

     1) A Python dictionary
     2) A function
     3) A file handle
     4) A method within a class

_Answer is 3) A file handle_

** 3. What method do you call in an SQLIte cursor object in Python to run an SQL command?**

     1) send()
     2) run()
     3) socket()
     4) execute()

_Answer is 4) execute()_

** 4. In the following SQL,**
```Python
cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
```
** what is the purpose of the "?"?**

    1) It is a syntax error
    2) It is a placeholder for the contents of the "org" variable
    3) It allows more than one boolean operation in the WHERE clause
    4) It is a search wildcard

_Answer is 2) It is a placeholder for the contents of the "org" variable_

** 5. In the following Python code sequence (assuming cur is a SQLite cursor object),**
```Python
cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
row = cur.fetchone()
```
** what is the value in row if no rows match the WHERE clause?**

    1) None
    2) -1
    3) An empty dictionary
    4) An empty list

_Answer is 1) None_

** 6. What does the LIMIT clause in the following SQL accomplish?**
```SQL
SELECT org, count FROM Counts
   ORDER BY count DESC LIMIT 10
```

     1) It only retrieves the first 10 rows from the table
     2) It only sorts on the first 10 characters of the column
     3) It reverses the sort order if there are more than 10 rows
     4) It avoids reading data from any table other than Counts

_Answer is 1) It only retrieves the first 10 rows from the table_

** 7. What does the executescript() method in the Python SQLite cursor object do that the normal execute() method does not do?**

    1) It allows embeded Python to be executed
    2) It allows embedded JavaScript to be executed
    3) It allows database tables to be created
    4) It allows multiple SQL statements separated by semicolons

_Answer is 4) It allows multiple SQL statements separated by semicolons_

** 8. What is the purpose of "OR IGNORE" in the following SQL:**
```SQL
INSERT OR IGNORE INTO Course (title) VALUES ( ? )
```
     1) It makes sure that if a particular title is already in the table, there are no duplicate rows inserted
     2) It ignores errors in the SQL syntax for the statement
     3) It updates the created_at value if the title already exists in the table
     4) It ignores any foreign key constraint errors

_Answer is 1) It makes sure that if a particular title is already in the table, there are no duplicate rows inserted_

** 9. What do we generally avoid in a many-to-many junction table?**

    1) An AUTOINCREMENT primary key column
    2) A logical key
    3) Two foreign keys
    4) Data items specific to the many-to-many relationship

  _Answer is 3) Two foreign keys_
