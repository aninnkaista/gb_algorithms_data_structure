def find_max_negative(masiv: list):
    """To find the maximum negative element"""
    # to select all negative elements in masiv
    neg_masiv = [i for i in masiv if i < 0]
    # to find maximum
    max_neg = max(neg_masiv)

    return max_neg
