## Get the dragon's name

The story time program generates a story and prints it to the screen so that you can read it. 

First, use the `print` function to display text in the 'Text output' area of the Editor.

--- task ---

Type this code on a new line.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 3
---
from random import choice

print("We are going to hear a story about a dragon!")

--- /code ---

--- /task ---

--- task ---

Click on the <strong>Run</strong> button to see what happens. You should see the words “We are going to hear a story about a dragon!” appear in the output display.

--- /task ---

You’re ready to ask the user for input, to learn more about the dragon.

--- task ---

Create a new variable called `name`. 

Use the `input` function to ask the user for the dragon's name. 

Store the input in the new `name` variable.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 5
---
from random import choice

print("We are going to hear a story about a dragon!")

name = input("What is the name of the dragon? ")

--- /code ---

--- /task ---

--- task ---

Run your code again to test whether the program asks for input.

--- /task ---


Add another line of code to print the name of the dragon to the screen. 

--- task ---

Use the `name` variable to print the name to the screen. 

In Python, you can use the `+` operator to join strings together.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 6
---
from random import choice

print("We are going to hear a story about a dragon!")

name = input("What is the name of the dragon? ")
print("Excellent. The dragon is called " + name)

--- /code ---

--- /task ---

--- task ---

**Test**: Run your code again and check the output.

--- /task ---