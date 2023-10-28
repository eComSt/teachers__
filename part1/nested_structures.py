data = [
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9],
    ]
# print(data[0][2])
summ = 0
for i in data:
    for j in i:
        summ = summ + j
print(summ)
summ = 0
for i in data:
   summ = summ + sum(i)
print(summ)