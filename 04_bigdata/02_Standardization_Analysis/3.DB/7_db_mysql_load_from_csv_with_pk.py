import csv
import MySQLdb
import sys
from datetime import datetime, date

# 아래와 같이 테이블 생성 할 것
# CREATE TABLE IF NOT EXISTS Suppliers2
# 		(ITT_ID int not null auto_increment primary key,
# 		Supplier_Name VARCHAR(20),
# 		Invoice_Number VARCHAR(20),
# 		Part_Number VARCHAR(20),
# 		Cost FLOAT,
# 		Purchase_Date DATE);

# Path to and name of a CSV input file
input_file = sys.argv[1]  # supplier_data.csv

# db: Database명 create database my_suppliers <= 이렇게 생성한 db명과 매칭
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='open_source', passwd='1111')
c = con.cursor()

# Read the CSV file
# Insert the data into the Suppliers table
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        if column_index < 4:
            data.append(str(row[column_index]).lstrip('$').replace(',', '').strip())
        else:
            a_date = datetime.date(datetime.strptime(str(row[column_index]), '%m/%d/%y'))  # y를 대문자로 저장하면 에러
            a_date = a_date.strftime('%y-%m-%d')
            # a_date = a_date.strftime('%Y-%m-%d')
            data.append(a_date)
    # print(data)
    c.execute("""INSERT INTO Suppliers2 (Supplier_Name, Invoice_Number, Part_Number, Cost, Purchase_Date)\
     VALUES (%s, %s, %s, %s, %s);""", data)
con.commit()

# Query the Suppliers table
c.execute("SELECT * FROM Suppliers2")
rows = c.fetchall()
for row in rows:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
    print(row_list_output)
