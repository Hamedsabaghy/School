from s_da import *
import matplotlib.pyplot as plt
dbm=dbm()

class student:
    def __init__(self,name,family):
        L = dbm.select('Select count(*) from student')
        self.id = L[0][0] + 1
        self.name=name
        self.family=family
        self.avr=0

    def get(self):
        return self.id,self.name,self.family,self.avr

    def insert(self):
        Q='INSERT INTO student VALUES (?,?,?,?)'
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
        print(L)
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





class teacher:
    def __init__(self,name,family,idc):
        L = dbm.select('Select count(*) from teacher')
        self.id = L[0][0] + 1
        self.name=name
        self.family=family
        self.idc=idc

    def get(self):
        return self.id,self.name,self.family,self.idc

    def insert(self):
        Q='INSERT INTO teacher VALUES (?,?,?,?)'
        P=self.get()
        dbm.insert(Q,P)

    @staticmethod
    def select(course):
        Q='select * from teacher where idc={}'.format(course)
        L = dbm.select(Q)
        return L

    @staticmethod
    def check_id(id):
        Q = 'Select count(*) from teacher where id={}'.format(id)
        l = dbm.select(Q)
        return l[0][0]

    @staticmethod
    def search(idt):
        Q = 'select name,family from teacher where id={}'.format(idt)
        L = dbm.select(Q)
        return L[0][0],L[0][1]



class course:
    def __init__(self,name):
        L = dbm.select('Select count(*) from teacher')
        self.id = L[0][0] + 1
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
        Q = 'select name  from course where id={}'.format(idc)
        L = dbm.select(Q)
        return L[0][0]



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
        Q='select * from student where id in (select ids from unit_select where idt={})'.format(idt)
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

