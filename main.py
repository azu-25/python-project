import random

number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")

while True:
    guess = int(input("Take a guess:"))
    if guess == number:
        print("correct!")
        break
    elif guess < number:
        print("too low")
    else:
        print("too high")
