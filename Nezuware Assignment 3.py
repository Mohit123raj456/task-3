#!/usr/bin/env python
# coding: utf-8

# # Hangman game 

# In[ ]:


import random 
word_list=["apple","banana","potato"]
lives=6
choosen_word=random.choice(word_list)
print(choosen_word)
display=[]
for i in range(len(choosen_word)):
    display += "-"
print(display)
game_over=False
while not  game_over:
    guessed_letter=input("Guess a letter: ").lower()
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter==guessed_letter:
            display[position]= guessed_letter
    print(display)
    if guessed_letter not in choosen_word:
        lives -=1
        if lives ==0:
            game_0ver =True
            print("you looose")
    if'_' not in display:
        game_over = True
        print("you win")
        

