import random

lower = int(input("enter lower bound:"))
upper = int(input("enter upper bound:"))

answer = random.randrange(lower,upper)

lives = 9

guess_number = 0

while guess_number < lives:
    guess_number += 1

    guess = int(input("Guess a number:"))

    if answer == guess:
        print("you won.")
        print("you tried {} times".format(guess_number))
        break

    elif answer > guess:
        print("your guess too low")

    elif answer < guess:
        print("your guess too high.")


if guess_number >= lives:
    print("The number is {}".format(answer))
    print("You lose. Good luck next time")












