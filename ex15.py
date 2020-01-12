# this is pulling the argv module from the sys package
from sys import argv

# we want the script to run with 2 arguments; the first is the name of the script
script, filename = argv

# this line opens the filename give as an argument to the script running.
txt = open(filename)

# a simple 'format' line here to read out the argument
print(f"Here's your file {filename}:")

# this applies the "read" command, with no arguments (hence the empty parenthesis on the variable txt, and prints)
print(txt.read())

# this just asks us for an input
print("Type the filename again:")
# this sets a variable up, and asks us to input it using the prompt in parenthesis
file_again = input("> ")

# this defines the variable txt_again as the file we listed in the previous step
txt_again = open(file_again)

# again, we run the 'read' command on the variable txt_again, which is then printed.
print(txt_again.read())

# now we close the files
txt.close() # this is calling the function  CLOSE on the variable txt, with no arguements
txt_again.close()
