# Imports the script "argv" from the library "sys"
from sys import argv

# States the array of arguments 
script, filename = argv

# Creates a variable that is equal to the the file object value returned by running the open command with the filename stated in the argv argument.
txt = open(filename)

# Prints an fstring that includes the value of the filename argument passed through the command line
print(f"Here's your file {filename}")
# Prints the output of the read function - which returns the text content of the file stored in the variable "txt" as a string
print(txt.read())

# Prints a string
print("Type the filename again:")
# Creates a variable that is equal to a user input, which is intended to be a filename/path as stated in the previous line
file_again = input("> ")

# Creates a variable the is equal to the file object value returned by running the open command with the filename stored in the variable "file_again" as a string
txt_again = open(file_again)

# Prints the output of the read function - which returns the text content of the file stored in the variable txt_again as a string
print(txt_again.read())