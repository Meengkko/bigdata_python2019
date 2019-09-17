#  목적: 워크시트 집합에 걸쳐서 특정 행 필터링하기

# 라이브러리 호출
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

# 시스템 인자로 인풋/아웃풋 설정
input_file = sys.argv[1]  # sales_2013.xlsx
output_file = sys.argv[2]  # output_files/11_output_basic.xls

# 워크북클래스, 시트 이름 설정
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('set_of_worksheets')

my_sheets = [0, 1]
threshold = 1900.0
sales_column_index = 3

first_worksheet = True
# 파일 오픈 및 1월 데이터 가져오기
with open_workbook(input_file) as workbook:
    data = []
    for sheet_index in range(workbook.nsheets):
        if sheet_index in my_sheets:
            worksheet = workbook.sheet_by_index(sheet_index)
            if first_worksheet:
                header_row = worksheet.row_values(0)
                data.append(header_row)
                first_worksheet = False
            for row_index in range(1, worksheet.nrows):
                row_list = []
                sale_amount = worksheet.cell_value(row_index, sales_column_index)
                if sale_amount > threshold:
                    for column_index in range(worksheet.ncols):
                        cell_value = worksheet.cell_value(row_index, column_index)
                        cell_type = worksheet.cell_type(row_index, column_index)
                        if cell_type == 3:
                            date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                            date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                            row_list.append(date_cell)
                        else:
                            row_list.append(cell_value)
                if row_list:
                    data.append(row_list)

    for list_index, output_list in enumerate(data):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)
