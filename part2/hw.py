# data = input()
# data_list = data.split()
# data_list = [int(i) for i in data_list]
# ans = {}
# for i in data_list:
#     x = str(i)
#     summ = 0
#     for j in x:
#         summ = summ +int(j)
#     ans[i] = summ
# print(ans)

print({int(i):sum([int(j) for j in i]) for i in input().split()})