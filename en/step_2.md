## Input and output

--- task ---
Open the  starter project.

**Online**: open the starter project at [rpf.io/storytimeon](http://rpf.io/storytimeon){:target="_blank"}.

**Offline**: open the [starter project](http://rpf.io/p/en/storytime-go){:target="_blank"} in Python

If you need to download and install Python, you can find it at [rpf.io/pythonoff](http://rpf.io/pythonoff){:target="_blank"}.

In the starter project, you should see a single line of code

```python
from random import choice
```
--- /task ---


The purpose of the story time program is to generate a story, and print it to the screen so that someone can read it. A good way to start, therefore, is understanding how to use the Python `print` function.

--- task ---
In your `storytime.py` file open type the following on a new line:
	
	```python
	print("Hello reader")
	```

<iframe src="https://trinket.io/embed/python/3b593eb9e4" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

--- /task ---

	
2. Save the file by clicking on **File** and **Save**. Next, run the program to see what happens. To run a program click on **Run** followed by **Run Module**. You should see the words "Hello reader" appear in the Python Shell window. 

	**Note**: this tutorial uses Python 3 syntax, so you must be using IDLE3 to run your program.

	![](images/story1.png)

3. Now that you can print to the screen, let's find out some information from the person using the program and store it in a variable. At the top of your code type:

	```python
	name = input("What is your name? ")
	print("Hello " + name)
	```

4. Save the file and run your code to see what happens. Notice that the input question is printed to the screen and then the information entered by the user is stored in the variable 'name'; this is then used in the printed statement saying "Hello".	 

	![](images/story2.png)
	
5. Can you now create two more variables to store information about what **gender** the user is, and what **day of the week** it is? You will need this information in your final story.


