def mergeSort(my_list):
    if len(my_list) > 1:
        middle = len(my_list) // 2
        first_half = mergeSort(my_list[:middle])
        second_half = mergeSort(my_list[middle:])
        my_list = mergeArr(first_half, second_half)
    return my_list




def mergeArr(arr_left: list, arr_right: list) -> list:
    if arr_right is None:
        return arr_left
    new_arr = []
    while len(arr_left) > 0 and len(arr_right) > 0:
        if arr_left[0] < arr_right[0]:
            new_arr.append(arr_left.pop(0))
        else:
            new_arr.append(arr_right.pop(0))
    new_arr.extend(arr_left)
    new_arr.extend(arr_right)
    return new_arr

if __name__ == '__main__':
    my_array = [15, 18, 5, 4, 9, 8, 7, 1, 3, 10, 12]
    print(mergeSort(my_array))
