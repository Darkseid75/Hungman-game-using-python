import random
from stage import*
from word import*
l1=words #words for game
chosen_word=random.choice(l1)#choose the word
end_game=False
diplay = []
lenth =len(chosen_word)
print(chosen_word)
live=6#lives
for i in range(lenth):#creating blanksf
    diplay.append("_")
print(diplay)

while not end_game:
    guess = input("chose the word :").lower()  # check for the char in choosen word

    for k in range(lenth):#check availability
        latter =chosen_word[k]
        if latter ==guess:
            diplay[k]=latter
            print(guess,
            "is a correct")
            #reducwe life if guessed wrong

    print(stages[live])
    print(diplay)

    if guess not in chosen_word:
        live-=1
        print(guess,"not the correct latter")
        if live==0:
            end_game=True
            print("you lost")

    #if win



    if "_" not in diplay:
        end_game=True
        print(" you win")
