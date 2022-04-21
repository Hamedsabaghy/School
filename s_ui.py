from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import s_bl as bl

main_id = 0
main_name = ""
role = ""


def Add_student():
    global name_student
    global family_student
    global password_student

    Add_student_Tk = Tk()
    Add_student_Tk.title('Add student')
    Add_student_Tk.geometry("425x100")

    Label(Add_student_Tk, text='Name').grid(row=0)
    Label(Add_student_Tk, text='Family').grid(row=1)
    Label(Add_student_Tk, text='Password').grid(row=2)

    name_student = Entry(Add_student_Tk, width=25)
    name_student.grid(row=0, column=1)

    family_student = Entry(Add_student_Tk, width=25)
    family_student.grid(row=1, column=1)

    password_student = Entry(Add_student_Tk, width=25,show='*')
    password_student.grid(row=2, column=1)

    Add = Button(Add_student_Tk, text='Add', width=25, command=Add_student2)
    Add.grid(row=3)


def Add_student2():
    global name_student
    global family_student
    global password_student

    name_S = name_student.get()
    family_S = family_student.get()
    password_S = password_student.get()

    check = bl.check_password(password_S, 10)

    if check == True :
        s = bl.student(name_S, family_S, password_S)
        s.insert()
        l = bl.student.get(s)
        txt = '\t' + 'id:' + str(l[0]) + '  ' + 'name:' + l[1] + '  ' + 'family:' + l[2]
        messagebox.showinfo('Add student ', 'Added student :)' + txt)
    else:
        messagebox.showerror('Add student ', 'The number of characters in the password must be 6 and 10 characters')


# .......................

def Add_teacher():
    global name_teacher
    global family_teacher
    global password_teacher
    global lbc_Add_teacher

    Add_teacher_Tk = Tk()
    Add_teacher_Tk.title('Add teacher')
    Add_teacher_Tk.geometry("425x400")

    Label(Add_teacher_Tk, text='Name').grid(row=0)
    Label(Add_teacher_Tk, text='Family').grid(row=1)
    Label(Add_teacher_Tk, text='Password').grid(row=2)

    name_teacher = Entry(Add_teacher_Tk, width=25)
    name_teacher.grid(row=0, column=1)

    family_teacher = Entry(Add_teacher_Tk, width=25)
    family_teacher.grid(row=1, column=1)

    password_teacher = Entry(Add_teacher_Tk, width=25,show='*')
    password_teacher.grid(row=2, column=1)

    Label(Add_teacher_Tk, text="Course:").grid(row=3)

    scrollbar_add_teacher = Scrollbar(Add_teacher_Tk)
    scrollbar_add_teacher.grid(row=3, column=1)

    lbc_Add_teacher = Listbox(Add_teacher_Tk, yscrollcommand=scrollbar_add_teacher.set)
    l = bl.course.select()
    for i in l:
        lbc_Add_teacher.insert(END, i)
    lbc_Add_teacher.grid(row=3, column=1)
    scrollbar_add_teacher.config(command=lbc_Add_teacher.yview)

    Add = Button(Add_teacher_Tk, text='Add', width=25, command=Add_teacher2)
    Add.grid(row=4)


def Add_teacher2():
    global name_teacher
    global family_teacher
    global password_teacher
    global lbc_Add_teacher

    name = name_teacher.get()
    family = family_teacher.get()
    password_T = password_teacher.get()
    course = lbc_Add_teacher.get(ANCHOR)
    idc = course[0]

    check = bl.check_password(password_T, 10)

    if check == True:
        s = bl.teacher(name, family, idc, password_T)
        s.insert()
        l = bl.teacher.get(s)
        txt = '\t' + 'id:' + str(l[0]) + '  ' + 'name:' + l[1] + '  ' + 'family:' + l[2] + '  ' + 'id course: ' + str(
            l[3])
        messagebox.showinfo('Add teacher ', 'Added teacher :)' + txt)

    else:
        messagebox.showerror('Add teacher ', 'The number of characters in the password must be 6 and 10 characters')


