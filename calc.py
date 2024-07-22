import numpy as np

def calc(x):
    try:
        print(str(eval(x,{"__builtins__":None},{})))
    except:
        print("Error!")

while True:
    times = input("Input: ")
    calc(times)