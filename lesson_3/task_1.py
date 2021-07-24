# to prepare dictionary for division counts with numbers as keys and counts as values
count_div = dict(zip(range(2, 10), [0]*8))
# to calculate the division for each of numbers from the dict
for cur_number in range(2, 100):
    # by increasing values by 1 if divisible
    for cur_div in count_div.keys():
        if cur_number % cur_div == 0:
            count_div[cur_div] += 1
# print the result
print('(Number, count) pairs:', *count_div.items(), sep='\n')
