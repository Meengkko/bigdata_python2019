#  목적: 단일 워크시트 처리

# 라이브러리 호출
import pandas as pd
import sys

# 시스템 인자로 인풋/아웃풋 설정
input_file = sys.argv[1]  # sales_2013.xlsx
output_file = sys.argv[2]  # output_files/3_output_pandas.xls

#  data_frame = pd.read_excel(input_file, sheetname = 'january_2013')
#  sheetname은 deprecate 되었음
data_frame = pd.read_excel(input_file, sheet_name='january_2013')

writer = pd.ExcelWriter(output_file)
data_frame.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()
