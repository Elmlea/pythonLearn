from sys import argv

script, origFile, destFile = argv

print(f"Copying from {origFile} to {destFile}.")

print(f"Loading {origFile} and generating an object file, then reading data...")

inData = open(origFile).read()
# this line defines the var inData as the content of origFile
# the open cmd 'loads' it like a DVD, and then you run the function read on it

print(f"This script has read {len(inData)} bytes.")

open(destFile, 'w').write(inData)
# line 15 'loads' the destination file in write mode, then calls the write function

print("Operation complete.")
