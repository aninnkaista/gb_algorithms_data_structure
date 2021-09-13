my_list = [5, 1, 4, 8, 7, 6, 1, 3, 9, 8, 7]

middle = len(my_list) // 2 + 1
i = len(my_list) - 1
# go from the left and from the right
while i != middle:
    max_len = i
    for l in range(0, i):
        if my_list[l] > my_list[i]:
            for r in range(i-1, l, -1):
                if my_list[r] < my_list[i]:
                    max_len = r
                    a = my_list[r]
                    my_list[r] = my_list[l]
                    my_list[l] = a
                    break
    a = my_list[max_len]
    my_list[max_len] = my_list[i]
    my_list[i] = a
    if i > middle:
        i = max_len - 1
    else:
        i = max_len + 1

print(i)




