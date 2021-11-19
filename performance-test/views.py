"""
All web app views (aka routes) for flask application found in here.
"""

from typing import List
from time import perf_counter
from flask import (Blueprint, render_template)



# Configure Blueprint
main = Blueprint("main", __name__)


@main.route('/')
def main_index():
    """Main index route 'Homepage'

    Returns:
        GET - index.html template.

    """
    # Start the timer
    t0 = perf_counter()

    calculatePrimes(1,20000)

    # Stop the timer
    t1 = perf_counter()

    time = t1-t0

    return render_template("index.html", time=time)

def calculatePrimes(min: int, max: int) -> List[int]:
    """
    Returns a list containing all prime numbers 
    between min and max range values.

    Args:
        min: minimum integer value in range.
        max: maximum integer value in range.

    Returns:
        A list of prime intergers between min and max range. 
        Empty list returned if none calculated.
    """

    primes = []

    for num in range(min, max + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)

    return primes