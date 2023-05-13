def days ():
    days = years * 365
    return days

def weeks ():
    weeks = years * 52
    return weeks

def months ():
    months = years * 12
    return months

def hours ():
    hours = years * 365 * 24
    return hours

years = int(input("Enter number of years"))
choice = int(input("""Enter your choice: 
                  1 - days
                  2 - weeks
                  3 - months
                  4 - hours
                  """))

if choice == 1:
    day = days()
    print(day)

elif choice == 2:
    week = weeks()
    print(week)

elif choice == 3:
    month = months()
    print(month)

elif choice == 4:
    hour = hours()
    print(hour)

else:
    print("Please pick the right choice")
