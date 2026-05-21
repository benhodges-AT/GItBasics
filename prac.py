""" 
def addition(a, b):
    total = a + b 
    return total

result = addition(10, 20000)
print(result)
"""
"""
class Microwave:
    def __init__(self, brand: str, power_rating: str,):
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on : bool = False

    def turn_on(self):
        if self.turned_on:
            print(f'Microwave ({self.brand }) is already turned on')
        else: 
            self.turned_on = True
            print(f'Microwave ({self.brand}) is now on.')

    def turn_off(self):
        if self.turned_on:
            self.turned_on = False
            print(f'Microwave ({self.brand }) is turned off')
        else: 
            self.turned_on = True
            print(f'Microwave ({self.brand}) is now turned off')    

    def run_microwave(self, seconds: int):
        if self.turned_on:
            print(f'Running {self.brand} for {seconds} seconds')
        else: 
            print(f'You must turn on your {self.brand} microwave first!')
    
    def __str__(self) -> str:
        return f'{self.brand} (Rating: {self.power_rating})'

Whirlpool : Microwave = Microwave("Whirlpool", "1000W")
Samsung : Microwave = Microwave("Samsung", "1300W")

print(Whirlpool)

"""
'''
nums = [1, 2, 3, 4, 5]

for num in nums:
    for letter in 'abc':
        print(num, letter)
'''


''' 
x = 0 

while x < 10: 
    print(x) 
    x += 1 

    
'''
''' 
def hello_func(greeting, name ='You'):
    return '{}, {}'.format(greeting, name)

print(hello_func('Hi', name = 'Bejji'))

'''

"""
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['math', 'art']
info = {'name': 'John', 'age':22}

student_info(*courses, **info)

student_info('Math', 'Art', name = 'John', age = 22) 

the_list = [
    143266561,
    1738152473,
    312377936,
    1027708881,
    1871655963,
    1495785517,
    1858250798,
    1693786723,
    374455497,
    430158267,
]

largest_value = 0

for val in the_list:
    if val > largest_value:
        largest_value = val
    

    
    


max_in = 0

for val in the_list:
    if val > max_in:
        max_in = val

import math 


def circle_perimeter(radius):
    perimeter = math.pi * 2 * radius
    return perimeter

"""
""" 
def print_even_numbers(start, stop):
    if start % 2 != 0: 
        start += 1
    for i in range(start, stop, 2):
            print(i)
        
"""

""" total = 0 
for i in range(0, 1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)
"""
""" celsius = 0 
def fahrenheit_to_celsius(temp):
    celsius = temp - 32 / 1.8
    return celsius


fahrenheit_to_celsius(200)

import string 

import string 

def num_pairs():
    for first in string.ascii_lowercase:
        for second in string.ascii_lowercase:
            print(first + second)  
            
num_pairs()


FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]
def sorbet_menu():
    for f1 in FLAVORS:
        for f2 in FLAVORS:
            if f1 != f2 or f2 != f1:
                print(f1 + ", " + f2)
                
sorbet_menu() """

x = ('apple', 'banana', 'cherry')
y = enumerate(x) 

print(x)