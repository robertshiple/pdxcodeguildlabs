"""

>>> shrink('1235')
2

>>> shrink('13')
4

>>> shrink('1123581321')
9

"""

def shrink(num):
    result = sum(int(n) for n in num) # im a generator expression! AKA A COMPREHENSION. IM MUCH COOLER THAN LIST COMPREHENSION
    print(result)


shrink('1235')



