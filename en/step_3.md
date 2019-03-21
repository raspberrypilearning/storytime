## If or else

Now that you know the dragon's name, it's time to get some more information about it.

--- task ---
Can you add `input` and `print` functions to find out if the dragon is *big* or *small*, and to find out how old the dragon is?

--- hints --- --- hint ---
Use `input` to ask if the dragon is big or small. Then, use a `print` function to tell the user the size of the dragon.
--- /hint --- --- hint ---
Here is some code to ask for the dragon's size and then print it.
```python
size = input("Is the dragon big or small? ")
print("It was a " + size + " dragon")
```
Now do the same for the dragon's age.
--- /hint --- --- hint ---
Here's the full code that you will need to ask for the dragon's size and age.
<iframe src="https://trinket.io/embed/python/3f9399e144" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
--- /hint --- --- /hints ---
--- /task ---

Now that you know the age of the dragon, you can work out whether it is young or old. Dragons live for a long time, so a dragon is only truly considered old if it's older than 1000.

You can use conditional selection to work out whether the dragon is young or old. In Python, you can use `if` and `else` statements to make decisions in your program and the *greater than* operator (`>`) to see if a number is larger than another number.

--- task ---
Add some code to decide if the dragon is young or old. You need to **typecast** the `age` variable so that the computer knows it is a number. In Python, there is a big difference between the characters `1` `0` `0` and the number `100`.

<iframe src="https://trinket.io/embed/python/a3e3d4568c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
--- /task ---

--- task ---
Add another `print()` function to tell the user whether the dragon is young or old, and then two more to give a break before the story begins.

<iframe src="https://trinket.io/embed/python/c747445ac5" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
--- /task ---

