# Find common elements in both strings
list_a = [0, 1, 2, 3, 4, 5]
list_b = [5, 6, 7, 8, 9, 0]
intersection = lambda list_a, list_b: list(filter(lambda x: x in list_b, list_a))

result = intersection(list_a,list_b)
print(result)

# Check if the element is a number
list_num = 'bla'

check_number = lambda x: x.isdigit()
result = check_number(list_num)
print(result)

# Max/Min length
strings = ["hello", "world", "foo", "bar"]

max_min_len = lambda strings: (max(len(s) for s in strings), min(len(s) for s in strings))

max_len, min_len = max_min_len(strings)

print(max_len)
print(min_len)




