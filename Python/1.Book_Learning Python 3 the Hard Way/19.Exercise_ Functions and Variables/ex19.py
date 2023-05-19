# Defines a function "cheese_and_crackers" that accepts two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Prints an f string that inserts the "cheese_count" argument
    print(f"You have {cheese_count} cheeses!")
    # Prints an f string that inserts the "boxes_of_crackers" argument
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # Prints a string
    print("Man that's enough for a party!")
    # Prints a string which includes creating a break
    print("Get a blanket. \n")

# Prints a string
print("We can just give the function numbers directly:")
# Uses the "cheese_and_crackers" function with two numerical arguments
cheese_and_crackers(20, 30)

# Prints a string
print("OR, we can use variables from our script:")
# Creates a variable "amount of cheese" with a numerical value
amount_of_cheese = 10
# Creates a variable "amount of cheese" with a numberical value
amount_of_crackers = 50

# Uses the "cheese_and_crackers" function with two variables as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Prints a string
print("We can even do math inside too:")
# Uses the "cheese_and_crackers" function with two sets of arithmetic as arguments
cheese_and_crackers(10 + 20, 5 + 6)

# Prints a string
print("And we can combine the two, variables and math:")
# Uses the "cheese_and_crackers" function with variables and arithmetic as arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)