# Python Set
print("Sets")
cars = {"volve", "benze", "toyota", "honda"}
print(cars)
print()

print("A mixed set")
x = {"peter", 23, True}
print(x)

print()

print("Acessing Item in list")
cars = {"volve", "benze", "toyota", "honda"}
for car in cars:
    print(car)
print()

print("Adding to Set")
cars = {"volve", "benze", "toyota", "honda"}
cars.add("range")
print(cars)
print()

print("++Changing an item in Set==")
cars = {"volve", "benze", "toyota", "honda"}
cars.remove("benze")
print(cars)

print()

print("==Discard method=")
cars = {"volve", "benze", "toyota", "honda"}
cars.discard("toyota")
print(cars)
print()

print("=Pop Method=")
cars = {"volve", "benze", "toyota", "honda"}
cars.pop()
print(cars)
print()

print("=Getting the Lenght of A set=")
cars = {"volve", "benze", "toyota", "honda"}
print(len(cars))
print()

print("=Checking if an item Exists=")
cars = {"volve", "benze", "toyota", "honda"}
cars = "toyota" in cars
print(cars)
print()

print("===Combine Two Sets===")
x = {1, 2, 3, 4, 5}
y = {6, 7, 8}
x.update(y)
print(x)
print()

print("====Difference of Two Sets===")
x = {1, 2, 3, 4}
y = {3, 4, 5, 6}
print("x-y:", x - y)
print("y-x:", y - x)
print()

print("==Another Way to Create a Set==")
cars = set(("volve", "benze", "toyota", "honda"))
print(cars)
