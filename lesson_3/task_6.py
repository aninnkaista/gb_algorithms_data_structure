def find_sum_bn_min_max(masiv: list) -> float:
    """
    To find the sum of elements between indices of max and min.
    Not including max and min elements. Returns this sum.
    """
    # to find the index of max el
    ind_max = masiv.index(max(masiv))
    # to find the index of min el
    ind_min = masiv.index(min(masiv))
    # to check which index is first and then find the sum of els in between
    if ind_min > ind_max + 1:
        m_sum = sum(masiv[ind_max+1:ind_min])
    elif ind_min < ind_max - 1:
        m_sum = sum(masiv[ind_min+1:ind_max])
    else:
        m_sum = 0
    return m_sum



