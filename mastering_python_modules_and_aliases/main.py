# Objective: The aim of this assignment is to enhance your proficiency in using Python modules, both standard and custom, with a specific focus on importing with aliases.

# Task 1: Custom Module with Aliases 

# Problem Statement: Create a custom module named `text_utils.py` with functions for string manipulation (e.g., reversing a string, capitalizing). In your main script, import this module using an alias and utilize its functions.

import text_utils as tu

class UserInputEmpty(Exception):
    pass

while True:
    try:
        user_option = input("Would you like to enter a string for alteration?\n(yes or no)\n").lower
        if user_option() == "no":
            break
        elif user_option() == "":
            raise UserInputEmpty
        else:
            string_to_alter = input("What would you like to say?\n")
            user_alteration = input("Would you like to capitalize the phrase or reverse it?\n(capitalize or reverse)\n").lower
            if user_alteration() == "":
                raise UserInputEmpty
            elif user_alteration() == "capitalize":
                print(tu.capitalize_string(string_to_alter))
            elif user_alteration() == "reverse":
                print(tu.reverse_string(string_to_alter))
            else:
                print("Selection Invalid. I can only capitalize or reverse the string.")
    except UserInputEmpty:
        print("Input was empty. Please try again.")
print ("Goodbye!")


# - Expected Outcome: Your main script should be able to use the functions from `text_utils.py` via an alias, demonstrating an understanding of custom module creation and aliasing.