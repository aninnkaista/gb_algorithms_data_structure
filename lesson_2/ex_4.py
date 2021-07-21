import sys
n = int(input('Enter a number of elements to add: '))
# to check if it is non-negative number
if n < 0:
    print('Number of elements should be non-negative integer')
    sys.exit()


def get_row_sum(n: int) -> float:
    """To get the sum of n elements in a row"""
    if n == 0:
        return 0
    else:
        return ((-0.5) ** (n-1)) + get_row_sum(n-1)


# to print the result
print(f'The total sum of the row of {n} elements is {get_row_sum(n)}')