
string_emp = '25'
string_full = '0'

int_full = 25
int_emp = 100

bool_full = True
bool_emp = False

#print(bool(string_emp)) # should be False
#print(bool(string_full)) # should be True

#print(bool(int_full)) # should be True
#print(bool(int_emp)) # should be false

#print(int(bool_full)) # turns into 1
#print(int(bool_emp)) # turns into 0

#print(int(string_emp)) # can't happen if it's not a string number
#print(int(string_full)) # can't happen if it's not a string number

#print(str(bool_full)) # word True
#print(str(bool_emp)) #word True

#print(str(int_emp)) # turns number into words
#print(str(int_full))  # turns number into words

'''
>
<
>=
<=
==
!=
'''

#a = 100
#b = 200

#print(a > b) # False
#print(a < b) # True
# print(a == b) # False
# print(a < b) # True
# print(a <= b) # True
# print(a >= b) # False

#a = input('type the number: ')
b = '200'
#                                                                  IF / elif /  else
#print(str(a) > str(b)) # if 201 - True if 200 - False

#sentence = input('Enter a number: ')
# if sentence.isdigit():
#     print(f'{int(sentence)} is a good number')
# else:
#     print(f'{sentence} - is not a number')


# str_input = input('type it: ')
#
# if str_input.startswith('Hello'):
#     print('Hello Sir')
#
# elif str_input.isdigit() and not str_input.startswith('2'):
#     print('Sorry, I do not know numbers')
# else:
#     print('Sorry I do not get it')

# eyes = int(input('Enter the amount of eyes: '))
# legs = int(input('Enter the amount of legs: '))

# if eyes >= 8:
#     if legs == 8:
#         print('It is a spider')
#     elif legs == 6:
#         print('It is a cockroach')
#     else:
#         print('I do not know this one')
# else:
#     if eyes == 2 and legs == 4:
#         print('It is a cat')
#     else:
#         print('I have no idea')
#                                                           Lists

new_fruit = 'pear'
fruits = ['apple', 'banana', new_fruit]
# print(type(fruits)) # type of the variable
# print(id(fruits)) # id of the list
# print(len(fruits))
#print(fruits[3]) # getting an elements by index start fromm 0
#print(fruits[-1]) # getting the last element
#print(fruits.index('pear')) # getting the id of the element in the list
#fruits.pop() # deleting the last element
#del fruits[1] # deleting the list element with index
fruits.append('kiwi') # adding an alement to the list
fruits.clear() # cleaning the list
print(fruits)


