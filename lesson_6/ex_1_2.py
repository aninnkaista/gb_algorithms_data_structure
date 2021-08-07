# MEMORY UTILIZATION OF LESSON_1/EX_8
"""
# the size of function itself leap_year is 136 bits
# the size of input_year is 28 bits, this int is referred then in function leap year
# the size of 4, 400 and 0 is 28 bits
# the size of boolean values True or False is 28 bits

"""

# function to define if leap year
from memory_profiler import profile
@profile(precision=5)
def leap_year(en_year: int) -> bool:
    """
    To return True if year is leap
    and False otherwise
    """
    if en_year % 4 == 0:
        if en_year % 400 == 0:
            return True
        elif en_year % 100 != 0:
            return True
    return False

# user input
if __name__ == "__main__":
    input_year = int(input("Please enter your year: "))
    if leap_year(input_year):
        print("This is leap year")
    else:
        print("This is not leap year")
