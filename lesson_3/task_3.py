def swap_max_min(masiv: list) -> list:
    """The function to swap max and min elements of the list
    The function takes as an input list of values and returns list of values with swapped min and max"""
    # min element
    min_el = min(masiv)
    # to find all indices corresponding to min element in the array
    ind_min = []
    i = -1
    while min_el in masiv[i+1:]:
        i = masiv.index(min_el, i+1)
        ind_min.append(i)
    # maximum element
    max_el = max(masiv)
    # to find all indices corresponding to max elements in the array
    ind_max = []
    i = -1
    while max_el in masiv[i+1:]:
        i = masiv.index(max_el, i+1)
        ind_max.append(i)
    # substitute min values with maximum values
    for i in ind_min:
        masiv[i] = max_el
    # substitute max values with minimum values
    for i in ind_max:
        masiv[i] = min_el

    return masiv