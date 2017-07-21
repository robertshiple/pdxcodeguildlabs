"""

>>> fizz_buzz(15)
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

>>> fizz_buzz(10)
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']

REMEMBER: Use Encapsulation! D.R.Y.
>>> joined_buzz(15)
'1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz'
"""

def fizz_buzz(num):
    listy = list()
    for num in range(1, num+1):
        if num % 3 == 0 and num % 5 == 0:    # compound cond.
            listy.append('FizzBuzz')
        elif num % 3 == 0:
            listy.append('Fizz')
        elif num % 5 == 0:
            listy.append('Buzz')
        else: 
            listy.append(str(num))

    return listy


def joined_buzz(num):
    listy = fizz_buzz(num)
    join = ' '.join(listy)
    return join
    

