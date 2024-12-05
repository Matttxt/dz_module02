def calculate_structure_sum(data_structure, *args):
    summ = 0
    for i in data_structure:
        if isinstance(i, dict):
            for key, value in i.items():
                if isinstance(key, (int, float)) and isinstance(value, str):
                    summ += key
                    summ += len(value)
                elif isinstance(key, str) and isinstance(value, (int, float)):
                    summ += len(key)
                    summ += value
                elif isinstance(value, (list, tuple, dict, set)):
                    summ += calculate_structure_sum(value)
        elif isinstance(i, (int, float)):
            summ += i
        elif isinstance(i, str):
            summ += len(i)
        elif isinstance(i, (tuple, list, dict, set)):
            summ += calculate_structure_sum(i)
        elif isinstance(i, (tuple, list, set)):
            for j in i:
                if isinstance(j, (int, float)):
                    summ += j
                elif isinstance(j, str):
                    summ += len(j)
                elif isinstance(j, (tuple, list, dict, set)):
                    summ += calculate_structure_sum(j)


    return summ

data_structure = [

[1, 2, 3],

{'a': 4, 'b': 5},

(6, {'cube': 7, 'drum': 8}),

"Hello",

((), [{(2, 'Urban', ('Urban2', 35))}])

]
res = calculate_structure_sum(data_structure)
print(res)


