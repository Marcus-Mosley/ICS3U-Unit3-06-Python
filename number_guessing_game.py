#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on September 2020
# This program is a Number Guessing Game with
#   Random Numbers and Try Catch


import random


def main():
    # This function creates a random number and checks if the user's guess
    #   is equal to the generated number

    # Input
    guess_str = input("Enter a number between 0 and 9: ")
    print("")

    # Process & Output
    random_number = random.randint(0, 9)  # A number between 0 and 9

    try:
        guess_int = int(guess_str)
    except Exception:
        print("That is not an integer, please input a number between 0 and 9!")
    else:
        if guess_int == random_number:
            print("That is correct, the right number was {0}!"
                  .format(guess_int))
        else:
            print("That is incorrect, the right number was {0}!"
                  .format(random_number))
    finally:
        print("")
        print("Thanks for Playing!")


if __name__ == "__main__":
    main()
