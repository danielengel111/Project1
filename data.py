import pandas
import sys


def load_data(path, features):
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    new_data = {}
    for feat in features:
        new_data[feat] = data[feat]
    return new_data


def filter_by_feature(data, feature, values):
    length = len(data[feature])
    data1 = {}
    data2 = {}
    for key in data:
        data1[key] = []
        data2[key] = []
    for i in range(length):
        for key in data:
            if data[feature][i] in values:
                data1[key].append(data[key][i])
            else:
                data2[key].append(data[key][i])
    return data1, data2


def print_details(data, features, statistic_functions):
    pass
    # for feature in features:
    #   data1, data2 = filter_by_feature(data, feature,)
