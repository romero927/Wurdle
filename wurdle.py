import sys
import os
import enchant
import random
import string

os.system('cls' if os.name == 'nt' else 'clear')

def instructions():
    print("----------------------------------")
    print("WURDLE")
    print("----------------------------------")
    print("Instructions:")
    print("The player must guess the 5-letter word in 6 attempts or less.")
    print("""\u2611 : The letter at that position was guessed correctly.""")
    print("""\u2610 : The letter at that position is in the hidden word, but in a different position.""")
    print("""\u2612 : The letter at that position is wrong, and isn't in the hidden word.""")
    print("----------------------------------")

instructions()

def check_word():
  d = enchant.Dict("en_US")
  letters = string.ascii_lowercase

  hidden_word = "xflpo"
  while len(hidden_word) != 5 or not d.check(hidden_word): 
    word = "".join([random.choice(letters) for _ in range(5)])
    word_suggestions = d.suggest(word)

    while len(word_suggestions) < 1:
        word = "".join([random.choice(letters) for _ in range(5)])
        word_suggestions = d.suggest(word)

    hidden_word = word_suggestions[0].upper()


  attempt = 6

  while attempt > 0:
    print("")
    guess = ""
    while len(guess) != 5 or not d.check(guess) :
        guess = str(input("Your guess: "))
        guess = guess.upper()
        if(len(guess) != 5): 
            print("Word must be 5 letters!")
        if(not d.check(guess)):
            print("Word '" + guess+"' is not valid in English.")
        print("")

    print("----------------------------------")

    for word, char in zip(hidden_word, guess):
                sys.stdout.write(char + '\t' )

    print("")
      
    for word, char in zip(hidden_word, guess):
        if word in hidden_word and char in word:
            sys.stdout.write("\u2611\t")
        elif char in hidden_word:
            sys.stdout.write("\u2610\t")
        else:
            sys.stdout.write("\u2612\t")    

    print("")
    print("----------------------------------")
    if guess == hidden_word:
      print("")
      print("The Word was: '" + hidden_word + "'. You guessed it in '"+str(6 - attempt + 1)+"' attempt(s). YOU WIN!")
      print("")
      break
    else:
      attempt = attempt - 1

      print(f"You have {attempt} attempt(s) remaining. \n ")
      
      if attempt == 0:
        print("Word not guessed in 6 attempts or less. The word was '"+hidden_word+"'. YOU LOSE!")

check_word()
