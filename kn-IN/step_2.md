## ನಿಮ್ಮ ಕಥೆಯನ್ನು ಸಂವಾದಾತ್ಮಕಗೊಳಿಸಿ

\--- ಕಾರ್ಯ \---

ಸ್ಟಾರ್ಟರ್ ಪ್ರಾಜೆಕ್ಟ್ ತೆರೆಯಿರಿ.

** ಆನ್‌ಲೈನ್ **:Trinket ಸ್ಟಾರ್ಟರ್ ಪ್ರಾಜೆಕ್ಟ್ ತೆರೆಯಲು [ rpf.io/storytimeon ](http://rpf.io/storytimeon){:target="_blank"} ಬಳಸಿ.

** ಆಫ್‌ಲೈನ್ **:[ಸ್ಟಾರ್ಟರ್ ಪ್ರಾಜೆಕ್ಟ್](http://rpf.io/p/en/storytime-go) {: target="_blank"} ಡೌನ್ಲೋಡ್ ಮಾಡಿ ನಂತರ ಅದನ್ನು ಟೆಕ್ಸ್ಟ್ ಎಡಿಟರ್ ನಲ್ಲಿ ತೆರೆಯಿರಿ

[rpf.io/pythonoff](http://rpf.io/pythonoff){:target="_blank"},ಇದರಿಂದ ನೀವು Python ಡೌನ್ಲೋಡ್ ಮತ್ತು ಇನ್ಸ್ಟಾಲ್ ಮಾಡಬಹುದು.

ಸ್ಟಾರ್ಟರ್ ಪ್ರಾಜೆಕ್ಟಿನಲ್ಲಿ ನೀವು ಒಂದೇ ಸಾಲಿನ ಕೋಡನ್ನು ನೋಡಬಹುದು:

```python
from random import choice
```

\--- /task \---

ಸ್ಟೋರಿ ಟೈಮ್ ಪ್ರೋಗ್ರಾಮಿನ ಉದ್ದೇಶ ಏನೆಂದರೆ ನೀವು ನಿಮ್ಮ ಕಥೆಯನ್ನು ರಚಿಸಿ, ಅದನ್ನು ಕಂಪ್ಯೂಟರ್ ಸ್ಕ್ರೀನಿನ ಮೇಲೆ ಪ್ರಿಂಟ್ ಮಾಡಿ ಓದಬಹುದು. ಮೊದಲು ನೀವು Python `print` ಫಂಕ್ಷನ್ ಹೇಗೆ ಉಪಯೋಗಿಸುವುದು ಎಂದು ಕಲಿಯಬೇಕು.

\--- task \---

ನಿಮ್ಮ `storytime.py` ಫೈಲಿನಲ್ಲಿ, ಈ ಕೋಡನ್ನು ಹೊಸ ಸಾಲಿನಲ್ಲಿ ಟೈಪ್ ಮಾಡಿ:

```python
print("We are going to hear a story about a dragon!")
``` <iframe src="https://trinket.io/embed/python/3b593eb9e4" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

\--- /task \---

\--- task \---

ಈಗ ಪ್ರೋಗ್ರಾಮನ್ನು ರನ್ ಮಾಡಿ, ಏನಾಗುತ್ತೋ ನೋಡಿ. ನೀವು ಔಟ್ಪುಟ್ ಸ್ಕ್ರೀನಿನ ಮೇಲೆ “We are going to hear a story about a dragon!” ಎಂದು ಕಾಣಬಹುದು.

\--- /task \---

ಈಗ ನೀವು ಪ್ರಿಂಟ್ ಮಾಡಲು ಕಲಿತಿದ್ದೀರಿ ಹಾಗಾಗಿ, ಈಗ ನೀವು ಯೂಸರ್ ಇಂದ ಇನ್ಪುಟ್ ಕೇಳಲು ಸಿದ್ಧರಾಗಿದ್ದೀರಿ, ಇದರಿಂದ ಡ್ರ್ಯಾಗನ್ ಬಗ್ಗೆ ಹೆಚ್ಚು ತಿಳಿದುಕೊಳ್ಳಬಹುದು.

\--- task \---

ಹೊಸ ವೇರಿಯೇಬಲ್(variable) `name` ರಚಿಸಿ. ಡ್ರ್ಯಾಗನ್ ಹೆಸರನ್ನು ಯೂಸರ್ ಇಂದ ಪಡೆಯಲು `input` ಫಂಕ್ಷನ್ ಉಪಯೋಗಿಸಿ. ಯೂಸರ್ ಇಂದ ಪಡೆದಿರುವ ಹೆಸರನ್ನು, `name` ವೇರಿಯಬಲ್ ಅಲ್ಲಿ ಸಂಗ್ರಹಿಸಿ. <iframe src="https://trinket.io/embed/python/0de60dee6d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

\--- /task \---

\--- task \---

ಮತ್ತೊಮ್ಮೆ ನಿಮ್ಮ ಕೋಡನ್ನು ರನ್ ಮಾಡಿ ಇನ್ಪುಟ್ ಕೇಳುತ್ತಾ ಅಥವಾ ಇಲ್ಲವಾ ಎಂದು ಪರೀಕ್ಷಿಸಿ.

\--- /task \---

ಈಗ ನಿಮ್ಮ ಹತ್ತಿರ ಡ್ರ್ಯಾಗನ್ನಿನ ಹೆಸರು ಇದೆ, ಹೀಗಾಗಿ `name` ವೇರಿಯಬಲ್ ಅನ್ನು ಉಪಯೋಗಿಸಿ ಹೆಸರನ್ನು ಸ್ಕ್ರೀನಿನ ಮೇಲೆ ಪ್ರಿಂಟ್ ಮಾಡಿ. Python ನಲ್ಲಿ `+` ಆಪರೇಟರ್ ಉಪಯೋಗಿಸಿ ಸ್ಟ್ರಿಂಗ್ ಗಳನ್ನು ಒಂದಾಗಿ ಸೇರಿಸಬಹುದು.

\--- task \---

ಡ್ರ್ಯಾಗನ್ನಿನ ಹೆಸರನ್ನು ಸ್ಕ್ರೀನಿನ ಮೇಲೆ ಪ್ರಿಂಟ್ ಮಾಡಲು ಇನ್ನೊಂದು ಸಾಲಿನ ಕೋಡ್ ಅನ್ನು ಸೇರಿಸಿ. ನಂತರ ಕೋಡನ್ನು ರನ್ ಮಾಡಿ. <iframe src="https://trinket.io/embed/python/e651eca8ca" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

\--- /task \---