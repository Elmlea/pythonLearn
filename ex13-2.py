# study drill 13-3
from sys import argv
script, firstEntry, secondEntry = argv # when you run it, the name of the script is the first argument!
print(f"You ran this script, called {script}, with the arguments {firstEntry} and {secondEntry}.")
thirdEntry = input("You can put another entry in here if you like? ")
print(f"You just typed {thirdEntry}.  I've got no idea why we'd do it this way.")
