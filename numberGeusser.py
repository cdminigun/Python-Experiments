import random


def main():
    numberGuesser()


def numberGuesser():
    """a function to generate a random number and has the user guess"""
    promptUser = "Guess a hole number(Non negative)from 1 to 100:"
    test = 0
    userNumber = int(input(promptUser))
    randnumber = random.randint(1, 100)
    while test == 0:

        if randnum == userNumber:
            print("You're correct!")
            userAnswer = input("play again?")
            if userAnswer.upper() == "NO":
                print("Have a great day!")
                test = 1
            else:
                userNum = int(input(promptUser))
        elif randnum < userNumber:
            print('lower')
            userNumber = int(input("Guess Again: "))

        else:
            print('higher')
            userNumber = int(input("Guess Again: "))

main()
