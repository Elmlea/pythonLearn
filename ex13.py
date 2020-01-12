from sys import argv
# I should be reading the WYSS section for how to run this
# Line 1 has pulled the "argv" feature from sys.  This adds this feature to my Py script.
# things like argv or sys are MODULES
# I'll now define the arguments, and run the script with them to populate them.
# argv holds the variables passed to the script when it is run.
script, first, second, third = argv #this is the unpacking line; it tells argv "take the arguments you've been given and assign them to these variables"

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
