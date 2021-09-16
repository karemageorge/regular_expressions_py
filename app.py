import re
# Raw string - is a string prefixed with an ‘r’ - it tells python not to handle backslashes in any special way.
# example of raw string implementation. 
# First we show what happens without the prefix r

print('\tTab')  
print(r'\tTab') # note the difference in one there is a tab the other there isnt

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa
Metacharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
345*456*4567
800-567-9800
900-456-3456

Mr . Schafer
Mr Smith
'''
pattern = re.compile(r'abc') 
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match) # prints out <re.Match object; span=(1, 4), match='abc'>

    # the span is the begining and the end index(range) of the match

print(text_to_search[1:4])

# slicing - extracting certain elements in our lists or strings.

# metacharacters (Need to be escaped):
# . ^ $ * + ? { } [ ] | \ ( ) example below:
pattern = re.compile(r'.') 
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)    # prints out almost all the characters and numbers thats why we escape


pattern = re.compile(r'coreyms\.com') # escape using the '\'
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)  


# . 	- matches any character except new line
# \d 	- Digit (0-9)
# \D 	- Not a digit (0-9)
# \w	- Word Character (a-z, A-Z, 0-9, _ )
# \W 	- not a word character
# \s 	- whitespace (space, tab, newline)
# \S 	- Not whitespace (space, tab, newline)
# \b 	- word boundary
# \B 	- Not a word Boundary
# ^ 	- Beginning of a string
# $ 	- end of a string

# []	- matches the characters in brackets e.g [.-]
# [^ ]	- matches characters not in brackets

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') 
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match) 


pattern = re.compile(r'[89]00[.-]\d\d\d[.-]\d\d\d\d') # use of character sets [.-] 
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match) 

pattern = re.compile(r'[a-zA-Z]') # use of character sets [.-] 
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match) 


#   |     - EITHER OR
#   ()     - Group

# Quantifiers:
# * - 0 or More
# + - 1 or more 
# ? - 0 or One 
# {3} - exact number
# {3,4} - range of numbers(minimum, maximum)

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(3)) 


pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
subbed_urls = pattern.sub(r'\2\3', urls) # replace those urls with the groups 2 and 3
print(subbed_urls)