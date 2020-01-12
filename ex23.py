import sys # this is command line argument handling
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline() #reads a line from language_file

    if line: #if statement; the indented lines below run if true
        print_line(line, encoding, errors) #lines 9/10 skipped if above false
        return main(language_file, encoding, errors)
        # calling main within main makes it loop until line 8 is false

def print_line(line, encoding, errors):
    next_lang = line.strip() # removes the white space (and apparently \n)
                             # we can put a string in to strip too
    raw_bytes = next_lang.encode(encoding, errors=errors)
# this calls encode on the next_lang string, and the arguments are the encoding
# and error handling
    cooked_string = raw_bytes.decode(encoding, errors=errors)
#this is the inverse of line 16
    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")
# we define here that the file we're handling is encoded in UTF-8
main(languages, encoding, error)
