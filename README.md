storytime
=========

This tutorial allows you to tell a story with code. It demonstrates the simple use of if/else statements to evaluate user input that generates a cute fairy story.









```python
import random
import subprocess

name = raw_input("What is your name? ")
print("Your name is, " + name)

gender = raw_input("Are you a boy or a girl? ")
print("You are a " + gender)

day = raw_input("What day is it? ")
print("Today is " + day)


if gender == "girl":
    pronoun = "she"
elif gender == "boy":
    pronoun = "he"
else:
    pronoun = "it"


roles = ["knight", "princess", "prince", "frog", "wizard", "ogre" ]
places = ["computopia", "turingville", "programistan", "digitopolis", "bool city"]
names = ["Alice", "Bob", "Eve", "John", "Jill", "Alan", "Ada", "Grace", "Linus"]
actions = ["slay", "kiss", "save", "marry", "rescue", "eat", "steal"]

player_role = random.choice(roles)
actor_role = random.choice(roles)
actor_name = random.choice(names)
quest = random.choice(actions)

story = "Once upon a time, there was a " + player_role + " called " + name + ". " + pronoun + " and some friends found themselves in the magic land of " + random.choice(places) + ". This land was ruled by " + actor_name + " the " + actor_role + ". All of a sudden a mysterious voice spoke to them from high in the sky and said you must " + quest + " " + actor_name + " the " + actor_role + " to lift the curse of not being able to use technology...."


print(story)
```
