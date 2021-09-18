def bubble_sort_desc(list_to_sort):
    """To sort given list with bubble sort descending"""
    sorted_list = list_to_sort.copy()
    # outer cycle from 0 to LEN-2
    for i in range(len(sorted_list) - 1, 0, -1):
        # inner cycle from 0 to i-1
        for j in range(i):
            # to compare two neighbouring numbers
            if sorted_list[j] < sorted_list[j+1]:
                # if number at index j is smaller than at j+1 then switch them
                a = sorted_list[j]
                sorted_list[j] = sorted_list[j+1]
                sorted_list[j+1] = a
    return sorted_list

my_list = [3, 11, 2, -5, 6, 7, 5]
# to print initial list
print(my_list)
sorted_my_list = bubble_sort_desc(my_list)
print(sorted_my_list)