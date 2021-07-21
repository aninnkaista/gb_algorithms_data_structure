def prove_sum(n):
    """To prove the summing formula"""
    # independent calculation
    calc_sum = sum(range(1, n+1))
    form_sum = n * (n + 1) / 2
    if calc_sum == form_sum:
        print(f'Given formula for the sequence of {n} integers is true')
    else:
        print('Something went wrong..')

if __name__ == '__main__':
    cur_n = int(input('Enter positive integer to check the formula: '))
    prove_sum(cur_n)