# .......................

def Add_course():
    global name_course

    Add_course_Tk = Tk()
    Add_course_Tk.title('Add course')
    Add_course_Tk.geometry("425x100")

    Label(Add_course_Tk, text='Name').grid(row=0)

    name_course = Entry(Add_course_Tk, width=25)
    name_course.grid(row=0, column=1)

    Add = Button(Add_course_Tk, text='Add', width=25, command=Add_course2)
    Add.grid(row=3)


def Add_course2():
    global name_course

    name = name_course.get()

    s = bl.course(name)
    s.insert()
    l = bl.course.get(s)
    txt = '\t' + 'id:' + str(l[0]) + '  ' + 'name:' + l[1]
    messagebox.showinfo('Add course ', 'Added course :)' + txt)


# ..............................

def Add_admin_config(access):
    global var_Add_admin, Add_admin_Tk

    access = var_Add_admin.get()

    label = Label(Add_admin_Tk, text=" ", fg='RED')
    label.grid(row=5)

    if access == 1:

        text2 = 'Add admin by access 1,2,3 and delete admins with all access'
        

    elif access == 2:

        text2 ='Add admin by access 2 and 3 and delete admins with access 2 and 3'
        
    elif access == 3:

        text2 = "Can't add admin and delete admins with access 3"


    label.config(text=text2)
    
def Add_admin():
    global name_admin, family_admin, password_admin, access, var_Add_admin, Add_admin_Tk


    Add_admin_Tk = Tk()
    Add_admin_Tk.title('Add Admin')
    Add_admin_Tk.geometry("500x400")

    Label(Add_admin_Tk, text='Name: ',).grid(row=0)
    Label(Add_admin_Tk, text='Family').grid(row=1)
    Label(Add_admin_Tk, text='Password').grid(row=2)
    Label(Add_admin_Tk, text='Access: ').grid(row=3)

    name_admin = Entry(Add_admin_Tk)
    name_admin.grid(row=0, column=1)

    family_admin = Entry(Add_admin_Tk)
    family_admin.grid(row=1, column=1)

    password_admin=Entry(Add_admin_Tk,show='*')
    password_admin.grid(row=2, column=1)

    accesses = []
    for i in range(access,4):
        accesses.append(str(i))

    var_Add_admin = IntVar()


    set_access = OptionMenu(Add_admin_Tk, var_Add_admin, *accesses,command=Add_admin_config)
    set_access.grid(row=3,column=1)



    Add_button_Add_admin=Button(Add_admin_Tk, text='Add', width=25, command=Add_admin2)
    Add_button_Add_admin.grid(row=6)



def Add_admin2():
    global name_admin, family_admin, password_admin, var_Add_admin

    name = name_admin.get()
    family = family_admin.get()
    password = password_admin.get()
    access=var_Add_admin.get()

    admin=bl.admin(name, family, password, access)
    admin.insert()

    l = bl.admin.get(admin)
    txt = '\t' + 'Id:' + str(l[0]) + '  ' + 'Name:' + l[1] + '  ' + 'family:' + l[2] + '  '+ 'access:' + l[4]
    messagebox.showinfo('Add admin ', 'Added admin :)' + txt)

#................................

def Unit_selection():
    global unit_selection, next, lbc_unit_selection, next_button_unit_selection

    unit_selection = Tk()
    unit_selection.title('Unit selection')
    unit_selection.geometry("425x400")

    Label(unit_selection, text="Course:").grid(row=1)

    scrollbar_course_unit_selection = Scrollbar(unit_selection)
    scrollbar_course_unit_selection.grid(row=1, column=1)

    lbc_unit_selection = Listbox(unit_selection, yscrollcommand=scrollbar_course_unit_selection.set)
    l = bl.course.select()

    for i in l:
        lbc_unit_selection.insert(END, i)

    lbc_unit_selection.grid(row=1, column=1)
    scrollbar_course_unit_selection.config(command=lbc_unit_selection.yview)

    next_button_unit_selection = Button(unit_selection, text='Next', width=25, command=Unit_selection2)
    next_button_unit_selection.grid(row=2)


