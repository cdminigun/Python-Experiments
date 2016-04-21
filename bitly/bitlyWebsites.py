import pycurl
import re
from StringIO import StringIO

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
buffer = StringIO()
c = pycurl.Curl()
for char in letters:
    bitly = "bit.ly/" + char
    c.setopt(c.URL, bitly)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    body = buffer.getvalue()
for line in body.split('\n'):
    if re.search('<body><a href="', line):
        print line

print "done"


