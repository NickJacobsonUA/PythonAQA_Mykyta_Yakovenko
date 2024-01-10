import random

# Task 1

# min = 15
#
# if 0 <= min <= 15:
#     print(f'The number {min} is in 1st quarter of an hour')
# elif 30 >= min > 15:
#     print(f'The number {min} is in 2nd quarter of an hour')
# elif 45 >= min > 30:
#     print(f'The number {min} is in 3rd quarter of an hour')
# else:
#     print(f'The number {min} is in 4th quarter of an hour')

# Task 2

# birth_month = int(input('Enter the month number of your birthday: '))
#
# if 2 < birth_month < 6:
#     print('Весна - Все довкола розцвітало.')
# elif 5 < birth_month < 9:
#     print('Літо - Діти насолоджувались літніми канікулами.')
# elif 8 < birth_month < 12:
#     print('Осінь - Все довкола загоралось яскравими фарбами.')
# elif 0 < birth_month < 3 or birth_month == 12:
#     print('Зима - За вікном падав сніг.')
# else:
#     print(f'A month with number {birth_month} does not exist')

# Task 3

# rand_num = random.randint(0, 1000000)
#
# x = rand_num / 8
# str_x = str(x)
# print(type(str_x), str_x)
# if '.0' in str_x:
#     print(f'The number {rand_num} can be divided by 6')
# else:
#     print(f'The number {rand_num} can not be divided by 6')

# Task 4

x = float(input("Enter X: "))
y = float(input("Enter Y: "))
print(type(x), x)
if x < 0:
    print('True')

if x > 0:
    if y > 0:
        print(f'The Coordinates {x} and {y} are in 1st quarter')
    elif y < 0:
        print(f'The Coordinates {x} and {y} are in 4th quarter')
else:
    if x < 0:
        if y <0:
            print(f'The Coordinates {x} and {y} are in 3rd quarter')
        elif y > 0:
            print(f'The Coordinates {x} and {y} are in 2nd quarter')













