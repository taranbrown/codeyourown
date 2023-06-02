#Introduction#

print("""Hello User! You have now entered the RAPUNZEL story. Make choices along the way to try to survive and live your happily every after.
Good Luck!""") 
input("Press any key to continue") 
print()  
##Background##

print("You have lived in your tower for all of your life, not allowed to explore the real world. But your 17th birthday is approaching and you REALLY want to see the lights...")
input ("Press any key to continue.")
print()

###Choice 1###
choice_1 = True 
leave = input("You are singing to your chameleon when you see a strange man climbing through your window. You jump up from your seat in shock. Which weapon do you grab? (enter f for fork or p for pan ").lower()
while choice_1 == True: 
  if leave == "f":
    print()
    print("You grab the fork to protect yourself but get distracted and start combing your hair! The fork gets stuck in your hair so you grab the pan instead.")
  leave == "p"
  if leave == "p":
    print ()
    print ("You grab the pan and hit the man across the head.")
    choice_1 == False
    break
  else:
    leave = input("That was not an option. Please enter f for fork or p for pan ").lower()


## Choice 2##

print("You tie up the man with your hair. When he wakes up you order him to take you to the royal castle so that you can see the lights on your birthday!")
input("Press any key to continue.")
print()
print("After a perilous journey. You finally make it to the castle. As the sun sets the lights begin to emerge and you are entranced. You look over at the man next to you. Flynn Rider.")
smooch = input("Do you give this man a special thank you? enter y for yes or n for no").lower()
if smooch == "y":
  print("You say thanks...")
elif smooch == "n":
  print("You don't say thanks. Kind of rude but okay.")
else:
  print("That was not an option. You probably got confused because you were so nervous around Flynn so we'll help you out. You said thanks...")
input ("Press any key to continue.")
print()
print("""The night ends and you are very happy BUT just as you are about to leave you hear a woman shout. IT'S MOTHER GOTHEL! OH NO!
She is very disappointed to see you with this strange boy and immediately takes you home.""")
input ("Press any key to continue.")
print ()
####CHoice 3 ####
print("You are back at the tower with your mom and you seem to find yourself missing FLynn. Just then he enters the tower! He fights off your evil mother and grabs a piece of glass. He is going to cut your hair")
cut_hair = input("Do you let him cut your hair? Enter y for yes or n for no").lower()
if cut_hair == "y":
  print("You let him cut your hair. It's SUPER SHORT and it turns dark brown. It is no longer golden :( Fortunately with you hair gone, your mother dies. Yay! You get to live happily ever after with Flynn.")
  
if cut_hair == "n":
  print("You don't let Flynn cut your hair. He gets distracted and your mom kills him. He's dead and you remain a prisoner for the rest of your life.")
else:
  print("That was not an option. You don't let him cut your hair so your mom kills him and keeps you prisoner")

print("The end")