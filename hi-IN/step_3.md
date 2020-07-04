## बड़ा या छोटा, बूढ़ा या जवान

ड्रैगन के बारे में कुछ और जानकारी प्राप्त करने का समय आ चूका है।

\--- task \---

`input` और `print` फंक्शन जोड़े यह पता लगाने के लिए की:

1. ड्रैगन **बड़ा** है या **छोटा**
2. ड्रैगन की उम्र क्या है

\--- hints \--- \--- hint \---

`input` का उपयोग करें यह पूछने के लिए कि ड्रैगन बड़ा है या छोटा। फिर, ` print ` का उपयोग करें उपयोगकर्ता को ड्रैगन का माप बताने के लिए।

\--- /hint \--- \--- hint \---

निम्नलिखित वह कोड है जो ड्रैगन के आकार के लिए पूछता है और फिर इसे प्रिंट करता है।

```python
size = input("ड्रैगन बड़ा है या छोटा? ")
print ("यह ड्रैगन आकार में "+ size +" था")
```

अब ड्रैगन की उम्र के लिए भी ऐसा ही करें।

\--- /hint \--- \--- hint \---

यहाँ पूर्ण कोड है जिसे इस्तेमाल करके आप ड्रैगन का आकार और उम्र निकाल सकते है। <iframe src="https://trinket.io/embed/python/3f9399e144" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

\--- /hint \--- \--- /hints \--- \--- /task \---

अब जब आप ड्रैगन की उम्र जानते हैं, तो आप यह पता लगा सकते हैं कि वह युवा है या बूढ़ा। ड्रेगन लंबे समय तक जीवित रहते हैं, इसलिए उन्हें बूढ़ा केवल तभी माना जाता है यदि वे 1000 वर्षो से अधिक वर्ष के हो जाते है हैं।

आप ** प्रतिबंधात्मक चयन ** का उपयोग कर सकते हैं यह जानने के लिए कि ड्रैगन युवा है या बूढ़ा। ` if ` और ` else ` विवरण के साथ, आप अपने Python कार्यक्रम में निर्णय ले सकते हैं। ** बड़ा संचालक (greater than operator) ** (`>`), की सहायता से आप परीक्षण कर सकते हैं कि क्या एक संख्या दूसरी संख्या से बड़ी है।

\--- task \---

यह जानने के लिए कि ड्रैगन युवा है या बूढ़ा कोड जोड़ें। आपको ` age ` वेरिएबल को **टाइप कास्ट (type cast)** करना होगा </strong>ताकि कंप्यूटर जान सके कि यह एक ** संख्या ** है और ना की **वर्णमाला स्ट्रिंग </0> । This is important because for the Python language, there is a big difference between the **characters** `1` `0` `0` and the **number** `100`.</p> <iframe src="https://trinket.io/embed/python/a3e3d4568c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

\--- /task \---

\--- task \---

Add another `print` statement to tell the user whether the dragon is young or old. Then add two more `print` statements to create a break before the story begins. <iframe src="https://trinket.io/embed/python/c747445ac5" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

\--- /task \---