def Unit_selection2():
    global next_button_unit_selection, lbc_unit_selection, unit_selection
    global next3, lbt_unit_selection, course

    course = lbc_unit_selection.get(ANCHOR)
    course = course[0]
    next_button_unit_selection.destroy()

    Label(unit_selection, text="Teacher:").grid(row=2)

    scrollbar_teacher_unit_selection = Scrollbar(unit_selection)
    scrollbar_teacher_unit_selection.grid(row=2, column=1)

    lbt_unit_selection = Listbox(unit_selection, yscrollcommand=scrollbar_teacher_unit_selection.set)
    l = bl.teacher.select(course)

    for i in l:
        lbt_unit_selection.insert(END, i)

    lbt_unit_selection.grid(row=2, column=1)
    scrollbar_teacher_unit_selection.config(command=lbt_unit_selection.yview)

    OK_button = Button(unit_selection, text='OK', width=25, command=Unit_selection3)
    OK_button.grid(row=3)


def Unit_selection3():
    global OK_button, lbt_unit_selection, course, main_id, unit_selection

    Teacher = lbt_unit_selection.get(ANCHOR)
    Name_teacher_unit_selection = "'" + Teacher[0] + "'"
    Family_teacher_unit_selection = "'" + Teacher[1] + "'"

    id_teacher_unit_selection = str(
        bl.teacher.search(None, 2, Name_teacher_unit_selection, Family_teacher_unit_selection))

    Unit_selection = bl.unit_select(main_id, course, id_teacher_unit_selection)
    Unit_selection.insert()

    messagebox.showinfo('Unit selection', 'Unit selected :)')
    unit_selection.destroy()


# .....................

def Add_mark():
    global lbs_add_mark, mark_add_mark, main_id

    add_mark = Tk()
    add_mark.title('Add mark')
    add_mark.geometry("425x400")

    Label(add_mark, text="student:").grid(row=1)

    scrollbar_add_mark = Scrollbar(unit_selection)
    scrollbar_add_mark.grid(row=1, column=1)

    lbs_add_mark = Listbox(add_mark, yscrollcommand=scrollbar_add_mark.set)
    l = bl.unit_select.select_student(main_id)

    for i in l:
        lbs_add_mark.insert(END, i)
    lbs_add_mark.grid(row=1, column=1)
    scrollbar_add_mark.config(command=lbs_add_mark.yview)

    Label(add_mark, text='Mark:').grid(row=2)

    mark_add_mark = Entry(add_mark)
    mark_add_mark.grid(row=2, column=1)

    add = Button(add_mark, text='Add', width=25, command=Add_mark3)
    add.grid(row=3)


def Add_mark3():
    global lbs_add_mark, mark_add_mark, main_id

    student = lbs_add_mark.get(ANCHOR)
    mark = float(mark_add_mark.get())

    if mark > 20 or mark < 0:
        messagebox.showerror('Add mark ', 'Mark is out of range!!')
    else:
        bl.unit_select.Add_mark(main_id, student[0], mark)
        messagebox.showinfo('Add mark', 'Added :)')


# .......................


def Get_report_cart():
    location = filedialog.askdirectory()

    bl.unit_select.get_report_cart(main_id, location)
    messagebox.showinfo('Get report cart', 'Saved :)')


# .......................

def Report():
    report = Tk()
    report.title('Report')
    report.geometry("400x150")

    total, best, worst = bl.student.get_all_avg()

    Label(report, text='Total Average :').grid(row=0)
    Label(report, text='Best student :').grid(row=1)
    Label(report, text='Worst student :').grid(row=2)

    Label(report, text=str(total)).grid(row=0, column=1)
    Label(report, text=best).grid(row=1, column=1)
    Label(report, text=worst).grid(row=2, column=1)

    get_plot = Button(report, text='Get plot ', width=25, command=Get_plot)
    get_plot.grid(row=3)


