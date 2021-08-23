import random

a = random.randint(1, 100)

b = int(input ("Please guess the random number:"))
n=1

while (a != b):
    n += 1
    if (b-a > 0):
        print ("Your guess is too high.")
    elif (b-a < 0):
        print ("Your guess is too low.")

    b = int(input ("Please guess another random number:"))

else:
    print("Your guess is right! You've tried ", n, "times.")

