def sum_dicts(*args) -> dict:
    # write your code here
    total_dict = {}
    for arg in args:
        for key, value in arg.items():
            if key not in total_dict:
                total_dict[key] = value
            else:
                total_dict[key] += value

    return total_dict


first = {"a": 9, "b": 4}
second = {"a": 2, "b": 13}
third = {"d": -5}

print(sum_dicts(first))
print(sum_dicts(first, second, third))
print(sum_dicts(first, second))
print(sum_dicts(third, second))
