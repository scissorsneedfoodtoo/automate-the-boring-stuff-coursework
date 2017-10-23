import random

print("Hello! What's your name?")
name = input()
secret_number = random.randint(1, 20)
print("Well {}, I'm thinking of a number between 1 and 20. You have 6 guesses to figure it out.".format(name))

for guesses_taken in range(1, 7):
    if guesses_taken == 1:
        print("Take a guess.")
    else:
        print("Try again! You have {} guesses left.".format(7 - guesses_taken))
    try:
        guess = int(input())

        if guess > secret_number:
            print("Your guess was too high.")
        elif guess < secret_number:
            print("Your guess was too low.")
        elif guess == secret_number:
            break # guessed the number correctly
    except:
        print("You did not enter a number.")

if guess == secret_number:
    print("Good job, {}! You got it in {} guesses.".format(name, str(guesses_taken)))
else:
    print("Bummer, {}! The number I was thinking of was {}. Better luck next time.".format(name, str(secret_number)))
