len_row = 10
cur_row = list()
# to go through all symbols from 32 to 127
for i in range(32, 122):
    # make rows
    if len(cur_row) < 10:
        cur_row.append(str(i) + ' ' + chr(i))
    else:
        # once it reaches 10 elements, print, empty and start adding again
        print(*cur_row, sep='\t')
        cur_row = list()
        cur_row.append(str(i) + ' ' + chr(i))
# if cur_row is not left empty, print the last row
if cur_row:
    print(*cur_row, sep='\t')