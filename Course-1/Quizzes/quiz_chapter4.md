** 1- Which Python keyword indicates the start of a function definition?**

     1) return
     2) continue
     3) rad
     4) def

_Answer is 4) def_

** 2-In Python, how do you indicate the end of the block of code that makes up the function? **

    1) You add a line that has at least 10 dashes
    2) You de-indent a line of code to the same indent level as the def keyword
    3) You put the "END" keyword in column 7 of the line which is to be the last line of the function
    4) You put the colon character (:) in the first column of a line

_Answer is 2)You de-indent a line of code to the same indent level as the def keyword_

** 3- In Python what is the input() feature best described as? **

    1) A reserved word
    2) A built-in function
    3) A data structure that can hold multiple values using strings as keys
    4) A user-defined function

_Answer is 2) A built-in function_

** 4- What does the following code print out?**
```Python
def thing():
    print('Hello')

print('There')
```

    1) Hello
       There
    2) Hello
    3) There
    4) thing
       Hello
       There

_Answer is 3) There_

** 5- In the following Python code, which of the following is an "argument" to a function?**

```Python
x = 'banana'
y = max(x)
z = y * 2
```
    1) x
    2) max
    3) 'banana'
    4) y

_Answer is 1) x_

** 6- What will the following Python code print out?**
```Python
def func(x) :
    print(x)

func(10)
func(20)
```
    1) 10
       20
    2) x
       10
       x
       20
    3) func
       func
    4) x
       20

_Answer is 1) 10 20_

** 7- Which line of the following Python program will never execute?**
```Python
def stuff():
    print('Hello')
    return
    print('World')

stuff()
```
    1) print ('World')
    2) print('Hello')
    3) stuff()
    4) def stuff():
    5) return

_Answer is 1) print ('World')_

** 8- What will the following Python program print out?**
```Python
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('fr'),'Michael')
```
    1) Bonjour Michael
    2) def
       Hola
       Bonjour
       Hello
       Michael
    3) Hola Michael
    4) Hola
       Bonjour
       Hello
       Michael

_Answer is 1) Bonjour Michael_

** 9- What does the following Python code print out? (Note that this is a bit of a trick question and the code has what many would consider to be a flaw/bug - so read carefully). **
```Python
def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)
```
    1) 2
    2) 7
    3) 9
    4) 14

_Answer is 1) 2_

** 10- What is the most important benefit of writing your own functions? **

    1) Avoiding writing the same non-trivial code more than once in your program
    2) Following the rule that whenever a program is more than 10 lines you must use a function
    3) Following the rule that no function can have more than 10 statements in it
    4) To avoid having more than 10 lines of sequential code without an indent or de-indent

_Answer is 1) Avoiding writing the same non-trivial code more than once in your program_
