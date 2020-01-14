from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = int(input("> "))
    if choice <= 1:
        dead("Man, learn to type a number.")

    elif choice < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice =  input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def snake_room():
    print("Well you have found a room full of snakes, how wonderful.")
    print("You can see just under the pile of snakes there might be a door.")
    print("You know that you can light torches to scare the snakes away.")
    print("How many torches will you light?")
    torches = int(input("> "))
    print("How many minutes does it take you to light a torch?")
    timing = int(input('> '))

    if torches < 5 and timing <= 4:
        dead("Not enought torches!")
    elif torches >= 10 and timing <= 2:
        print("Great, it looks like they might be getting scared.")
        print(f"""We need to move this along,
what else are the snakes afraid of beyond {torches} torches?""")
        scared_snakes = input('> ')
        list_of_fears = scared_snakes.split(' ')
        print("""if I understand you correctly this is what you think snakes
are afraid of:""")
        for fear in list_of_fears:
            print(f"Snakes are afraid of {fear}.")

        print("How many of those do you have with you?")
        start = int(input("> "))
        print("How many do you think you could get?")
        end = int(input("> "))
        print("Great lets see how many snakes it kills.")
        dead_snakes = []
        while start < end or start == end:
            print(f"You killed {start} snake(s).")
            dead_snakes.append(start)
            start += 2
        print("Great job you killed:")
        for num in dead_snakes:
            print(num)
        print("Now you are able to get to the door.")
        gold_room()

    elif torches > 100 or timing < 2:
        dead("You are on fire! Literally.")

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There are three doors: 1, 2, or 3.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "1":
        bear_room()
    elif choice == "2":
        cthulhu_room()
    elif choice == "3":
        snake_room()
    else:
        dead("You stumble around the room until you starve.")


start()
