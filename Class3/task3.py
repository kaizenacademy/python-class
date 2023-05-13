foods = ("apple", "banana", "orange", "mango", "strawberry", "grape", "mandarin", "strawberry")
calories = (52, 96, 62, 60, 33, 68, 50, 33)
print(foods)
print(calories)

foods1 = ["apple", "banana", "orange", "mango", "strawberry", "grape", "mandarin", "strawberry"]
print(foods1)

foods_list = list(foods)
calories_list = list(calories)
print(foods_list)
print(calories_list)

print(type(calories_list))

print(f"{foods1[4]} has 33 kcal")
print(f"{foods1[-2]} has 50 kcal")
print(set(foods1))

foods2 = {"apple": 52, "banana": 96, "orange": 62, "mango": 60, "strawberry": 33, "grape": 68, "mandarin": 50, "strawberry": 33}
print(foods2)

foods2["tomato"] = 60
print(foods2)

foods2["grape"] = 50
print(foods2)