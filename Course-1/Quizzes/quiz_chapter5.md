** 1- What is wrong with this Python loop:**
```Python
n = 5
while n > 0 :
    print(n)
print('All done')
```
    1) This loop will run forever
    2) The print('All done') statement should be indented four spaces
    3) There should be no colon on the while statement
    4) while is not a Python reserved word

_Answer is 1) This loop will run forever_

** 2- What does the break statement do?**

    1) Jumps to the "top" of the loop and starts the next iteration
    2) Exits the currently executing loop
    3) Exits the program
    4) Resets the iteration variable to its initial value

_Answer is 2) Exits the currently executing loop_

** 3- What does the continue statement do? **

    1) Resets the iteration variable to its initial value
    2) Jumps to the "top" of the loop and starts the next iteration
    3) Exits the currently executing loop
    4) Exits the program

_Answer is 2) Jumps to the "top" of the loop and starts the next iteration_

** 4- What does the following Python program print out?**
```Python
tot = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)
```
    1) 10
    2) 0
    3) 15
    4) 5

_Answer is 4) 5_

** 5- What is the iteration variable in the following Python code:**
```Python
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
     print('Happy New Year:',  friend)
print('Done!')
```
    1) friend
    2) Glenn
    3) Sally
    4) friends

_Answer is 1) friend_

** 6- What is a good description of the following bit of Python code?**
```Python
zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)
```
    1) Find the smallest item in a list
    2) Count all of the elements in a list
    3) Find the largest item in a list
    4) Sum all the elements of a list

_Answer is 4) Sum all the elements of a list_

** 7- What will the following code print out?**
```Python
smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)
```
_Hint: This is a trick question and most would say this code has a bug - so read carefully_

    1) -1
    2) 74
    3) 42
    4) 3

_Answer is 1) -1_

** 8- What is a good statement to describe the is operator as used in the following if statement:**
```Python
if smallest is None :
     smallest = value
```
    1) matches both type and value
    2) Looks up 'None' in the smallest variable if it is a string
    3) The if statement is a syntax error
    4) Is true if the smallest variable has a value of -1

_Answer is 1) matches both type and value_

** 9- Which reserved word indicates the start of an "indefinite" loop in Python?**

     1) def
     2) while
     3) indef
     4) break
     5) for

_Answer is 2) while_

** 10- How many times will the body of the following loop be executed?**
```Python
n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')
```
    1) 0
    2) This is an infinite loop
    3) 5
    4) 1

_Answer is 1) 0_
