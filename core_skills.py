import random
rand_list = random.randint(1, 100)
print(rand_list)
list_comprehension_below_10 = [x for x in a if x < 10]

list_comprehension_below_10 = a.filter(lambda x: x < 10)
