from random import choice

print("سنسمع قصة عن تنين!")
name = input("ماهو اسم التنين؟ ")
print("ممتاز، التنين يسمى " + name)
size = input("هل التنين ضخم أو صغير؟ ")
print (" لقد كان "+ size +" تنين ")
age = input("ماهو عمر التنين؟ ")
print("التنين هو " + age + " سنة")

print("")
print("")

if int(age) > 1000:
      description = "كبير العمر"
else:
      description = "صغير العمر"

things = ["يقاتل", "كيك", "شوكولاتة", "صخور", "قطط صغيرة"]
friends = ["ليلى", "نايومي", "نويل", "ادريس", "جون", "آري"]
actions = ["ذبح", "يقبل", "ينقذ", "يتزوج", "يتنقذ", "يأكل"]
places = ["الارض الوسطى", "نارنيا", "هاكوارت", "الديران"]

friend = choice(friends)
thing = choice(things)
action = choice(actions)
place = choice(places)

story = "ذات مرة، كان هناك تنين يسمى " + name + ". كان التنين مخلوق "+ description +" للغاية، وكان "+ size +" للغاية. لم يحب شيء أفضل من " +  action + " " + thing + ". للأسف، كان التنين رائعًا جدًا في هذا الأمر لدرجة أنه نفد من "+ thing +" إلى "+ action +" في "+ place +". أصبح التنين يشعر بالملل الشديد. لحسن الحظ كان للتنين صديق يسمى "+ friend +". " + friend + " كان يعرف أين يمكن أن يجد التنين الكثير من " + thing + " وقد سافر الاثنان بعيدا عن " + place + " ووجدا أرضا مليئة بالكثير من " + thing + " الجميلة" + " إلى " + action + ". " + name + " و " + friend + " عاشوا بسعادة مطلقة، مع كل " + thing + " الذي يريدونه."

print(story)
