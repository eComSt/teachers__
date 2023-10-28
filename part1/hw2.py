init_data = (1,2,3,4,5,6,7,8,9)
n = int(input())
if n not in init_data:
    print(init_data)
else:
    print(init_data[:n-1]+init_data[n:])