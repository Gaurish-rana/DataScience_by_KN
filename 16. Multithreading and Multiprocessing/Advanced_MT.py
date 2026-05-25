# Mutithreading using Thread Pool Executer

from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(number):
    time.sleep(1)
    return f"Number : {number}"

numbers=[1,2,3,4,5]

with ThreadPoolExecutor(max_workers=3) as executor: # Creates a thread pool with 3 threads running at the same time.
    results=executor.map(print_numbers,numbers) # Assigns each number to a thread, calling print_numbers() in parallel and storing the results.

for result in results:
    print(result)
