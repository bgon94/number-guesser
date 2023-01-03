import random


def guess_random_number(tries, start, stop):
    r = random.randint(start, stop)
    while tries > 0:
        print("Tries remaining:", tries)
        guess = int(input("Guess a number: "))
        if guess == r:
            print("You got it!")
            return
        elif guess > r:
            print("Too high!")
            tries -= 1
        elif guess < r:
            print("Too low!")
            tries -= 1
    print("You lost! The number was:", r)

# guess_random_number(5,0,10)


def guess_random_num_linear(tries, start, stop):
    r = random.randint(start, stop)

    print("The number to guess is: ", r)
    print("Number of tries:", tries)
    for n in range(start, stop):
        while tries > 0:
            print("The computer guessed:", n)
            if n == r:
                print("The computer got it!")
                return
            else:
                tries -= 1
                print("The computer guess wrong, ties remaining:", tries)
                break
    print("The computer failed to guess the correct answer")

# guess_random_num_linear(5,0,10)


def guess_random_num_binary(tries, start, stop):
    r = random.randint(start, stop)  # lets say its 8
    lower_bound = start
    upper_bound = stop
    print("The number to guess is", r)
    while lower_bound <= upper_bound and tries > 0:
        pivot = (lower_bound + upper_bound) // 2
        if pivot == r:
            print("The computer got it!")
            return
        if pivot > r:
            print("The computer guessed", pivot)
            print("Guessing lower")
            tries -= 1
            upper_bound = pivot - 1
        else:
            print("The computer guessed", pivot)
            print("Guessing higher")
            tries -= 1
            lower_bound = pivot + 1
    print("The computer failed to find the number")
    return -1


guess_random_num_binary(5, 0, 100)
