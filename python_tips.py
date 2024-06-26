#global scope
# my_global = 10

# def fn1():
#     enclosed_v = 8
#     def fn2():
#         local_v = 5
#         print('Access to Global', my_global)
#         print('Access to Enclosed', enclosed_v)

#list
# list1 = [1, 2, 3, 4, 5]
# print(list1)
# list1.insert(len(list1), 6)
# list1.append(7)
# list1.extend([8,9,10])
# del list1[2]
# print(list1)
# for x in list1:
#     print('Value', x)

#tuples
# my_tuple = (1, 'strings', 4.5, True, 'strings')
# print(my_tuple.count('strings'))
# print(my_tuple.index(4.5))

#sets (they dont allow dupicate values)
# set_a = {1, 2, 3, 4, 5}
# set_b = {1, 2, 5, 7, 8}
# set_a.remove(2)
# set_a.add(6)
# set_a.discard(1)

# print(set_a)
# print(set_a.union(set_b)) # or set_a | set_b
# print(set_a.intersection(set_b)) # or set_a & set_b
# print(set_a - set_b) # difference
# print(set_a ^ set_b) # symmetrical difference

#Dictionaries
sample_dict = {1: 'coffee', 'Name': 'Dera'}
sample_dict[2] = 'Okay'
print(sample_dict)

for key, value in sample_dict.items():
    print(str(key) + ':' + str(value))
# employee_dict = {
#     12345: {
#         "id": "12345",
#         "name": "John", 
#         "department": "Kitchen"    
#     },
#     12458: {
#         "id": "12458",
#         "name": "Paul", 
#         "department": "House Floor"    
#     }
# }

# def get_employee_from_dict(id):
#     return employee_dict[id];


# print(get_employee_from_dict(12458));

#args
# def sum_of(*args):
#     sum = 0
#     for x in args:
#         sum += x
#     return sum

# print(sum_of(5, 7, 5))

#kwargs
def sum_of(**kwagrs):
    sum = 0
    for k, v in kwagrs.items():
        sum += v
    return round(sum, 2)
print(sum_of(coffee = 2.3, bread = 4.5, garri = 6.5))
