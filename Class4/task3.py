sum = 0
list1 = []

while sum < 100:
    num = int(input("Enter number: "))
    sum = sum + num
    list1.append(num)

print(f"Here is the list: {list1}")