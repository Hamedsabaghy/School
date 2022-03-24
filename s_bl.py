from s_da import *
import matplotlib.pyplot as plt
import random
from datetime import date

dbm=dbm()

class student:
    def __init__(self,name,family,password):
        L = dbm.select('Select count(*) from student')
        self.id = L[0][0] + 2000
        self.name=name
        self.family=family
        self.password=password
        self.avr=0

    def get(self):
        return self.id,self.name,self.family,self.avr,self.password

    def insert(self):
        Q='INSERT INTO student VALUES (?,?,?,?,?)'
        P=self.get()
        dbm.insert(Q,P)
    @staticmethod
    def check_id(id):
        Q= 'Select count(*) from student where id={}'.format(id)
        l=dbm.select(Q)
        return l[0][0]

    @staticmethod
    def allname():
        Q='select name,family from student'
        l=dbm.select(Q)

        names=[]
        for i in l :
            names.append(i[0]+' '+i[1])
        return names

    @staticmethod
    def search(ids):
        Q='select name,family from student where id={}'.format(ids)
        L=dbm.select(Q)
        return L[0][0],L[0][1]
    @staticmethod
    def getavg(ids):
        Q='select avg from student where id={}'.format(ids)
        L=dbm.select(Q)
        return L[0][0]

    @staticmethod
    def get_all_avg():
        global Marks

        Q='select avg from student '
        l=dbm.select(Q)
        Marks=[]
        for i in l:
            Marks.append(i[0])
        Total=sum(Marks)/len(Marks)
        best=Marks.index(max(Marks))
        worst=Marks.index(min(Marks))

        name_b,family_b=student.search(best+1)
        name_w,family_w=student.search(worst+1)
        Best=name_b+' '+family_b
        Worst=name_w+' '+family_w
        return (Total,Best,Worst)

    @staticmethod
    def getplot():
        global Marks

        names=student.allname()
        plt.bar(names,Marks)
        plt.show()
        plt.savefig('plot.png')

    @staticmethod
    def check_password(ids,password_s):
        Q='select password from student where id={}'.format(ids)
        password=dbm.select(Q)

        if password_s==password[0][0]:
            return True





class teacher:
    def __init__(self,name,family,idc,password):
        L = dbm.select('Select count(*) from teacher')
        self.id = L[0][0] + 1000
        self.name=name
        self.family=family
        self.idc=idc
        self.password=password

    def get(self):
        return self.id,self.name,self.family,self.idc,self.password

    def insert(self):
        Q='INSERT INTO teacher VALUES (?,?,?,?,?)'
        P=self.get()
        dbm.insert(Q,P)

    @staticmethod
    def select(course):
        Q='select name,family from teacher where idc={}'.format(course)
        L = dbm.select(Q)
        return L

    @staticmethod
    def check_id(id):
        Q = 'Select count(*) from teacher where id={}'.format(id)
        l = dbm.select(Q)
        return l[0][0]

    @staticmethod
    def search(idt=1,mood=1,name='',family=''):

        if mood ==1:
            Q = 'select name,family from teacher where id={}'.format(idt)
            L = dbm.select(Q)
            print(L,idt)
            return L[0][0],L[0][1]

        elif mood==2:
            Q='select id from teacher where name={} AND family={}'.format(name,family)
            L = dbm.select(Q)
            return L[0][0]

    @staticmethod
    def check_password(idt, password_t):
        Q = 'select password from teacher where id={}'.format(idt)
        password = dbm.select(Q)

        if password_t == password[0][0]:
            return True

    @staticmethod
    def select_course(idt):
        Q = 'select name from course where id in (select idc from teacher where id={}) '.format(idt)
        course=dbm.select(Q)

        return course[0][0]



class admin:
    def __init__(self, name, family, password, access):

        self.id = random.randrange(10**5, 999999)
        self.name = name
        self.family = family
        self.password = password
        self.access=access

    def get(self):
        return self.id, self.name, self.family, self.password, self.access

    def insert(self):
        Q='INSERT INTO admin VALUES (?,?,?,?,?)'
        P=self.get()
        dbm.insert(Q,P)

    @staticmethod
    def check_password(id, password_d):
        Q = 'select password from admin where id={}'.format(id)
        password = dbm.select(Q)

        if password_d == password[0][0]:
            return True

    @staticmethod
    def search(id):
        Q = 'select name,family from admin where id={}'.format(id)
        L = dbm.select(Q)
        return L[0][0], L[0][1]

    @staticmethod
    def check_id(id):
        Q = 'Select count(*) from admin where id={}'.format(id)
        l = dbm.select(Q)
        return l[0][0]


