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
plaatsen = ["Midden Aarde", "Narnia", "Zweinstein", "Alderaan"]

vriend = choice(vrienden)
ding = choice(dingen)
actie = choice(acties)
plaats = choice(plaatsen)

verhaal = "Er was eens een draak genaamd" + naam + ". De draak was een heel " + beschrijving + " beest, en het was heel " + grootte + ". Het vond niets leuker dan " + actie + " " + ding + ". Helaas was de draak hier zo goed in dat hij geen " + ding + " naar " + actie + " in " + plaats + " had. De draak verveelde zich erg. Gelukkig had de draak een vriend genaamd " + vriend + ". " + vriend + " wist waar de draak veel " + ding + " kon vinden en de twee reisden ver weg van " + plaats + " en vonden een land vol met veel mooie " + ding + " om te " + actie + ". " + naam + " en "+ vriend + " leefden nog lang en gelukkig, met al het " + ding + " dat ze wilden."

print(verhaal)
