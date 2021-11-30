import math
import time


def my_decorator(func):
    def wrap(*args):
        print("Function: ", func.__name__, "called")
        Start = time.time()
        res = func(*args)
        print("Time taken for execution: ", time.time()-Start, "ns\n\n")
        return res
    return wrap


@my_decorator
def calculate_sqare(w, h):
    const = 0.000022957
    return (w**2) * const * (h**2) * const


@my_decorator
def get_velocity(height):
    start_speed = 0
    speed_up = 9.8
    return math.sqrt(start_speed**2)+2*speed_up*height


inp = input("Task №1\nPlease, input width and height: ").split()
w, h = int(inp[0]), int(inp[1])
print("Result:", calculate_sqare(w, h))

inp = input("Task №2\nPlease, input height: ")
print("Result:", get_velocity(int(inp)))
