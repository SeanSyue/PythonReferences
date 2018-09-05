# https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-Regular-Expressions
import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

sentence = 'Start a sentence and then bring it to an end'

# match() method only finds whether a matched pattern at the beginning of the target.
print(re.compile(r'Start').match(sentence))

# To find out a certain pattern throughout the whole target, use search() method:
print(re.compile(r'a').search(sentence))

# To ignore the differences between lower and upper cases, use flag re.IGNORECASE, or re.I:
print(re.compile(r'start', re.I).search(sentence))

pattern = re.compile(r'M(r|s|rs)\.?\s\[a-zA-Z]+')

# findall() method only return the result of the first group
print(pattern.findall(text_to_search))

# finditer() method returns a iterator object.
matches = pattern.finditer(text_to_search)
print(matches)

# To display exact every elements returned by finditer() method, use a for loop:
for match in matches:
    print(match)

# The for loop return the location of matched pattern in the target.
# Use a string splitting technique to check it.
print(text_to_search[1:4])

# Also, parsing contents from other files is possible, simply by using:
with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# To search by grouping:
url_patterns = re.compile(r'https?://(www.)?(\w+)(\.\w+)')
url_matches = url_patterns.finditer(urls)
for url_match in url_matches:
    print(url_match.group(0))  # group(0) refers to the entire match.
    print(url_match.group(2))

# Use sub() method:
subbed_url = url_patterns.sub(r'\2\3', urls)
print(subbed_url)
