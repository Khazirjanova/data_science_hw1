import time
import random
from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer
from task3 import decorator_1


@decorator_1
def func1():
    # print("I am ready to Start")
    result = 0
    n = random.randint(10000, 300000)
    for i in range(n):
        result += (i ** 2)


@decorator_1
def func2(n=2, m=5):
    # print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(35000, 40000)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i


if __name__ == "__main__":
    print("--------------------------------------------------------------------------")
    print("Task 1. The function is called and started running.")
    kwargsAcceptFun(book="Data Science", year=2025, hw="Number 1")
    print("Task 1 finished\n")
    print("--------------------------------------------------------------------------")

    print("Task 2. The function is called and started running.")
    print(typeBasedTransformer(a=3.5, b="Data Science", c=False, d=[10, 11, 12], e={"x": 13, "y": 23}))
    print("Task 2 completed!\n")
    print("--------------------------------------------------------------------------")

    print("Task 3. The function is called and started running.")
    func1()
    func2()
    func1()
    func2()
    func1()
    print("Task 3 completed!\n")
    print("--------------------------------------------------------------------------")

    print("All tasks completed!")
