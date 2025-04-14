import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    final_dict = {"series_1": [], "series_2": [], "series_3": []}
    with open(file_path, mode="r", encoding="utf-8") as new_file:
        reader = csv.DictReader(new_file)
        for row in reader:
            for key, value in row.items():
                final_dict[key].append(value)

    return final_dict


def selection_sort(number_list: list):

    for i in range(len(number_list)):
        min_index = i
        for j in range(i + 1, len(number_list)):
            if number_list[j] < number_list[min_index]:
                min_index = j

        number_list[i], number_list[min_index] = number_list[min_index], number_list[i]

    return number_list


def main():
    selection_sort([5, 56, 38, 94, 3, 18])


if __name__ == '__main__':
    main()
