
number = int(input("Enter a number to see it's multiplication table:"))

for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")