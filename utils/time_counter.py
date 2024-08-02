from imports import *
from data.data import *

N = 0


def update():
    global N
    N = N + 1


def time_counter(duration, function: str):
    a = 0

    while a < UPS * duration:
        start_time = time.time()
        for i in range(FPU):
            eval(function)
        while time.time() - start_time <= 1 / UPS:
            pass
        a += 1


tic = time.time()
time_counter(0.001, "update()")
tac = time.time()
print(N)
print(tac - tic)
