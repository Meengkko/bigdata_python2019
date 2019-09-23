import csv
import MySQLdb
import sys
from datetime import datetime, date

input_file = sys.argv[1]  # Basic_Student_Info.csv

con = MySQLdb.connect(host='localhost', port=3306, db='my_student', user='root', passwd='1111', charset='utf8')
c = con.cursor()

# Read the CSV file
# Insert the data into the Suppliers table


def initializer():
    c.execute("TRUNCATE Student_Info")
    con.commit()
    file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
    header = next(file_reader)
    for row in file_reader:
        data = []
        for column_index in range(len(header)):
            if column_index >= 1:
                data.append(str(row[column_index]).replace(',', '').strip())
        print(data)
        c.execute("""INSERT INTO Student_Info (Name, Sex, Age, Major)\
         VALUES (%s, %s, %s, %s);""", data)
    con.commit()


def data_creat():
    data_input = input('* 생 성 *\n데이터를 입력하세요.\n(ex: 홍길동 남 45 행정학)')
    data_input = data_input.strip().split()
    c.execute("""INSERT INTO Student_Info (Name, Sex, Age, Major)\
             VALUES (%s, %s, %s, %s);""", data_input)
    con.commit()


def data_search():
    index_input = input('조회하고자 하는 학생의 ID번호를 입력해주세요.')
    c.execute(f"SELECT * from Student_Info WHERE Student_ID = {index_input};")
    print(c.fetchall())


def data_update():
    index_input = input('변경하고자 하는 학생의 ID번호를 입력해주세요.')
    c.execute(f"SELECT * from Student_Info WHERE Student_ID = {index_input};")
    print(c.fetchall())
    update_info = input('이름, 성별, 나이, 전공 순으로 새로운 데이터를 입력 하세요.\n 예) 홍길동 남 45 행정학\n>>>')
    update_info = update_info.split()
    c.execute(f'UPDATE Student_Info SET Name="{update_info[0]}", Sex="{update_info[1]}", Age="{update_info[2]}", Major="{update_info[3]}" WHERE Student_ID = "{index_input}";')
    con.commit()


def data_delete():
    index_input = input('삭제하고자 하는 학생의 ID번호를 입력해주세요.')
    c.execute(f"SELECT * from Student_Info WHERE Student_ID = {index_input};")
    print(c.fetchall())
    delete_order = input('삭제하시겠습니까? (Y/N): ')
    if delete_order.lower()[0] == 'y':
        c.execute(f"DELETE FROM Student_Info WHERE Student_ID = {index_input}")
        con.commit()


def main():
    menu_option = """
    DB용 학생 주소록 관리프로그램 v1.0
    0. 초기화(Initialize)
    1. 생성(Insert)
    2. 조회(Select)
    3. 변경(Update)
    4. 삭제(Delete)
    5. 종료
    """
    while True:
        option_selection = input(menu_option)
        if option_selection == '0':
            initializer()
        elif option_selection == '1':
            data_creat()
        elif option_selection == '2':
            data_search()
        elif option_selection == '3':
            data_update()
        elif option_selection == '4':
            data_delete()
        else:
            print("프로그램이 종료됩니다.")
            return


if __name__ == "__main__":
    main()
