myName = 'Mark'
myAge = 40 # not a lie
myHeight = 68 # inches
myWeight = 220.0 # lbs
myEyes = 'Brown'
myTeeth = 'White'
myHair = 'Brown'

print(f"Let's talk about {myName}.")
print(f"He's {myHeight} inches tall.")
print(f"He's {myWeight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {myEyes} eyes and {myHair} hair.")
print(f"His teeth are usually {myTeeth} depending on the coffee.")

#This line is tricky, try to get it exactly right.
total = myAge + myHeight + myWeight
print(f"If I add {myAge}, {myHeight}, and {myWeight} I get {total}.")

myHeightMetric = myHeight * 2.54
myWeightMetric = round(myWeight / 2.2)
print(f"If you want metric values, my height is {myHeightMetric} cm.")
print(f"...and my weight is {myWeightMetric} kgs.")
