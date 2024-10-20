"""Exercise Set 3: Numpy Exercises"""

import numpy as np
import matplotlib as plt

# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    arr = np.empty((4, 2), dtype=np.int16)
    print("The attributes of the array are:", end=" ")
    for row in arr:
        for num in row:
            print(num, end=" ")
    print("\nThe array is:\n", arr)


# ex2
def exercise2():
    arr = np.arange(100, 200, 10).reshape(5, 2)
    print("The attributes of the array are:", end=" ")
    for row in arr:
        for num in row:
            print(num, end=" ")
    print("\nThe array is:\n", arr)


# ex3
def exercise3():
    arr = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
    col3 = arr[:, 2]
    print("The array of items in the third column: ", col3)


# ex4
def exercise4():
    arr = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
    arr2 = np.array(arr[::2,1::2])
    print("The array of items with odd rows and even columns is:\n", arr2)


# ex5
def exercise5():
    arr = np.array([[5, 6, 9], [21 ,18, 27]])
    arr2 = np.array([[15 ,33, 24], [4 ,7, 1]])
    arrRes = np.add(arr, arr2)
    arrSqrt = np.sqrt(arrRes)
    print("The result array of items with a square root is:\n", arrSqrt)


# ex6
def exercise6():
    arr = np.array([[34,43,73],[82,22,12],[53,94,66]])
    arrSort = np.sort(arr)
    print("The sorted array is:\n", arrSort)


# ex7
def exercise7():
    arr = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
    print("The maximum of axis 0 is: ", np.max(arr, axis=0))
    print("The maximum of axis 1 is: ", np.min(arr, axis=1))


# ex8
def exercise8():
    arr = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
    new_column = [10,10,10]
    arr = np.delete(arr, 1, axis=1)
    arr = np.insert(arr, 1, new_column, axis=1)
    print("Modified array:\n", arr)



if __name__ == "__main__":
    print("EXERCISE SET 3: NumPy Exercises")
    print("EX1")
    exercise1()
    print("EX2")
    exercise2()
    print("EX3")
    exercise3()
    print("EX4")
    exercise4()
    print("EX5")
    exercise5()
    print("EX6")
    exercise6()
    print("EX7")
    exercise7()
    print("EX8")
    exercise8()
