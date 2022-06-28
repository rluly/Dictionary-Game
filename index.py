import random
import datetime
import pymongo
import time

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

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.test
db = client['Groomstone']
users = db.users
user = users.find_one({"username" : username, "password": password})

if(user == None):
    # print("bad user")
    user = {"username": username, 
    "password": password,
    "shortest" : 999999,
    "fastest": 999999,
    "startdate": datetime.datetime.utcnow()}
    user_id = users.insert_one(user).inserted_id

oldshort = user["shortest"]
oldfast = user["fastest"]
guesses = 0

start = time.time()
while(not win):
    choice = input("Choose a word: ")
    # print(choice)
    if(choice == answer):
        print("Congratulations you have won!")
        end = time.time()
        final = end-start
        print(final)
        print(guesses)

    elif(choice > answer):
        print("The answer is closer to A.")
        guesses = guesses + 1
    else:
        print("The answer is closer to Z.")
        guesses = guesses + 1
