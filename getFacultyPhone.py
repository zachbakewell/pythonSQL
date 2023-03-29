import pyodbc

login  = 'zachary_bakewell1'
pw='MIS4322student'

cn_str = (
'Driver={SQL Server Native Client 11.0};Server=MIS-SQLJB;Database=School;UID='+login+';''PWD='+pw+';')
cn = pyodbc.connect(cn_str)
cursor = cn.cursor()

cursor.execute('exec getFacultyPhone')

data = cursor.fetchall()

print('FirstName'.ljust(10),'LastName'.ljust(15),'Home_Phone'.ljust(15),'Cell_Phone'.ljust(20),'Work_Phone'.ljust(20))

for row in data:
    print(row[0].ljust(10),row[1].ljust(15),row[2].ljust(20),row[3].ljust(20),row[4].ljust(20))