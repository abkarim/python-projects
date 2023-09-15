# Import math and regex module from python
import math
import re

# ANSI escape code for colored text
red_color_code = "\033[91m"
green_color_code = "\033[92m"
reset_color_code = "\033[0m"


def get_integer_input(message):
    """
    Prompts the user for input and returns an integer if the input is a valid integer.

    Args:
        message (str): The message to display to the user as a prompt.

    Returns:
        int: An integer entered by the user

    Note:
        This function will keep prompting the user until a valid integer is entered.
        If the input is not a valid integer, a message will be displayed in red, 
        and the user will be prompted to enter a valid integer again.
    """

    # Get input
    input_value = input(message)

    # Return value, if the user input's a valid number
    if re.match("^[0-9]+$", input_value):
        # convert input value to integer
        return int(input_value)

    # Get value again
    print(red_color_code + "Please enter a number valid number" + reset_color_code)
    return get_integer_input(message)


# Get user input for a
a = get_integer_input("enter the value of a: ")

# Get user input for b
b = get_integer_input("enter the value of b: ")

# Get user input for c
c = get_integer_input("enter the value of c: ")

# Check if the values are correct for a triangle
# Approach: A triangle is valid if sum of its two sides is greater than the third side
if (a+b) > c and (b+c) > a and (c+a) > b:
    # Apply Heron's formula
    # calculate semi-perimeter of the triangle
    s = (a+b+c)/2

    # calculate area
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))

    # Print the area
    print(green_color_code + "The area is: %s" % (area) + reset_color_code)

else:
    print(red_color_code +
          "Triangle with the provided value is not possible" + reset_color_code)
