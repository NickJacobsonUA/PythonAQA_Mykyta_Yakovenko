import random

# Task 1
# Creating two lists with common number 0
odd = 1, 3, 0, 5, 7, 9, 0
even = 2, 4, 0, 5, 6, 8, 0


def find_same_numbers():
    same_name = []
    for i in odd:
        if i in even:
            same_name.append(i)

    return same_name


result = find_same_numbers()
print(f'The same numbers are {result}')

# Task 2 - Show average and accepted students
students = {'John': 6,
            'Sarah': 2,
            'Mark': 7,
            'Nick': 4,
            'Zoe': 3,
            'Emma': 10,
            }


def check_average_score():
    sum_grades = sum(students.values())
    students_amount = len(students)
    av_sc = sum_grades / students_amount
    return av_sc


# if the score is more than 5 points, the student passes
def check_accepted_students():
    keys_arr = []
    for key, value in students.items():
        if value > 5:
            keys_arr.append(key)
    return keys_arr


result_avg = check_average_score()
print(f'The average score for the students is {result_avg}')

result_acc = check_accepted_students()
print(f'The students who passed are: {result_acc}')

# Task 3 Dictionary creating with random data from the lists

list_name = ['Alex', 'John', 'Mike']
list_surname = ['Johnson', 'Wong', 'Rodrigues']
list_location = ['Rome', 'New York', 'London']
random_name = random.choice(list_name)
random_surname = random.choice(list_surname)
random_location = random.choice(list_location)

dict_people = {}


def add_people_to_dict():
    dict_people.update({
        'Name': random_name,
        'Surname': random_surname,
        'Location': random_location
    })


add_people_to_dict()
print(dict_people)
