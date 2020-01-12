from sys import argv

script, user_name, password = argv # this means the user must run the script with their user_name
prompt = '---> '

print(f"Hi {user_name}, I'm the {script} script.") # the 'f' is what we need to let us embed variables
print("I'd like to ask you a few questions.")
print(f"Do you like me, {user_name}?")
likes = input(prompt)

print(f"Where do you live, {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer.  Nice.
Also you're slack with security, your password is {password}!
""")
