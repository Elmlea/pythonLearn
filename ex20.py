from sys import argv

script, input_file = argv

# We define the function print_all
# It needs argument f to run, which is the file in question
# It prints the whole file by reading all the data from it; calling the read function
def print_all(f):
    print(f.read())

# This sets 'rewind(file)' as shorthand for calling seek(0) on the file
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline()) #readline is a new function
    # calls readline on the function with no arguements, and prints the line we chose

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
