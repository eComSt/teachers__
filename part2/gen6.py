from pprint import pprint
square = {}
for i in range(1, 21):
    square[i] = i**0.5
square = {i:i**0.5 for i in range(1, 21) if i%2==0}
pprint(square)