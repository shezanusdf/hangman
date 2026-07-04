import random, sys

HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""
]

BIRDS = ["EAGLE", "PIGEON", "VULTURE", "SPARROW", "CROW","HUMMINGBIRD","PARROT","EMU","OSTRICH"]
result = BIRDS[random.randint(0,(len(BIRDS) - 1))]
placeholder = ["_"] * len(result)
missed_letters = []

def main():
    while True:
        print(HANGMAN_PICS[len(missed_letters)])
        print("The category is: Birds")
        print("Missed Letters:", " ".join(missed_letters))
        x = take_input()
        check_letter(x)
        if check_win_or_loss():
            break


def take_input():
    print(" ".join(placeholder))
    letter = input("Guess a Letter: ")
    return letter

def check_letter(letter):
    if letter in result:
        for i in range(len(result)):
            if letter == result[i]:
                placeholder[i] = letter
    if not letter in result:
        missed_letters.append(letter)

def check_win_or_loss():
    # check Win
    if "".join(placeholder) == result and len(missed_letters) < len(HANGMAN_PICS):
        print("You Won!")
        return True
    elif len(missed_letters) >= len(HANGMAN_PICS):
        print("You lost!")
        return True
     
    
if __name__ == "__main__":
    main()


        



    