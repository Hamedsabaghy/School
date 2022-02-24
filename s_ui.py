from tkinter import *
from tkinter import  messagebox
import s_bl as bl
from datetime import date

def Add_student():
    global name_student
    global family_student

    addstudent=Tk()
    addstudent.title('Add student')
    addstudent.geometry("425x100")

    Label(addstudent, text='Name' ).grid(row=0)
    Label(addstudent, text='family' ).grid(row=1)

    name_student =Entry(addstudent,width=25)
    name_student.grid(row=0, column=1)

    family_student =Entry(addstudent,width=25)
    family_student.grid(row=1, column=1)

    Add=Button(addstudent, text='Add', width=25,command=adds )
    Add.grid(row=3)

def adds():
    global name_student
    global family_student
    name=name_student.get()
    family=family_student.get()
    s=bl.student(name,family)
    s.insert()
    l = bl.student.get(s)
    txt = '\t' + 'id:' + str(l[0]) + '  ' + 'name:' + l[1] + '  ' + 'family:' + l[2]
    messagebox.showinfo('Add sudent ','Added student :)'+txt)

#.......................

def Add_teacher():
    global name_teacher
    global family_teacher
    global lbc
    addteacher=Tk()
    addteacher.title('Add teacher')
    addteacher.geometry("425x400")

    Label(addteacher, text='Name' ).grid(row=0)
    Label(addteacher, text='family' ).grid(row=1)

    name_teacher =Entry(addteacher,width=25)
    name_teacher.grid(row=0, column=1)

    family_teacher =Entry(addteacher,width=25)
    family_teacher.grid(row=1, column=1)

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
    global lbc

    name=name_teacher.get()
    family=family_teacher.get()
    course = lbc.get(ANCHOR)
    idc=course[0]
    s=bl.teacher(name,family,idc)
    s.insert()
    l=bl.teacher.get(s)
    txt='\t'+'id:'+str(l[0])+'  '+'name:'+l[1]+'  '+'family:'+l[2]+'  '+'id course: '+str(l[3])
    messagebox.showinfo('Add teacher ','Added teacher :)'+txt)

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

    name=name_course.get()

    s=bl.course(name)
    s.insert()
    l = bl.course.get(s)
    txt = '\t' + 'id:' + str(l[0]) + '  ' + 'name:' + l[1]
    messagebox.showinfo('Add course ','Added course :)'+txt)

#.......................

def Unit_selection ():
    global student_id
    global next
    global unitselection

    unitselection=Tk()
    unitselection.title('Unit selection')
    unitselection.geometry("425x400")

    Label(unitselection,text='student id :').grid(row=0)

    student_id=Entry(unitselection)
    student_id.grid(row=0,column=1)

    next=Button(unitselection,text='Next',width=25,command=Unit_selection2)
    next.grid(row=1)
def Unit_selection2 ():
    global student_id,next
    global unitselection,next2,lbc2,ids_student

    ids_student=int(student_id.get())
    check=bl.student.check_id(ids_student)
    if check==True:
        next.destroy()

        Label(unitselection, text="Course:").grid(row=1)

        lbc2 = Listbox(unitselection)
        l = bl.course.select()
        for i in l:
            lbc2.insert(END, i)
        lbc2.grid(row=1,column=1)

        next2 = Button(unitselection, text='Next', width=25, command=Unit_selection3)
        next2.grid(row=2)

    else:
        messagebox.showerror("Unit selection",'id:'+str(ids_student)+'\t'+'Not found')
        unitselection.destroy()
        Unit_selection()

def Unit_selection3():
    global next2, lbc2, ids_student,unitselection
    global ids_student,next3,lbt,course

    course = lbc2.get(ANCHOR)
    course=course[0]
    next2.destroy()

    Label(unitselection, text="Teacher:").grid(row=2)

    lbt = Listbox(unitselection)
    l = bl.teacher.select(course)
    for i in l:
        lbt.insert(END, i)
    lbt.grid(row=2,column=1)
    OK = Button(unitselection, text='OK', width=25, command=Unit_selection4)
    OK.grid(row=3)

def Unit_selection4():
    global ids_student, OK, lbt,course

    teacher=lbt.get(ANCHOR)

    Unit_selection=bl.unit_select(ids_student,course,teacher[0])
    Unit_selection.insert()
    messagebox.showinfo('Unit selection','Unit selected :)')
#.....................
def Add_mark():
    global add_mark, teacher_id, nextt

    add_mark=Tk()
    add_mark.title('Add mark')
    add_mark.geometry("425x400")
    
    Label(add_mark,text='Teacher id: ').grid(row=0)

    teacher_id = Entry(add_mark)
    teacher_id.grid(row=0, column=1)

    nextt = Button(add_mark, text='Next', width=25, command=Add_mark2)
    nextt.grid(row=1)

