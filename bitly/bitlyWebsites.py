import pycurl
import re
from StringIO import StringIO

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
buffer = StringIO()
i = 0
c = pycurl.Curl()
for char in letters:
    bitly = "bit.ly/" + char
    c.setopt(c.URL, bitly)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    body = buffer.getvalue()
for line in body.split('\n'):
    if re.search('<body><a href="', line):
        if re.search('https://bitly.com/a/warning', line):
           i += 1
        print line
print "The total number of warning sites is: ", i
print "done"


