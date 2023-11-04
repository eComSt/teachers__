f = open('data.txt', 'r')
summ, choko = 0, 0
for line in f:
    try:summ += int(line)
    except:choko += 1
f.close()
print(summ, choko)
