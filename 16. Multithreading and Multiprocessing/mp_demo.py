# Multiprocessing

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Cube: {i*i*i}")


if __name__ == "__main__": # It ensures that the code runs only when the file is executed directly, not when it is imported, and it is essential for multiprocessing on Windows to prevent infinite process creation.

    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    t = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finished = time.time() - t
    print(finished)
