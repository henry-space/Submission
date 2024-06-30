# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 05:51:30 2024

@author: Administrator
"""

# Review 1

def add_to_list(value, my_list=[]):

    my_list.append(value)

    return my_list

'''
Comment: The default value of parameter my_list is List which is mutable.
So that the modifiation on my_list by this function could cause the modifiation the default value []
'''
#Revised version
def add_to_list_v2(value, my_list=[]):
    my_list = list(my_list)
    my_list.append(value)
    return my_list
print(add_to_list_v2(1))
print(add_to_list_v2(1))
print(add_to_list_v2(1,[1,2,3]))

# Review 2

def format_greeting(name, age):

    return "Hello, my name is {name} and I am {age} years old."
'''
Comment: The result will only be "Hello, my name is {name} and I am {age} years old." no matter what the input is 
The syntax of format is incomplete.
'''
#Revised version
def format_greeting_v2(name, age):

    return f"Hello, my name is {name} and I am {age} years old."

print(format_greeting_v2('hhy',26))



# Review 3

class Counter:

    count = 0

 

    def __init__(self):

        self.count += 1

 

    def get_count(self):

        return self.count

'''
Comment: If variable "count" here is to record the number of instances of class Counter,
function __init__ and get_count is only related to modify and show instance variable "count"
rather than class variable "count".
'''
#Revised version:
class Counter_v2: 

    count = 0

 

    def __init__(self):

        Counter_v2.count += 1 #Counter_v2.count rather than self.count 

 
    @staticmethod
    def get_count():

        return Counter_v2.count #Counter_v2.count rather than self.count 

Counter_v2()
print(Counter_v2.get_count())
Counter_v2()
print(Counter_v2.get_count())

# Review 4

import threading

 

class SafeCounter:

    def __init__(self):

        self.count = 0

 

    def increment(self):

        self.count += 1

 

def worker(counter):

    for _ in range(1000):

        counter.increment()

 

counter = SafeCounter()

threads = []

for _ in range(10):

    t = threading.Thread(target=worker, args=(counter,))

    t.start()

    threads.append(t)

 

for t in threads:

    t.join()

'''
The codes "for t in threads: t.join()" seems to want to run the threads one by one
in the order of creation order. But actually the threads are running at the same time which could be non-thread-safe.
'''
#Revised version:
import threading

 

class SafeCounter:

    def __init__(self):

        self.count = 0

 

    def increment(self):

        self.count += 1

 

def worker(counter):

    for _ in range(1000):

        counter.increment()

 

counter = SafeCounter()

threads = []
# The above is not changed

for _ in range(10):

    t = threading.Thread(target=worker, args=(counter,))

    t.start()
    
    t.join()
    
    threads.append(t)
print(counter.count)


# Review 5

def count_occurrences(lst):

    counts = {}

    for item in lst:

        if item in counts:

            counts[item] =+ 1

        else:

            counts[item] = 1

    return counts


'''
"+=" rather than "=+". e.g. a+=1 is equal to a=a+1; a=+1 is equal to a = 1 
'''
def count_occurrences_v2(lst):

    counts = {}

    for item in lst:

        if item in counts:

            counts[item] += 1

        else:

            counts[item] = 1

    return counts

print(count_occurrences_v2([1,2,2,3,3]))
print(count_occurrences_v2([]))