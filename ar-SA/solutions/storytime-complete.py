from random import choice

print("سنسمع قصة عن تنين!")
name = input("ماهو اسم التنين؟ ")
print("ممتاز، التنين يسمى " + name)
size = input("هل التنين ضخم أو صغير؟ ")
print("It was a " + size + " dragon")
age = input("How old is the dragon? ")
print("The dragon is " + age + " years old")

print("")
print("")

if int(age) > 1000:
    description = "old"
else:
    description = "young"

things = ["slay", "cakes", "chocolate", "rocks", "kittens"]
friends = ["Lila", "Naomi", "Noelle", "Idris", "Jonah", "Ari"]
actions = ["slay", "kiss", "save", "marry", "rescue", "eat"]
places = ["Middle Earth", "Narnia", "Hogwarts", "Alderaan"]

friend = choice(friends)
thing = choice(things)
action = choice(actions)
place = choice(places)

story = "Once upon a time, there was a dragon called " + name + ". The dragon was a very " + description + " creature, and it was very " + size + ". It liked nothing better than to " +  action + " " + thing + ". Sadly, the dragon was so great at this that it ran out of " + thing + " to " + action + " in " + place + ". The dragon became very bored. Luckily the dragon had a friend called " + friend + ". " + friend + " knew where the dragon could find lots of " + thing + " and the two of them travelled far away from " + place + " and found a land filled with lots of lovely " + thing + " to " + action + ". " + name + " and " + friend + " lived happily ever, with all the " + thing + " they wanted."

print(story)
