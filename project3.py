#hangman game (jumble letters)
import random

words=["UMBRELLA","COMPUTER","TELESCOPE","SMARTPHONE"]
word=random.choice(words)
total_chances=7
guessed_word="_"*len(word)
print(guessed_word)

while total_chances !=0:
    print(guessed_word)
    letter=input("Guess a letter: ").upper()
    if letter in word:
        for index in range(len(word)):
            if word[index]==letter:
                guessed_word=guessed_word[:index]+letter+guessed_word[index+1:]
                #print(guessed_word)
        if guessed_word==word:
            print("congratulations you won!!")
            break
    else:
        total_chances -=1
        print("Incorrect guess")
        print("The remaining chances are: ",total_chances)
else:
    print("Game Over")
    print("You Lose")
    print("All the chances are exhausted")
print("The correct word is",word)