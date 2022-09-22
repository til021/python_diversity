
"""
To play the game it's necessary to install the beautifulsoup4 and the unicode libraries!
Para rodar o programa é necessário instalar a biblioteca beautifulsoup4 e a biblioteca unidecode!
""";

# Setting environment:
from bs4 import BeautifulSoup
from urllib.request import urlopen
import random
import unidecode

# Getting list of words:
url = "https://www.suzano.com.br/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

text = soup.get_text().split()
word_list = []

for item in text:
    if item.isalpha():
        if len(item) > 6:
                word_list.append(item.lower())
          
# From the list above we select a randon word:
secret = random.choice(word_list)
unaccented_secret = unidecode.unidecode(secret)

# Functions used

def guess_verification(guess, unaccented_secret):
    if unidecode.unidecode(guess) == unaccented_secret:
        return("end")
    elif unidecode.unidecode(guess) == "arrego":
        return("arrego")
    else:
        for item in unaccented_secret:
            if guess == item:
                return("continue")
        else:
            return
          
def update_word(word_visual, guess, secret, unaccented_secret):
    for item in range(len(unaccented_secret)):
        if unidecode.unidecode(guess) == unaccented_secret[item]:
            word_visual[item] = (secret[item] + " ")
    return word_visual
  
def update_missing_digits(word_visual):    
    missing_digits = 0
    for item in word_visual:
        if item == "_ ":
            missing_digits += 1
    return missing_digits
  
def arrego_function(word_visual, secret, unaccented_secret):
    for item in range(len(word_visual)):
        if word_visual[item] == "_ ":
            word_visual[item] = (secret[item] + " ")
            return word_visual
          
# Initial game setup:
game = "start"
lives = 6
arrego = 0
word_visual = []
for item in range(len(secret)):
    word_visual.append("_ ")
    
# Game greetings
print(f"It's the hangmans game! You have {lives} lives!\n")
print(f"Try to guess the hidden word or a letter within it: {'_ '*len(secret)} \n")
print(f"-> Here's a tip: the word has {len(secret)} digits!")
print(f"-> If you don't know what to guess, type 'arrego' for a tip! (use it only once) \n")

# Main game body

while game != "end":
    
    guess = input("Type here your guess: ").lower()

    while not (len(guess) > 5 or len(guess) == 1):
        guess = input("Enter a valid guess: a").lower()
    
    game = guess_verification(guess, unaccented_secret)
    
    if game == "end":
        print("Congratulations! You made it! You guessed the hidden word correctly!! \n")
        print(f"The hidden word was: {secret}")
        break
        
    elif game == "continue":
        word_visual = update_word(word_visual, guess, secret, unaccented_secret)
        missing_digits = update_missing_digits(word_visual)
        
        print("\nYou are on the right track! ")
        print(f"The hidden word is: {''.join(word_visual)} \n")
        print(f"You still have to guess {missing_digits} digits! You have {lives} lives. \n")
        
    elif game == "arrego":
        if arrego == 0:
            word_visual = arrego_function(word_visual, secret, unaccented_secret)
            missing_digits = update_missing_digits(word_visual)
            arrego = 1
            
        print("\nYou arregated!! Here's your tip!")
        print(f"The hidden word is: {''.join(word_visual)} \n")
        print(f"You still have to guess {missing_digits} digits! You have {lives} lives. \n")
        
    else:
        print("\nNot this time.. ")
        lives -= 1
        if lives > 0:
            print(f"Now you have {lives} chances to guess the word correctly! \n")
        else:
            print("You ran out of lives!")
            print(f"The hidden word was: {secret}")
            game = "end"
