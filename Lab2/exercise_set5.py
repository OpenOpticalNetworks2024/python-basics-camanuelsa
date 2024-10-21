"""Exercise Set 5: JSON"""

import numpy as np
import matplotlib as plt
import json
#json_obj = '{" Name ": " David ", " Class ": "I", "Age ": 6}'
#python_obj = {'name':'David','class':'I','age':6}
# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    json_obj = '{" Name ": " David ", " Class ": "I", "Age ": 6}'
    dic = json.loads(json_obj)
    print("Dictionary: ", dic)

# ex2
def exercise2():
    python_obj = {'name': 'David', 'class': 'I', 'age': 6}
    json_obj = json.dumps(python_obj, indent=2)
    print("JSON Data: ")
    print(json_obj)


# ex3
def exercise3():
    python_obj = {'name': 'David', 'class': 'I', 'age': 6}
    json_str = json.dumps(python_obj)
    print("JSON String: ", json_str)


# ex4
def exercise4():
    python_obj = {'name': 'David', 'class': 'I', 'age': 6}
    json_obj = json.dumps(python_obj, sort_keys=True, indent=2)
    print("JSON Data:")
    print(json_obj)


# ex5
def exercise5():
    file = open('../states.json', 'r')
    data = json.load(file)
    file.close()
    for state in data["states"]:
        if "area_codes" in state:
            del state["area_codes"]
    new_file = open('../statesNAC.json', 'w')
    json.dump(data, new_file, indent=2)
    new_file.close()
    print("New JSON file created without the 'area_codes' field.")


if __name__ == "__main__":
    print("EXERCISE SET 5")
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
