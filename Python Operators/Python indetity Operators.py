##Python Identity Operators
'''Identity operator are used to compare two values to determine
 if they point to the same object.'''

# Is Operator

x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)

x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is z)
print(x is y)

print()

# Is not Operator
x = [1, 2, 3]
y = [1, 2, 3]
print(x is not y)

x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is not z)
