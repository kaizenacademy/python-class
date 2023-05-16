limit = int(input("Enter the stopping values"))

first_term = 0
second_term = 1

next_term = first_term + second_term

while next_term <= limit:
    print(next_term)

    first_term = second_term
    second_term = next_term

    next_term = first_term + second_term