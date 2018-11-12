from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url: http://py4e-data.dr-chuck.net/comments_135852.html
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

spans = soup('span')
numbers = []

for span in spans:
    numbers.append(int(span.string))

print (sum(numbers))
# Answer is 2565
