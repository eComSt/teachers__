import sys
o_list = []
o_tup = ()
size_list = sys.getsizeof(o_list)
size_tup = sys.getsizeof(o_tup)
print(f"List:{size_list} bytes, Tuple:{size_tup} bytes")

import sys
# o_list = [1,2,3,4,5,6,7,8,9,10]
# o_tup = (1,2,3,4,5,6,7,8,9,10)
# size_list = sys.getsizeof(o_list)
# size_tup = sys.getsizeof(o_tup)
# print(f"List:{size_list} bytes, Tuple:{size_tup} bytes")

objects_list = []
for num in range(10_000):
    objects_list.append(num)
print(sys.getsizeof(objects_list))    
objects_tuple = tuple(objects_list)
print(sys.getsizeof(objects_tuple))   

objects_list = []
for num in range(10_000_000):
    objects_list.append(num)
print(sys.getsizeof(objects_list))    

objects_tuple = tuple(objects_list)
print(sys.getsizeof(objects_tuple))   



