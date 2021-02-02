## Groot of klein, oud of jong

Het is tijd om wat meer informatie over de draak te krijgen.

--- task ---

Voeg `input` en `print` functies toe om erachter te komen:

1. Of de draak **groot** of **klein** is
2. Hoe oud de draak is

--- hints ---
 --- hint ---

Gebruik `input` om te vragen of de draak groot of klein is. Gebruik vervolgens een `print` functie om de gebruiker de grootte van de draak te vertellen.

--- /hint --- --- hint ---

Hier is wat code die om de grootte van de draak vraagt en deze vervolgens afdrukt.

```python
grootte = input("Is de draak groot of klein? ")
print("Het was een " + grootte + " draak")
```

Doe nu hetzelfde voor de leeftijd van de draak.

--- /hint --- --- hint ---

Hier is de volledige code die je nodig hebt om de grootte en leeftijd van de draak op te vragen. 
<iframe src="https://trinket.io/embed/python/3f9399e144" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

--- /hint ------ /hints --- --- /task ---

Nu je de leeftijd van de draak kent, kun je uitzoeken of hij jong of oud is. Draken leven lang, dus ze worden pas als oud beschouwd als ze ouder zijn dan 1000 jaar.

Je kunt **voorwaardelijke selectie** gebruiken om uit te vinden of de draak jong of oud is. Met de `if` en `else` instructies kun je beslissingen nemen in je Python-programma. Met de **groter dan** operator (`>`) kun je testen of een getal groter is dan een ander getal.

--- task ---

Voeg wat code toe om erachter te komen of de draak jong of oud is. Je moet het **type converteren** van de `leeftijd` variabele, zodat de computer weet dat het een **getal** is en geen **tekenreeks**. Dit is belangrijk omdat voor de Python taal er is een groot verschil is tussen de **tekens** `1` `0` `0` en het **getal** `100`. 
<iframe src="https://trinket.io/embed/python/a3e3d4568c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

--- /task ---

--- task ---

Voeg nog een `print` instructie toe om de gebruiker te vertellen of de draak jong of oud is. Voeg vervolgens twee `print` instructies toe om wat lege regels te maken voordat het verhaal begint. 
<iframe src="https://trinket.io/embed/python/c747445ac5" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

--- /task ---