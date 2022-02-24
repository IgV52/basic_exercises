# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

from collections import Counter

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
student = Counter([name['first_name'] for name in students])
for key in student:
    print(key, student[key])

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
student = Counter([name['first_name'] for name in students])
max_name = 0
big_name = ''
for key in student:
    if student[key] > max_name:
        max_name = student[key]
        big_name = key
print(f'Самое частое имя среди учеников: {big_name}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
often_name = []
num_class = 0
for group in school_students:
    student = Counter([name['first_name'] for name in group])
    max_name = 0
    big_name = ''
    for key in student:
        if student[key] > max_name:
            max_name = student[key]
            big_name = key
    num_class += 1
    often_name.append(f'Самое частое имя в классе {num_class}: {big_name}')
print(*often_name, sep='\n')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
info_class = []
for groups in school:
    for group in groups:
            if isinstance(groups[group], str):
                num_class = groups[group]
            if isinstance(groups[group], list):
                male = 0
                girl = 0
                for student in groups[group]:
                    if not is_male[student['first_name']]:
                        girl += 1
                    else:
                        male += 1
                info_class.append(f'Класс {num_class}: девочки {girl}, мальчики {male}')
print(*info_class, sep='\n')

        


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
info_class = []
for groups in school:
    for group in groups:
        if isinstance(groups[group], str):
            num_class = groups[group]
        if isinstance(groups[group], list):
            male = 0
            girl = 0
            for student in groups[group]:
                if is_male[student['first_name']]:
                    male += 1
                else:
                    girl += 1
            info_class.append(f'{num_class},{girl},{male}')
variants = 0
for info in info_class:
    variants += 1
    if variants == 1:
        class1 = info.split(',')
    else:
        class2 = info.split(',')

if class1[2] > class2[2]:
    print(f'Больше всего мальчиков в классе {class1[0]}')
if class1[2] < class2[2]:
    print(f'Больше всего мальчиков в классе {class2[0]}')
if class1[1] > class2[1]:
    print(f'Больше всего девочек в классе {class1[0]}')
if class1[1] < class2[1]:
    print(f'Больше всего девочек в классе {class2[0]}')

