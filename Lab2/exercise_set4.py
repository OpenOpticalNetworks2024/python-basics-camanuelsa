"""Exercise Set 4: Pandas & Matplotlib"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    df = pd.read_csv("../sales_data.csv")
    plt.plot(df['month_number'], df['total_profit'])
    plt.show()


# ex2
def exercise2():
    df = pd.read_csv("../sales_data.csv")
    plt.plot(df['month_number'], df['total_profit'], color='r', marker='o', markerfacecolor='k', linestyle='-', linewidth=3)
    plt.title('Profile data of last year')
    plt.show()


# ex3
def exercise3():
    df = pd.read_csv("../sales_data.csv")
    plt.plot(df['month_number'], df['facecream'], label='Facecream', marker='o')
    plt.plot(df['month_number'], df['facewash'], label='Facewash', marker='o')
    plt.plot(df['month_number'], df['toothpaste'], label='Toothpaste', marker='o')
    plt.plot(df['month_number'], df['bathingsoap'], label='Bathing Soap', marker='o')
    plt.plot(df['month_number'], df['shampoo'], label='Shampoo', marker='o')
    plt.plot(df['month_number'], df['moisturizer'], label='Moisturizer', marker='o')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.title('Product Sales Data')
    plt.legend()
    plt.grid(True)
    plt.show()


# ex4
def exercise4():
    df = pd.read_csv("../sales_data.csv")
    plt.scatter(df['month_number'], df['toothpaste'])
    plt.xlabel('Month')
    plt.ylabel('Toothpaste sales')
    plt.title('Toothpaste sales over a year')
    plt.grid(True)
    plt.show()


# ex5
def exercise5():
    df = pd.read_csv("../sales_data.csv")
    plt.bar(df['month_number'], df['bathingsoap'])
    plt.xlabel('Month')
    plt.ylabel('Bathing soap sales')
    plt.title('Bathing soap sales over a year')
    plt.grid(True)
    plt.savefig('bathingsoapBar.png')
    plt.show()

# ex6
def exercise6():
    df = pd.read_csv("../sales_data.csv")
    plt.hist(df['total_profit'], edgecolor='black')
    plt.title('All sales over a year')
    plt.grid(True)
    plt.show()


# ex7
def exercise7():
    df = pd.read_csv("../sales_data.csv")
    plt.subplot(121)
    plt.plot(df['month_number'], df['facewash'], marker='o')
    plt.title('Facewash sales over a year')
    plt.grid(True)
    plt.subplot(122)
    plt.plot(df['month_number'], df['bathingsoap'], marker='o')
    plt.title('Bathing soap sales over a year')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    print("EXERCISE SET 4")
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
