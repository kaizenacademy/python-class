total_sum = 0

for num in range(1,101):
    total_sum += num

print(total_sum)

for num in range(100,0,-1):
    print(num)

val = [0,1,2,3,4,5,6,7,8,9,10]

for hello in val:
    if hello % 2 == 0:
        print(hello)

number=int(input("Enter number: "))

for num in val:
    print(number*num)