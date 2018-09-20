** 1- What do we do to a Python statement that is immediately after an if
statement to indicate that the statement is to be executed only when the if
statement is true? **

    1) Start the statement with a "#" character
    2) Begin the statement with a curly brace {
    3) Underline all of the conditional code
    4) Indent the line below the if statement

_Answer is 4) Indent the line below the if statement _

** 2- Which of these operators is not a comparison / logical operator?**

     1) !=
     2) >
     3) =
     4) ==

_Answer is 3) =_

** 3- What is true about the following code segment: **
```Python
if  x == 5 :
    print('Is 5')
    print('Is Still 5')
    print('Third 5')
```

    1) Depending on the value of x, either all three of the print statements will execute or none of the statements will execute.
    2) The string 'Is 5' will always print out regardless of the value for x.
    3) The string 'Is 5' will never print out regardless of the value for x.
    4) Only two of the three print statements will print out if the value of x is less than zero.

_Answer is 1) Depending on the value of x, either all three of the print statements will execute or none of the statements will execute._

** 4- When you have multiple lines in an if block, how do you indicate the end of the if block? **

    1) You use a curly brace { after the last line of the if block
    2) You omit the semicolon ; on the last line of the if block
    3) You de-indent the next line past the if block to the same level of indent as the original if statement
    4) You put the colon : character on a line by itself to indicate we are done with the if block

_Answer is 3) You de-indent the next line past the if block to the same level of indent as the original if statement_


** 5- You look at the following text: **
```Python
if x == 6 :
    print('Is 6')
    print('Is Still 6')
    print('Third 6')
```
_It looks perfect but Python is giving you an 'Indentation Error' on the second print statement. What is the most likely reason?_

    1) In order to make humans feel inadequate, Python randomly emits 'Indentation Errors' on perfectly good code - after about an hour the error will just go away without any changes to your program
    2) You have mixed tabs and spaces in the file
    3) Python thinks 'Still' is a mis-spelled word in the string
    4) Python has reached its limit on the largest Python program that can be run

_Answer is 2) You have mixed tabs and spaces in the file_


** 6- What is the Python reserved word that we use in two-way if tests to indicate the block of code that is to be executed if the logical test is false? **

    1) else
    2) except
    3) iterate
    4) break

_Answer is 1) else_


** 7- What will the following code print out? **
```Python
x = 0
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')
```

    1) LARGE
       All done
    2) All done
    3) Small
       Medium
       LARGE
       All done
    4) Small
       All done

_Answer is 4) Small All done_


** 8- For the following code, **
```Python
if x < 2 :
    print('Below 2')
elif x >= 2 :
     print('Two or more')
else :
    print('Something else')
```
_What value of 'x' will cause 'Something else' to print out?_

    1) This code will never print 'Something else' regardless of the value for 'x'
    2) x = -22
    3) x = 2.0
    4) x = -2.0

_Answer is 1) This code will never print 'Something else' regardless of the value for 'x'_

** 9- In the following code (numbers added) - which will be the last line to execute successfully? **
```Python
(1)   astr = 'Hello Bob'
(2)   istr = int(astr)
(3)   print('First', istr)
(4)   astr = '123'
(5)   istr = int(astr)
(6)   print('Second', istr)
```
    1) 1
    2) 2
    3) 6
    4) 5

_Answer is 1) 1_


** 10- For the following code: **
```Python
astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1
```
_What will the value be for istr after this code executes?_

    1) 0
    2) -1
    3) The istr variable will not have a value
    4) It will be the 'Not a number' value (i.e. NaN)

_Answer is 2) -1_
