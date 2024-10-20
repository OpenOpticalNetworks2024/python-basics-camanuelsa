"""Exercise Set 1: Python Basics"""

import numpy as np
import matplotlib as plt


# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    product = num1 * num2
    if product > 1000:
        sum = num1 + num2
        print("The sum is:", sum)
    else:
        print("The product is:", product)


# ex2
def exercise2():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    if start > end:
        print("Start number should be less than or equal to end number.")
        return
    previous_number = 0
    for i in range(start, end + 1):
        current_sum = previous_number + i
        print(f"Current number: {i}, Previous number: {previous_number}, Sum: {current_sum}")
        previous_number = i


# ex3
def exercise3():
    nums = []
    num = int(input("Enter an integer (or '-1' to finish): "))
    while num != -1:
            nums.append(num)
            num = int(input("Enter another integer (or '-1' to finish): "))
    if nums[0]==nums[-1]:
        print(f"Both numbers are equal to {nums[0]}")
    else:
        print("The start and the end of the list are not equal")


# ex4
def exercise4():
    nums = []
    num = int(input("Enter an integer (or '-1' to finish): "))
    while num != -1:
            nums.append(num)
            num = int(input("Enter another integer (or '-1' to finish): "))
    for i in range(len(nums)):
        if nums[i] % 5 == 0:
            print(nums[i], " is divisible by 5")


# ex5
def exercise5():
    sen = "Emma is a good developer. Emma is also a writer"
    tim = sen.count("Emma")
    print(f"Emma is present {tim} times in the sentence: {sen}")

# ex6
def exercise6():
    nums1 = []
    num = int(input("Enter an integer (or '-1' to finish) for list 1: "))
    while num != -1:
            nums1.append(num)
            num = int(input("Enter another integer (or '-1' to finish) for list 1: "))
    nums2 = []
    num = int(input("Enter an integer (or '-1' to finish) for list 2: "))
    while num != -1:
            nums2.append(num)
            num = int(input("Enter another integer (or '-1' to finish) for list 2: "))
    print("The first list is: ", nums1)
    print("The second list is: ", nums2)
    oddeven = []
    for i in range(len(nums1)):
        if nums1[i] % 2 == 1:
            oddeven.append(nums1[i])
            print(f"The odd number {nums1[i]} is added to the third list")
    for i in range(len(nums2)):
        if nums2[i] % 2 == 0:
            oddeven.append(nums2[i])
            print(f"The even number {nums2[i]} is added to the third list")
    print("The third list is: ", oddeven)


# ex7
def exercise7():
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    s3 = s1[:len(s1)//2] + s2 + s1[len(s1)//2:]
    print("The resulting string is: ", s3)


# ex8
def exercise8():
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    s3_1 = s1[0] + s1[len(s1) // 2] + s1[-1]
    s3_2 = s2[0] + s2[len(s2) // 2] + s2[-1]
    s3 = s3_1 + s3_2
    print("The resulting string is: ", s3)


# ex9
def exercise9():
    s = input("Enter the string: ")
    low = 0
    up = 0
    dig = 0
    sps = 0
    for char in s:
        if char.islower():
            low += 1
        elif char.isupper():
            up += 1
        elif char.isdigit():
            dig += 1
        else:
            sps += 1
    print("Lowercase characters: ", low)
    print("Uppercase characters: ", up)
    print("Digits: ", dig)
    print("Special symbols: ", sps)


# ex10
def exercise10():
    s = input("Enter a string: ")
    print("The number of occurrences of 'USA' is: ", s.lower().count("usa"))


# ex11
def exercise11():
    s = input("Enter the string: ")
    sum = 0
    dig = 0
    for char in s:
        if char.isdigit():
            sum += int(char)
            dig += 1
    if dig != 0:
        avg = sum / dig
    else:
        avg = 0
    print("Sum of the digits: ", sum)
    print("Average of the digits: ", avg)


# ex12
def exercise12():
    s = input("Enter the string: ")
    dict = {}
    for char in s:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    for char, cnt in dict.items():
        print(f"'{char}': {cnt} times")


if __name__ == "__main__":
    print("EXERCISE SET 1")
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
    print("EX9")
    exercise9()
    print("EX10")
    exercise10()
    print("EX11")
    exercise11()
    print("EX12")
    exercise12()
