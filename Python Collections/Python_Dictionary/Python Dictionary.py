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

# print("Accessing a key that those not exist")
# person = {
#     "first_name": "peter",
#     "last_name": "bread Winner",
#     "gender": "male",
#     "state": "ogun",
#     "age": 30
# }
# print(person["Occupation"])
# print()

print("Get()Method used to access Items")
person = {
    "first_name": "peter",
    "last_name": "bread Winner",
    "gender": "male",
    "state": "ogun",
    "age": 30
}
print(person.get("state"))
print()

print("Accessing a key that those not exist with Get()")
person = {
    "first_name": "peter",
    "last_name": "bread Winner",
    "gender": "male",
    "state": "ogun",
    "age": 30
}
print(person.get("Occupation"))
print()

print("Adding Items")
person = {"first_name": "peter",
          "last_name": "bread Winner",
          "gender": "male",
          "state": "ogun",
          "age": 30}
person["Occupation"] = "programmer"
print(person)
print()

print("==Changing an item,s Value==")
person = {"first_name": "peter",
          "last_name": ("Bamidele"),
          "gender": "male",
          "state": "ogun",
          "age": 30}
print(person)
print()

print("=Removing an Item==")
person = {
    "first_name": "peter",
    "last_name": "bread Winner",
    "gender": "male",
    "state": "ogun",
    "age": 30
}
person.pop("age")
print(person)
print()

print("del keyword ")
person = {
    "first_name": "peter",
    "last_name": "bread Winner",
    "gender": "male",
    "state": "ogun",
    "age": 30
}
del person["state"]
del person["age"]
print(person)
print()

print("==Getting the length of a Dictionary==")
person = {
    "first_name": "peter",
    "last_name": "bread Winner",
    "gender": "male",
    "state": "ogun",
    "age": 30
}
print(len(person))
print()

print("==Checking if a Key Exists==")
person = {
    "first_name": "peter",
    "last_name": "bread Winner",
    "gender": "male",
    "state": "ogun",
    "age": 30
}
if "age" in person:
    if "state" in person:
        print('the "age" and "state"key exits')
print()

print("==Looping Through a Dictionary====")
person = {
    "first_name": "peter",
    "last_name": "bread Winner",
    "gender": "male",
    "state": "ogun",
    "age": 30
}
for item in person:
    print(person)
print()

print("======Nesting Dictionary====")

employees = {
    "manager": {
        "name": "Ruth",
        "age": 40
    },
    "Programmer": {
        "name": "peter",
        "age": 35,
    }
}
print(employees)
print()

print("=======Accessing item in Nesting Dictionary=======")
employees = {
    "manager": {
        "name": "Ruth",
        "age": 40
    },
    "Programmer": {
        "name": "peter",
        "age": 35,
    }
}
print(employees["manager"]["name"])
print(employees["Programmer"]["name"])
