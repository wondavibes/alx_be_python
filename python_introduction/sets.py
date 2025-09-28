import random
new = set()
count = 12

while count > 0:
    new.add(random.randint(1,15))
    count -= 1
print(new)