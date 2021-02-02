from random import choice

print("We gaan een verhaal over een draak horen!")
naam = input("Wat is de naam van de draak? ")
print("Uitstekend, de draak heet " + naam)
grootte = input("Is de draak groot of klein? ")
print("Het was een " + grootte + " draak")
leeftijd = input("Hoe oud is de draak? ")
print("De draak is " + leeftijd + " jaar oud")

print("")
print("")

if int(leeftijd) > 1000:
    beschrijving = "oud"
else:
    beschrijving = "jong"

dingen = ["kam", "cakes", "chocolade", "rotsen", "kitten"]
vrienden = ["Lila", "Naomi", "Noelle", "Idris", "Jonah", "Ari"]
acties = ["doden", "kussen", "redden", "trouwen", "bevrijden", "eten"]
places = ["Middle Earth", "Narnia", "Hogwarts", "Alderaan"]

friend = choice(friends)
thing = choice(things)
action = choice(actions)
place = choice(places)

story = "Once upon a time, there was a dragon called " + name + ". The dragon was a very " + description + " creature, and it was very " + size + ". It liked nothing better than to " +  action + " " + thing + ". Sadly, the dragon was so great at this that it ran out of " + thing + " to " + action + " in " + place + ". The dragon became very bored. Luckily the dragon had a friend called " + friend + ". " + friend + " knew where the dragon could find lots of " + thing + " and the two of them travelled far away from " + place + " and found a land filled with lots of lovely " + thing + " to " + action + ". " + name + " and " + friend + " lived happily ever, with all the " + thing + " they wanted."

print(story)
