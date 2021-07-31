def init_function(func_name):
    return f"""
from __main__ import {func_name}
inp_number = input('Please enter your number: ').strip()
"""

# recursion
def get_reverse_rec(inp_number: str) -> str:
    """Gets input number as a string and returns reverse number as a string as well"""
    if len(inp_number) == 1:
        return inp_number
    else:
        return inp_number[-1] + get_reverse_rec(inp_number[:-1])

# reverse index
def get_reverse_list(inp_number: str) -> str:
    return inp_number[::-1]

# reverse loop
def get_reverse_loop(inp_number: str) -> str:
    opp_number = ''
    for i in range(len(inp_number)-1, -1, -1):
        opp_number += inp_number[i]
    return opp_number

# to measure execution time
# from timeit import timeit
#
# print('Recursion function time is ', timeit(setup=init_function('get_reverse_rec'),
#              stmt="get_reverse_rec(inp_number)",
#              number=10000))
#
# print('Reverse index function time is ', timeit(setup=init_function('get_reverse_list'),
#                                                     stmt="get_reverse_list(inp_number)",
#                                                     number=10000))
# print('Loop function time is', timeit(setup=init_function('get_reverse_loop'),
#                                       stmt="get_reverse_loop(inp_number)",
#                                       number=10000))
# """As the result of time mesurement for input number of 56789 the timing of:
#     - recursion function was the slowest, about 6 times slower than reverse index and about 1,5 times slower than loop
# """

# profiling the execution
import cProfile
# to increase recursion depth
import sys
sys.setrecursionlimit(2000)
def main():
    inp_number = '4657465745646541545'*100
    rec_output = get_reverse_rec(inp_number)
    ind_output = get_reverse_list(inp_number)
    loop_output = get_reverse_loop(inp_number)

cProfile.run('main()')

"""The only available result is for recursion execution that runs function 1900 times and tottime is 0.006s other times were rounded to 0"""