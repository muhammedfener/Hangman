import random

def gameplay():
    print('H A N G M A N')
    wordlist = ('python', 'java', 'kotlin', 'javascript')
    choiceword = random.choice(wordlist)
    a = list("-" * (len(choiceword)))
    lives = 8
    tryletter = []
    while lives > 0:
        display_word = "".join(a)
        if "-" not in display_word:
            print(f"\n{display_word}")
            print('You guessed the word!')
            print('You survived!')
            break
        letter = input(f"\n{display_word}\nInput a letter: ")
        if (2 > len(letter) > 0) == False:
            print("You should input a single letter")
            continue
        if not letter.islower():
            print("Please enter a lowercase English letter")
            continue
        if letter in tryletter:
            print("You've already guessed this letter")
            continue
        else:
            tryletter.append(letter)
        if letter in display_word:
            print("No improvements")
            lives -= 1
            if lives == 0:
                print("You lost!")
                break
            continue
        if letter in choiceword:
            for i in range(len(choiceword)):
                if letter == choiceword[i]:
                    a[i] = letter
        else:
            lives -= 1
            print("That letter doesn't appear in the word")
            if lives == 0:
                print("You lost!")
                break

def gamereq():
    game = input('Type "play" to play the game, "exit" to quit: >')
    return game

while True:
    game = gamereq()
    if game == "play":
        gameplay()
    elif game == "exit":
        break
    else:
        break
