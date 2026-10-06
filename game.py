from random import randint
wand = 0
def main():
    print("Welcome Hero, you are selected for a journey. You may die",end=": ")
    print(" you may be burned to death, you may be turned into a frog, and who knows what. You have to survive all of the challenges.", end="")
    print(" Do not give up. There will be downtimes,\nbut those downtimes, will save you in the end.")
    yes_or_no = challenge_1()
    if yes_or_no == "yes":
        challenge_2a()
    else:
        challenge_2b()
    
    

def challenge_1():
    print("Welcome to Challenge 1. A witch is standing in front of you.")
    print("Witch: Hahaha, I have taken you hostage. There is no more escape for you now!")
    global wand
    wand += 1
    print("You have currently found a wand. You can use this throughout the game. You can use this to skip a challenge.")
    yes_or_no = input("Would you like to use your wand? If you say no, you cannot use it in this challenge. ")
    yes_or_no = yes_or_no.lower()
    if yes_or_no == "y" or yes_or_no == "yes":
        wand -= 1
        return "yes"
    print("As a witch who is kind, you have to face this challenge. You have to guess the number between 1 and 100. If you get the answer right, I will let you go, or I will make you a frog. I will give you ten tries. 😡")
    number = randint(1, 100)
    tries = 10
    while True:
        try:
            number1 = int(input("Guess the number: "))
            if number == number1:
                print("Oh no! You beat the challenge. I guess I have to let you go.")
                return "yes"
            else:
                tries -= 1
                print(f"Tries: {tries}")
                if number1 < number:
                    print("Too low")
                else:
                    print("Too high")
            
            if tries == 0:
                print("Hahaha, you are horrible at my challenge. I guess I will have to make you a frog.")
                return "no"
        except ValueError:
            print("Not a number")
def challenge_2a():
    global wand
    print("Welcome to Challenge 2:")
    if wand != 0:
        yes = input("You currently have a wand. Do you want to use your wand?. ")
        yes = yes.lower()
        if yes == "y" or yes == "yes":
            wand -= 1
            return "yes"
    print("You are in a giant medieval cellar, locked up in chains. You have some clues to get out.")
    print("You found a list.")
    print("        List        \n Solve 5+5\n Write who is the current prime minister of India\n Write who is the current president of US.")
    number = input("What is 5+5? ")
    if number != "10":
        print("Well well well, you have lost everything. I will even give you negative 1 wands. If you have one wand, you have 0, and if you have 0, it is -1. I am burning you, and your curse is to do this game all over again. ")
        wand -= 1
        challenge_1()
        challenge_2a()
    name = input("What is India's current prime minister? (name and last name)")
    name = name.lower()
    if name != "narendra modi":
        print("Well well well, you have lost everything. I will even give you negative 1 wands. If you have one wand, you have 0, and if you have 0, it is -1. I am burning you, and your curse is to do this game all over again. ")
        wand -= 1
        challenge_1()
        challenge_2a()

    name = input("Who is current American president? ")
    if name != "donald trump":
        name = name.lower()
        print("Well well well, you have lost everything. I will even give you negative 1 wands. If you have one wand, you have 0, and if you have 0, it is -1. I am burning you, and your curse is to do this game all over again. ")
        wand -= 1
        challenge_1()
        challenge_2a()
    print("You win! 🥇")

def challenge_2b():
    global wand
    if wand >= 1:
        yes = input("Would you like to skip the challenge? ")
        yes = yes.lower()
        if yes == "yes" or "y":
            print("You won the entire game! Good job 👏")
        
    print("You are a frog. ")
    print("You have to kiss the right princess. You have to solve a riddle. Only one of the princess can say the truth.")
    print("Princess A: I am the real princess")
    print("Princess B: Princess A is a fraud.")
    print("Princess C: Princess B is telling the truth.")
    variable = input("Which one is telling the truth? ")
    if variable != "2":
        print("You failed. You died as a frog.")
    else:
        print("You won. Coongragulations 🎉!")


            
        
if __name__ == "__main__":
    main()