import pyodbc

login  = 'zachary_bakewell1'
pw='MIS4322student'

cn_str = ('Driver={SQL Server Native Client 11.0};Server=MIS-SQLJB;Database=School;UID='+login+';''PWD='+pw+';')
cn = pyodbc.connect(cn_str)
cursor = cn.cursor()

cursor.execute('exec getStudentEmail')

data = cursor.fetchall()

print('First Name'.ljust(15), 'Last Name'.ljust(15), 'Personal Email'.ljust(30), 'Work Email'.ljust(30))

for row in data:
    print(row[0].ljust(15),row[1].ljust(15),row[2].ljust(30),row[3].ljust(30))