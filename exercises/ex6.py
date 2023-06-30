from random import randint

secret_number = randint(1, 9)
guess = input("Guess a number greater of equal to 1 and lower or equal to 9: ")
count = 1
found = False
while not found:
    if not guess.isnumeric():
        guess = input("The value you entered is not a number. Try again: ")
    else:
        guess_n = int(guess)
        if guess_n == secret_number:
            print(f"You won in {count} attempts!")
            found = True
        elif guess_n < secret_number:
            guess = input("Your number is to low. Try again: ")
            count += 1
        else:
            guess = input("Your number is to high. Try again: ")
            count += 1
