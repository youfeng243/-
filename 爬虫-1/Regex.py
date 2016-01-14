import re
import sys



Test_String = "123.125.528.256\nasd.asd.asd.asd\n123456789.2.2.2\n123.125.528.256"

Regex_Pattern = r"[^\n]{3}\.[^\n]{3}\.[^\n]{3}\.[^\n]{3}"

text = r"[^\n]{3}[.][^\n]{3}[.][^\n]{3}[.][^\n]{3}"

match = re.findall(Regex_Pattern, Test_String)

print match

print "Number of matches :", len(match)