#This line sets the variable types_of_people to 10.
types_of_people = 10
#This defines a string; the 'f' term is needed because you're putting a string inside a string.
x = f"There are {types_of_people} types of people."

# these lines are more simple variable establishments; line 9 is hiding strings again.
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

#We've defined variables, so this prints them.
print(x)
print(y)

#these terms add more detail around the strings, so they're embedded in a longer string.
print(f"I said: {x}")
print(f"I also said: '{y}'")

#this sets the variable hilarious to false; but false isn't a string?
#it's a boolean thing apparently
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

#I don't get this line.
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print (w + e)
