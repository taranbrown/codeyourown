import pickle
from os import path

USERS_FILE = "users.pkl"
users = load(USERS_FILE)
if users is None:
  users = {}

while True:
    user = input("Enter a username, or s to stop, or a to see all users: ").lower()
    if user == "s":
        break
    elif user == "a":
        for user, user_info in users.items():
          print (user, ": ", user_info, sep="")
          break
    elif user in users:
        print("Welcome back", user)
        break
    else:
        print("Welcome", user)
        users[user] = ""
        break 
  
save(users, USERS_FILE)   
  