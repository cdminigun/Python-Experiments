import random

def main():
    number_guesser()
    main_test = 0
    while main_test == 0 :
        userAnswer = input("play again?")
        if userAnswer.upper() == "NO":
            print("Have a great day!")
            main_test = 1
        else:
            number_guesser()
def number_guesser():
    """a function to generate a random number and has the user guess"""
    promptUser = "Guess a hole number(Non negative)from 1 to 100:"
    test = 0
    randnumber = random.randint(1, 100)
    userNumber = int(input(promptUser))
    while test == 0 :
        
        try:
            if randnumber == userNumber:
                print("You're correct!")
                randomnumber = 0
                randomnumber = random.randint(1,100)
                test = 1
            elif randnumber < userNumber:
                print('lower')
                userNumber = int(input("Guess Again: "))

            else:
                print('higher')
                userNumber = int(input("Guess Again: "))
        except ValueError:
            print("Inter a valid integer.")
if __name__ == '__main__':
    main()
