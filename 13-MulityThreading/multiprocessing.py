##multiprocessing

import multiprocessing
import time

def square_number():
    for i in range (5):
        print("Square:", i*i)
        time.sleep(0.5)

def cube_number():
    for i in range (5):
        print("Cube:", i*i*i)
        time.sleep(0.5)

square_number()
cube_number()

##create 2 process

process1 = multiprocessing.Process(target=square_number)
process2 = multiprocessing.Process(target=cube_number)

process1.start()
process2.start()

process1.join()
process2.join()
