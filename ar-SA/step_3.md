## كبير أو صغير ، كبير السن أو صغير السن

حان الوقت للحصول على مزيد من المعلومات حول التنين.

\--- task \---

Add `input` and `print` functions to find out:

1. Whether the dragon is **big** or **small**
2. How old the dragon is

\--- hints \--- \--- hint \---

Use `input` to ask if the dragon is big or small. Then, use a `print` function to tell the user the size of the dragon.

\--- /hint \--- \--- hint \---

Here is some code that asks for the dragon's size and then print it.

```python
size = input("Is the dragon big or small? ")
print("It was a " + size + " dragon")
```

Now do the same for the dragon's age.

\--- /hint \--- \--- hint \---

Here's the full code that you need to ask for the dragon's size and age. <iframe src="https://trinket.io/embed/python/3f9399e144" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

\--- /hint \--- \--- /hints \--- \--- /task \---

Now that you know the age of the dragon, you can work out whether it is young or old. Dragons live for a long time, so they are only considered old if they are older than 1000.

You can use **conditional selection** to work out whether the dragon is young or old. With the`if` and `else` statements, you can make decisions in your Python program. With the **greater than** operator (`>`), you can test whether a number is larger than another number.

\--- task \---

Add some code to work out whether the dragon is young or old. You need to **type cast** the `age` variable so that the computer knows it is a **number** and not a **character string**. This is important because for the Python language, there is a big difference between the **characters** `1` `0` `0` and the **number** `100`. <iframe src="https://trinket.io/embed/python/a3e3d4568c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

\--- /task \---

\--- task \---

Add another `print` statement to tell the user whether the dragon is young or old. Then add two more `print` statements to create a break before the story begins. <iframe src="https://trinket.io/embed/python/c747445ac5" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

\--- /task \---