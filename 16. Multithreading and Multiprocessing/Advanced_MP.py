# Multiprocessing using Process Pool Executer

from concurrent.futures import ProcessPoolExecutor
import time

def square_numbers(number):
    time.sleep(1)
    return f"Square : {number*number}"

numbers=[1,2,3,4,5]


if __name__=="__main__": # Ensures the code runs safely when creating new processes (mandatory on Windows).
    with ProcessPoolExecutor(max_workers=3) as executor: #Creates a pool of 3 worker processes.
        results=executor.map(square_numbers,numbers) # Distributes the numbers among the processes and executes square_numbers() in parallel.

    for result in results:
        print(result)
