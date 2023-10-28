numbers = []
for i in range(100, 1001):
    if i%7 == 0:
        numbers.append(i)
print(numbers)

numbers = [i for i in range(100, 1001) if i%7 == 0]
print(numbers)