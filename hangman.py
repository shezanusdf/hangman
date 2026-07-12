import random

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

CATEGORIES = {
    "BIRDS" : ["EAGLE", "PIGEON", "VULTURE", "SPARROW", "CROW","HUMMINGBIRD","PARROT","EMU","OSTRICH"],
    "ANIMALS" : ["ELEPHANT","GIRAFFE","RHINO","TIGER","PENGUIN","BEAR","CAT","DOG","FOX"],
    "COUNTRIES" : ["INDIA","AUSTRALIA","BRAZIL","CUBA","MEXICO","GERMANY","AUSTRIA","LUXEMBOURG"],
    "FRUITS" : ["APPLE","BANANA","ORANGE","MANGO","LITCHI","KIWI","STRAWBERRY","BLUEBERRY"],
    "COLORS" : ["VIOLET","INDIGO","GREEN","PURPLE","BLACK","MAROON","ORANGE","YELLOW"]
}
CATEGORY = random.choice(list(CATEGORIES.keys()))
result = random.choice(CATEGORIES[CATEGORY])
placeholder = ["_"] * len(result)
missed_letters = []

def main():
    while True:
        print(HANGMAN_PICS[len(missed_letters)])
        print("The category is:",CATEGORY)
        print("Missed Letters:", " ".join(missed_letters))
        x = take_input()
        check_letter(x)
        if check_win_or_loss():
            break


def take_input():
    print(" ".join(placeholder))
    letter = (input("Guess a Letter: ")).upper()
    return letter

def check_letter(letter):
    if letter in result:
        for i in range(len(result)):
            if letter == result[i]:
                placeholder[i] = letter
    elif not letter in result:
        if letter in missed_letters:
            print("You already entered this letter! Try again!")
        else:
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


        



    