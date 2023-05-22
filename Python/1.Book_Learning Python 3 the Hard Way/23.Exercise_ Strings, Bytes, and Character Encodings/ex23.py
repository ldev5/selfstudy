# Imports the library "sys"
import sys
# States the array of arguments that will be processed by the argv function derived from the sys library. 
# One being the actual python script file location, the second is the type of encoding to add and the third is 
script, input_encoding, error = sys.argv

# Creates a function "main" with three parameters.
def main(language_file, encoding, errors):
    # Creates a variable "line" that is equal to the value of a line read from the currently open file, as specified in the parameter
    line = language_file.readline()
    
    # Runs the nested code if the variable line returns a value
    if line:
        # Calls the function print_line with three parameters
        print_line(line, encoding, errors)
        # Runs the function main again
        return main(language_file, encoding, errors)

# Creates a function "print_line" with three parameters
def print_line(line, encoding, errors):
    # Creates a variable from the parameter line that is equal to the string less any spaces at either end
    next_lang = line.strip()
    # Encodes the string with the encoding specified in the encoding parameter and the error method
    raw_bytes = next_lang.encode(encoding, errors=errors)

    # Decodes the string encoded in the previous line
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    
    # Prints the string stored in the variable raw_bytes, a static visual divder, followed the decoded string stored in cooked_string
    print(raw_bytes, "<===>", cooked_string)

# Opens the file languages.txt in memory and sets it to be read in utf-8
languages = open("languages.txt", encoding="utf-8")

# Calls the function main with , and the two additional arguments set in argv
main(languages, input_encoding, error)