years = int(input("Please enter your age: "))

if years < 13:
    print("You are child")

elif years >= 13 and years < 18:
    print("You are teenager")

elif years >= 18 and years < 65:
    print("You are adult")

elif years >=65:
    print("You are elder")

else:
    print("Wrong input")

tip = int(input("Please enter tip amount: "))

if tip == 15:
    print("Standard")

elif tip == 18:
    print("Good")

elif tip == 20 :
    print("great")

elif tip > 20:
    print("my hero")

else:
    print("Wrong input")