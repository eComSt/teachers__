from pprint import pprint
N=int(input("Введите N: "))
table = []
for i in range(1,N+1):
    row = []
    for j in range(1,N+1):
        row.append(i*j)
    table.append(row)

table = [[i*j for j in range(1,N+1)] for i in range(1,N+1)]
pprint(table)