import saved

user = saved.load()
if user is None:
  user = input ("Please enter the username you would like to use.")
  saved.save(user)
else:
  print ("Welcome back,", user)
  
""" 
input("Hello user you have entered the Rapunzel story. Press any key to continue")
import choice1
import choice2 
import choice3 """

