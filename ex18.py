# this line generates a function that works like argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# it now says that *args is pointeless, so it can be written as:
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# here's a version that takes just one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

# THE FUNCTION CHECKLIST
# Start with def
# Stick to characters & _ for naming (use camelCase!)
# Open brackets right after the function name
# Arguments after the parenthesis, separated by commas.
# No duplicated argument names
# Close parenthesis and put a colon after the Arguments
# Indent all lines 4 spaces (one tab in Atom)
# 'Dedent' to close the function off; start typing without the 4 spaces

# RUNNING A FUNCTION
# Call the function by name
# Put the required arguments in parenthesis
# End the function call by closing the parenthesis
