#------8--------
# matrix size
rows = 5
cols = 4
# to create empty list for matrix
m = []
# to fill in matrix by rows
for i in range(rows):
    j = list(map(float, input(f'Enter {i+1} row of the matrix consisting of {cols} elements').split()))
    # to add sum of els as the last element
    j.append(sum(j))
    # add row to matrix
    m.append(j)

# to print matrix
for i in range(rows):
    for j in range(cols+1):
        print(m[i][j], end='\t')
    print()


#--------9------------
def max_min_cols(matrix: list, nrows, ncols) -> float:
    """To return the maximum element from min of matrix cols given matrix and its size as arguments"""
    min_list = []
    # to find the list of minimum values across the columns
    for i in range(ncols):
        cur_col = []
        a = matrix[0][i]
        for j in range(1, nrows):
            if matrix[j][i] < a:
                a = matrix[j][i]
        min_list.append(a)
    # to return maximum element of min from cols
    return max(min_list)
