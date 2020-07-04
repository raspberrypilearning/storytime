from random import choice

print("हम एक ड्रैगन के बारे में एक कहानी सुनने जा रहे हैं!")
name = input("ड्रैगन का नाम क्या है? ")
print("उत्कृष्ट, ड्रैगन का नाम है " + name)
size = input("ड्रैगन बड़ा है या छोटा? ")
print ("यह ड्रैगन आकार में "+ size +" था")
age = input("ड्रैगन की उमर कितनी है? ")
print("ड्रैगन की उम्र " + age + " वर्ष है")

print("")
print("")

if int(age) > 1000:
    description = "बूढ़ा"
else:
    description = "जवान"

things = ["हत्या", "केक", "चॉकलेट", "चट्टानें", "बिल्ली के बच्चे"]
friends = ["लीला", "नाओमी", "नोएल", "इदरीस", "जोनाह", "अरी"]
actions = ["हत्या", "चुंबन", "बचाने", "शादी", "बचाव", "खाने"]
places = ["मध्य पृथ्वी", "नार्निया", "हॉगवर्ट्स", "एल्डरान"]

friend = choice(friends)
thing = choice(things)
action = choice(actions)
place = choice(places)

story = "एक बार की बात है, " + name + " नामक एक ड्रैगन था। ड्रैगन एक बहुत "+ description +" प्राणी था, और यह बहुत "+ size +" था। इसे "+ action +" "+ thing +" से बेहतर कुछ भी नहीं लगता था। अफसोस की बात है कि ड्रैगन इस पर इतना महान था कि उसके पास "+ thing +" से "+ action +" से "+ place +" खतम हो गया था। ड्रैगन बहुत बोर हो गया। सौभाग्य से ड्रैगन का एक दोस्त था जिसका नाम "+ friend +" था। " + friend + " knew where the dragon could find lots of " + thing + " and the two of them travelled far away from " + place + " and found a land filled with lots of lovely " + thing + " to " + action + ". " + name + " and " + friend + " lived happily ever, with all the " + thing + " they wanted."

print(story)
