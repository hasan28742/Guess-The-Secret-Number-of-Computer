import random
# random.randint(a, b)
# Return a random integer N such that a <= N <= b


def guess():
    try:
        x = int(input("Enter the lowest limit: "))
        print(f"Lowest Limit is {x}.")
        y = int(input("Enter the highest limit: "))
        print(f"Highest limit is {y}.")
        random_number = random.randint(x, y)
        guess = 0
        while guess != random_number:
            guess = int(input(f"Guess a number between {x} and {y} : "))
            if x < guess < random_number:
                print("Opps, Too Low. Try again: ")
            elif y > guess > random_number:
                print("Opps, Too High. Try again: ")
            elif guess < x or guess > y:
                print("Out of the range.")
        print(f"You got the right number which was {random_number}")
    except ValueError:
        print("Invalid Input, Please insert a number.")


guess()





