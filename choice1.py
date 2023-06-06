choice_1 = True
leave = input(
  "You are singing to your chameleon when you see a strange man climbing through your window. You jump up from your seat in shock. Which weapon do you grab? (enter f for fork or p for pan "
).lower()
while choice_1 == True:
  if leave == "f":
    print()
    print(
      "You grab the fork to protect yourself but get distracted and start combing your hair! The fork gets stuck in your hair so you grab the pan instead."
    )
    leave = "p"
  if leave == "p":
    print()
    print(
      "You grab the pan and hit the man across the head, succesfully knocking him out!"
    )
    choice_1 == False
    break
  else:
    leave = input(
      "That was not an option. Please try again. ").lower() 
