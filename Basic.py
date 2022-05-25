
# https://codelearn.io/learning/python-fundamentals



###array - vector --------------------------------------------------


# a = [12, 13 ,14, 15]

# print(*a)


# the same as print(*a)
# for i in a: 
#     print(i, end = " ")

# a = input("Enter your numbers: ")

# list = []

# list.append(a)
# print(*list)

# a = list(map(int, input("Enter something: ").split()))
# print(a)

# a = list(map(int, input("Enter something: ").split()))

# print([i for i in a if i%2 == 0])



###filter ---------------------------------------------------------

# age = [5, 12, 17, 25, 32]

# def myFunc(x): 
#     return x%2==0
 
# b = filter(myFunc, age)

# print(list(b))

##nump libary----------------------------------------------------- 

# https://www.youtube.com/watch?v=QUT1VHiLmmI ---- MUST WATCH!!!!

import numpy as np 
import matplotlib.pyplot as plt # ******** Research more on this part!!! **********


# arr = np.array((45,1,6,4,5)) # This is an actual list, it is wayy faster thus allowing us to handle picture and data processing. 

# print(np.sort(arr))

# speed = [57,67,54,55,65,59,59]

# x = np.std(speed) # This is to find out how fast the program to compute 

# print(x) 

# age = [5,31,43,48,50,41,7,11,15,39,80,42,33,12,39,23]

# y = np.sort(age)

# x = np.percentile(age,50)

# print(y)
# print(x)
x = np.random.uniform(1.0,5.0,100) # ******** Research more on this part!!! **********
print(x)
plt.hist(x,30) # ******** Research more on this part!!! **********
plt.show() # ******** Research more on this part!!! **********











