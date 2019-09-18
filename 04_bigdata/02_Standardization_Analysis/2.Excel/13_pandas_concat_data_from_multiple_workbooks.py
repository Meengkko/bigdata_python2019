#!/isr/bin/env python3

# 라이브러리 호출
import pandas as pd
import glob
import os
import sys

# 시스템 인자로 인풋/아웃풋 설정
input_path = sys.argv[1]  # sales_2013.xlsx
output_file = sys.argv[2]  # output_files/13_output_pandas.xls

all_workbooks = glob.glob(os.path.join(input_path, '*.xls*'))
data_frame = []
for workbook in all_workbooks:
    all_worksheets = pd.read_excel(workbook, sheet_name=None, index_col=None)
    for worksheet_name, data in all_worksheets.items():
        data_frame.append(data)
all_data_concatenated = pd.concat(data_frame, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
all_data_concatenated.to_excel(writer, sheet_name='all_data_all_workbooks', index=False)
writer.save()
