import csv
import sqlite3
import sys

con = sqlite3.connect('Suppliers.db')
c = con.cursor()

# 중복 레코드를 제거하는 distinct
# output = c.execute("SELECT distinct Supplier_Name from suppliers")

# WHERE 이후 여러 조건
# output = c.execute("SELECT * FROM Suppliers WHERE Supplier_Name = 'Supplier X' and Purchase_Date = '1/20/14' ")

# 부정연산자
# output = c.execute("SELECT * FROM Suppliers WHERE Part_Number <> '2341' ")

# 검색 조건 리스트
# output = c.execute("SELECT * FROM Suppliers WHERE Supplier_Name NOT IN('Supplier X', 'Supplier Y')")

# 테이블 값 정렬
# output = c.execute("select * from Suppliers order by cost")

# 전체 레코드 계산
# output = c.execute("SELECT count(*) from suppliers")

# 함수 사용 (MAX, MIN)
output = c.execute("SELECT MAX(cost) from suppliers")

rows = output.fetchall()
print("Select 결과")
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)
