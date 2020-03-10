# from Character import character

# character1 = character("John", "Protagonist", "Mercenary", 21)

# print(character1.__str__())

global player

def goblin():
    print("The goblins, aye? Well, you have your reasons. I'll send ya over to em.")


def bullworm():
    print("Ohh, the bullworm, eh? Good luck")


def lazereel():
    print("You sir are the most ballsy of the adventurers yet. None have challenged the eels.")


def intro():
    global player
    choice = ""
    player = input("Welcome weary traveller. What's your name? ")
    print(f"Hello, {player}. What is it you would like to do? We've got a few "
          f"jobs available. Someone's gotta deal with the goblins, though they're a bit boring. (1)"
          )
    print(
        "Then we have the alaskan bull worm (2) and the space lazer-eels (3). They're deadly, but need taking care of. ")


    if input(choice) == "1":
        return goblin()
    elif choice == "2":
        return bullworm()
    elif choice == "3":
        return lazereel()


intro()


