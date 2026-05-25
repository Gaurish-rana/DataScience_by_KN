'''Real-World Example: Multiprocessing for CPU bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers, involve significant computational work.
Multiprocessing can be used to distribute the workload across multiple CPU core, improving performance.
'''

import multiprocessing
import math
import sys
import time

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

# Function to compute the factorial of a given number
def compute_fac(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__=="__main__":
    numbers=[5000,6000,700,8000]

    start_time=time.time()

    # Create a pool of worker processes
    with multiprocessing.Pool() as pool: # This line creates a group (pool) of worker processes that can work at the same time.
        results=pool.map(compute_fac,numbers) # distributes tasks among them to execute in parallel and return the results.

    end_time=time.time()

    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")