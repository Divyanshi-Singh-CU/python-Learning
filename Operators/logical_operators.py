#logical operators

age = 18
has_uid = True
has_permission = False

print("Age:", age)
print("Has ID:", has_uid)
print("Has Permission:", has_permission)

# AND Operator
print("\nAND Operator:")
print(age >= 18 and has_uid)

# OR Operator
print("\nOR Operator:")
print(age >= 18 or has_permission)

# NOT Operator
print("\nNOT Operator:")
print(not has_permission)
