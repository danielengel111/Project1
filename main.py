import sys
import statistics
import data as data_lib


def print_stats(data):
    for feat in data:
        if feat == "is_holiday" or feat == "season":
            continue
        feat_list = data[feat]
        sum = statistics.sum(feat_list)
        mean = statistics.mean(feat_list)
        median = statistics.median(feat_list)
        print("{}: {}, {}, {}".format(feat, sum, mean, median))


def main(argv):
    print("Question 1:")
    csv_path = argv[1]
    features = argv[2]
    features = list(features.split(", "))
    data = data_lib.load_data(csv_path, features)

    data1, data2 = data_lib.filter_by_feature(data, "season", [1])
    print("Summer:")
    print_stats(data1)

    data1, data2 = data_lib.filter_by_feature(data, "is_holiday", [1])
    print("Holiday:")
    print_stats(data1)

    print("All:")
    print_stats(data)


if __name__ == '__main__':
    main(sys.argv)
