# Made by 403Code
# Game Name: Guess the Code
# Built at: 15 November 2023 - 11:23 p.m
# Beautified with Black

import random, string


def picker():
    ok = set()
    while len(ok) < 4:
        ok.add(random.choice(string.digits))
    return "".join(list(ok))


def check(guess, real):
    notation = []
    for i, j in enumerate(guess):
        if real.find(j) == i:
            notation.append("√")
        elif real.find(j) == -1:
            notation.append("×")
        elif real.find(j) != i:
            notation.append("-")
    print(" ".join(list(guess)))
    print(" ".join(notation))
    print(10 * "-")
    if notation.count("√") == 4:
        return 1
    else:
        return 0


if __name__ == "__main__":
    chances = 5
    real = picker()
    print("Welcome to guess the code game!")
    print("You have %d chances to guess | CTRL+C to stop." % chances)
    print("Tips: - : number is correct, but wrong position.")
    print("      × : number is incorrect and wrong position.")
    print("      √ : number is correct and in right position.")
    print("? ? ? ?")
    while 1:
        if chances < 1:
            print("The right answer is %s!" % real)
            print("Try again!")
            break
        try:
            gs = input("guess > ").strip().replace(" ", "")
            if gs.isdigit():
                if len(gs) < 4 or len(gs) > 4:
                    print("Wrong input length, min & max is 4 digits.")
                else:
                    if check(gs, real):
                        print("Congratulations! You guessed right!")
                        break
                    chances -= 1
                    print("You have %d chances left." % chances)
            else:
                print("Wrong input, type a number with 4 digits.")
        except KeyboardInterrupt:
            print("Stopped.")
            break
