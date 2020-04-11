import random
numbers = [] 

counter = 0
while counter < 7:
    numbers.append(random.randint(1,50))
    counter += 1

print(numbers)

