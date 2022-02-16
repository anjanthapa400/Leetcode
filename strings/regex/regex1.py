# This section of code includes regex protion of practice for strings

import re

s = "I finally found a good approach to coding"

match = re.search(r'to',s)
print(match.start())
print(match.end())