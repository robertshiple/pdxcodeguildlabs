"""
# Test Data Below.  Leave this line alone.
>>> names = ['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']

>>> people = [('Kieran', 'Prasch', 'Instructor'), ('Alfonzo', 'Ward', 'Student'), ('Fin', 'Balnik', 'Student')]

>>> long_names(5)
['Kieran', 'Serada', 'Alfonzo']

>>> starts_with('S')
['Suki', 'Serada']

>>> last_names(people)
['Prasch', 'Ward', 'Balnik']

>>> smoosh(people)
['Kieran', 'Prasch', 'Instructor', 'Alfonzo', 'Ward', 'Student', 'Fin', 'Balnik', 'Student']

"""

names = ['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']

people = [('Kieran', 'Prasch', 'Instructor'), ('Alfonzo', 'Ward', 'Student'), ('Fin', 'Balnik', 'Student')]


def long_names(num: int) -> list:
    resulty = [name for name in names if len(name) > num]
    return resulty


def starts_with(letter: str) -> list:
    namey = [name for name in names if name.startswith(letter)]
    return namey


def last_names(people: str) -> list:
    lasty = [last[1] for last in people]
    return lasty


# def smoosh(people: str) -> list:
#     listy = []
#     for people in people:
#         join = ' '.join(people)
#         listy.append(join)
#     return listy 


# def smoosh(people: str) -> list:
#     listy = []
#     for people in people:
#         for name in people:
#             listy.append(name)
#     return listy 


def smoosh(people: str) -> list:
    listy = [name for people in people for name in people]
    return listy 
