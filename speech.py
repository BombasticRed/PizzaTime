import speech_recognition as sr
from OrderPizzaPy import OrderPizza
from Main import FName
from Main import LName
from Main import Email
from Main import PhoneNumber
from Main import add
from Main import City
from Main import State
from Main import Zip
from Main import CardN
from Main import CVV
from Main import Exp
from Main import CardZip
from Main import FoodItem


while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: " + str(text))
        if format(text) == "Pizza Time":
            OrderPizza(FName, LName, Email, PhoneNumber, add, City, State, Zip, CardN, CVV, Exp, CardZip, FoodItem)
    except:
        print("Sorry could not recognize what you said")