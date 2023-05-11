years = int(input("Please input number of years to converts: "))

unit = int(input("""Choose which unit to convert to
             1 - Days
             2 - Weeks
             3 - Months
             input:
             """))

if unit  == 1 :
   print(f"{365 * years} days")
elif (unit == 2) :
   print(f"{52 * years} weeks")
elif unit == 3 :
   print(f"{12 * years} months")
else:
   print("Wrong choice")