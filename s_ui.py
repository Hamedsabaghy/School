from tkinter import *
from tkinter import messagebox
import s_bl as bl


main_id=0
main_name=0
role=0

def Add_student():
    global name_student
    global family_student
    global password_student

    addstudent=Tk()
    addstudent.title('Add student')
    addstudent.geometry("425x100")

    Label(addstudent, text='Name' ).grid(row=0)
    Label(addstudent, text='Family' ).grid(row=1)
    Label(addstudent, text='Password').grid(row=2)

    name_student =Entry(addstudent,width=25)
    name_student.grid(row=0, column=1)

    family_student =Entry(addstudent,width=25)
    family_student.grid(row=1, column=1)

    password_student = Entry(addstudent, width=25)
    password_student.grid(row=2, column=1)


    Add=Button(addstudent, text='Add', width=25,command=adds )
    Add.grid(row=3)

def adds():
    global name_student
    global family_student
    global password_student

    name_S=name_student.get()
    family_S=family_student.get()
    password_S=password_student.get()

    check=bl.checkpassword(password_S,10)

    if check==True:
        s=bl.student(name_S,family_S,password_S)
        s.insert()
        l = bl.student.get(s)
        txt = '\t' + 'id:' + str(l[0]) + '  ' + 'name:' + l[1] + '  ' + 'family:' + l[2]
        messagebox.showinfo('Add student ','Added student :)'+txt)
    else:
        messagebox.showerror('Add student ','The number of characters in the password must be 6 and 10 characters')
#.......................

def Add_teacher():
    global name_teacher
    global family_teacher
    global password_teacher
    global lbc

    addteacher=Tk()
    addteacher.title('Add teacher')
    addteacher.geometry("425x400")

    Label(addteacher, text='Name' ).grid(row=0)
    Label(addteacher, text='Family').grid(row=1)
    Label(addteacher, text='Password').grid(row=2)

    name_teacher =Entry(addteacher,width=25)
    name_teacher.grid(row=0, column=1)

    family_teacher =Entry(addteacher,width=25)
    family_teacher.grid(row=1, column=1)

    password_teacher=Entry(addteacher,width=25)
    password_teacher.grid(row=2, column=1)

    Label(addteacher,text="Course:").grid(row=3)

    lbc=Listbox(addteacher)
    l = bl.course.select()
    for i in l :
        lbc.insert(END,i)
    lbc.grid(row=3,column=1)

    Add=Button(addteacher, text='Add', width=25,command=addt )
    Add.grid(row=4)

def addt():
    global name_teacher
    global family_teacher
    global password_teacher
    global lbc

    name=name_teacher.get()
    family=family_teacher.get()
    password_T=password_teacher.get()
    course = lbc.get(ANCHOR)
    idc = course[0]

    check=bl.checkpassword(password_T,10)

    if check==True:
        s=bl.teacher(name,family,idc,password_T)
        s.insert()
        l=bl.teacher.get(s)
        txt='\t'+'id:'+str(l[0])+'  '+'name:'+l[1]+'  '+'family:'+l[2]+'  '+'id course: '+str(l[3])
        messagebox.showinfo('Add teacher ','Added teacher :)'+txt)

    else:
        messagebox.showerror('Add teacher ','The number of characters in the password must be 6 and 10 characters')
#.......................

def Add_course():
    global name_course

    addcourse=Tk()
    addcourse.title('Add course')
    addcourse.geometry("425x100")

    Label(addcourse, text='Name' ).grid(row=0)

    name_course =Entry(addcourse,width=25)
    name_course.grid(row=0, column=1)

    Add=Button(addcourse, text='Add', width=25,command=addc )
    Add.grid(row=3)

def addc():
    global name_course

    name = name_course.get()

    s = bl.course(name)
    s.insert()
    l = bl.course.get(s)
    txt = '\t' + 'id:' + str(l[0]) + '  ' + 'name:' + l[1]
    messagebox.showinfo('Add course ', 'Added course :)'+txt)

#.......................

