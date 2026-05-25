cross multiple CPU core, improving performance.
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