from random import randint

random_list = [randint(1, 10) for _ in range(100)]

counts = {x:random_list.count(x) for x in set(random_list)}

print(counts)