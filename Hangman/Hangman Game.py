# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 11:25:13 2021

@author: Fenil
"""
import random
import time

print("\nWelcome to Hangman\n")
name = input("Enter your name: ")
print("Hello " + name + "! Its time to show some skills.")
time.sleep(2)
print("Game setup is about to ready")
time.sleep(3)


def main():
    global count
    global display
    global word
    global already_guessed
    global l
    global play_game
    
    word_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
    word = random.choice(word_guess)
    l  =len(word)
    count = 0
    display = "_"*l
    already_guessed = []
    play_game = ""
    
def re_exicution():
    global play_game
    
    play_game = input("Do You want to play again? y = yes, n = no \n")
    
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    
    if play_game == "y" or play_game == "Y":
        main()
        
    elif play_game == "n" or play_game == "N":
        print("Thanks For Playing! We expect you back again!")
        
        
        
        

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    
    
    guess = guess.strip()
    
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    
    elif guess in word:
        
        while word.count(guess):
            already_guessed.append(guess)
            index = word.find(guess)
            word = word[:index] + "_" + word[index + 1:]
            display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
        
        
    elif guess in already_guessed:
        print("Try another letter.\n")
    
    else:
        
        
        count +=1
        
        
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
            
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            re_exicution()
            
            
    if word == '_' * l:
            print("Congrats! You have guessed the word correctly!")
            re_exicution()
        
    elif count != limit:
        hangman()
    
              
main()
hangman()
            
        
        
    
        
    