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




 