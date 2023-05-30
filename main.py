#Introduction#

print("""Hello User! You have now entered the RAPUNZEL story.
Make choices along the way to try to survive and live your happily every after.
Good Luck!""")
input("Press any key to continue")
print()

##Background##

print("You have lived in your tower for all your life, not allowed to explore the real world. But your 17th birthday is approaching and you REALLY want to see the lights...")
print()

###Choice 1###
choice_1 = True
leave = input("You are singing to your chameleon when you hear a strange man climbing through your window. Which weapon do you grab? (enter f for fork or p for pan").lower()
while choice_1 == True: 
  if leave == "f":
    print()
    print("You grab the fork to protect yourself but get distracted and start combing your hair. The fork gets stuck in your hair so you grab the pan instead.")
  leave == "p"
  if leave == "p":
    print ()
    print ("You grab the pan and hit the man across the head.")
    choice_1 == False
  else:
    leave = input("That was not an option. Please enter f for fork or p for pan").lower()


## Choice 2

tie = input ("You tie him up with your hair.")
print("")