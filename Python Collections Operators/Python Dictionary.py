# Python Dictionary
print("Dictionary")

person = {
    "first_name": "peter",
    "last_name": "bread Winner",
    "gender": "male",
    "state": "ogun",
    "age": 30
}
print(person)
print()

print("==Accessing Items ==")
person = {
    "first_name": "peter",
    "last_name": "bread Winner",
    "gender": "male",
    "state": "ogun",
    "age": 30
}
x = person["first_name"]
y = person["last_name"]
z = person["gender"]
a = person["state"]
b = person["age"]

print("First Name:", x)
print("Last Name:", y)
print("Gender:", z)
print("State:", a)
print("Age:", b)
print()

print("Accessing a key that those not exist")
person = {
    "first_name": "peter",
    "last_name": "bread Winner",
    "gender": "male",
    "state": "ogun",
    "age": 30
}
print(person["Occupation"])


