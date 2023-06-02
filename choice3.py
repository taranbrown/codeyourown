####Choice 3 ####
print(
  "You are back at the tower with your mom and find yourself missing FLynn. Just then he enters the tower! Just as he is about to help you escape, Mother Gothel jumps out from the corner!! He fights off your evil mother and grabs a piece of glass. He is about to cut your hair..."
)
cut_hair = input(
  "Do you let him cut your hair? Enter y for yes or n for no").lower()
if cut_hair == "y":
  print(
    "You let him cut your hair. It's SUPER SHORT and it turns dark brown. It is no longer golden :( Fortunately with you hair gone, your mother dies. Yay! You get to live happily ever after with Flynn."
  )

if cut_hair == "n":
  print(
    "You don't let Flynn cut your hair. He gets distracted and your mom kills him. He's dead and you remain a prisoner for the rest of your life..."
  )
else:
  print(
    "That was not an option. You don't let him cut your hair so your mom kills him and keeps you prisoner"
  )

print("The end")