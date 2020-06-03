import random
number = random.randint(1, 100)
guess = input("Try and guess the number between 1 and 100!:  ")
count = 0
while count < 10:
    if int(guess) == number:
        print("Winner!!!")
        print("you won in " + str(count) + " rounds!!!")
        break
    elif int(guess) < 0 or int(guess) > 100:
        print("Whoa there buddy, we need a number from 1 to 100")
        guess = input("Try again!")
    elif int(guess) > number:
        print("Too high")
        guess = input()
        count += 1
    elif int(guess) < number:
        print("Too low")
        guess = input()
        count += 1
else:
    print("You ran out of lives...You lose")