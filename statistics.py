import math


def sum(values):
    s = 0
    for num in values:
        s += num
    return s


def mean(values):
    s = sum(values)
    return s / len(values)


def sort(values):
    length = len(values)
    for i in range(length):
        max_value = values[0]
        max_index = 0
        for j in range(length - i):
            if values[j] > max_value:
                max_value = values[j]
                max_index = j

        values[max_index] = values[length - i - 1]
        values[length - i - 1] = max_value


def median(values):
    length = len(values)
    new_values = values.copy()
    sort(new_values)
    if len(new_values) % 2 == 0:
        return (new_values[length // 2 - 1] + new_values[length // 2]) / 2
    else:
        return new_values[math.ceil(length / 2)]


def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    pass