def Get_plot():
    bl.student.Get_plot()


# ...........................................................................................

def change_password():
    global new_password_entry_change_password
    global confirm_password_entry_change_password
    global change_password_Tk

    change_password_Tk = Tk()
    change_password_Tk.title('Change password')
    change_password_Tk.geometry("400x200")

    new_password_label_change_password = Label(change_password_Tk, text='New password: ').grid(row=0)
    confirm_password_label_change_password = Label(change_password_Tk, text='Confirm password: ').grid(row=1)

    new_password_entry_change_password = Entry(change_password_Tk,show='*')
    new_password_entry_change_password.grid(row=0, column=1)
    confirm_password_entry_change_password = Entry(change_password_Tk,show='*')
    confirm_password_entry_change_password.grid(row=1, column=1)

    change_change_password = Button(change_password_Tk, text='Change', command=change_password2, width=25)
    change_change_password.grid(row=2)


def change_password2():
    global main_id, role, change_password_Tk
    global new_password_entry_change_password
    global confirm_password_entry_change_password

    new_password = (new_password_entry_change_password.get())
    confirm_password = (confirm_password_entry_change_password.get())

    if new_password == confirm_password:
        check = bl.change_password(new_password, role, main_id)

        if check == True:
            messagebox.showinfo("Change password", 'Password changed successfully :)')
            change_password_Tk.destroy()

        elif role == 'admin':
            messagebox.showerror("Change password",
                                 'The number of characters in the password must be 6 and 15 characters')

        else:

            messagebox.showerror("Change password",
                                 'The number of characters in the password must be 6 and 10 characters')

    else:
        messagebox.showerror("Change password", 'New password and confirm password are not mach ')


# ...........................................................................................



def Login():
    global id_login, password_login, var_login, login_Tk

    login_Tk = Tk()
    login_Tk.title('Login')
    login_Tk.geometry("500x300")

    roles = ["Admin", "Student", "Teacher"]
    var_login = StringVar()
    var_login.set("Set role")


    set_role_login = OptionMenu(login_Tk, var_login, *roles)
    set_role_login.grid(row=3)

    Label(login_Tk, text='ID').grid(row=0)
    Label(login_Tk, text='Password').grid(row=1)

    id_login = Entry(login_Tk, width=25)
    id_login.grid(row=0, column=1)

    password_login = Entry(login_Tk, width=25, show='*')
    password_login.grid(row=1, column=1)

    login_button = Button(login_Tk, text="Login", width=25, command=Login2)
    login_button.grid(row=4)


def Login2():
    global id_login, password_login, var_login, login_Tk
    global main_name, main_id, role

    role = var_login.get()

    id = int(id_login.get())
    password = password_login.get()

    # checks for student
    if role == "Student":
        check = bl.student.check_id(id)

        if check == True:
            check2 = bl.student.check_password(id, password)
            if check2 == True:
                name, family = bl.student.search(id)
                main_name = name + ' ' + family
                main_id = id
                role = 'student'

                login_Tk.destroy()
                main.destroy()
                Home()

                messagebox.showinfo('Login', 'Welcome   ' + main_name)

            else:
                messagebox.showerror('Login', 'Wrong id or password')

        else:
            messagebox.showerror('Login', 'Wrong id or password')

    # checks for teacher
    elif role == "Teacher":
        check = bl.teacher.check_id(id)

        if check == True:
            check2 = bl.teacher.check_password(id, password)
            if check2 == True:
                name, family = bl.teacher.search(id)
                main_name = name + ' ' + family
                main_id = id
                role = 'teacher'

                login_Tk.destroy()
                main.destroy()
                Home()

                messagebox.showinfo('Login', 'Welcome   ' + main_name)

            else:
                messagebox.showerror('Login', 'Wrong id or password')

        else:
            messagebox.showerror('Login', 'Wrong id or password')

    # checks for admin
    elif role == "Admin":
        check = bl.admin.check_id(id)

        if check == True:
            check2 = bl.admin.check_password(id, password)
            if check2 == True:
                name, family = bl.admin.search(id)
                main_name = name + ' ' + family
                main_id = id
                role = 'admin'

                login_Tk.destroy()
                main.destroy()
                Home()

                messagebox.showinfo('Login', 'Welcome   ' + main_name)

            else:
                messagebox.showerror('Login', 'Wrong id or password')

        else:
            messagebox.showerror('Login', 'Wrong id or password')
    elif role== "Set role":
        messagebox.showerror("Login","Select role")

