# Story Time with Python

![](book-open.png)

This tutorial allows you to tell a story with code. It demonstrates the simple use of if/else statements to evaluate user input that generates a cute fairy story. This is a fun way to get started with Python programming that allows you to really use your imagination and story telling abilities!

## Step 0: Setting up your Raspberry Pi

You will need to set up your Raspberry Pi to take part in this activity. See the Raspberry Pi Start Guide here to get you up and running.

## Step 1: Using a Text Editor

A great way to write your code and test it in intavals is to use a text editor. You will be writing your code in Python 3, and the Python programming environment **IDLE3** has a text editor that you can use with it. 

1. Load **IDLE3** by either double clicking the dekstop icon, or by click on the **Main Menu**, followed by **Programming** and then selecting **IDLE3**.

2. Once the Python Shell window has loaded click on **File** and **New Window**. This will open a text editor window in which you can write, save and test your code.

3. Save the file as `storytime.py` by clicking on **File** and **Save As**.

## Step 2: Get user input and print to the screen

The purpose of the story time program is to generate a story and print it to the screen so someone can read it. A good way to start therefore is understanding how to use the Python `print` function.

1. In your `storytime.py` file open in a text editor window type the following line:
	
	```python
	print("Hello reader")
	```
	
2. Save the file by clciking on **File** and **Save**. Next run the program to see what happens. To run a program click on **Run** followed by **Run Module**. You should see the words hello reader appear in the Python Shell window. 

	*Note that this tutorial uses Python 3 syntax so you must be using IDLE3 to run your program.*

	![](story1.png)

3. Now that you can print to the screen, let's find out some information from the person using the program and store it in a variable. At the top of your code type:

	```python
	name = input('What is your name? ')
	print("Hello " + name)
	```

4. Save the file and run your code to see what happens. Notice that the input question is printed to the screen and then your inputted information is stored in the variable 'name' which is then used in the printed statement saying hello.	 
	![](story2.png)
	
5. Can you now create two more variables to store information about what gender the user is, and whay day of the week it is?

## Step 2: If 	

```python
import random

name = input('What is your name? ')
print("Your name is, " + name)

gender = input('Are you a boy or a girl? ')
print("You are a " + gender)

day = input('What day is it? ')
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
