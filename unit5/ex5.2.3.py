from itertools import combinations

dollar_bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
combinations_list = list()
for len_of_comb in range(1, len(dollar_bills) + 1):
    combinations_list.extend(combinations(dollar_bills, len_of_comb))

valid_combinations = set([combination for combination in combinations_list if sum(combination) == 100])
for combination in valid_combinations:
    print(combination)
