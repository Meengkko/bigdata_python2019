#  목적: 빅데이터에서 카테고리별 통계치 계산하기
import sys
import pandas as pd


input_file = sys.argv[1]  # 월수도꼭지.xlsx
# output_file = sys.argv[2]  # output_files/2_output.csv

data_frame = pd.read_excel(input_file, sheet_name='Sheet1')
data_frame_value_meets_condition = data_frame[data_frame['행정구역'] == '서울특별시']
