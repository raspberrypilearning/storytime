## Choose random details

Randomly pick one item from each list. 

This will help generate your story, and should make it fun!

--- task ---

Create a variable called `friend`. 

Assign the new variable a random item from the `friends` list and use the `friend` variable in a `print` function.

--- code ---
---
language: python
line_numbers: true
line_number_start: 21
line_highlights: 26-27
---
things = ["goblins", "cakes", "chocolate", "rocks", "trees"]
friends = ["Amilyn", "Lila", "Nuala", "Idris", "Jonah", "Ari"]
actions = ["slay", "kiss", "save", "marry", "rescue", "eat"]
places = ["Middle Earth", "Narnia", "Hogwarts", "Alderaan"]

friend = choice(friends)
print("The friend is " + friend)

--- /code ---

--- /task ---

--- task ---

**Test**: Run your code and check the output.
Each time you run the code, the variable should be randomly assigned a new item from the `friends` list.
--- /task ---

--- task ---

**Delete** the print line.

Create three more variables called `action`, `place`, and `thing`. 

Assign them random items from the `actions`, `places`, and `things` lists.

--- code ---
---
language: python
line_numbers: true
line_number_start: 21
line_highlights: 27-29
---
things = ["goblins", "cakes", "chocolate", "rocks", "trees"]
friends = ["Amilyn", "Lila", "Nuala", "Idris", "Jonah", "Ari"]
actions = ["slay", "kiss", "save", "marry", "rescue", "eat"]
places = ["Middle Earth", "Narnia", "Hogwarts", "Alderaan"]

friend = choice(friends)
thing = choice(things)
action = choice(actions)
place = choice(places)

--- /code ---

--- /task ---
