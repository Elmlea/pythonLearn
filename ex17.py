from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we'll come back to this to combine these next 2 lines into 1
in_file = open(from_file) # think of this as loading a tape; in_file is the "loaded tape"
indata = in_file.read() # this is then reading from the tape

# The syntax is OBJECT.FUNCTION(ARGS)

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
