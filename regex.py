# RegEx=regular expression
# it is a pattern used to search text
# normal search-- looks for exact text
# RegEx-- looks for pattern eg: numbers,emails,words starting with capital let
import re # want to use regular expression
txt="The rain in Spain"
x=re.search("^The.*Spain$",txt)
if x:
    print("yes matched")
else:
    print("no match")  

"""
^ -- means string should START with
The-- exact word
.* -- , .- represents any character, *- represents zero or more occurrences
any characters any number of times
$--  must end with--"Spain".
"""


#findall() re.findall(pattern, string)-what we want to search, where we want to search
import re
txt="The rain in Spain"
x=re.findall("ai",txt)
print(x) # ['ai','ai'] appears due to python finds 2 matches
#findall() always returns a list

import re
txt="My numbers are 9876 and 1234"
x=re.findall("\d",txt)
print(x)

#search() -- searches the string for a match
import re
txt="The rain in Spain"
x=re.search("\s",txt) # \s means any wjite space character
print(x)

#split() -- split function splits a string when ever a match is found
import re
txt="The rain in Spain"
x=re.split("\s",txt)
print(x)

import re
txt="apple,banana,mango"
x=re.split(",",txt)
print(x)

# sub() -- is used to replace matched text with another value
# syntax -- re.sub(pattern, replacement, string)
import re
txt="The rain in Spain"
x=re.sub("\s","9",txt)  # \s means any white space character so it is replaced by 9
print(x)

import re
txt="I like apples"
x=re.sub("apples","mangoes",txt)
print(x)

#count Parameter -- can limit how many replacements happen
# re.sub(pattern, replacement, string, count)
import re
txt="The rain in Spain"
x=re.sub("\s","9",txt,2)
print(x)