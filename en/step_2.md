## Input and output

--- task ---
Open the  starter project.

**Online**: open the starter project at [rpf.io/storytimeon](http://rpf.io/storytimeon){:target="_blank"}.

**Offline**: open the [starter project](http://rpf.io/p/en/storytime-go){:target="_blank"} in Python

If you need to download and install Python, you can find it at [rpf.io/pythonoff](http://rpf.io/pythonoff){:target="_blank"}.

In the starter project, you should see a single line of code:

```python
from random import choice
```
--- /task ---


The purpose of the story time program is to generate a story, and print it to the screen so that someone can read it. A good way to start, therefore, is understanding how to use the Python `print` function.

--- task ---
In your `storytime.py` file, type the following on a new line:
	
```python
print("We are going to hear a story about a dragon!")
```

<iframe src="https://trinket.io/embed/python/3b593eb9e4" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

--- /task ---

--- task ---
Run the program to see what happens.
--- /task ---

Now that you can print to the screen, let's find out how to get input from a user to learn a little more about the dragon.

--- task ---
You can create a new variable called `name` and use the `input` function to ask the user for the dragon's name. The name will be stored in your new variable.

<iframe src="https://trinket.io/embed/python/0de60dee6d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
--- /task ---

--- task ---
Run your code again, to test if the program asks for input.
--- /task ---


Now that you have stored the name of the dragon, you can use the `name` variable to print the name to the screen. In Python, you can use the `+` operator to join together strings.

--- task ---
Add another line to your code that prints out the name of the dragon. Then run your code.

<iframe src="https://trinket.io/embed/python/e651eca8ca" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
--- /task ---