def Unit_selection ():
    global unit_selection,next,lbc_unit_selection,next_button_unit_selection

    unit_selection=Tk()
    unit_selection.title('Unit selection')
    unit_selection.geometry("425x400")
    
    Label(unit_selection, text="Course:").grid(row=1)

    lbc_unit_selection = Listbox(unit_selection)
    l = bl.course.select()
    
    for i in l:
        lbc_unit_selection.insert(END, i)

    lbc_unit_selection.grid(row=1,column=1)

    next_button_unit_selection = Button(unit_selection, text='Next', width=25, command=Unit_selection2)
    next_button_unit_selection.grid(row=2)


def Unit_selection2():
    global next_button_unit_selection, lbc_unit_selection,unit_selection
    global next3,lbt_unit_selection,course

    course = lbc_unit_selection.get(ANCHOR)
    course=course[0]
    next_button_unit_selection.destroy()

    Label(unit_selection, text="Teacher:").grid(row=2)

    lbt_unit_selection = Listbox(unit_selection)
    l = bl.teacher.select(course)

    for i in l:
        lbt_unit_selection.insert(END, i)

    lbt_unit_selection.grid(row=2,column=1)

    OK_button = Button(unit_selection, text='OK', width=25, command=Unit_selection3)
    OK_button.grid(row=3)

def Unit_selection3():
    global OK_button, lbt_unit_selection,course,main_id,unit_selection

    Teacher=lbt_unit_selection.get(ANCHOR)
    Name_teacher_unit_selection="'"+Teacher[0]+"'"
    Family_teacher_unit_selection="'"+Teacher[1]+"'"

    id_teacher_unit_selection=str(bl.teacher.search(None,2,Name_teacher_unit_selection,Family_teacher_unit_selection))

    Unit_selection=bl.unit_select(main_id,course,id_teacher_unit_selection)
    Unit_selection.insert()

    messagebox.showinfo('Unit selection','Unit selected :)')
    unit_selection.destroy()

#.....................

def Add_mark():
    global  lbs_add_mark, mark_add_mark, main_id

    add_mark = Tk()
    add_mark.title('Add mark')
    add_mark.geometry("425x400")

    Label(add_mark, text="student:").grid(row=1)

    lbs_add_mark = Listbox(add_mark)
    l = bl.unit_select.select_student(main_id)
    print(l)

    for i in l:
        lbs_add_mark.insert(END, i)
    lbs_add_mark.grid(row=1,column=1)

    Label(add_mark,text='Mark:').grid(row=2)

    mark_add_mark=Entry(add_mark)
    mark_add_mark.grid(row=2,column=1)

    add=Button(add_mark,text='Add', width=25, command=Add_mark3)
    add.grid(row=3)

def Add_mark3():
    global lbs_add_mark, mark_add_mark, main_id

    student=lbs_add_mark.get(ANCHOR)
    mark=float(mark_add_mark.get())

    if mark>20 or mark<0 :
        messagebox.showerror('Add mark ','Mark is out of range!!')
    else:
        bl.unit_select.addmark(main_id,student[0],mark)
        messagebox.showinfo('Add mark','Added :)')

#.......................


def Get_report_cart():

    bl.unit_select.get_report_cart(main_id)
    messagebox.showinfo('Get report cart','Saved :)')

#.......................

def Report():
    report = Tk()
    report.title('Report')
    report.geometry("400x150")

    total,best,worst=bl.student.get_all_avg()

    Label(report,text='Total Average :').grid(row=0)
    Label(report, text='Best student :').grid(row=1)
    Label(report, text='Worst student :').grid(row=2)

    Label(report, text=str(total)).grid(row=0,column=1)
    Label(report, text=best).grid(row=1,column=1)
    Label(report, text=worst).grid(row=2,column=1)

    getplot=Button(report, text='Get plot ', width=25, command=Getplot)
    getplot.grid(row=3)

def Getplot():
    bl.student.getplot()


#...........................................................................................



def Login():
    global id_login, password_login,var_login,login


    login = Tk()
    login.title('Login')
    login.geometry("500x300")
    var_login = IntVar()


    student_radio = Radiobutton(login, text='Student', variable=var_login, value=1)
    student_radio.grid(row=2, column=1)

    teacher_radio = Radiobutton(login, text='Teacher', variable=var_login, value=2)
    teacher_radio.grid(row=2)

    admin_radio = Radiobutton(login, text='Admin', variable=var_login, value=3)
    admin_radio.grid(row=2, column=2)

    Label(login, text='ID').grid(row=0)
    Label(login, text='Password').grid(row=1)

    id_login = Entry(login, width=25)
    id_login.grid(row=0, column=1)

    password_login = Entry(login, width=25)
    password_login.grid(row=1, column=1)

    Login_button = Button(login, text="Login", width=25, command=Login2)
    Login_button.grid(row=3)


