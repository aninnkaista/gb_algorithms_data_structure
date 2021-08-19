stroka = 'banana'
def count_comb(stroka: str)-> int:
    # to calculate all of the different combinations
    set_comb = set()
    for length in range(1, len(stroka)):
        for i in range(0, len(stroka), length):
            if len(stroka[i:(i + length)]) == length:
                  set_comb.add(stroka[i:(i + length)])
    count_dif_comb = len(set_comb)
    return count_dif_comb

print(count_comb(stroka))
