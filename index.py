import random
from datetime import datetime
import mysql.connector
from mysql.connector import errorcode

f = open("dictionary.txt","r")
list = []
for line in f:
    list.append(line[:-1])
f.close()

random.seed()
seed = random.randint(0,999)
answer = list[seed]
# print(answer)

win = 0
print("Welcome to the Dictionary Game. There is a hidden, common word and you must submit guesses to try and find it. Please log in or sign up via username and password to save highscores and fastest times.")
username = input("Please input a username: ")
password = input("Please input a password: ")

f2 = open("mysql.txt","r")
info = []
for line in f2:
    info.append(line[:-1])
f2.close()

try:
    cnx = mysql.connector.connect(user= info[0], password= info[1], host= info[2], database = info[3])
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Connection failed")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print("Connection successful")

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

cnx.close()