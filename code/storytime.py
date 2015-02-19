import random

name = input('What is your name? ')
print("Hello " + name)
gender = input('Are you a girl or a boy? ')
print("You are a " + gender)
day = input('What day is it? ')
print("Today is " + day)

if gender == "girl":
    pronoun = "she"
elif gender == "boy":
    pronoun = "he"
else:
    pronoun = "it"

roles = ["knight", "princess", "prince", "frog", "wizard", "ogre"]    
names = ["Ben", "Dave", "Liz", "Alex", "Rachel", "Clive", "Eben"]
actions = ["slay", "kiss", "save", "marry", "rescue", "eat"]
places = ["Computopia", "Turingville", "Digitopolis", "Bool City"]

actor_name = random.choice(names)
actor_role = random.choice(roles)
quest = random.choice(actions)
magic_place = random.choice(places)

story = "Once upon a time, there was a " + actor_role + " called " + name + ". " + pronoun + " and some friends found themselves in the magic land of " + magic_place + ". This land was ruled by " + actor_name + " the " + actor_role + ". All of a sudden a mysterious voice spoke to them from high in the sky and said you must " + quest + " " + actor_name + " the " + actor_role + "to lift the curse of not being able to use technology... "

print(story)
