Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> numbers_list=[1,2,3,4,5]
>>> fruits_list=['apple','banana','watermelon','grapes']
>>> float_list=[1.5,1.7,2.6,7.9,3.1]
>>> boolean_list=[true,false,true,false]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    boolean_list=[true,false,true,false]
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> print(fruit_list[0])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(fruit_list[0])
NameError: name 'fruit_list' is not defined. Did you mean: 'fruits_list'?
>>> print(fruits_list[0])
apple
>>> print(fruits_list[2])
watermelon
>>> print(fruits_list[-2])
watermelon
>>> fruits_list[1]='blueberry'
>>> print(fruits_list)
['apple', 'blueberry', 'watermelon', 'grapes']
>>> fruits_list.append('orange')
>>> print(fruits_list)
['apple', 'blueberry', 'watermelon', 'grapes', 'orange']
>>> fruits_list.insert(1,'kiwi')
>>> print(fruits_list)
['apple', 'kiwi', 'blueberry', 'watermelon', 'grapes', 'orange']
>>> fruits_list.remove('kiwi')
>>> print(fruits_list)
['apple', 'blueberry', 'watermelon', 'grapes', 'orange']
>>> last_fruit=fruits_list.pop()
>>> print(last_fruit)
orange
>>> fruits_list.clear()
>>> print(fruits_list)
[]
numbers=[0,1,2,3,4,5,6,7,8,9]
print(numbers[1:4])
[1, 2, 3]
print(numbers[:9])
[0, 1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[0:])
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(numbers))
10
number.sort()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    number.sort()
NameError: name 'number' is not defined. Did you mean: 'numbers'?
numbers.sort()
print(numbers)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.reverse()
print(numbers)
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(fruits_list.index('apple'))
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(fruits_list.index('apple'))
ValueError: 'apple' is not in list
fruits_list=['apple','banana','watermelon','grapes']
print(fruits_list.count('watermelon'))
1
print(fruits_list.index('apple'))
0
