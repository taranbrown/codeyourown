import pickle
from os import path

def save (object, file):
    """Serialize a dictionary to a file."""
    with open(file, "wb") as f:
        pickle.dump(object, f)

def load(file):
    """Load a dictionary from a serialized file.
     Or return None if the file doesn't exist."""
    if path.exists(file):
        with open(file, "rb") as f:
            return pickle.load(f)
          
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
  