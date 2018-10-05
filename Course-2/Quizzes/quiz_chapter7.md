** 1- Given the architecture and terminology we introduced in Chapter 1,
where are files stored?**

    1) Motherboard
    2) Main Memory
    3) Machine Language
    4) Secondary memory

_Answer is 4) Secondary memory_

** 2- What is stored in a "file handle" that is returned from a successful open() call?**

    1) The handle is a connection to the file's data
    2) All the data from the file is read into memory and stored in the handle
    3) The handle contains the first 10 lines of a file
    4) The handle has a list of all of the files in a particular folder on the hard drive

_Answer is 1) The handle is a connection to the file's data_

** 3- What do we use the second parameter of the open() call to indicate?**

    1) What disk drive the file is stored on
    2) How large we expect the file to be
    3) The list of folders to be searched to find the file we want to open
    4) Whether we want to read data from the file or write data to the file

_Answer is 4) Whether we want to read data from the file or write data to the file_

** 4- What Python function would you use if you wanted to prompt the user for a file name to open?**

    1) input()
    2) read()
    3) file_input()
    4) cin

_Answer is 1) input()_

** 5- What is the purpose of the newline character in text files?**

    1) It enables random movement throughout the file
    2) It indicates the end of one line of text and the beginning of another line of text
    3) It allows us to open more than one files and read them in a synchronized manner
    4) It adds a new network connection to retrieve files from the network

_Answer is 2) It indicates the end of one line of text and the beginning of another line of text_

** 6- If we open a file as follows:**
```Python
xfile = open('mbox.txt')
```
_What statement would we use to read the file one line at a time?_

```Python
1) while (<xfile>) {

2) while ( getline (xfile,line) ) {

3) READ (xfile,*,END=10) line

4) for line in xfile:
```

_Answer is 4) for line in xfile:_


** 7- What is the purpose of the following Python code?**
```Python
fhand = open('mbox.txt')
x = 0
for line in fhand:
       x = x + 1
print(x)
```

    1) Convert the lines in mbox.txt to lower case
    2) Remove the leading and trailing spaces from each line in mbox.txt
    3) Reverse the order of the lines in mbox.txt
    4) Count the lines in the file 'mbox.txt'

_Answer is 4) Count the lines in the file 'mbox.txt'_

** 8- If you write a Python program to read a text file and you see extra blank lines in the output that are not present in the file input as shown below, what Python string function will likely solve the problem?**
```
From: stephen.marquard@uct.ac.za

From: louis@media.berkeley.edu

From: zqian@umich.edu

From: rjlowe@iupui.edu
```
    1) trim()
    2) split()
    3) ljust()
    4) rstrip()

_Answer is 2) 4) rstrip()_


** 9- The following code sequence fails with a traceback when the user enters a file that does not exist. How would you avoid the traceback and make it so you could print out your own error message when a bad file name was entered?**
```Python
fname = input('Enter the file name: ')
fhand = open(fname)
```
    1) setjmp / longjmp
    2) try / except
    3) try / catch / finally
    4) signal handlers

_Answer is 2) try / except_

** 10- What does the following Python code do?**
```Python
fhand = open('mbox-short.txt')
inp = fhand.read()
```
    1) Checks to see if the file exists and can be written
    2) Reads the entire file into the variable inp as a string
    3) Turns the text in the file into a graphic image like a PNG or JPG
    4) Prompts the user for a file name

_Answer is 2) Reads the entire file into the variable inp as a string_
