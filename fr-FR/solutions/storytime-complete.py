from random import choice

print("Nous allons entendre une histoire sur un dragon !")
nom = input("Quel est le nom du dragon ?")
print("Excellent, le dragon s'appelle " + nom)
taille = input("Le dragon est-il grand ou petit ?")
print("C'était un " + taille + " dragon")
age = input("Quel est l'âge du dragon ?")
print("Le dragon a " + age + " ans")

print("")
print("")

if int(age) > 1000:
    description = "ancien"
else:
    description = "jeune"

choses = ["gobelins", "gâteaux", "chocolats", "rochers", "chatons"]
amis = ["Lila", "Naomi", "Noelle", "Idris", "Jonah", "Ari"]
actions = ["tuer", "embrasser", "sauver", "épouser", "sauver", "manger"]
lieux = ["la Terre du Milieu", "Narnia", "Poudlard", "Alderaan"]

ami = choice(amis)
chose = choice(choses)
action = choice(actions)
lieu = choice(lieux)

histoire = "Il était une fois un dragon appelé " + nom + ". Le dragon était une très " + description + " créature, et il était très " + taille + ". Il n'aimait rien de mieux que de " + action + " des  " + chose + ". Malheureusement, le dragon était si génial dans ce domaine qu'il manquait de " + chose + " à " + action + " dans " + lieu + ". Le dragon s'ennuyait beaucoup. Heureusement, le dragon avait un ami appelé " + ami + ". " + ami + " savait où le dragon pouvait trouver beaucoup de " + chose + " et les deux ont voyagé loin de " + lieu + " et ont trouvé une terre remplie de beaucoup de beaux " + chose + " à " + action + ". " + nom + " et " + ami + " vécurent heureux à tout jamais, avec tous les " + chose + " qu'ils voulaient."

print(histoire)
