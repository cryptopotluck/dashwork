import numpy as np

mylist = [1,2,3,4]

#convert list to a array
arr = np.array(mylist)

#build a array 0->9
a = np.arange(0,10)

#step size
a = np.arange(0,10,2)

#Build a 2D array of 0
np.zeros((5,5))

#Build 2d array 1
np.ones((2,4))

#return a random number 0-99
np.random.randint(0,100)

#return a random 2d array
np.random.randint(0,100,(5,5))

#return 6 numbers and equally space them 0->10
np.linspace(0,10,6)

#seed the same random generator
np.random.seed()

#---------------------------
arr2 = np.random.randint(0,100,10)

print(arr2)

#calls highest number
arr2.max()

#calls smallest number
arr2.min()

#add all numbers & devide
arr2.mean()

#index of max number
arr2.argmax()

#reshape array
arr2.reshape(2,5)
#-----------------------

mat = np.arange(0,100).reshape(10,10)

#call a specific area
mat[5,2]

#call a collum
mat[:,2]

#call a row
mat[3,:]

#call numbers higher than 50
mat[mat>50]

