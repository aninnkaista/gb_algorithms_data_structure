# MEMORY UTILIZATION IN LESSON_/EX_1 Python 3.8.10 Architecture: x86-64
"""
- the size of a function is 136 bits
- the size of an empty dict is 232 and python has allocated memory for 10 pointers right away, overall size of dictionary
    is then 360 bits; dict also contains 8 ints * 28 bits, so overall size would be 584 bits
- in a loop range is used of size 48 bits, then each integer from 2 to 99 takes up 28 bits, so overall
    98 * 28 + 48 = 2792 bits of memory,  but it is not stored in a variable, so after loop memory should be freed
- cur_number and cur_div refer to ints of sizes 28 bits which are already used in dict and range
- the size of None is 16 bits
"""

@profile
def my_function():
    count_div = dict(zip(range(2, 10), [0]*8))
    # to calculate the division for each of numbers from the dict
    for cur_number in range(2, 100):
        # by increasing values by 1 if divisible
        for cur_div in count_div.keys():
            if cur_number % cur_div == 0:
                count_div[cur_div] += 1
    # print the result
    print('(Number, count) pairs:', *count_div.items(), sep='\n')
    return None

if __name__ == "__main__":
    my_function()