# ============================================================================

def Home():
    global role, main_id, main_name, access

    home = Tk()
    home.title('Home')
    home.geometry("910x500")

    Label(home, text='Role :  ' + (role) + '\t\t', font=('Times 14')).grid(row=0)
    Label(home, text='ID :  ' + str(main_id) + '\t\t', font=('Times 14')).grid(row=0, column=1)
    Label(home, text='Name :  ' + (main_name) + '\t\t', font=('Times 14')).grid(row=0, column=2)

    if role == 'student':
        unit_selection = Button(home, text='Unit selection', font=('Times 14'), width=25, command=Unit_selection)
        unit_selection.grid(row=1)
        Report_cart = Button(home, text='Get report cart', font=('Times 14'), width=25, command=Get_report_cart)
        Report_cart.grid(row=2)
        Change_password_Button_Home = Button(home, text="Change Password", width=25, font=('Times 14'),command=change_password)
        Change_password_Button_Home.grid(row=1, column=1)

    if role == 'teacher':
        course = bl.teacher.select_course(main_id)
        Label(home, text='course : ' + course, font=('Times 14')).grid(row=0, column=3)

        Add_mark_Button_Home = Button(home, text='Add mark', font=('Times 14'), width=25, command=Add_mark)
        Add_mark_Button_Home.grid(row=1)
        Change_password_Button_Home = Button(home, text="Change Password", width=25, font=('Times 14'),
                                             command=change_password)
        Change_password_Button_Home.grid(row=1, column=1)

    if role == 'admin':
        access=bl.admin.select_access(main_id)
        Label(home, text="Access: " + str(access), font=('Times 14')).grid(row=0, column=3)

        report = Button(home, text='Report', font=('Times 14'), width=25, command=Report)
        report.grid(row=1)
        add_course = Button(home, text='Add Course', width=25, font=('Times 14'), command=Add_course)
        add_course.grid(row=2)
        add_teacher = Button(home, text='Add Teacher', width=25, font=('Times 14'), command=Add_teacher)
        add_teacher.grid(row=3)
        Change_password_Button_Home = Button(home, text="Change Password", width=25, font=('Times 14'),command=change_password)
        Change_password_Button_Home.grid(row=1, column=1)

        if access<3 :
            Add_admin_Button= Button(home, text=" Add Admin", width=25, font=('Times 14'),command=Add_admin)
            Add_admin_Button.grid(row=2, column=1)



# .............................................................

Login()


main = Tk()
main.title('School')
main.geometry("600x500")

Label(main, text='Welcome to School', fg='#2debb8', font=('Times 14'), width=60, height=15).grid(row=0)

about_school = Button(main, text='About School', font=('Times 14'), width=50, bg='#ffffff')
about_school.grid(row=3)
login_B = Button(main, text='Login', font=('Times 14'), width=25, bg='#0afffb', command=Login)
login_B.grid(row=2)
sing_up = Button(main, text='Sing up student', font=('Times 14'), width=25, bg='#ebff0a', command=Add_student)
sing_up.grid(row=1)

mainloop()
