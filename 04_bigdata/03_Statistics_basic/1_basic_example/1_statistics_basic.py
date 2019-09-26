import csv
from math import sqrt


def get_row_index(search_key):
    index = 0
    for row in big_data:
        if row[0] == search_key:
            return index
        index += 1


def print_row(key_index):
    for content in big_data[key_index + 1]:
        print(content, end=' ')
    return


def get_column_instance(column_name):
    col_instance = []
    row_index = big_data[0].index(column_name)
    for row in big_data[1:]:
        col_instance.append(float(row[row_index]))
    return col_instance


def print_column(column_name):
    print(column_name)
    for column_data in get_column_instance(column_name):
        print(column_data, end=' ')


def my_sum(column_name):
    return sum(check_type(get_column_instance(column_name)))


def my_average(column_name):
    return my_sum(column_name)/len(get_column_instance(column_name))


def my_max(column_name):
    return max(check_type(get_column_instance(column_name)))


def my_min(column_name):
    return min(check_type(get_column_instance(column_name)))


def my_deviation(column_name):
    value_column = check_type(get_column_instance(column_name))
    sample_mean = my_average(column_name)
    print("표본\t평균\t편차")
    for sample in value_column:
        print('%.2f\t%.2f\t%.2f' % (sample, sample_mean, sample-sample_mean))


def my_standard_deviation(column_name):
    return sqrt(my_variance(column_name))


def my_variance(column_name):
    value_column = check_type(get_column_instance(column_name))
    sample_mean = my_average(column_name)
    square_deviation_sum = 0
    for sample in value_column:
        square_deviation_sum += (sample - sample_mean) ** 2
    return square_deviation_sum / len(value_column)


def my_sorting(column_name):
    value_column = check_type(get_column_instance(column_name))
    ascending_sorted = sorted(value_column)
    descending_sorted = sorted(value_column, reverse=True)
    print("오름차순 정렬: ", end='')
    [print(i, end=' ') for i in ascending_sorted]
    print()
    print("내림차순 정렬: ", end='')
    [print(i, end=' ') for i in descending_sorted]


def check_type(list_object):
    try:
        result = list(map(int, list_object))
    except ValueError:
        result = list(map(float, list_object))
    return result


def printer_set(print_index, print_object):
    print_dict = {'3': '총합', '4': '평균', '5': '최대값',
                  '6': '최소값', '8': '분산', '9': '표준편차'}
    print(f"다음의 결과가 출력됩니다.\n{print_dict[print_index]}: {print_object}")


with open('Demographic_Statistics_By_Zip_Code.csv', newline='') as inflie:
    big_data = list(csv.reader(inflie))


while True:
    main_option = '''
    원하는 서비스를 입력하세요.
    | 1. 행   | 2. 열   | 3. 총합    | 4. 평균    | 5. 최대값    | 6. 최소값    |
    | 7. 편차 | 8. 분산 | 9. 표준편차 | 10. 정렬(오름차순, 내림차순) |  11. 종료  |
    : '''
    option_selection = input(main_option)

    if option_selection == '1':
        print_row(get_row_index(input("Access Key를 입력하세요: ")))
    elif option_selection == '2':
        print_column(input("검색하고자 하는 데이터필드명을 입력하세요: "))
    elif option_selection == '3':
        printer_set(option_selection, my_sum(input("총합을 구하고자 하는 데이터필드명을 입력하세요: ")))
    elif option_selection == '4':
        printer_set(option_selection, my_average(input("평균을 구하고자 하는 데이터필드명을 입력하세요: ")))
    elif option_selection == '5':
        printer_set(option_selection, my_max(input("최대값을 구하고자 하는 데이터필드명을 입력하세요: ")))
    elif option_selection == '6':
        printer_set(option_selection, my_min(input("최소값을 구하고자 하는 데이터필드명을 입력하세요: ")))
    elif option_selection == '7':
        my_deviation(input("총합을 구하고자 하는 데이터필드명을 입력하세요: "))
    elif option_selection == '8':
        printer_set(option_selection, my_variance(input("분산을 구하고자 하는 데이터필드명을 입력하세요: ")))
    elif option_selection == '9':
        printer_set(option_selection, my_standard_deviation(input("표준편차를 구하고자 하는 데이터필드명을 입력하세요: ")))
    elif option_selection == '10':
        my_sorting(input("정렬된 결과를 구하고자 하는 데이터필드명을 입력하세요: "))
    elif option_selection == '11':
        print('조회가 종료됩니다.')
        break
