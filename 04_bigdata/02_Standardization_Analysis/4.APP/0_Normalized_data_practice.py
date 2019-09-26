import openpyxl
import MySQLdb

con = MySQLdb.connect(host='localhost', port=3306, db='erd_students', user='open_source', passwd='1111', charset='utf8')
c = con.cursor()


# Make two tables with each of the queries below

'''
CREATE TABLE IF NOT EXISTS Basic_Student_Info
                          (Student_ID VARCHAR(15),
                          Name VARCHAR(10),
                          Sex VARCHAR(5),
                          Age INT,
                          Major VARCHAR(30));


CREATE TABLE IF NOT EXISTS Student_Language
                          (Student_ID VARCHAR(15),
                          Name VARCHAR(10),
                          Level VARCHAR(5),
                          Period VARCHAR(10));
'''

# Insert given data to the tables

'''
student_file = 'Basic_Student_Info_example.xlsx'
language_file = 'Student_Language.xlsx'

workbook = openpyxl.load_workbook(student_file)
sheet = workbook.worksheets[0]

for row in sheet.rows:
    if 'ITT' not in row[0].value:
        continue
    data_to_insert = []
    for element in row:
        data_to_insert.append(element.value)
    c.execute("""INSERT INTO Basic_Student_Info VALUES (%s, %s, %s, %s, %s);""", data_to_insert)
con.commit()

workbook = openpyxl.load_workbook(language_file)
sheet = workbook.worksheets[0]

for row in sheet.rows:
    if 'ITT' not in row[0].value:
        continue
    data_to_insert = []
    for element in row:
        data_to_insert.append(element.value)
    c.execute("""INSERT INTO Student_Language VALUES (%s, %s, %s, %s);""", data_to_insert)
con.commit()
'''


# Select all and get summarized information from normalized db (main subject)


c.execute("SELECT * FROM Basic_Student_Info")
rows = c.fetchall()

student_count = len(rows)
ages_packages = {'20': 0, '30': 0, '40': 0}
male_count = 0
major_count = 0

for row in rows:
    if row[2] == '남':
        male_count += 1
    if '컴퓨터' in row[4] or '통계' in row[4]:
        major_count += 1
    if row[3] in range(20, 30):
        ages_packages['20'] += 1
    elif row[3] in range(30, 40):
        ages_packages['30'] += 1
    else:
        ages_packages['40'] += 1


c.execute("SELECT * FROM Basic_Student_Info b JOIN Student_Language s USING(Student_ID);")
rows_joined = c.fetchall()
id_library = []
non_beginner = 0
python_programmer = 0
is_python = False
advanced_programmer = 0
is_advanced = False
for joined_row in rows_joined:
    if joined_row[0] not in id_library:
        id_library.append(joined_row[0])
        non_beginner += 1
        is_python = False
        is_advanced = False
    else:
        if 'py' in joined_row[-3].lower():
            python_programmer += 1
            is_python = True
        if joined_row[-2] == '상':
            advanced_programmer += 1
            is_advanced = True


print("* 전체 학생수:%d" % student_count)
print("* 성별\n - 남학생: %s명(%0.1f%%)\n - 여학생: %s명(%0.1f%%)" %
      (male_count, (male_count / student_count) * 100, (student_count - male_count),
       ((student_count - male_count) / student_count) * 100))
print('* 전공여부')
print("- 전공자(컴퓨터 공학, 통계): %s명 (%0.1f%%)" % (major_count, (major_count / student_count) * 100))
print("- 프로그래밍 언어 경험자: %s명 (%0.1f%%)" % (non_beginner, (non_beginner / student_count) * 100))
print("- 프로그래밍 언어 상급자: %s명 (%0.1f%%)" % (advanced_programmer, (advanced_programmer / student_count) * 100))
print("- 파이썬 경험자: %s명 (%0.1f%%)" % (python_programmer, (python_programmer / student_count) * 100))
print('* 연령대')
print('- 20대: %s명 (%0.1f%%) %s' % (ages_packages['20'], (ages_packages['20'] / student_count) * 100, ages_packages['20']))
print('- 30대: %s명 (%0.1f%%) %s' % (ages_packages['30'], (ages_packages['30'] / student_count) * 100, ages_packages['30']))
print('- 40대: %s명 (%0.1f%%) %s' % (ages_packages['40'], (ages_packages['40'] / student_count) * 100, ages_packages['40']))
