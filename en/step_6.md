## Tell your story

Now you can have some fun with creating your story! 

Be as imaginative and creative as you like.

--- task ---

First, type `story =` to create a variable to store your story in.

--- /task ---

Now use all the variables you have to make an imaginative story of your own. There is an example provided below, but you can make any story you like.

--- task ---

Write your story putting the variables together. Then on the last line of your program, print the story to the screen.

--- code ---
---
language: python
line_numbers: true
line_number_start: 21
line_highlights: 31-33
---
things = ["goblins", "cakes", "chocolate", "rocks", "trees"]
friends = ["Amilyn", "Lila", "Nuala", "Idris", "Jonah", "Ari"]
actions = ["slay", "kiss", "save", "marry", "rescue", "eat"]
places = ["Middle Earth", "Narnia", "Hogwarts", "Alderaan"]

friend = choice(friends)
thing = choice(things)
action = choice(actions)
place = choice(places)

story = "Once upon a time, there was a dragon called " + name + ". The dragon was a very " + description + " creature, and it was very " + size + ". It liked nothing better than to " +  action + " " + thing + ". Sadly, the dragon was so great at this that it ran out of " + thing + " to " + action + " in " + place + ". The dragon became very bored. Luckily the dragon had a friend called " + friend + ". " + friend + " knew where the dragon could find lots of " + thing + " and the two of them travelled far away from " + place + " and found a land filled with lots of lovely " + thing + " to " + action + ". " + name + " and " + friend + " lived happily ever, with all the " + thing + " they wanted."

print(story)

--- /code ---

--- /task ---

--- task ---

**Test**: Run your code to create your story!

--- /task ---
