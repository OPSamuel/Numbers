import random
import time

total = 0

print("\n******************************************")
print("******** ACCUMULATOR GAME ****************")
print("******************************************")

print("\nIn this game you have to try to accumulate")
print("points up to BUT NOT exceeding 40!")
print("\nYou will be offered ten random numbers so choose")
print("wisely... How close to 40 can you get?")

num1 = random.randint(1,10)
total = total + num1
print("\nYour first number is: ", num1)
print("This gives you a total of:", total)

while total < 40:
    answer = input("\nDo you want another number? (Y/N): ")
    if answer.upper() == "Y":
        num2 = random.randint(1,10)
        total = total + num2
        print("Your next number is: ", num2)
        print("This gives you a total of:", total)
    else:
        print("No number selected, your total is still: ", total)
        print("Program will exit in 10 seconds.")
        time.sleep(10)
        exit(0)
else:
    if total > 40:
        print("\nYou have exceeded 40 points and LOSE the game!")
        time.sleep(10)
    elif total == 40:
        print("Amazing you reached 40 exactly - well done!")
        time.sleep(10)
    else:
        print("Well done you stayed under 40")
        time.sleep(10)
