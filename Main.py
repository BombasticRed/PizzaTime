from OrderPizzaPy import *
import os
import sys
FName = None
LName = None
Email = None
PhoneNumber = None
add = None
address = None
City = None
State = None
Zip = None
CardN = None
CVV = None
Exp = None
CardZip = None
FoodItem = None
if os.stat("settings.txt").st_size == 0:
    settings = open("settings.txt", "w+")
    settings.writelines(["FName=","\n", "LName=", "\n", "Email=", "\n",  "PhoneNumber=", "\n", "Address=", "\n",  "City=", "\n", "State=", "\n",  "Zip=", "\n","CardNumber=", "\n", "Expiration=", "\n", "CVV=", "\n", "CardZip=", "\n", "FoodItem="])
    settings.close()
    print("Fill out the settings!")
    sys.exit(0)

else:
   read = open("settings.txt", "r")
   text = read.readlines()
   number = 0
   for i in text:
       number = number + 1
       if number == 1:
           FName = i.split('=')[1]
       if number == 2:
            LName = i.split('=')[1]
       if number == 3:
           Email = i.split('=')[1]
       if number == 4:
            PhoneNumber = i.split('=')[1]
       if number == 5:
           add = i.split('=')[1]
        
       if number == 6:
            City = i.split('=')[1]   
       if number == 7:
            State = i.split('=')[1]   
       if number == 8:
            Zip = i.split('=')[1]    
       if number == 9:
            CardN = i.split('=')[1]    
       if number == 10:
            Exp = i.split('=')[1]    
       if number == 11:
            CVV = i.split('=')[1]    
       if number == 12:
            CardZip = i.split('=')[1]    
       if number == 13:
            FoodItem = i.split('=')[1]    
exec(open("./speech.py").read())