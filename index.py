import random
from datetime import datetime

f = open("dictionary.txt","r")
list = []
for line in f:
    list.append(line[:-1])

random.seed()
seed = random.randint(0,999)
answer = list[seed]
# print(answer)

win = 0
print("Welcome to the Dictionary Game. There is a hidden, common word and you must submit guesses to try and find it. Please log in or sign up via username and password to save highscores and fastest times.")
username = input("Please input a username: ")
password = input("Please input a password: ")
while(not win):
    choice = input("Choose a word: ")
    # print(choice)
    if(choice == answer):
        print("Congratulations you have won!")
        win = 1
    elif(choice > answer):
        print("The answer is closer to A.")
    else:
        print("The answer is closer to Z.")