class course:
    def __init__(self,name):
        L = dbm.select('Select count(*) from teacher')
        self.id = L[0][0] + 1500
        self.name=name

    def get(self):
        return self.id,self.name

    def insert(self):
        Q='INSERT INTO course VALUES (?,?)'
        P=self.get()
        dbm.insert(Q,P)
    @staticmethod
    def select():
        L = dbm.select('select * from course')
        return L

    @staticmethod
    def search(idc):
        Q = 'select name from course where id={}'.format(idc)
        L = dbm.select(Q)
        return L[0][0]

    @staticmethod
    def check_id(id):
        Q = 'Select count(*) from teacher where id={}'.format(id)
        l = dbm.select(Q)
        return l[0][0]


class unit_select:
    def __init__(self,ids,idc,idt):
        L = dbm.select('Select count(*) from unit_select')
        self.id = L[0][0] + 1
        self.ids=ids
        self.idc=idc
        self.idt=idt
        self.mark=0

    def get(self):
        return self.id,self.ids,self.idc,self.idt,self.mark

    def insert(self):
        Q='INSERT INTO unit_select VALUES (?,?,?,?,?)'
        P=self.get()
        dbm.insert(Q,P)

    @staticmethod
    def select_student(idt):
        Q='select id,name,family from student where id in (select ids from unit_select where idt={})'.format(idt)
        L = dbm.select(Q)
        return L

    @staticmethod
    def addmark(idt,ids,mark):
        Q='update unit_select set mark={} where ids={} AND idt={}'.format(mark,ids,idt)
        dbm.update(Q)
        unit_select.avg(ids)


    @staticmethod
    def select(ids):
        Q='select * from unit_select where ids={}'.format(ids)
        L=dbm.select(Q)
        return L

    @staticmethod
    def avg(ids):
        marks=[]
        Q='select mark from unit_select where ids={}'.format(ids)
        l=dbm.select(Q)
        for i in l:
            marks.append(i[0])
        avr=sum(marks)/len(marks)

        Q='update student set avg={} where id={}'.format(avr,ids)
        dbm.update(Q)
        
    @staticmethod
    def get_report_cart(main_id):
        
        L=unit_select.select(main_id)

        name_student,family_student =student.search(main_id)

        txt='____________________________Report cart____________________________'
        txt+='\n'+'Date: '+str(date.today())+'\t'+'Name: '+name_student +' '+ family_student+'\t\t'+'ID:'+str(main_id)
        txt+='\n'+'-------------------------------------------------------------------'
        txt+='\n'+'Count'+'\t'+'Teacher'+'\t\t\t\t'+'Course'+'\t\t\t\t'+'Mark'

        count=1
        summark=0
        for i in L:
            name_teacher, family_teacher=teacher.search(i[3])
            name_course=course.search(i[2])
            txt+='\n'+str(count)+'\t\t'+name_teacher+' '+family_teacher+'\t\t\t'+name_course+'\t\t'+str(i[4])
            summark+=i[4]
            count+=1

        txt+='\n'+'___________________________________________________________________'
        txt+='\n'+'Average: '+str(student.getavg(main_id))+'\t\t'+'Total sum:'+str(summark)

        n='Report cart of id {} .txt'.format(str(main_id))
        file=open(n,'w')
        file.write(txt)
        
        

def checkpassword(password,max):
    password_letters=len(password)
    if password_letters<=max and password_letters>=6:
        return True
    else :
        return False

def change_password(password,role,id):
    if role=='admin':
        check=checkpassword(password,15)
    elif role=='student' or role=='teacher' :
        check=checkpassword(password,10)

    if check == True:
        Q='update {} set password={} where id={}'.format(role,password,str(id))
        dbm.update(Q)
        return True
    else:
        return False
