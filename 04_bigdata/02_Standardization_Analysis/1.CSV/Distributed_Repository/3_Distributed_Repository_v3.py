#  분산 저장 v3
#  분산저장을 하기 위하여 현재 저장중인 파일의 사이즈를 구함
import csv
import os

output_file = '시뮬레이션_서울특별시_관광지별_방문객.csv'
simulation_count = 100
file_size_limit = 10000


def get_request_url():
    pass


def get_tour_point_visitor():
    pass


def get_tour_point_data():
    filewriter.writerow(simulation_data)
    return


file_size = os.path.getsize(output_file)
print(f"'{output_file}' file size: {file_size}")
print(f"파일당 size 제한: {file_size_limit}")

csv_out_file = open(output_file, 'w', newline='')
filewriter = csv.writer(csv_out_file)
header_list = ['addrCd', 'gungu', 'resNm', 'rnum', 'csForCnt', 'csNatCnt']
simulation_data = ['1111', '종로구', '서울특별시', '창덕궁', '1', '14137', '43677']
filewriter.writerow(header_list)

for index in range(simulation_count):
    get_tour_point_data()
csv_out_file.close()
