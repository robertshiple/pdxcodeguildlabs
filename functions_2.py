"""

>>> combine(7, 4)
11

>>> combine(42)
42

>>> combine_many(980, 667, 4432, 788, 122, 9, 545, 222)
7765

>>> choose_longest("Greg", "Rooney")
'Rooney'

>>> choose_longest("Greg", "Rooney", "Philip", "Maximus", "Gabrielle")
'Gabrielle'

>>> choose_longest("Greg", [0, 0, 0, 0, 4])
[0, 0, 0, 0, 4]

"""


def combine(num: int, numb=0) -> int:
    nums = num + numb 
    return nums
    

def combine_many(num: int, *args) -> int:
    numbs = sum(args) + num
    return numbs

    
def choose_longest(names, *args) -> list:
    names = max(names, key=len)
    return namey
    


