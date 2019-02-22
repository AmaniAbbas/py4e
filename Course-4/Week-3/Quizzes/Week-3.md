** 1. What is the primary added value of relational databases over flat files?**

    1) Ability to quickly convert data to HTML
    2) Ability to execute Python code within the file
    3) Ability to execute JavaScript in the file
    4) Ability to store data in a format that can be sent across a network
    5) Ability to scan large amounts of data quickly

_Answer is 5) Ability to scan large amounts of data quickly_

** 2. What is the purpose of a primary key?**

    1) To look up a row based on a string that comes from outside the program
    2) To look up a particular row in a table very quickly
    3) To point to a particular row in another table
    4) To track the number of duplicate values in another column

_Answer is 2) To look up a particular row in a table very quickly_

** 3. Which of the following is NOT a good rule to follow when developing a database model?**

    1) Never repeat string data in more than one table in a data model
    2) Model each "object" in the application as one or more tables
    3) Use a person's email address as their primary key
    4) Use integers as primary keys

_Answer is 3) Use a person's email address as their primary key_

** 4. If our user interface (i.e., like iTunes) has repeated strings on one column of the user interface, how should we model this properly in a database?**

    1) Encode the entire row as JSON and store it in a TEXT column in the database
    2) Put the string in the first row where it occurs and then put that row number in the column of all of the rest of the rows where the string occurs
    3) Put the string in the last row where it occurs and put the number of that row in the column of all of the rest of the rows where the string occurs
    4) Put the string in the first row where it occurs and then put NULL in all of the other rows
    5) Make a table that maps the strings in the column to numbers and then use those numbers in the column

_Answer is 5) Make a table that maps the strings in the column to numbers and then use those numbers in the column_

** 5. Which of the following is the label we give a column that the "outside world" uses to look up a particular row?**

    1) Foreign key
    2) Logical key
    3) Remote key
    4) Primary key
    5) Local key

_Answer is 2) Logical key_

** 6. What is the label we give to a column that is an integer and used to point to a row in a different table?**

     1) Primary key
     2) Remote key
     3) Local key
     4) Logical key
     5) Foreign key

_Answer is 5) Foreign key_

** 7. What SQLite keyword is added to primary keys in a CREATE TABLE statement to indicate that the database is to provide a value for the column when records are inserted?**

    1) INSERT_AUTO_PROVIDE
    2) AUTO_INCREMENT
    3) AUTOINCREMENT
    4) ASSERT_UNIQUE

_Answer is 3) AUTOINCREMENT_

** 8. What is the SQL keyword that reconnects rows that have foreign keys with the corresponding data in the table that the foreign key points to?**

    1) COUNT
    2) APPEND
    3) CONNECT
    4) JOIN
    5) CONSTRAINT

_Answer is 4) JOIN_

** 9. What happens when you JOIN two tables together without an ON clause?**

    1) Leaving out the ON clause when joining two tables in SQLite is a syntax error
    2) The number of rows you get is the number of rows in the first table times the number of rows in the second table
    3) You get no rows at all
    4) The rows of the left table are connected to the rows in the right table when their primary key matches
    5) You get all of the rows of the left table in the JOIN and NULLs in all of the columns of the right table

_Answer is 2) The number of rows you get is the number of rows in the first table times the number of rows in the second table_

** 10. When you are doing a SELECT with a JOIN across multiple tables with identical column names, how do you distinguish the column names?**

    1) tablename.columnname
    2) tablename->columnname
    3) tablename/columnname
    4) tablename['columnname']

_Answer is 1) tablename.columnname_