def Login2():
    global id_login, password_login,var_login,login
    global main_name, main_id ,role

    role=var_login.get()
    id = int(id_login.get())
    password = password_login.get()

    # checks for student
    if role == 1:
        check = bl.student.check_id(id)

        if check == True:
            check2 = bl.student.check_password(id, password)
            if check2 == True:
                name, family = bl.student.search(id)
                main_name = name + ' ' + family
                main_id = id
                role='student'

                login.destroy()
                main.destroy()
                Home()

                messagebox.showinfo('Login', 'Welcome   '+main_name)

            else:
                messagebox.showerror('Login', 'Wrong id or password')

        else:
            messagebox.showerror('Login', 'Wrong id or password')

    # checks for teacher
    if role == 2:
        check = bl.teacher.check_id(id)

        if check == True:
            check2 = bl.teacher.check_password(id, password)
            if check2 == True:
                name, family = bl.teacher.search(id)
                main_name = name + ' ' + family
                main_id = id
                role='teacher'

                login.destroy()
                main.destroy()
                Home()

                messagebox.showinfo('Login', 'Welcome   '+main_name)

            else:
                messagebox.showerror('Login', 'Wrong id or password')

        else:
            messagebox.showerror('Login', 'Wrong id or password')

    # checks for admin
    if role == 3:
        check = bl.admin.check_id(id)

        if check == True:
            check2 = bl.admin.check_password(id, password)
            if check2 == True:
                name, family = bl.admin.search(id)
                main_name = name + ' ' + family
                main_id = id
                role='admin'

                login.destroy()
                main.destroy()
                Home()

                messagebox.showinfo('Login', 'Welcome   '+main_name)

            else:
                messagebox.showerror('Login', 'Wrong id or password')

        else:
            messagebox.showerror('Login', 'Wrong id or password')

# ============================================================================

def Home():
    global role,main_id,main_name

    home=Tk()
    home.title('Home')
    home.geometry("890x500")

    Label(home,text='Role :  '+(role)+'\t\t',font=('Times 14')).grid(row=0)
    Label(home, text='ID :  ' + str(main_id)+'\t\t',font=('Times 14')).grid(row=0,column=1)
    Label(home, text='Name :  ' + (main_name)+'\t\t',font=('Times 14')).grid(row=0, column=2)

    if role=='student':
        unit_selection = Button(home, text='Unit selection', font=('Times 14'), width=25, command=Unit_selection)
        unit_selection.grid(row=1)
        reportcart = Button(home, text='Get report cart', font=('Times 14'), width=25, command=Get_report_cart)
        reportcart.grid(row=2)

    if role=='teacher':
        course=bl.teacher.select_course(main_id)
        Label(home,text='course : '+course,font=('Times 14')).grid(row=0,column=3)

        addmark = Button(home, text='Add mark', font=('Times 14'), width=25, command=Add_mark)
        addmark.grid(row=1)

    if role=='admin':
        report = Button(home, text='Report', font=('Times 14'), width=25, command=Report)
        report.grid(row=1)
        add_course = Button(home, text='Add Course', width=25, font=('Times 14'), command=Add_course)
        add_course.grid(row=2)
        add_teacher = Button(home, text='Add Teacher', width=25, font=('Times 14'), command=Add_teacher)
        add_teacher.grid(row=3)


# .............................................................

Login()
main=Tk()
main.title('School')
main.geometry("600x500")

Label(main,text='Welcome to School',fg='#2debb8',font=('Times 14'), width=60, height=15).grid(row=0)

about_school =Button(main,text='About School',font=('Times 14'), width=50,bg='#ffffff')
about_school.grid(row=3)
login_B=Button(main,text='Login',font=('Times 14'), width=25,bg='#0afffb',command=Login)
login_B.grid(row=2)
sing_up =Button(main,text='Sing up student',font=('Times 14'), width=25,bg='#ebff0a',command=Add_student)
sing_up.grid(row=1)


mainloop()

