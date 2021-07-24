def find_most_common(seq: list):
    """To return the most frequent element(s) in a sequence"""
    # dictionary of all unique elements and their counts
    el_count = dict(zip(set(seq), [seq.count(el) for el in set(seq)]))
    # maximum count
    max_count = max(el_count.values())
    # elements corresponding to maximum counts
    output_els = tuple(el for el in el_count.keys() if el_count[el] == max_count)
    if len(output_els) == 1:
        return output_els[0]
    return output_els

