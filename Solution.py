import re

file_name = "Development Set.txt"

f = open(file_name, "r")
article = str(f.read())

word_count = re.findall(r'\S+', article)
print('Number of words = ', len(word_count))