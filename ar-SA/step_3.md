## كبير أو صغير ، كبير السن أو صغير السن

حان الوقت للحصول على مزيد من المعلومات حول التنين.

\--- task \---

Add `input` and `print` functions to find out:

1. سواء كان التنين **كبير** أو **صغير**
2. كم عمر التنين

\--- hints \--- \--- hint \---

استخدم `input` للسؤال عما إذا كان التنين ضخماً أم صغيرًا. ثم استخدم دالة الطباعة `print` لإخبار المستخدم بحجم التنين.

\--- /hint \--- \--- hint \---

إليك بعض الكود الذي يطلب حجم التنين وثم تطبعه.

```python
size = input("هل التنين ضخم أم صغير؟ ")
print (" لقد كان "+ size +" تنين ")
```

الآن افعل الشيء نفسه بالنسبة لعمر التنين.

\--- /hint \--- \--- hint \---

إليك هنا الكود الكامل الذي تحتاجه للسؤال عن حجم التنين وعمره. <iframe src="https://trinket.io/embed/python/3f9399e144" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

\--- /hint \--- \--- /hints \--- \--- /task \---

الآن بعد أن عرفت عمر التنين، يمكنك معرفة ما إذا كان صغيرًا أم كبيرًا. تعيش التنانين لفترة طويلة، لذا فهي تعتبر قديمة فقط إذا كان عمرها أكبر من 1000.

يمكنك استخدام **التحديد الشرطي** لمعرفة ما إذا كان التنين صغيرًا أم كبيرًا. باستخدام عبارات `if` و `else` يمكنك اتخاذ القرارات في برنامج Python الخاص بك. مع العملية المنطقية **أكبر من** (`>`) ، يمكنك اختبار ما إذا كان الرقم أكبر من الرقم الآخر.

\--- task \---

أضف بعض التعليمات البرمجية لمعرفة ما إذا كان التنين صغيرًا أم كبيرًا. You need to **type cast** the `age` variable so that the computer knows it is a **number** and not a **character string**. This is important because for the Python language, there is a big difference between the **characters** `1` `0` `0` and the **number** `100`. <iframe src="https://trinket.io/embed/python/a3e3d4568c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

\--- /task \---

\--- task \---

Add another `print` statement to tell the user whether the dragon is young or old. Then add two more `print` statements to create a break before the story begins. <iframe src="https://trinket.io/embed/python/c747445ac5" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark"></iframe> 

\--- /task \---