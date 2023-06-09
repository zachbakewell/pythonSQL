import pyodbc
import tkinter

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('200x100')
        self.main_window.title('SQL Server Login')

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bot_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text='Login:')
        self.login = tkinter.Entry(self.top_frame, width=20)

        self.label1.pack(side='left')
        self.login.pack(side='left')

        self.label2 = tkinter.Label(self.mid_frame,text='Password:')
        self.password = tkinter.Entry(self.mid_frame,show='*',width=20)

        self.label2.pack(side='left')
        self.password.pack(side='left')

        self.loginbutton = tkinter.Button(self.bot_frame, text='Login',width=8, command=self.access_database)

        self.loginbutton.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bot_frame.pack()

        tkinter.mainloop()
    
    def access_database(self):
        pw = self.password.get()
        login = self.login.get() 

        self.main_window.destroy()

        login = 'zachary_bakewell1'
        pw = 'MIS4322student'

        preList = {}
        courseList = []

        cn_str = (
    'Driver={SQL Server Native Client 11.0};'   #Data source driver, go to Administrative

    'Server=MIS-SQLJB;' #Server name

    'Database=School;' #Database name

    'UID='+login+';' #user name

    'PWD='+pw+';' #user password

    )


        #connect to server

        cn = pyodbc.connect(cn_str)

        cursor = cn.cursor()
        cursor.execute('select * from School.dbo.Course')

        data = cursor.fetchall()

        for course in data:
            courseID = course[0]
            title = course[1]
            credits = course[2]
            deptID = course[3]

            preList = {'CourseID':courseID, 'Title':title, 'Credits':credits, 'DeptID':deptID}

            courseList.append(preList)

        #print(courseList)

        a = int(input('Enter Course ID: '))

        for dictionary in courseList:
            if a == dictionary['CourseID']:
                print(f'Title: {dictionary["Title"]}')
                print(f'Credits: {dictionary["Credits"]}')
                print(f'Dept ID: {dictionary["DeptID"]}')

        #print(data)

MySQL = myGUI()

