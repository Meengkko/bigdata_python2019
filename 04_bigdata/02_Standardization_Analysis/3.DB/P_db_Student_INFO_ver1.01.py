import csv
import MySQLdb
import sys

input_file = sys.argv[1]  # Basic_Student_Info.csv

con = MySQLdb.connect(host='localhost', port=3306, db='my_student', user='root', passwd='1111', charset='utf8')
c = con.cursor()


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
    validated_field = ['이름', '성별', '나이', '전공']
    data_input_number = input('* 생 성 *\n총 입력의 개수를 입력하세요: ')
    if data_input_number.isdigit():
        data_input_number = int(data_input_number)
    else:
        print('잘못된 입력입니다.')
        return
    for i in range(data_input_number):
        data_to_be_updated = []
        for field_name in validated_field:
            data_to_be_updated.append(input("%s 입력: " % field_name))

        print("\n입력되었습니다!\n")
        c.execute("""INSERT INTO Student_Info (Name, Sex, Age, Major)\
             VALUES (%s, %s, %s, %s);""", data_to_be_updated)
        con.commit()


def data_search():
    search_menu = '''
    <데이터 조회 메뉴>
    1. 전체 조회
    2. 아이디 조회
    3. 이전 메뉴
    메뉴를 입력하세요: '''

    search_selection = input(search_menu)

    if search_selection == '1':
        c.execute("SELECT * from Student_Info;")
        for row in c.fetchall():
            print('\t', end="|")
            for column in row:
                print(column, end='\t|' if len(str(column)) >= 4 else '\t\t|')
            print()
    elif search_selection == '2':
        index_input = input('조회하고자 하는 학생의 ID를 입력해주세요.')
        c.execute(f"SELECT * from Student_Info WHERE Student_ID = {index_input};")
        print('|', end='')
        for element in list(c.fetchall()[0]):
            print(element, end='\t|')
    elif search_selection == '3':
        return


def data_update():
    input_info = ["이름", "성별", "나이", "전공"]
    field_list = ['Name', 'Sex', 'Age', 'Major']
    update_option = '''
    1. 모든 필드의 데이터를 변경한다
    2. 한 필드에 해당하는 값만 변경한다.
    3. 변경하지 않는다.
    >>> '''
    index_input = input('변경하고자 하는 학생의 ID를 입력해주세요.')
    c.execute(f"SELECT * from Student_Info WHERE Student_ID = {index_input};")
    print('|', end='')
    student_list = c.fetchall()[0]
    student_list = list(student_list)[1:]
    for element in student_list:
        print(element, end='\t|')
    update_option_selection = input(update_option)
    if update_option_selection == '1':
        for index, content in enumerate(student_list):
            update_each = input("%s를 입력하세요. (Before: %s) >>> " % (input_info[index], content))
            c.execute('UPDATE Student_Info SET %s = "%s" WHERE Student_ID = "%s";'
                      % (field_list[index], update_each, index_input))
            con.commit()
    elif update_option_selection == '2':
        for key, value in enumerate(input_info):
            print(str(key+1)+'. '+value)
        input_field_selection = int(input('어떤 값을 변경하시겠습니까?'))
        if input_field_selection in range(1, 5):
            update_indi = input("%s를 입력하세요. (Before: %s) >>> "
                                % (input_info[input_field_selection-1], student_list[input_field_selection-1]))
            c.execute('UPDATE Student_Info SET %s = "%s" WHERE Student_ID = "%s";'
                      % (field_list[input_field_selection-1], update_indi, index_input))
            con.commit()
    elif update_option_selection == '3':
        return


def data_delete():
    index_input = input('\n삭제하고자 하는 학생의 ID를 입력해주세요.')
    c.execute(f"SELECT * from Student_Info WHERE Student_ID = {index_input};")
    for element in list(c.fetchall()[0]):
        print(element, end='\t|')
    delete_order = input('\n삭제하시겠습니까? (Y/N): ')
    if delete_order.lower()[0] == 'y':
        c.execute(f"DELETE FROM Student_Info WHERE Student_ID = {index_input}")
        con.commit()


def main():
    menu_option = """
     
    DB용 학생 주소록 관리프로그램 v1.01
    =================================
    | 0. 초기화(Initialize)         |
    | 1. 생성(Insert)               |
    | 2. 조회(Select)               |
    | 3. 변경(Update)               |
    | 4. 삭제(Delete)               |
    | 5. 종료                       |
    =================================
    >>> """
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
