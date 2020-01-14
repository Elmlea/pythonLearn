def iterate(target):
    runStep = 0
    while runStep < target:
        print(f"At the top, the number is {runStep}")
        numbers.append(runStep)

        runStep += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom, the number is {runStep}")

numbers = []
chosenNumber = int(input("How many iterations?"))
iterate(chosenNumber)

print("The numbers: ")

for num in numbers:
    print(num)
