import random

def lower(last_guess, lower_limit, target): 
    print("lower")
    new_guess = int(input(f"Enter guess between {lower_limit} and {last_guess}: "))
    guess(new_guess, lower_limit, last_guess, target)
    

def higher(last_guess, upper_limit, target):
    print("higher")
    new_guess = int(input(f"Enter guess between {last_guess} and {upper_limit}: "))
    guess(new_guess, last_guess, upper_limit, target)

def guess(last_guess, lower_limit, upper_limit, target):
    if last_guess > upper_limit or last_guess < lower_limit:
        print("Guess out of bounds")
        guess(last_guess, lower_limit, upper_limit, target)
    else:
        if last_guess == target:
            print("found")

        elif last_guess > target:
            lower(last_guess, lower_limit, target)

        elif last_guess < target:
            higher(last_guess, upper_limit, target)
    
print("Guess the number")
lower_limit = int(input("Enter lower bound: "))
upper_limit = int(input("Enter upper bound: "))
new_guess = int(input(f"Enter guess between {lower_limit} and {upper_limit}: "))

target = random.randint(lower_limit, upper_limit)

guess(new_guess, lower_limit, upper_limit, target)