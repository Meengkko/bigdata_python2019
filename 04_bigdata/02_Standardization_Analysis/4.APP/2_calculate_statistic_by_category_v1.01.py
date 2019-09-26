import csv
import sys
from statistics import mean


input_file = sys.argv[1]  # customer_finance.csv
output_file = sys.argv[2]  # output_files/2_output_p.csv

packages = {}  # structuring formatted data to dictionary
counters = {}
mean_value_package = {}

header_for_dict = ['소득', '금융자산', '부채', '순자산']

with open(input_file, 'r', newline='') as input_csv_file:
    filereader = csv.reader(input_csv_file)
    header = next(filereader)  # assign header of csv as a list
    for row in filereader:

        financial_data_list = []

        financial_data_list.append(row[2])
        financial_data_list.append(row[7])
        financial_data_list.append(row[-2])
        financial_data_list.append(row[-1])

        ages_index = str(row[0])[0] + '0대'

        if not ages_index in packages:
            packages[ages_index] = {}
            mean_value_package[ages_index] = []
            counters[ages_index] = 1
        else:
            counters[ages_index] += 1


        packages[ages_index][counters[ages_index]] = []

        for index, field_name in enumerate(header_for_dict):
            packages[ages_index][counters[ages_index]].append(financial_data_list[index])

packages = dict(sorted(packages.items()))

header_for_save = ['나이대', '번호'] + header_for_dict

mean_of_data = [[], [], [], []]
mean_of_income_by_ages = {}
previous_age = 'N/A'
mean_packages = {'전체 평균': []}

for customer_ages, customer_name_value in packages.items():
    current_age = customer_ages
    if previous_age != current_age:
        mean_of_income_by_ages[current_age] = [[], [], [], []]
        for customer_index, customer_index_value in customer_name_value.items():
            for mean_box_index, mean_box_list in enumerate(mean_of_data):
                mean_box_list.append(float(customer_index_value[mean_box_index]))
                mean_of_income_by_ages[current_age][mean_box_index].append(float(customer_index_value[mean_box_index]))


for ages_index, data_by_age in mean_of_income_by_ages.items():
    ages_index_dict = ages_index + ' 평균'
    mean_packages[ages_index_dict] = []
    for data_by_age_each in data_by_age:
        mean_packages[ages_index_dict].append(mean(data_by_age_each))


for financial_data_set in mean_of_data:
    mean_packages['전체 평균'].append(mean(financial_data_set))


with open(output_file, 'w', newline='') as output_csv_file:
    filewriter = csv.writer(output_csv_file)
    filewriter.writerow(header_for_save)
    for customer_ages, customer_name_value in packages.items():
        for customer_index, customer_index_value in customer_name_value.items():
            row_of_output = []
            row_of_output.append(customer_ages)
            row_of_output.append(customer_index)
            row_of_output += customer_index_value

            filewriter.writerow(row_of_output)

    for mean_key, mean_list in mean_packages.items():
        filewriter.writerow([mean_key, ''] + mean_list)
