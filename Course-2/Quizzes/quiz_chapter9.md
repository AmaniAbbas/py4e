** 1- How are Python dictionaries different from Python lists?**

    1) Python lists maintain order and dictionaries do not maintain order
    2) Python lists can store strings and dictionaries can only store words
    3) Python lists store multiple values and dictionaries store a single value
    4) Python dictionaries are a collection and lists are not a collection

_Answer is 1) Python lists maintain order and dictionaries do not maintain order_

** 2- What is a term commonly used to describe the Python dictionary feature in other programming languages?**

    1) Closures
    2) Sequences
    3) Lambdas
    4) Associative arrays

_Answer is 4) Associative arrays_

** 3- What would the following Python code print out?**
```Python
stuff = dict()
print(stuff['candy'])
```
    1) 0
    2) -1
    3) The program would fail with a traceback
    4) candy

_Answer is 3) The program would fail with a traceback_

** 4- What would the following Python code print out?**
```Python
stuff = dict()
print(stuff.get('candy',-1))
```
    1) -1
    2) 0
    3) 'candy'
    4) The program would fail with a traceback

_Answer is 1) -1_

** 5- (T/F) When you add items to a dictionary they remain in the order in which you added them.**

    1) False
    2) True

_Answer is 1) False_

** 6- What is a common use of Python dictionaries in a program?**

    1) Sorting a list of names into alphabetical order
    2) Splitting a line of input into words using a space as a delimiter
    3) Computing an average of a set of numbers
    4) Building a histogram counting the occurrences of various strings in a file

_Answer is 4) Building a histogram counting the occurrences of various strings in a file_

** 7- Which of the following lines of Python is equivalent to the following sequence of statements assuming that counts is a dictionary?**
```Python
if key in counts:
    counts[key] = counts[key] + 1
else:
    counts[key] = 1
```
    1) counts[key] = counts.get(key,-1) + 1
    2) counts[key] = (counts[key] * 1) + 1
    3) counts[key] = counts.get(key,0) + 1
    4) counts[key] = (key in counts) + 1
    5) counts[key] = key + 1

_Answer is 3) counts[key] = counts.get(key,0) + 1_

** 8- In the following Python, what does the for loop iterate through?**
```Python
x = dict()
...
for y in x :
     ...
```
    1) It loops through the values in the dictionary
    2) It loops through the integers in the range from zero through the length of the dictionary
    3) It loops through the keys in the dictionary
    4) It loops through all of the dictionaries in the program

_Answer is 3) It loops through the keys in the dictionary_

** 9- Which method in a dictionary object gives you a list of the values in the dictionary?**

    1) keys()
    2) items()
    3) all()
    4) each()
    5) values()

_Answer is 5) values()_

** 10- What is the purpose of the second parameter of the get() method for Python dictionaries?**

    1) An alternate key to use if the first key cannot be found
    2) The value to retrieve
    3) The key to retrieve
    4) To provide a default value if the key is not found

_Answer is 4) To provide a default value if the key is not found_
