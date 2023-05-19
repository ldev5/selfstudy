# Imports the script argv from the sys library
from sys import argv

# States the array of arguments that will be processed by argv
script, input_file = argv

# Creates a function "print_all" that accepts the argument "f"
def print_all(f):
    # Prints the read value returned by the file specified in argument f
    print(f.read())

# Creates a function "rewind" that accepts the argument "f"
def rewind(f):
    # Changes the read/write location of the file specified in argument f to the beginning
    f.seek(0)

# Creates a function "print_a_line" that accepts two arguments
def print_a_line(line_count, f):
    # Prints an argument and then prints the content of the file object specified in the "f" argument
    print(line_count, f.readline())

# Creates a variable with the returned value of a file object
current_file = open(input_file)

# Prints a string with a break at the end
print("First let's print the whole file:\n")

# Uses the function "print_all" with a variable as the argument
print_all(current_file)

# Prints a string
print("Now let's rewind, kind of like a tape.")

# Places the read/write location back to the beginning of the file stored in the variable current_file
rewind(current_file)
# Prints a string
print("Let's print three lines:")

# Creates a variable with a numerical value
current_line = 1

# Runs the function print_a_line with two variables for the arguments
print_a_line(current_line, current_file)

# Adds the number one to the current value of current_line
current_line = current_line + 1
# Runs the function print_a_line with two variables for the arguments
print_a_line(current_line, current_file)

# Adds the number one to the current value of current_line
current_line = current_line + 1
# Runs the function print_a_line with two variables for the arguments
print_a_line(current_line, current_file)
