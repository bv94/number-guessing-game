
import random

guess_num = random.randint(1, 100)
playing = True


while(playing):
    difficulty = input(
        "What is your preference for difficulty\nhard or medium or easy\n>")
    if(difficulty == "h" or difficulty == "hard" or difficulty == 1):
        life = 5

    elif(difficulty == "m" or difficulty == "medium" or difficulty == 2):
        life = 7
    else:
        life = 10
    while(True):
        if(life < 1):
            print("you ran out of life\n")
            if(input("Would you like to give it another go\n'y' for yes\n>" == "y")):
                break
            else:
                playing = False
                break
        user_guess = int(input("what is your guess"))
        if(user_guess > guess_num):
            print("too high\n")
            life -= 1
            print(f"you lost a life,\n you have {life} remaining")
        elif(user_guess < guess_num):
            print("too low\n")
            print(f"you lost a life,\n you have {life} remaining")
        else:
            print("you win\n")
            print("you ran out of life\n")
            if(input("Would you like to give it another go\n'y' for yes\n>" == "y")):
                break
            else:
                playing = False
                break
print("thanx for playing :>")
