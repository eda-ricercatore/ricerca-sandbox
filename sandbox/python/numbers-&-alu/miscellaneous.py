#!/Users/zhiyang/anaconda3/bin/python3
###!/usr/local/bin/python3


import numpy as np
# From https://docs.python.org/3/library/statistics.html
import statistics as s
# Use the math.ceil() and math.floor() functions
import math


# Python code to illustrate  
# abs() built-in function 
  
# floating point number 
float = -54.26
print('Absolute value of float is:', abs(float)) 
  
# An integer 
int = -94
print('Absolute value of integer is:', abs(int)) 
  
# A complex number 
complex = (3 - 4j) 
print('Absolute value or Magnitude of complex is:', abs(complex)) 



"""
	Methods to find the average number of numbers in a list.
	
	https://www.geeksforgeeks.org/find-average-list-python/
"""


my_list = [2, -3, 5, -9, -6, 8]
abs_my_list = []
for elem in my_list:
	abs_my_list.append(abs(elem))
print("abs_my_list:",abs_my_list,"=")

abs_my_list_2 = []
for index, elem in enumerate(my_list):
	#print("index:",index,"=")
	abs_my_list_2.insert(index,abs(elem))
print("abs_my_list_2:",abs_my_list_2,"=")

abs_my_list_3 = np.absolute(my_list)
print("abs_my_list_3:",abs_my_list_3,"=")



#sum_of_absolute_numbers = sum(abs(my_list))
sum_of_absolute_numbers = sum(abs_my_list)
print("sum_of_absolute_numbers:",sum_of_absolute_numbers,"=")
#average_of_absolute_numbers = sum(abs(my_list))/len(my_list)
average_of_absolute_numbers = sum(abs_my_list)/len(abs_my_list)
print("average_of_absolute_numbers:",average_of_absolute_numbers,"=")
average_of_absolute_numbers = np.mean(abs_my_list)
print("average_of_absolute_numbers, via NumPy:",average_of_absolute_numbers,"=")
average_of_absolute_numbers = s.mean(abs_my_list)
print("average_of_absolute_numbers, via statistics module/package:",average_of_absolute_numbers,"=")
average_of_absolute_numbers = sum(abs_my_list_3)/len(abs_my_list_3)
print("average_of_absolute_numbers, for abs_my_list_3:",average_of_absolute_numbers,"=")
print("	This solution produces a rounded-off/down solution.")
average_of_absolute_numbers = s.mean(abs_my_list_3)
print("average_of_absolute_numbers, via NumPy and absolute():",average_of_absolute_numbers,"=")


x = None
if x:
	print("if x")
if x is not None:
	print("if x is not None")
if x is None:
	print("if x is None")



"""
	In this case, they are the same. None is a singleton object (there only ever exists one None).
	is checks to see if the object is the same object, while == just checks if they are equivalent.
	
	Reference:
		https://stackoverflow.com/a/3257951/1531728
"""
p = [1]
q = [1]
if p is q:
	print("p is q; [1] is [1]; something is wrong!!!")
else:
	print("False because they are not the same actual object.")
if p == q:
	print("p == q; [1] == [1]")
	print("True because they are equivalent.")
else:
	print("p != q; [1] != [1]; something is wrong!!!")
# But since there is only one None, they will always be the same, and is will return True.
p = None
q = None
p is q # True because they are both pointing to the same "None"


a = 32.1923
b = math.floor(a)
print("b is:",b,".")
c = math.floor(a)
print("c is:",c,".")
"""
	Use the round() function to round off numbers, instead of the
		following functions.
	+ math.ceil()
	+ math.floor()
"""
d = round(a)
print("d is:",d,".")
d = round(54.9744)
print("d is:",d,".")
d = round(546789.57928)
print("d is:",d,".")
d = round(152.5)
print("d is:",d,".")



print("--------------------------------------------")
try:
	print("Dividing a number, 23, by 0", 23/0,"=")
except ZeroDivisionError:
	print("Cannot dividing 23 by 0.")