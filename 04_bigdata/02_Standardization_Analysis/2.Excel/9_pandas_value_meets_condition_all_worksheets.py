#!/isr/bin/env python3

# 라이브러리 호출
import pandas as pd
import sys

# 시스템 인자로 인풋/아웃풋 설정
input_file = sys.argv[1]  # sales_2013.xlsx
output_file = sys.argv[2]  # output_files/9_output_pandas.xls

data_frame = pd.read_excel(input_file, sheet_name=None, index_col=None)

row_output = []
for worksheet_name, data in data_frame.items():
    row_output.append(data[data['Sale Amount'].replace('$', '').replace(',', '').astype(float)> 2000.0])
filtered_rows = pd.concat(row_output, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name='sale_amount_gt2000', index=False)
writer.save()
