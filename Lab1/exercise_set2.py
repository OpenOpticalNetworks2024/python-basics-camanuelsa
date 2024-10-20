"""Exercise Set 2: Data Structures"""

import numpy as np
import matplotlib as plt

# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    listOne = [3, 6, 9, 12, 15, 18, 21]
    listTwo = [4, 8, 12, 16, 20, 24, 28]
    odd = listOne[1::2]
    even = listTwo[0::2]
    listThree = odd + even
    print("The third list will be: ", listThree)

# ex2
def exercise2():
    sampleList = [34, 54, 67, 89, 11, 43, 94]
    item = sampleList[4]
    sampleList.pop(4)
    sampleList.insert(2, item)
    sampleList.append(item)
    print("The list will be: ", sampleList)


# ex3
def exercise3():
    sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    List1 = sampleList[:int(len(sampleList)/3)]
    List1.reverse()
    List2 = sampleList[int(len(sampleList)/3):int(len(sampleList)*2/3)]
    List2.reverse()
    List3 = sampleList[int(len(sampleList)*2/3):int(len(sampleList))]
    List3.reverse()
    print("The first list will be: ", List1)
    print("The second list will be: ", List2)
    print("The third list will be: ", List3)

# ex4
def exercise4():
    sampleList = [11, 45, 8, 11, 23, 45, 23, 45, 89]
    dict = {}
    for num in sampleList:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    for num, cnt in dict.items():
        print(f"'{num}': {cnt} times")


# ex5
def exercise5():
    firstList = [2, 3, 4, 5, 6, 7, 8]
    secondList = [4, 9, 16, 25, 36, 49, 64]
    pairset = set(zip(firstList, secondList))
    print("The paired set is: ", pairset)


# ex6
def exercise6():
    firstSet = {23, 42, 65, 57, 78, 83, 29}
    secondSet = {57, 83, 29, 67, 73, 43, 48}
    setIntersection = firstSet.intersection(secondSet)
    firstSet -= setIntersection
    print("The first set without intersection is: ", firstSet)


# ex7
def exercise7():
    firstSet = {57, 83, 29}
    secondSet = {57, 83, 29, 67, 73, 43, 48}
    if firstSet.issubset(secondSet):
        firstSet -= firstSet.intersection(secondSet)
        print("The first set is a subset of the second")
    if secondSet.issubset(firstSet):
        secondSet -= firstSet.intersection(firstSet)
        print("The second set is a subset of the first")
    if firstSet.issuperset(secondSet):
        secondSet -= firstSet.intersection(firstSet)
        print("The first set is a superset of the second")
    if secondSet.issuperset(firstSet):
        firstSet -= firstSet.intersection(secondSet)
        print("The second set is a superset of the first")

# ex8
def exercise8():
    rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
    sampleDict = {"Jhon":47, "Emma":69, "Kelly":76, "Jason":97}
    i = 0
    while i<len(rollNumber):
        bool = True
        for key, value in sampleDict.items():
            if value == rollNumber[i]:
                bool = False
                print(f"The value {rollNumber[i]} has a key {key}")
                i += 1
                break
        if bool:
            print(f"The value {rollNumber[i]} hasn't a key so it's removed")
            rollNumber.pop(i)


# ex9
def exercise9():
    speed = {"Jan":47, "Feb":52, "March":47, "April":44, "May":52,
    "June":53, "July":54, "Aug":44, "Sept":54}
    list1 = list(set(speed.values()))
    print("The list of the values without duplicates is: ", list1)


# ex10
def exercise10():
    sampleList = [87, 52, 44, 53, 54, 87, 52, 53]
    noDups = list(set(sampleList))
    tpl = tuple(noDups)
    print("The tuple is: ", tpl)
    print("The maximum value is: ", max(tpl))
    print("The minimum value is: ", min(tpl))

if __name__ == "__main__":
    print("EXERCISE SET 2: Data Structures")
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
