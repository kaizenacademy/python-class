fav_foodsl = ["burger", "sushi", "cheeseburger", "pizza"]

print(fav_foodsl)

fav_foodsl.append("Salad")
fav_foodsl.append(9)

print(fav_foodsl)

fav_foodsl.pop()

print(fav_foodsl)

new_food = input("Enter new food: ")
fav_foodsl.append(new_food)
print(fav_foodsl)