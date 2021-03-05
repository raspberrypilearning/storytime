## Grand ou petit, ancien ou jeune

Il est temps d'obtenir plus d'informations sur le dragon.

\--- task \---

Ajoute `input` et `print` pour savoir :

1. Si le dragon est **grand** ou **petit**
2. Quel est l'âge du dragon

\--- hints \--- \--- hint \---

Utilise `input` pour demander si le dragon est grand ou petit. Ensuite, utilise une fonction `print` pour indiquer à l'utilisateur la taille du dragon.

\--- /hint \--- \--- hint \---

Voici du code qui demande la taille du dragon et ensuite l'affiche.

```python
taille = input("Le dragon est-il grand ou petit ?") print ("C'était un " + taille + " dragon")
```

Maintenant, fais la même chose pour l'âge du dragon.

\--- /hint \--- \--- hint \---

Voici le code complet dont tu as besoin pour demander la taille et l'âge du dragon. <iframe src="https://trinket.io/embed/python/3f9399e144" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

\--- /hint \--- \--- /hints \--- \--- /task \---

Maintenant que tu connais l'âge du dragon, tu peux déterminer s'il est jeune ou vieux. Les dragons vivent depuis longtemps, donc ils ne sont considérés comme anciens que s'ils sont âgés de plus de 1000 ans.

You can use **conditional selection** to work out whether the dragon is young or old. With the`if` and `else` statements, you can make decisions in your Python program. With the **greater than** operator (`>`), you can test whether a number is larger than another number.

\--- task \---

Add some code to work out whether the dragon is young or old. You need to **type cast** the `age` variable so that the computer knows it is a **number** and not a **character string**. This is important because for the Python language, there is a big difference between the **characters** `1` `0` `0` and the **number** `100`. <iframe src="https://trinket.io/embed/python/a3e3d4568c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

\--- /task \---

\--- task \---

Add another `print` statement to tell the user whether the dragon is young or old. Then add two more `print` statements to create a break before the story begins. <iframe src="https://trinket.io/embed/python/c747445ac5" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

\--- /task \---