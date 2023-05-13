def add(i, j):
    return i + j

def sub(i, j):
    return i - j

def mult(i, j):
    return i * j

def div(i, j):
    return i / j

val1 = float(input("Provide 1st value: "))
val2 = float(input("Provide 2nd value: "))

oper = input("""Chooes option: 
+ add
- sub
* mult
/ div
Input: """)

if oper == "+":
    total = add(val1, val2)
    print(f"total value is: {total}")

elif oper == "-":
    total = sub(val1, val2)
    print(f"total value is: {total}")

elif oper == "*":
    total = mult(val1, val2)
    print(f"total value is: {total}")

elif oper == "/":
    total = div(val1, val2)
    print(f"total value is: {total}")