# Input: Two numbers
x = float(input("What's X?"))
y = float(input("What's Y?"))

# say the unrounded quotient is ...
print("The quotient of {x} and {y} is {z}".format(x=x, y=y, z=x / y))
print(x / y)
# say the unrounded sum is ...
print("The sum of {x} and {y} is {z}".format(x=x, y=y, z=x + y))
print(x + y)
# say the unrounded difference is ...
print("The difference of {x} and {y} is {z}".format(x=x, y=y, z=x - y))
print(x - y)
# say the unrounded product is ...
print("The product of {x} and {y} is {z}".format(x=x, y=y, z=x * y))
print(x * y)

# return sayings
print("The rounded sum of {x} and {y} is {z}".format(x=x, y=y, z=round(x + y, 1)))
print(
    "The rounded difference of {x} and {y} is {z}".format(x=x, y=y, z=round(x - y, 1))
)
print("The rounded product of {x} and {y} is {z}".format(x=x, y=y, z=round(x * y, 1)))
print("The rounded quotient of {x} and {y} is {z}".format(x=x, y=y, z=round(x / y, 1)))
print("The rounded sum of {x} and {y} is {z}".format(x=x, y=y, z=round(x + y, 1)))


