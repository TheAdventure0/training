def calculate_structure_sum(a):
    global summa
    for i in a:
        if isinstance(i, (list, tuple, set)):
            calculate_structure_sum(i)
        if isinstance(i, dict):
            calculate_structure_sum(i.items())
        elif isinstance(i, (int, float)):
            summa += i
        elif isinstance(i, str):
            summa += len(i)
    return summa

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

summa = 0
result = calculate_structure_sum(data_structure)
print(result)