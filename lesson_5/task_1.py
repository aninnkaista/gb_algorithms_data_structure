import collections
# to get the number of companies
n = int(input('Enter the number of companies: ').strip())

# to get data about all companies
comp_list = []
# tuple for each company
comp = collections.namedtuple('comp', ['name', 'profit'])
av_profit = 0

# to enter all companies and find their profits
for i in range(n):
    comp_name = input(f'Enter {i+1} company name: ')
    comp_profits = list(map(float, input(f'Enter {comp_name} profits for each quarter last year: ').split()))
    comp_list.append(comp(comp_name, comp_profits))
    av_profit += sum(comp_profits)/n


# lists of companies with profit above and below average

above_av = list()
below_av = list()
for c in comp_list:
    if sum(c.profit) > av_profit:
        above_av.append(c.name)
    elif sum(c.profit) < av_profit:
        below_av.append(c.name)

# to print out both lists
print('Companies with the annual profit above average are:\n', *above_av)
print('Companies with the annual profit below average are:\n', *below_av)

