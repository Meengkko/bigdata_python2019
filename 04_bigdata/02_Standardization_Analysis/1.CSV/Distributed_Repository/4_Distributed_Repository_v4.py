#  분산 저장 v4
#  분산저장을 하기 위한 파일명 분해 및 재조립
import csv
import os

base_repository_name = 'Bigdata_Repository'
dir_delimeter = '/'
file_name = '시뮬레이션_서울특별시_관광지별_방문객'
file_format = 'csv'
simulation_count = 100
file_size_limit = 10000


def get_request_url():
    pass


def get_tour_point_visitor():
    pass


def get_tour_point_data():
    filewriter.writerow(simulation_data)
    return


file_size = 0
try:
    file_size = os.path.getsize(f'{base_repository_name}{dir_delimeter}{file_name}.{file_format}')
    print(f"'{base_repository_name}{dir_delimeter}{file_name}.{file_format}' file size: {file_size}")
    print(f"파일당 size 제한: {file_size_limit}")
except:
    os.mkdir(base_repository_name)

csv_out_file = open(f'{base_repository_name}{dir_delimeter}{file_name}.{file_format}', 'w', newline='')
filewriter = csv.writer(csv_out_file)
header_list = ['addrCd', 'gungu', 'resNm', 'rnum', 'csForCnt', 'csNatCnt']
simulation_data = ['1111', '종로구', '서울특별시', '창덕궁', '1', '14137', '43677']
filewriter.writerow(header_list)

for index in range(simulation_count):
    get_tour_point_data()
csv_out_file.close()
