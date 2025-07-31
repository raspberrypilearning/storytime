## Size and age of the dragon

It's time to get some more information about the dragon.

--- task ---

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 8-12
---
from random import choice

print("We are going to hear a story about a dragon!")

name = input("What is the name of the dragon? ")
print("Excellent. The dragon is called " + name)

size = input("Is the dragon big or small? ")
print("It was a " + size + " dragon")

age = input("How old is the dragon? ")
print("The dragon is " + age + " years old")

--- /code ---

--- /task ---

--- task ---

**Test**: Run your code again and check the output.

--- /task ---

Dragons live for a long time. 

They are only old if their age is more than 1000 years!

--- task ---

Use **conditional selection** to set the description to 'young' or 'old'. 

With `if` and `else` statements, you can make decisions in your Python program. 

With the **greater than** operator (`>`), you can test whether a number is larger than another number.

**Notice**: You must **type cast** the `age` variable, so the computer uses it as a **number** and not a **character string**. In Python, there is a big difference between the **characters** `1` `0` `0` and the **number** `100`.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 14-19
---
from random import choice

print("We are going to hear a story about a dragon!")

name = input("What is the name of the dragon? ")
print("Excellent. The dragon is called " + name)

size = input("Is the dragon big or small? ")
print("It was a " + size + " dragon")

age = input("How old is the dragon? ")
print("The dragon is " + age + " years old")

if int(age) > 1000:
    description = "an old"
else:
    description = "a young"

print("It was an " + description + " dragon.")

--- /code ---

--- /task ---

--- task ---

**Test**: Run your code again and check the output.

If you enter an age less than 1000, you should see the dragon is young.

If you enter an age more than 1000, you should see the dragon is old.

What happens if you enter an age of exactly 1000?

--- /task ---

