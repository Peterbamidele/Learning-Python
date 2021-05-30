## Python List

# List are ordered container,they created using square bracket.

print("==Indexing==")
# ======Indexing======
pets = ["kegs", "cae", "rabbit"]
print(pets[0])
print(pets[1])
print(pets[2])

print()

print("==Negative Indexing===")
# =========Negative Indexing=============
pets = ["kegs", "cae", "rabbit"]
print(pets[-1])
print(pets[-2])
print(pets[-3])

print("========Range of Indexes ==============")
# ========Range of Indexes ==============
pets = ["dog", "cat", "rabbit", "fish", "hen"]
x = pets[1:3]
print(x)

pets = ["dog", "cat", "rabbit", "fish", "hen"]
x = pets[:2]
print(x)

print()

print("====Adding Items to a list=======")
pets = ["dog", "cat", "rabbit", "fish", "hen"]
pets.append("goat")
print(pets)  # "goat was  added to the pet list"

# =====Insert=
print("Insert...")
pets = ["dog", "cat", "rabbit", "fish", "hen"]
pets.insert(0, "goat")
pets.insert(2, "mouse")
pets.insert(6, 56)
print(pets)
print(pets[0])
print(pets[2])
print(pets[6])

print()

print("===Deleting Items from a list===")
pets = ["dog", "cat", "rabbit", "fish", "hen"]
pets.pop()
print(pets)

print("===Remove=")
pets = ["dog", "cat", "rabbit", "fish", "hen"]
pets.remove("rabbit")
print(pets)

print("==del")
pets = ["dog", "cat", "rabbit", "fish", "hen"]
del pets[1]
print(pets)
print()

print("=== Getting the length of a list ===")
pets = ["dog", "cat", "rabbit", "fish", "hen"]
print(len(pets))

print()

print("== Changing an Item's Value ==")
pets = ["dog", "cat", "rabbit", "fish", "hen"]
pets[3] = "goat"
print(pets)

print()

print("= Checking if an item Exists ==")
pets = ["dog", "cat", "rabbit", "fish", "hen"]
print("rabbit" in pets)
print("Lion" in pets)

print()

print("= Extending a list =")
value1 = [1, 2, 3]
value2 = [4, 5, 6]
value1.extend(value2)
print(value1)

print()

print("=Looping Through a list=")
pets = ["dog", "cat", "rabbit", "fish", "hen"]
for pet in pets:
    print(pet)

print()


print("=Another Way to crate a list===")
Pets = list(("dog", "cat", "rabbit"))
print(pets)