def Add_mark2():
    global add_mark, teacher_id, nextt, lbs, mark, idt_teacher


    idt_teacher=int(teacher_id.get())

    check=bl.teacher.check_id(idt_teacher)

    if check==True:
        nextt.destroy()

        Label(add_mark, text="student:").grid(row=1)

        lbs = Listbox(add_mark)
        l = bl.unit_select.select_student(idt_teacher)

        for i in l:
            lbs.insert(END, i)
        lbs.grid(row=1,column=1)

        Label(add_mark,text='Mark:').grid(row=2)

        mark=Entry(add_mark)
        mark.grid(row=2,column=1)

        add=Button(add_mark,text='Add', width=25, command=Add_mark3)
        add.grid(row=3)

    else:
        messagebox.showerror("Add mark", 'id:' + str(idt_teacher) + '\t' + 'Not found')
        add_mark.destroy()
        Add_mark()

def Add_mark3():
    global lbs, mark, idt_teacher

    student=lbs.get(ANCHOR)
    mark2=float(mark.get())

    if mark2>20 or mark2<0 :
        messagebox.showerror('Add mark ','Mark is out of range!!')
    else:
        bl.unit_select.addmark(idt_teacher,student[0],mark2)
        messagebox.showinfo('Add mark','Added :)')

#.......................

def Get_report_cart():
    global student_idg, get_report_cart, get

    get_report_cart = Tk()
    get_report_cart.title('Get report cart')
    get_report_cart.geometry("425x400")

    Label(get_report_cart, text='student id :').grid(row=0)

    student_idg = Entry(get_report_cart)
    student_idg.grid(row=0, column=1)

    get = Button(get_report_cart, text='Get', width=25, command=Get_report_cart2)
    get.grid(row=1)

def Get_report_cart2():
    global student_idg, get_report_cart, get

    ids_student = int(student_idg.get())
    check = bl.student.check_id(ids_student)

    if check == True:
        L=bl.unit_select.select(ids_student)

        name_s,family_s = bl.student.search(ids_student)

        txt='____________________________Report cart____________________________'
        txt+='\n'+'Date: '+str(date.today())+'\t'+'Name: '+name_s +' '+ family_s+'\t\t'+'ID:'+str(ids_student)
        txt+='\n'+'-------------------------------------------------------------------'
        txt+='\n'+'Count'+'\t'+'teacher'+'\t\t\t\t'+'Course'+'\t\t\t\t'+'Mark'

        count=1
        summark=0
        for i in L:
            name_t, family_t=bl.teacher.search(i[2])
            name_c=bl.course.search(i[3])
            txt+='\n'+str(count)+'\t\t'+name_t+' '+family_t+'\t\t\t'+name_c+'\t\t'+str(i[4])
            summark+=i[4]
            count+=1

        txt+='\n'+'___________________________________________________________________'
        txt+='\n'+'Average: '+str(bl.student.getavg(ids_student))+'\t\t'+'Total sum:'+str(summark)

        n='Report of cart id {} .txt'.format(str(ids_student))
        file=open(n,'w')
        file.write(txt)
        messagebox.showinfo('Get report cart','Saved :)')

    else:
        messagebox.showerror("Get report cart", 'id:' + str(ids_student) + '\t' + 'Not found')
        get_report_cart.destroy()
        Get_report_cart()

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


#---------------------------------------------------------------------
main=Tk()
main.title('School')
main.geometry("500x300")
frame1=Frame(main)
frame1.pack(side=LEFT)
frame2=Frame(main)
frame2.pack(side=RIGHT)

student=Button(frame1,text='Add student',font=('Times 14'), width=25,command=Add_student)
student.grid(row=0)
teacher=Button(frame1,text='Add teacher',font=('Times 14'), width=25,command=Add_teacher)
teacher.grid(row=1)
course=Button(frame1,text='Add course',font=('Times 14'), width=25,command=Add_course)
course.grid(row=2)

#.............................................................

Unitselection=Button(frame2,text='Unit selection',font=('Times 14'), width=25,command=Unit_selection)
Unitselection.grid(row=0)
addmark=Button(frame2,text='Add mark',font=('Times 14'), width=25,command=Add_mark)
addmark.grid(row=1)
report=Button(frame2,text='Report',font=('Times 14'), width=25,command=Report)
report.grid(row=2)
reportcart=Button(frame2,text='Get report cart',font=('Times 14'), width=25,command=Get_report_cart)
reportcart.grid(row=3)


mainloop()
