
from logo import logo1
import random
print(logo1)

count = 0
random_number = random.randint(1,100)
level = input("please select the level as easy or hard : ")
if(level == "easy"):
    count = 10
elif(level == "hard"):
    count = 5
else: print("Game over, you did not select the correct level")


def guess_number(count1):
    for i in range (count1):
        guess = int(input("enter your guess : "))
        if guess > random_number:
            print("number too high")
            print(f"you have {count1-1} attempts left")
        elif guess < random_number:
            print("number too low")
            print(f"you have {count1 - 1} attempts left")
        else:
            print("you guessed the number")
            break
        count1 = count1-1
        if(count == 0):
            print("your tries are over, Thanks for playing")
            break
guess_number(count)