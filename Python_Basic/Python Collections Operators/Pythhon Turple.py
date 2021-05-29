# Create a Tuple
print("====create a Tuple====")
pets = ("dogs", "Cat", "hen")
print(pets)

print()

print("----Indexing------")
pets = ("dog", "cats", "rabbit")
print(pets[0])
print(pets[1])
print(pets[2])

print("========Negative Indexing========")
pets = ("dog", "cats", "rabbit")
print(pets[-1])
print(pets[-2])
print(pets[-3])

print()

print("=========Range of Index=========")
pets = ("dog", "cats", "rabbit", "hen", "goat",)
x = pets[1:3]
print(x)

# If you don't specify the first index, the range starts from index 0.
pets = ("dog", "cats", "rabbit", "hen", "goat",)
x = pets[:3]
print(x)

# --If you don't specify the last  index, the range ends with last item of the tuple.in the case, the range includes
# the last item
pets = ("dog", "cats", "rabbit", "hen", "goat",)
x = pets[2:]
print(x)

print()

print("======Getting the length of A tuple======")
pets = ("dog", "cats", "rabbit", "hen", "goat",)
print(len(pets))

value = (4, 6, 5, 7, 8, 9, 2, 3, 0,)
print(len(value))
print()

print("==Looping Through a Tuple====")

pets = ("dog", "goat", "hen", "cow", "duck")
for pet in pets:
    print(pets)

values = (4, 6, 5, 7, 8, 9, 2, 3, 0,)
for value in values:
    print(values)

print()

print("=====Checking if an item Exists===")
pets = ("dog", "cat", "rabbit")
print("dog" in pets)
print("fish" in pets)

values = (4, 6, 5, 7, 8, 9, 2, 3, 0,)
print(10 in values)
print(5 in values)
print()

print("==Another Way to Create A tuple====")
pets = tuple(("dog", "cat", "rabbit"))
print(pets)

values = tuple((4, 6, 5, 7, 8, 9, 2, 3, 0,))
print(values)

print()

print("===Combine Tuples===")
pets1 = ("dog", "cat", "rabbit")
pets2 = ("hen", "goat", "chicken")
all_pets = pets1 + pets2
print(all_pets)

# Tuples are Immutable
# In python tuple are
# print immutable (unchangeable).
# it means you can not add,remove or change its items

