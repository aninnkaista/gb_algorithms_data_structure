# MEMORY CALCULATION
"""
- the size of my_function is 136 bits
- the size of len_row is 28 bit
- maximum size of list cur_row is 184 bit (init size of 56 bit + adding elements creats additional space for 4 additional pointers)
- then list contains 10 strings of len 3, so each of them takes up 49+3 = 52 bits, that is total 520 bits
- after each row is printed, variable cur_row is assigned with new empty list and filled anew, so reference for old lists
    is substituted by a new one and memory taken up by an old list should be freed;
so at any time of function run maximum amount of memory used is 136 + 28 + 184 + 520 = 868 bits
"""
def my_function():
    len_row = 10
    cur_row = list()
    # to go through all symbols from 32 to 127
    for i in range(32, 122):
        # make rows
        if len(cur_row) < len_row:
            cur_row.append(str(i) + ' ' + chr(i))
        else:
            # once it reaches 10 elements, print, empty and start adding again
            print(*cur_row, sep='\t')
            cur_row = list()
            cur_row.append(str(i) + ' ' + chr(i))
    # if cur_row is not left empty, print the last row
    if cur_row:
        print(*cur_row, sep='\t')
    return None


if __name__ == '__main__':
    my_function()