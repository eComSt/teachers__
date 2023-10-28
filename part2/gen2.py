numbers = [i**2 for i in range(1, int(input("Введите N: ")) + 1)]
print(numbers)
N = int(input("Введите N: "))
numbers = []
for i in range(1, N+1):
    numbers.append(i**2)
print(numbers)