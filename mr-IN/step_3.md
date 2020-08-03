## मोठे किंवा लहान, म्हातारे किंवा तरूण

ड्रॅगन बद्दल अधिक माहिती मिळविण्याची वेळ आली आहे.

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

आता ड्रॅगनच्या वयासाठीही असेच करा.

\--- /hint \--- \--- hint \---

येथे संपूर्ण कोड आहे ज्याचा वापर करून आपण ड्रॅगनचा आकार आणि वय शोधू शकता. <iframe src="https://trinket.io/embed/python/3f9399e144" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

\--- /hint \--- \--- /hints \--- \--- /task \---

आता आपल्याला ड्रॅगनचे वय माहित आहे, आपण ते तरुण की म्हातारे आहे ते शोधू शकता. ड्रॅगन जास्त काळ जगतात, म्हणूनच जर ते 1000 वर्षांपेक्षा जास्त जुने असतील तर त्यांना वृद्ध मानले जातील.

You can use **conditional selection** to work out whether the dragon is young or old. With the`if` and `else` statements, you can make decisions in your Python program. With the **greater than** operator (`>`), you can test whether a number is larger than another number.

\--- task \---

ड्रॅगन तरुण आहे की म्हातारा आहे हे शोधण्यासाठी कोड जोडा. You need to **type cast** the `age` variable so that the computer knows it is a **number** and not a **character string**. This is important because for the Python language, there is a big difference between the **characters** `1` `0` `0` and the **number** `100`. <iframe src="https://trinket.io/embed/python/a3e3d4568c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

\--- /task \---

\--- task \---

Add another `print` statement to tell the user whether the dragon is young or old. Then add two more `print` statements to create a break before the story begins. <iframe src="https://trinket.io/embed/python/c747445ac5" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

\--- /task \---