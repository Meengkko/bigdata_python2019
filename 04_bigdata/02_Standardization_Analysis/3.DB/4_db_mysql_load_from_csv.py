import csv
import MySQLdb
import sys
from datetime import datetime, date

# Path to and name of a CSV input file
input_file = sys.argv[1]

# Connect to a MySQL database
# con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='python_training', passwd='python_training')
# con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='root', passwd='1111')
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
    print(data)
    # c.execute("""INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s);""", data)
    # 아래 코드는 SQL injection 공격에 취약하다.
    # c.execute("""INSERT INTO Suppliers VALUES %r;""" % (tuple(data),))

    # var_string = ', '.join('?' * len(data))  # executemany 일 경우에
    var_string = ', '.join('?' * len(data)).replace('?', '%s')
    query_string = 'INSERT INTO Suppliers VALUES (%s);' % var_string
    c.execute(query_string, data)

con.commit()

# Query the Suppliers table
c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
    print(row_list_output)
