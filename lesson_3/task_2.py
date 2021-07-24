def return_ind_even(seq: list) -> list:
    """To return list of indices of the even numbers in the given list.
    Indices start from 1. """
    output_list = list()
    for i in range(len(seq)):
        if seq[i] % 2 == 0:
            output_list.append(i + 1)
    return output_list