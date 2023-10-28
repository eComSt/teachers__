from pprint import pprint
fruits = {
    'яблоко': 100,
    'груша': 200,
    'апельсин': 300,
    'банан': 400
}
pprint(fruits)
fruits_new = {i:j*1.2 for i, j in fruits.items()}
pprint(fruits_new)