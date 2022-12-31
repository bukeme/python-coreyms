from http.cookies import Morsel
import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
bat
pat
'''

sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'abc')
# pattern = re.compile(r'cba')
# pattern = re.compile(r'.') # needs to be escaped
# pattern = re.compile(r'\.')
# pattern = re.compile(r'coreyms\.com')
# pattern = re.compile(r'.') # matches every character except a new line
# pattern = re.compile(r'\d') # matches any digit between 0 and 9
# pattern = re.compile(r'\D') # matches non digits
# pattern = re.compile(r'\w') # matches a-z, A-Z, 0-9, _
# pattern = re.compile(r'\W') # matches non word characters
# pattern = re.compile(r'\s') # matches whitespaces (space, tab, newline)
# pattern = re.compile(r'\S') # matches non whitespace
# pattern = re.compile(r'\bHa') # \b matches search word with a word boundary (space, start of a new line, etc) before it
# pattern = re.compile(r'\BHa') # \b matches search word with no word boundary (space, start of a new line, etc) before it

# matches = pattern.finditer(text_to_search)

# pattern = re.compile(r'^Start') # ^ matches search word at the begining of a string
# pattern = re.compile(r'end$') # $ matches search word at the end of a string
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}') # [] matches only one character in the square bracket
# pattern = re.compile(r'[1-5]')
# pattern = re.compile(r'[a-zA-Z]')
# pattern = re.compile(r'[^a-zA-Z]') # matches everything not in the square bracket
# pattern = re.compile(r'[^b]at')
# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')


# Quantifiers:
# *           - 0 or More 
# +           - 1 or More 
# ?           - 0 or One 
# {3}         - Exact Number 
# {3, 4}      - Range of Numbers (Min, Max)



# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
# # matches = pattern.finditer(text_to_search)
# matches = pattern.findall(text_to_search) # matches groups. If there are no group, matches all matched characters

# for match in matches:
#     print(match)

# with open('file path') as f:
#     contents = f.read()
#     pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
#     matches = pattern.finditer(contents)

#     for match in matches:
#         print(match)



# pattern = re.compile(r'Start')
# pattern = re.compile(r'sentence')
# pattern = re.compile(r'start', re.IGNORECASE)
pattern = re.compile(r'start', re.I)

# match = pattern.match(sentence) # match only matches pattern at the begining of a string. sentence variable was assigned at the top of this file
match = pattern.search(sentence) # search through the string for match

print(match)