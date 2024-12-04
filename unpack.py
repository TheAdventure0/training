def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [True, 'wind', [3, 4, 1]]
values_dict = {'a': 'M', 'b': 3, 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['green', True]

print_params(*values_list_2, 42)
