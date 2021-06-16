import random

def guess(x):

    rand_num = random.randint(1, x)
    guess = 0

    while guess != rand_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))

        if guess < rand_num:
            print("Sorry, guess again.Too low")
        elif guess > rand_num:
            print("Sorry, guess again. Too high")

    print(f"Yay! congrats. You have guessed the {rand_num} correctly!!")

def comp_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":

        if low != high:
            guess = random.randint(low, high)
        else:
            guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)??").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"yay! computer guessed your num, {guess}, correctly!")

# guess(10)
comp_guess(15)
