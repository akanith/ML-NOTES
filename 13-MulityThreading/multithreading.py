##when to use MuliThrading 

## I\O bound task


import threading
import time

def print_number():
    for i in range (5):
        print("Number:", i)
        time.sleep(0.5)

def print_letter():
    for i in range (5):
        print("Letter:", i)
        time.sleep(0.5)

print_letter()
print_number()

# without multithrading 
# Code to be executed by the thread
def task(name):
    """A simple task that prints numbers"""
    for i in range(5):
        print(f"{name}: {i}")
        time.sleep(0.5)  # Simulate some work (like I/O)

# Create two threads
thread1 = threading.Thread(target=task, args=("Thread-1",))
thread2 = threading.Thread(target=task, args=("Thread-2",))

print("Starting threads...")

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("Both threads have finished.")
