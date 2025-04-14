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


def selection_sort(number_list: list, direction) -> list:

    for i in range(len(number_list)):
        min_index = i
        for j in range(i + 1, len(number_list)):
            if direction == "ascending":
                if number_list[j] < number_list[min_index]:
                    min_index = j
            elif direction == "descending":
                if number_list[j] > number_list[min_index]:
                    min_index = j

        number_list[i], number_list[min_index] = number_list[min_index], number_list[i]

    return number_list


def bubble_sort(number_list: list) -> list:

    for i in range(len(number_list) - 1):
        swapped = False
        for j in range(0, len(number_list) - 1 - i):
            if number_list[j] > number_list[j + 1]:
                temporary_number = number_list[j]
                number_list[j] = number_list[j + 1]
                number_list[j + 1] = temporary_number
                swapped = True
        if not swapped:
            break

    return number_list

def insertion_sort(number_list: list) -> list:
    for i in range(1, len(number_list)):
        key = number_list[i]
        j = i - 1

        while j >= 0 and key < number_list[j]:
            number_list[j + 1] = number_list[j]
            j -= 1

        number_list[j + 1] = key
    return number_list


def main():
    print(insertion_sort([88, 1, 1058, 1, 36, 8, 998, 21, 7, 1235]))


if __name__ == '__main__':
    main()
