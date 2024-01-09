import math
import random
# Task 1

first_name = 'mykyta'
last_name = 'yakovenko'
full_name = first_name + " " + last_name

# Lowercase string
print(full_name)

# Uppercase string
upper_full_name = full_name.upper()
print(upper_full_name)
# Capitazing the first letter
print(full_name.title())

first_name_new = '\t' + first_name
last_name_new = last_name
full_name_new = first_name_new + '\n' + last_name_new
print(full_name_new)
print(full_name.strip())

# Task 2

r = random.randint(2, 20)
l = 2 * math.pi * r
print(f'The circle length is {l}')
S = math.pi * r ** 2
print(f'The circle length is {S}')

# Task 3

dollar_rate = 38.14

calc = 1000 / dollar_rate

r_calc = round(calc, 2)

print(f'The current US Dollar exchange rate = {dollar_rate} per $1')
print(f'The amount of US Dollar for 1000 grn is = ${r_calc}')




