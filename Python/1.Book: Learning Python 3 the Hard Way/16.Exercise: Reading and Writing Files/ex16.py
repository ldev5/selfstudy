# Imports the script "argv" from the library "sys"
from sys import argv

# States the array of arguments argv will receive
script, filename = argv

# Prints an f string that includes the value of the variable "filename"
print(f"We're going to erase {filename}.")
# Prints a string
print("If you don't want that, hit CTRL-C (^C).")
# Prints a string
print("If you do want that, hit RETURN")

# Calls the input function and prints "?"
input("?")

# Prints a string
print("Opening the file...")
# Creates the variable "target" that returns the value of the file object "filename" through the read function, followed by the letter "w"
target = open(filename, 'w')

# Prints a string
print("Truncating the file. Goodbye!")
# Calls the function truncate, wiping the file referred to in the variable "target"
target.truncate()

# Prints a string
print("Now I'm going to ask you for three lines.")

# Creates three similar variables that store user inputs 
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Print a string
print("I'm going to write these to the file.")

# Writes the value returned by each variable line* to three separate lines 
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Prints a string
print("And finally, we close it.")
# Saves the file referred to in the variable "target" 
target.close()