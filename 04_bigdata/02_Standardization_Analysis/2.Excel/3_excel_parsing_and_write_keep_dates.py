#  목적: 단일 워크시트 처리

# 라이브러리 호출
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

# 시스템 인자로 인풋/아웃풋 설정
input_file = sys.argv[1]  # sales_2013.xlsx
output_file = sys.argv[2]  # output_files/2_output_basic.xls

# 워크북클래스, 시트 이름 설정
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

# 파일 오픈 및 1월 데이터 가져오기
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    # 행과 열마다 'cell_value'를 호출하여 쓰기
    for row_index in range(worksheet.nrows):
        row_list_output = []
        for col_index in range(worksheet.ncols):
            if worksheet.cell_type(row_index, col_index) == 3:
                date_cell = xldate_as_tuple(worksheet.cell_value(row_index, col_index), workbook.datemode)
                print(date_cell)
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                print(date_cell)
                row_list_output.append(date_cell)
                output_worksheet.write(row_index, col_index, date_cell)
            else:
                non_date_cell = worksheet.cell_value(row_index, col_index)
                row_list_output.append(non_date_cell)
                output_worksheet.write(row_index, col_index, non_date_cell)

output_workbook.save(output_file)
