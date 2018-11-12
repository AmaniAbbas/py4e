** 1- Which of the following best describes "Regular Expressions"?**

    1) A small programming language unto itself
    2) A way to solve Algebra formulas for the unknown value
    3) The way Python handles and recovers from errors that would otherwise cause a traceback
    4) A way to calculate mathematical values paying attention to operator precedence

_Answer is 1) A small programming language unto itself_

** 2- Which of the following is the way we match the "start of a line" in a regular expression?**

    1) ^
    2) str.startswith()
    3) \linestart
    4) String.startsWith()
    5) variable[0:1]

_Answer is 1) ^_

** 3- What would the following mean in a regular expression? [a-z0-9]**

    1) Match any number of lowercase letters followed by any number of digits
    2) Match a lowercase letter or a digit
    3) Match an entire line as long as it is lowercase letters or digits
    4) Match any text that is surrounded by square braces
    5) Match anything but a lowercase letter or digit

_Answer is 2) Match a lowercase letter or a digit_

** 4- What is the type of the return value of the re.findall() method?

    1) A list of strings
    2) An integer
    3) A boolean
    4) A single character
    5) A string

_Answer is 1) A list of strings_

** 5- What is the "wild card" character in a regular expression (i.e., the character that matches any character)?**

    1) .
    2) *
    3) $
    4) ^
    5) +
    6) ?

_Answer is 1) ._

** 6- What is the difference between the "+" and "*" character in regular expressions?**

    1) The "+" matches at least one character and the "*" matches zero or more characters
    2) The "+" matches upper case characters and the "*" matches lowercase characters
    3) The "+" matches the beginning of a line and the "*" matches the end of a line
    4) The "+" matches the actual plus character and the "*" matches any character
    5) The "+" indicates "start of extraction" and the "*" indicates the "end of extraction"

_Answer is 1) The "+" matches at least one character and the "*" matches zero or more characters_

** 7- What does the "[0-9]+" match in a regular expression?**

    1) Several digits followed by a plus sign
    2) Any number of digits at the beginning of a line
    3) Any mathematical expression
    4) Zero or more digits
    5) One or more digits

_Answer is 5) One or more digits_

** 8- What does the following Python sequence print out?**
```Python
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
```
    1) :
    2) ^F.+:
    4) ['From:']
    5) From:
    6) ['From: Using the :']

_Answer is 6) ['From: Using the :']_

** 9- What character do you add to the "+" or "*" to indicate that the match is to be done in a non-greedy manner?**

    1) \g
    2) **
    3) ++
    4) $
    5) ?
    6) ^

_Answer is 5) ?_

** 10- Given the following line of text:**
```Python
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
```
**What would the regular expression '\S+?@\S+' match?**

    1) d@u
    2) \@\
    3) From
    4) marquard@uct
    5) stephen.marquard@uct.ac.za

_Answer is 5) stephen.marquard@uct.ac.za_
