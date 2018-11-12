** 1. Which of the following Python data structures is most similar to the value returned in this line of Python:**
```Python
x = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
```
    1) file handle
    2) list
    3) regular expression
    4) dictionary
    5) socket

_Answer is 1) file handle_

** 2. In this Python code, which line actually reads the data?**
```Python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
```

    1) mysock.recv()
    2) socket.socket()
    3) mysock.close()
    4) mysock.connect()
    5) mysock.send()

_Answer is 1) mysock.recv()_

** 3. Which of the following regular expressions would extract the URL from this line of HTML:**
```Python
<p>Please click <a href="http://www.dr-chuck.com">here</a></p>
```
    1) href="(.+)"
    2) href=".+"
    3) http://.*
    4) <.*>

_Answer is1) href="(.+)"_

** 4. In this Python code, which line is most like the open() call to read a file: **
```Python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
```
     1) mysock.connect()
     2) import socket
     3) mysock.recv()
     4) mysock.send()
     5) socket.socket()

_Answer is 1) mysock.connect()_


** 5. Which HTTP header tells the browser the kind of document that is being returned?**

    1) HTML-Document:
    2) Content-Type:
    3) Document-Type:
    4) ETag:
    5) Metadata:

_Answer is 2) Content-Type:_

** 6. What should you check before scraping a web site?**

    1) That the web site returns HTML for all pages
    2) That the web site allows scraping
    3) That the web site only has links within the same site
    4) That the web site supports the HTTP GET command

_Answer is 2) That the web site allows scraping_

** 7. What is the purpose of the BeautifulSoup Python library?**

    1) It builds word clouds from web pages
    2) It allows a web site to choose an attractive skin
    3) It repairs and parses HTML to make it easier for a program to understand
    4) It optimizes files that are retrieved many times
    5) It animates web operations to make them more attractive

_Answer is 3) It repairs and parses HTML to make it easier for a program to understand_

** 8. What ends up in the "x" variable in the following code:**
```Python
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
x = soup('a')
```
    1) A list of all the anchor tags (<a..) in the HTML from the URL
    2) True if there were any anchor tags in the HTML from the URL
    3) All of the externally linked CSS files in the HTML from the URL
    4) All of the paragraphs of the HTML from the URL

_Answer is 1) A list of all the anchor tags (<a..) in the HTML from the URL_

** 9. What is the most common Unicode encoding when moving data between systems?**

     1) UTF-128
     2) UTF-8
     3) UTF-32
     4) UTF-64
     5) UTF-16

_Answer is 2) UTF-8_

** 10. What is the ASCII character that is associated with the decimal value 42?**

    1) !
    2) *
    3) ^
    4) /
    5) +

_Answer is 2) *_

** 11. What word does the following sequence of numbers represent in ASCII:
108, 105, 110, 101 **

    1) func
    2) tree
    3) lost
    4) line
    5) ping

_Answer is 4) line_

** 12. How are strings stored internally in Python 3?**

    1) EBCDIC
    2) UTF-8
    3) Unicode
    4) ASCII
    5) Byte Code

_Answer is 3) Unicode_

** 13. When reading data across the network (i.e. from a URL) in Python 3, what method must be used to convert it to the internal format used by strings? **

    1) trim()
    2) find()
    3) encode()
    4) decode()
    5) upper()

_Answer is 4) decode()_
