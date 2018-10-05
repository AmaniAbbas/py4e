** 1- What is the difference between a Python tuple and Python list?**

    1) Lists maintain the order of the items and tuples do not maintain order
    2) Tuples can be expanded after they are created and lists cannot
    3) Lists are indexed by integers and tuples are indexed by strings
    4) Lists are mutable and tuples are not mutable

_Answer is 4) Lists are mutable and tuples are not mutable_

** 2- Which of the following methods work both in Python lists and Python tuples?**

    1) reverse()
    2) sort()
    3) append()
    4) index()
    5) pop()

_Answer is 4) index()_

** 3- What will end up in the variable y after this code is executed?**
```Python
x , y = 3, 4
```
    1) 4
    2) A two item tuple
    3) 3
    4) A dictionary with the key 3 mapped to the value 4
    5) A two item list

_Answer is 1) 4_

** 4- In the following Python code, what will end up in the variable y?**
```Python
x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()
```
    1) A list of integers
    2) A tuple with three integers
    3) A list of strings
    4) A list of tuples

_Answer is 4) A list of tuples_

** 5- Which of the following tuples is greater than x in the following Python sequence?**
```Python
x = (5, 1, 3)
if ??? > x :
   ...
```
    1) (5, 0, 300)
    2) (6, 0, 0)
    3) (0, 1000, 2000)
    4) (4, 100, 200)

_Answer is 2) (6, 0, 0)_

** 6- What does the following Python code accomplish, assuming the c is a non-empty dictionary?**
```Python
tmp = list()
for k, v in c.items() :
    tmp.append( (v, k) )
```
    1) It computes the largest of all of the values in the dictionary
    2) It sorts the dictionary based on its key values
    3) It creates a list of tuples where each tuple is a value, key pair
    4) It computes the average of all of the values in the dictionary

_Answer is 3) It creates a list of tuples where each tuple is a value, key pair_

** 7- If the variable data is a Python list, how do we sort it in reverse order?**

    1) data.sort.reverse()
    2) data = sortrev(data)
    3) data = data.sort(-1)
    4) data.sort(reverse=True)

_Answer is 4) data.sort(reverse=True)_

** 8- Using the following tuple, how would you print 'Wed'? **
```Python
days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
```
    1) print(days.get(1,-1))
    2) print(days(2))
    3) print[days(2)]
    4) print(days[2])
    5) print(days{2})
    6) print(days[1])

_Answer is 4) print(days[2])_

** 9- In the following Python loop, why are there two iteration variables (k and v)?**
```Python
c = {'a':10, 'b':1, 'c':22}
for k, v in c.items() :
    ...
```
    1) Because the items() method in dictionaries returns a list of tuples
    2) Because the keys for the dictionary are strings
    3) Because for each item we want the previous and current key
    4) Because there are two items in the dictionary

_Answer is 1) Because the items() method in dictionaries returns a list of tuples_

** 10- Given that Python lists and Python tuples are quite similar - when might you prefer to use a tuple over a list?**

    1) For a list of items that want to use strings as key values instead of integers
    2) For a temporary variable that you will use and discard without modifying
    3) For a list of items that will be extended as new items are found
    4) For a list of items you intend to sort in place

_Answer is 2) For a temporary variable that you will use and discard without modifying_
