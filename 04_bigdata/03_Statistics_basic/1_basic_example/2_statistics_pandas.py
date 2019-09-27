import pandas as pd


def print_sorted_col(column_name):
    column_to_list = data_fm[column_name].values.tolist()
    ascending_sorted = sorted(column_to_list)
    descending_sorted = sorted(column_to_list, reverse=True)
    print("오름차순 정렬: ", end='')
    [print(i, end=' ') for i in ascending_sorted]
    print()
    print("내림차순 정렬: ", end='')
    [print(i, end=' ') for i in descending_sorted]


data_fm = pd.read_csv('Demographic_Statistics_By_Zip_Code.csv')

menu_option = '''
    원하는 서비스를 입력하세요.
    ===============================
    1. 행     2. 열     3. 총합
    4. 평균   5. 최대값  6. 최소값
    7. 편차   8. 분산    9. 표준편차
    10. 정렬(오름차순, 내림차순)
    11. 종료
    ===============================
    >>> '''

# COUNT PARTICIPANTS
while True:
    selected_menu = input(menu_option)

    if selected_menu == '1':
        input_access_key = int(input('Access Key를 입력하세요: '))
        for dat in data_fm.loc[data_fm["JURISDICTION NAME"] == input_access_key, :].values.tolist():
            print(dat, end=' ')
    elif selected_menu == '2':
        input_field_name = input('검색하고자 하는 데이터필드명을 입력하세요: ')
        print(data_fm[input_field_name].values)
    elif selected_menu == '3':
        input_field_name = input('총합을 구하고자 하는 데이터필드명을 입력하세요: ')
        print("\n필드명:", input_field_name, "\n총합:", data_fm[input_field_name].sum())
    elif selected_menu == '4':
        input_field_name = input('평균을 구하고자 하는 데이터필드명을 입력하세요: ')
        print("\n필드명:", input_field_name, "\n평균값:", data_fm[input_field_name].mean())
    elif selected_menu == '5':
        input_field_name = input('최대값을 구하고자 하는 데이터필드명을 입력하세요: ')
        print("\n필드명:", input_field_name, "\n최대값:", data_fm[input_field_name].max())
    elif selected_menu == '6':
        input_field_name = input('최소값을 구하고자 하는 데이터필드명을 입력하세요: ')
        print("\n필드명:", input_field_name, "\n최소값:", data_fm[input_field_name].min())
    elif selected_menu == '7':
        input_field_name = input('편차를 구하고자 하는 데이터필드명을 입력하세요: ')
        selected_col_list = data_fm[input_field_name].values.tolist()
        col_mean = round(data_fm[input_field_name].mean(), 2)
        print("표본\t평균\t편차")
        for dat in selected_col_list:
            print("%.2f\t%.2f\t%.2f" % (dat, col_mean, dat - col_mean))
    elif selected_menu == '8':
        input_field_name = input('분산을 구하고자 하는 데이터필드명을 입력하세요: ')
        print("\n필드명:", input_field_name, "\n분산:", data_fm[input_field_name].var())
    elif selected_menu == '9':
        input_field_name = input('표준편차를 구하고자 하는 데이터필드명을 입력하세요: ')
        print("\n필드명:", input_field_name, "\n분산:", data_fm[input_field_name].std())
    elif selected_menu == '10':
        input_field_name = input('정렬된 자료를 출력하고자 하는 데이터필드명을 입력하세요: ')
        print_sorted_col(input_field_name)
    elif selected_menu == '11':
        print('조회가 종료됩니다.')
        break
