import re
import string

s = "Hello, my name; is 'nishant'"
s = re.sub(r'[^\w\s]','',s)
print(s)