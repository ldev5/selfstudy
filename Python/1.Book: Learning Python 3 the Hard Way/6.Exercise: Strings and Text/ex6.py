#creates the variable "types_of_people" with a value of ten
types_of_people = 10
#creates the variable "x" with an f-string that contains the variable "types_of_people"
x = f"There are {types_of_people} types of people."

#creates the variable "binary"
binary = "binary"
#creates the variable "do_not"
do_not = "don't"
#creates the variable y with an f-string value that contains the variable "binary" and "do_not"
y = f"Those who know {binary} and those who {do_not}."

#prints the variable "x"
print(x)
#prints the variable "y"
print(y)

#prints an f-string that contains the variable "x"
print(f"I said: {x}")
#prints an f-string that contains the variable "y"
print(f"I also said: '{y}'")

#creates the variable "hilarious" with a value of False
hilarious = False
#creates the variable "joke_evaluation" with a string that includes empty brackers
joke_evaluation = "Isn't that joke so funny?! {}"

#prints the value of "joke_evaluation" with the variable "hilarious" as the input for the brackets
print(joke_evaluation.format(hilarious))

#creates the variable "w" that contains a string
w = "This is the left side of..."
#creates the variable "e" that contains a string
e = "a string with a right side."

#prints a combination of the "w" and "e" variables
print(w + e)