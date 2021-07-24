def find_2_mins(masiv: list):
    """To find 2 min els from the list. Returns those 2 numbers"""
    # to find the first min
    min_1 = min(masiv)
    # remove it (the first occurrence)
    masiv.remove(min_1)
    # find the second min
    min_2 = min(masiv)

    return min_1, min_2