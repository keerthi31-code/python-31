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