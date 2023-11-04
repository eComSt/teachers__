# data = input()
# data_list = data.split()
# count = 0
# for i in data_list:
#     unic = set(i)
#     if len(i) == len(unic):
#         count += 1

print(len(list(filter(lambda x: len(set(x)) == len(x), input().split()))))