'''file handling is an important part of any web application
python has several functions for creating, reading, updating and deleting files
key function for working files in python -- open() function
open function has takes 2 parameters: filename, mode
r - read
a - append - opens a file for appending, creates the file if it does not exist
w - write opens a file for writing, create if not exist
x - create- creates the specified file, return an error if the file exists
'''
# syntax is file=open("filename", "mode")
#eg: file = open("data.txt", "r")