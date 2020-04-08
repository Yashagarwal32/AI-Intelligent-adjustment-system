from tkinter import *
import sqlite3
import tkinter.messagebox

conn=sqlite3.connect('databse.db')
c=conn.cursor()

#empty list to later append the ids
ids=[]








class Application:
    def __init__(self,master):
        self.master=master

        self.sname_var=StringVar()
        self.day_var=StringVar()
        self.slot1_var=StringVar()
        self.slot2_var=StringVar()
        self.slot3_var=StringVar()
        self.slot4_var=StringVar()
        self.slot5_var=StringVar()
        self.slot6_var=StringVar()
        self.subject1_var=StringVar()
        self.subject2_var=StringVar()
        self.subject3_var=StringVar()
        self.subject4_var=StringVar()
            
        self.fsubject1_var=StringVar()
        self.fsubject2_var=StringVar()
        
        self.fsubject3_var=StringVar()
        self.fsubject4_var=StringVar()
        self.fname_var=StringVar()
        self.fuid_var=StringVar()
        self.fgender_var=StringVar()
        self.fdob_var=StringVar()
        self.fsalary_var=StringVar()
        self.fsection1_var=StringVar()
        self.fsection2_var=StringVar()

        self.stname_var=StringVar()
        self.stuid_var=StringVar()
        self.stgender_var=StringVar()
        self.stsection_var=StringVar()
        self.stnamem_var=StringVar()
        self.stpassword_var=StringVar()
        
        





                
        self.mainf=Frame(master,width=1500,height=720,bg='black')
        self.mainf.pack(side=LEFT)

                
        self.front=Frame(self.mainf,width=1270,height=720,bg='yellow')
        self.front.pack(side=LEFT)

        self.managestudent=Button(self.front,text="Students",width=20,height=2,bg='steelblue',command=self.student_login)
        self.managestudent.place(x=100,y=350)
        self.manager=Button(self.front,text="Managers",width=20,height=2,bg='steelblue',command=self.managers_entry)
        self.manager.place(x=500,y=350)
        self.manageteacher=Button(self.front,text="Teachers",width=20,height=2,bg='steelblue')
        self.manageteacher.place(x=900,y=350)

    def managers_entry(self):
        self.front.destroy()
        
        self.manage=Frame(self.mainf,width=1270,height=720,bg='crimson')
        self.manage.pack(side=LEFT)

        self.managestudent=Button(self.manage,text="Manage Students",width=20,height=2,bg='steelblue',command=self.manage_students)
        self.managestudent.place(x=100,y=400)
        
        self.managesection=Button(self.manage,text="Manage Sections",width=20,height=2,bg='steelblue',command=self.manage_sectionsf)
        self.managesection.place(x=500,y=400)
        
        self.manageteacher=Button(self.manage,text="Manage Teachers",width=20,height=2,bg='steelblue',command=self.manage_teachersf)
        self.manageteacher.place(x=900,y=400)

        self.fback=Button(self.manage,text="Go Back",width=8,height=1,bg='steelblue',command=self.back3_db)
        self.fback.place(x=10,y=10)



    def manage_sectionsf(self):        
        self.manage.destroy()
        self.left=Frame(self.mainf,width=1270,height=720,bg='lightgreen')
        self.left.pack(side=LEFT)

        #LABELS=======

        self.heading=Label(self.left,text="Section Details",font=('arial 25 bold'),fg='black',bg='lightgreen')
        self.heading.place(x=500,y=0)

        self.sectionname=Label(self.left,text="Section name",font=('arial 20 bold'),fg='black',bg='lightgreen')
        self.sectionname.place(x=450,y=50)

        self.day=Label(self.left,text="Day",font=('arial 18 bold'),fg='black',bg='lightgreen')
        self.day.place(x=0,y=140)
        
        self.slot1=Label(self.left,text="Slot1",font=('arial 18 bold'),fg='black',bg='lightgreen')
        self.slot1.place(x=0,y=180)

        self.slot2=Label(self.left,text="Slot2",font=('arial 18 bold'),fg='black',bg='lightgreen')
        self.slot2.place(x=0,y=220)

        self.slot3=Label(self.left,text="Slot3",font=('arial 18 bold'),fg='black',bg='lightgreen')
        self.slot3.place(x=0,y=260)

        self.slot4=Label(self.left,text="Slot4",font=('arial 18 bold'),fg='black',bg='lightgreen')
        self.slot4.place(x=0,y=300)

        self.slot5=Label(self.left,text="Slot5",font=('arial 18 bold'),fg='black',bg='lightgreen')
        self.slot5.place(x=0,y=340)

        self.slot6=Label(self.left,text="Slot6",font=('arial 18 bold'),fg='black',bg='lightgreen')
        self.slot6.place(x=0,y=380)

        self.subject1=Label(self.left,text="Subject 1",font=('arial 18 bold'),fg='black',bg='lightgreen')
        self.subject1.place(x=625,y=140)

        self.subject2=Label(self.left,text="Subject 2",font=('arial 18 bold'),fg='black',bg='lightgreen')
        self.subject2.place(x=625,y=180)

        self.subject3=Label(self.left,text="Subject 3",font=('arial 18 bold'),fg='black',bg='lightgreen')
        self.subject3.place(x=625,y=220)

        self.subject4=Label(self.left,text="Subject 4",font=('arial 18 bold'),fg='black',bg='lightgreen')
        self.subject4.place(x=625,y=260)

        #Entries=======================

        self.sname_ent=Entry(self.left,textvariable=self.sname_var,width=30)
        self.sname_ent.place(x=650,y=53)

        self.day_ent=Entry(self.left,textvariable=self.day_var,width=30)
        self.day_ent.place(x=250,y=143)
        
        self.slot1_ent=Entry(self.left,textvariable=self.slot1_var,width=30)
        self.slot1_ent.place(x=250,y=183)

        self.slot2_ent=Entry(self.left,textvariable=self.slot2_var,width=30)
        self.slot2_ent.place(x=250,y=223)

        self.slot3_ent=Entry(self.left,textvariable=self.slot3_var,width=30)
        self.slot3_ent.place(x=250,y=263)

        self.slot4_ent=Entry(self.left,textvariable=self.slot4_var,width=30)
        self.slot4_ent.place(x=250,y=303)
        
        self.slot5_ent=Entry(self.left,textvariable=self.slot5_var,width=30)
        self.slot5_ent.place(x=250,y=343)

        self.slot6_ent=Entry(self.left,textvariable=self.slot6_var,width=30)
        self.slot6_ent.place(x=250,y=383)

        self.subject1_ent=Entry(self.left,textvariable=self.subject1_var,width=30)
        self.subject1_ent.place(x=825,y=143)

        self.subject2_ent=Entry(self.left,textvariable=self.subject2_var,width=30)
        self.subject2_ent.place(x=825,y=183)

        self.subject3_ent=Entry(self.left,textvariable=self.subject3_var,width=30)
        self.subject3_ent.place(x=825,y=223)

        self.subject4_ent=Entry(self.left,textvariable=self.subject4_var,width=30)
        self.subject4_ent.place(x=825,y=263)

       #buttton===================

        self.adddetails=Button(self.left,text="Add Details",width=20,height=2,bg='steelblue',command=self.add_details)
        self.adddetails.place(x=620,y=350)
        
        self.clear=Button(self.left,text="clear",width=20,height=2,bg='steelblue',command=self.clear_db)
        self.clear.place(x=870,y=350)

        self.fback=Button(self.left,text="Go Back",width=8,height=1,bg='steelblue',command=self.back2_db)
        self.fback.place(x=10,y=10)
        c.execute("DELETE FROM sectiontime WHERE slot1='1'");
        c.execute("DELETE FROM sectiontime WHERE slot1='12345'");



        #Fuction to call=======================
    def add_details(self):
        self.val1=self.sname_ent.get()
        self.val2=self.day_ent.get()
        self.val3=self.slot1_ent.get()
        self.val4=self.slot2_ent.get()
        self.val5=self.slot3_ent.get()
        self.val6=self.slot4_ent.get()
        self.val7=self.slot5_ent.get()
        self.val8=self.slot6_ent.get()
        self.val9=self.subject1_ent.get()
        self.val10=self.subject2_ent.get()
        self.val11=self.subject3_ent.get()
        self.val12=self.subject4_ent.get()
        
        


  #=========testing===============
        if self.val1=="" or self.val2=="" or self.val3=="" or self.val4=="" or self.val5=="" or self.val6=="" or self.val7=="" or self.val8=="" or self.val9=="" or self.val10=="" or self.val11=="" or self.val12=="":
            tkinter.messagebox.showinfo("warning","Please fill up all boxes")


            #p=c.execute("SELECT subject1,subject2,subject3,subject4 FROM sectiontime INNER JOIN studentdetails on sectiontime.name = studentdetails.section");
          
            p=c.execute("SELECT slot1 FROM sectiontime INNER JOIN teachertime1 on sectiontime.name=teachertime1.section2")
            rows = p.fetchall()
            for row in rows:
                print(row)
            q=c.execute("SELECT uid from teachertime1")
            rows1=p.fetchone()
            #r=c.execute('SELECT  from managementlogin3 where name="%s' %(rows1))
            q=c.execute("SELECT teachertime1.subject1,teachertime1.subject2,teachertime1.subject3,teachertime1.subject4 FROM teachertime1 INNER JOIN sectiontime on teachertime1.uid=sectiontime.slot1")
            rows1=q.fetchall()
            for row1 in rows1:
                print(row1)
                                 
   
       
        else:
            #c.execute("create table sectiontime(name text,day text,slot1 text,slot2 text,slot3 text,slot4 text,slot5 text,slot6 text,subject1 text,subject2 text,subject3 text,subject4 text)")

            sql="INSERT INTO 'sectiontime' (name,day,slot1,slot2,slot3,slot4,slot5,slot6,subject1,subject2,subject3,subject4) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"
            c.execute(sql, (self.val1,self.val2,self.val3,self.val4,self.val5,self.val6,self.val7,self.val8,self.val9,self.val10,self.val11,self.val12))
            '''c.execute('select * from appointments1')
            
            for row in c.execute('select * from appointments1'):
                print(row)'''
            conn.commit()
            tkinter.messagebox.showinfo("Success"," Details of section " +str(self.val1) +" has been created ")

    def clear_db(self):
            self.sname_var.set("")
            self.day_var.set("")
            self.slot1_var.set("")
            self.slot2_var.set("")
            self.slot3_var.set("")
            self.slot4_var.set("")
            self.slot5_var.set("")
            self.slot6_var.set("")
            self.subject1_var.set("")
            self.subject2_var.set("")
            self.subject3_var.set("")
            self.subject4_var.set("")

            
            
            


    def manage_teachersf(self):
        
        self.manage.destroy()
        self.mteacher=Frame(self.mainf,width=1270,height=720,bg='red')
        self.mteacher.pack(side=LEFT)

        #LABELS=======

        self.heading=Label(self.mteacher,text="Faculty Details",font=('arial 25 bold'),fg='black',bg='red')
        self.heading.place(x=500,y=0)
        self.pdetails=Label(self.mteacher,text="Personal Details....",font=('arial 20 bold'),fg='black',bg='red')
        self.pdetails.place(x=0,y=70)
        self.fname=Label(self.mteacher,text="Name",font=('arial 20 bold'),fg='black',bg='red')
        self.fname.place(x=0,y=160)

        self.fuid=Label(self.mteacher,text="UID",font=('arial 18 bold'),fg='black',bg='red')
        self.fuid.place(x=0,y=200)
   
        self.fgender=Label(self.mteacher,text="Gender",font=('arial 18 bold'),fg='black',bg='red')
        self.fgender.place(x=0,y=240)
        
        self.fdob=Label(self.mteacher,text="Date of Birth",font=('arial 18 bold'),fg='black',bg='red')
        self.fdob.place(x=0,y=280)
        
        self.fsalary=Label(self.mteacher,text="Salary",font=('arial 18 bold'),fg='black',bg='red')
        self.fsalary.place(x=0,y=320)
        
        self.adetails=Label(self.mteacher,text="Subjects Details....",font=('arial 20 bold'),fg='black',bg='red')
        self.adetails.place(x=625,y=70)
        self.fsubject1=Label(self.mteacher,text="Subject 1",font=('arial 18 bold'),fg='black',bg='red')
        self.fsubject1.place(x=625,y=160)

        self.fsubject2=Label(self.mteacher,text="Subject 2",font=('arial 18 bold'),fg='black',bg='red')
        self.fsubject2.place(x=625,y=200)

        self.fsubject3=Label(self.mteacher,text="Subject 3",font=('arial 18 bold'),fg='black',bg='red')
        self.fsubject3.place(x=625,y=240)

        self.fsubject4=Label(self.mteacher,text="Subject 4",font=('arial 18 bold'),fg='black',bg='red')
        self.fsubject4.place(x=625,y=280)

        self.adetails=Label(self.mteacher,text="Section Details....",font=('arial 20 bold'),fg='black',bg='red')
        self.adetails.place(x=0,y=430)

        self.fsection1=Label(self.mteacher,text="Section 1",font=('arial 18 bold'),fg='black',bg='red')
        self.fsection1.place(x=0,y=500)

        self.fsection2=Label(self.mteacher,text="Section 2",font=('arial 18 bold'),fg='black',bg='red')
        self.fsection2.place(x=0,y=540)


        #Entries=======================

        self.fname_ent=Entry(self.mteacher,textvariable=self.fname_var,width=30)
        self.fname_ent.place(x=250,y=163)

        self.fuid_ent=Entry(self.mteacher,textvariable=self.fuid_var,width=30)
        self.fuid_ent.place(x=250,y=203)
        
        self.fgender_ent=Entry(self.mteacher,textvariable=self.fgender_var,width=30)
        self.fgender_ent.place(x=250,y=243)

        self.fdob_ent=Entry(self.mteacher,textvariable=self.fdob_var,width=30)
        self.fdob_ent.place(x=250,y=283)

        self.fsalary_ent=Entry(self.mteacher,textvariable=self.fsalary_var,width=30)
        self.fsalary_ent.place(x=250,y=323)

        self.fsubject1_ent=Entry(self.mteacher,textvariable=self.fsubject1_var,width=30)
        self.fsubject1_ent.place(x=825,y=163)
        
        self.fsubject2_ent=Entry(self.mteacher,textvariable=self.fsubject2_var,width=30)
        self.fsubject2_ent.place(x=825,y=203)

        self.fsubject3_ent=Entry(self.mteacher,textvariable=self.fsubject3_var,width=30)
        self.fsubject3_ent.place(x=825,y=243)

        self.fsubject4_ent=Entry(self.mteacher,textvariable=self.fsubject4_var,width=30)
        self.fsubject4_ent.place(x=825,y=283)

        self.fsection1_ent=Entry(self.mteacher,textvariable=self.fsection1_var,width=30)
        self.fsection1_ent.place(x=250,y=503)

        self.fsection2_ent=Entry(self.mteacher,textvariable=self.fsection2_var,width=30)
        self.fsection2_ent.place(x=250,y=543)

       #buttton===================

        self.adddetails=Button(self.mteacher,text="Add Details",width=20,height=2,bg='steelblue',command=self.fadd_details)
        self.adddetails.place(x=620,y=600)
        
        self.clear=Button(self.mteacher,text="clear",width=20,height=2,bg='steelblue',command=self.fclear_db)
        self.clear.place(x=870,y=600)

        self.fback=Button(self.mteacher,text="Go Back",width=8,height=1,bg='steelblue',command=self.back1_db)
        self.fback.place(x=10,y=10)



    def fadd_details(self):
        self.valu1=self.fname_ent.get()
        self.valu2=self.fuid_ent.get()
        self.valu3=self.fgender_ent.get()
        self.valu4=self.fdob_ent.get()
        self.valu5=self.fsalary_ent.get()
        self.valu6=self.fsubject1_ent.get()
        self.valu7=self.fsubject2_ent.get()
        self.valu8=self.fsubject3_ent.get()
        self.valu9=self.fsubject4_ent.get()
        self.valu10=self.fsection1_ent.get()
        self.valu11=self.fsection2_ent.get()    


  #=========testing===============
        if self.valu1=="" or self.valu2=="" or self.valu3=="" or self.valu4=="" or self.valu5=="" or self.valu6=="" or self.valu7=="" or self.valu8=="" or self.valu9=="" or self.valu10=="" or self.valu11=="":
            tkinter.messagebox.showinfo("warning","Please fill up all boxes")
            for row in c.execute('select * from teachertime1'):
                print(row)  

        else:
            #c.execute("create table teachertime1(name text,uid text,gender text,dob text,salary text,subject1 text,subject2 text,subject3 text,subject4 text,section1 text,section2 text,password text default '12345678',leave text default 'present')")

            sql="INSERT INTO 'teachertime1' (name,uid,gender,dob,salary,subject1,subject2,subject3,subject4,section1,section2) VALUES(?,?,?,?,?,?,?,?,?,?,?)"
            c.execute(sql, (self.valu1,self.valu2,self.valu3,self.valu4,self.valu5,self.valu6,self.valu7,self.valu8,self.valu9,self.valu10,self.valu11))
            conn.commit()
            tkinter.messagebox.showinfo("Success"," Details of faculty " +str(self.valu1) +" has been created.\n UID : "+str(self.valu2) +"\n Password : 12345678")

    def fclear_db(self):
            self.fsubject1_var.set("")
            self.fsubject2_var.set("")
            self.fsubject3_var.set("")
            self.fsubject4_var.set("")
            self.fname_var.set("")
            self.fuid_var.set("")
            self.fgender_var.set("")
            self.fdob_var.set("")
            self.fsalary_var.set("")
            self.fsection1_var.set("")
            self.fsection2_var.set("")


    def back1_db(self):
        self.mteacher.destroy()
        self.managers_entry()

    def back4_db(self):
        self.mstudents.destroy()
        self.managers_entry()


    def back2_db(self):
        self.left.destroy()
        self.managers_entry()


    def back3_db(self):
        self.manage.destroy()
        
        
        self.front=Frame(self.mainf,width=1270,height=720,bg='yellow')
        self.front.pack(side=LEFT)

        self.managestudent=Button(self.front,text="Students",width=20,height=2,bg='steelblue',command=self.student_login)
        self.managestudent.place(x=100,y=350)
        self.manager=Button(self.front,text="Managers",width=20,height=2,bg='steelblue',command=self.managers_entry)
        self.manager.place(x=500,y=350)
        self.manageteacher=Button(self.front,text="Teachers",width=20,height=2,bg='steelblue')
        self.manageteacher.place(x=900,y=350)
        
        
        
    def manage_students(self):
        
        self.manage.destroy()
        self.mstudents=Frame(self.mainf,width=1270,height=720,bg='crimson')
        self.mstudents.pack(side=LEFT)

        #LABELS=======

        self.heading=Label(self.mstudents,text="Student Details",font=('arial 25 bold'),fg='black',bg='crimson')
        self.heading.place(x=500,y=0)
        
        self.pedetails=Label(self.mstudents,text="Personal Details....",font=('arial 20 bold'),fg='black',bg='crimson')
        self.pedetails.place(x=0,y=70)
        
        self.stname=Label(self.mstudents,text="Name",font=('arial 20 bold'),fg='black',bg='crimson')
        self.stname.place(x=0,y=160)

        self.stuid=Label(self.mstudents,text="Registration ID",font=('arial 18 bold'),fg='black',bg='crimson')
        self.stuid.place(x=0,y=200)
   
        self.stgender=Label(self.mstudents,text="Gender",font=('arial 18 bold'),fg='black',bg='crimson')
        self.stgender.place(x=0,y=240)
        
        self.stsection=Label(self.mstudents,text="Section",font=('arial 18 bold'),fg='black',bg='crimson')
        self.stsection.place(x=0,y=280)
       #Entries=======
        self.stname_ent=Entry(self.mstudents,textvariable=self.stname_var,width=30)
        self.stname_ent.place(x=250,y=163)

        self.stuid_ent=Entry(self.mstudents,textvariable=self.stuid_var,width=30)
        self.stuid_ent.place(x=250,y=203)
        
        self.stgender_ent=Entry(self.mstudents,textvariable=self.stgender_var,width=30)
        self.stgender_ent.place(x=250,y=243)

        self.stsection_ent=Entry(self.mstudents,textvariable=self.stsection_var,width=30)
        self.stsection_ent.place(x=250,y=283)

        #buttons=======
        self.stadddetails=Button(self.mstudents,text="Add Details",width=20,height=2,bg='steelblue',command=self.stadd_details)
        self.stadddetails.place(x=20,y=330)
        
        self.stclear=Button(self.mstudents,text="clear",width=20,height=2,bg='steelblue',command=self.stclear_db)
        self.stclear.place(x=280,y=330)

        self.stback=Button(self.mstudents,text="Go Back",width=8,height=1,bg='steelblue',command=self.back4_db)
        self.stback.place(x=10,y=10)

    def stadd_details(self):
        self.value1=self.stname_ent.get()
        self.value2=self.stuid_ent.get()
        self.value3=self.stgender_ent.get()
        self.value4=self.stsection_ent.get()
    

  #=========testing===============
        if self.value1=="" or self.value2=="" or self.value3=="" or self.value4=="":
            tkinter.messagebox.showinfo("warning","Please fill up all boxes")
            for row in c.execute('select * from studentdetails'):
                print(row)   

        else:
            #c.execute("create table studentdetails(name text,uid text,gender text,section text,password text default '12345678')")

            sql="INSERT INTO 'studentdetails' (name,uid,gender,section) VALUES(?,?,?,?)"
            c.execute(sql, (self.value1,self.value2,self.value3,self.value4))
            conn.commit()
            tkinter.messagebox.showinfo("Success"," Details of student " +str(self.value1) +" has been created.\n Registration ID : "+str(self.value2) +"\n Password : 12345678")


    def stclear_db(self):
            self.stname_var.set("")
            self.stuid_var.set("")
            self.stgender_var.set("")
            self.stsection_var.set("")

    def student_login(self):
        self.front.destroy()
        
        self.studente=Frame(self.mainf,width=1270,height=720,bg='crimson')
        self.studente.pack(side=LEFT)
        self.studentlogi=Frame(self.studente,width=450,height=260,bg='black')
        self.studentlogi.place(x=410,y=200)
        self.heading1=Label(self.studentlogi,text="Student Login ",font=('arial 22 bold'),fg='white',bg='black')
        self.heading1.place(x=140,y=10)
        
        self.stnamem=Label(self.studentlogi,text="User Name",font=('arial 18 bold'),fg='white',bg='black')
        self.stnamem.place(x=0,y=80)
        
        self.stpassword=Label(self.studentlogi,text="Password",font=('arial 18 bold'),fg='white',bg='black')
        self.stpassword.place(x=0,y=140)

        self.stnamem_ent=Entry(self.studentlogi,textvariable=self.stnamem_var,width=30)
        self.stnamem_ent.place(x=200,y=84)
        

        self.stpassword_ent=Entry(self.studentlogi,textvariable=self.stpassword_var,width=30)
        self.stpassword_ent.place(x=200,y=144)

        self.stlogin=Button(self.studentlogi,text="Login",width=20,height=2,bg='steelblue',command=self.student_entry)
        self.stlogin.place(x=150,y=200)
        c.execute("DELETE FROM sectiontime WHERE slot1='1'");
        #c.execute("DELETE FROM sectiontime WHERE slot1='12345'");
        
    def student_entry(self):
        self.input1=self.stnamem_ent.get()
        self.input2=self.stpassword_ent.get()
 
        
        
        #SQL==================
        if self.input1=="" or self.input2=="":
            tkinter.messagebox.showinfo("warning","Please fill up all box")
        elif len(self.input1)<8:
            tkinter.messagebox.showinfo("warning","Username should be of at least 8 characters.")
        elif len(self.input2)<8:
            tkinter.messagebox.showinfo("warning","Password should be of at least 8 characters.")
           
        else:
            
            c.execute('SELECT * from studentdetails where uid="%s"' %(self.input1))
            
            if c.fetchone() is  not None :

                c.execute('SELECT * from studentdetails where password="%s"' %(self.input2))
                if c.fetchone() is  not None :
                    tkinter.messagebox.showinfo("success","Login Successfully.")
                    self.studente.destroy()
                    self.studente1=Frame(self.mainf,width=800,height=720,bg='blue')
                    self.studente1.place(x=0,y=0)
                    self.studente2=Frame(self.mainf,width=800,height=720,bg='black')
                    self.studente2.place(x=800,y=0)
                    
                    self.logs1=Label(self.studente2,text="Message",font=('arial 20 bold'), fg='white',bg='black')
                    self.logs1.place(x=10,y=10)
               
                    self.box1=Text(self.studente2,width=55,height=40)
                    self.box1.place(x=20,y=60)
                    
                                        
                    q=c.execute('SELECT section from studentdetails where uid="%s"' %(self.input1))
                    q1=q.fetchone()
                    w=c.execute('SELECT subject1,subject2,subject3,subject4 from sectiontime where name="%s"' %(q1))
                    w1=c.fetchone()
                    y=c.execute('SELECT slot1 from sectiontime where name="%s"' %(q1))
                    y1=c.fetchone()
                    sr=c.execute('SELECT subject1,subject2,subject3,subject4 from teachertime1 where uid="%s"' %(y1))
                    sr1=c.fetchone()
                    print(w1)
                    print(sr1)
                    #self.student_entry1()
                    st1=c.execute('SELECT * from studentdetails where uid="%s"' %(self.input1))
                    st2=st1.fetchone()
                    l=[]
                    l=st2
                    if "break" in y1:
                        self.sslot1=Label(self.studente1,text="9am-10am",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sslot1.place(x=10,y=370)
                        self.sslot11=Label(self.studente1,text="break",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sslot11.place(x=230,y=370)

                        
                    elif sr1 is not None:
                        for a in w1:
                            for b in sr1:
                                if a==b:
                                    print("slot1 is :",a)
                                    self.sslot1=Label(self.studente1,text="9am-10am",font=('arial 16 bold'),fg='white',bg='blue')
                                    self.sslot1.place(x=10,y=370)
                                    self.sslot11=Label(self.studente1,text=a,font=('arial 16 bold'),fg='white',bg='blue')
                                    self.sslot11.place(x=230,y=370)

                    y2=c.execute('SELECT slot5 from sectiontime where name="%s"' %(q1))
                    y3=c.fetchone()
                    
                    sr2=c.execute('SELECT subject1,subject2,subject3,subject4 from teachertime1 where uid="%s"' %(y3))
                    sr3=c.fetchone()
                    print(y3)
                    print("break" in y3)
                    if "break" in y3:
                        self.sslot5=Label(self.studente1,text="1pm-2pm",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sslot5.place(x=400,y=420)
                        self.sslot51=Label(self.studente1,text="break",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sslot51.place(x=620,y=420)
                    elif sr3 is not None:
                        for a in w1:
                            for b in sr3:
                                if a==b:
                                    print("slot5 is :",a)
                                    self.sslot5=Label(self.studente1,text="1pm-2pm",font=('arial 16 bold'),fg='white',bg='blue')
                                    self.sslot5.place(x=400,y=420)
                                    self.sslot51=Label(self.studente1,text=a,font=('arial 16 bold'),fg='white',bg='blue')
                                    self.sslot51.place(x=620,y=420)

                    y4=c.execute('SELECT slot2 from sectiontime where name="%s"' %(q1))
                    y5=c.fetchone()
                    
                    sr4=c.execute('SELECT subject1,subject2,subject3,subject4 from teachertime1 where uid="%s"' %(y5))
                    sr5=c.fetchone()
                    if "break" in y5:
                        self.sslot2=Label(self.studente1,text="10am-11am",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sslot2.place(x=10,y=420)
                        self.sslot21=Label(self.studente1,text="break",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sslot21.place(x=230,y=420)

                    elif sr5 is not None:
                        for a in w1:
                            for b in sr5:
                                if a==b:
                                    print("slot2 is :",a)
                                    self.sslot2=Label(self.studente1,text="10am-11am",font=('arial 16 bold'),fg='white',bg='blue')
                                    self.sslot2.place(x=10,y=420)
                                    self.sslot21=Label(self.studente1,text=a,font=('arial 16 bold'),fg='white',bg='blue')
                                    self.sslot21.place(x=230,y=420)

                    y6=c.execute('SELECT slot3 from sectiontime where name="%s"' %(q1))
                    y7=c.fetchone()
                    
                    sr6=c.execute('SELECT subject1,subject2,subject3,subject4 from teachertime1 where uid="%s"' %(y7))
                    sr7=c.fetchone()
                    if "break" in y7:
                        self.sslot3=Label(self.studente1,text="11am-12pm",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sslot3.place(x=10,y=470)
                        self.sslot31=Label(self.studente1,text="break",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sslot31.place(x=230,y=470)
                                    
                    if sr7 is not None:
                        for a in w1:
                            for b in sr7:
                                if a==b:
                                    print("slot3 is :",a)
                                    self.sslot3=Label(self.studente1,text="11am-12pm",font=('arial 16 bold'),fg='white',bg='blue')
                                    self.sslot3.place(x=10,y=470)
                                    self.sslot31=Label(self.studente1,text=a,font=('arial 16 bold'),fg='white',bg='blue')
                                    self.sslot31.place(x=230,y=470)
                                    
                    y8=c.execute('SELECT slot4 from sectiontime where name="%s"' %(q1))
                    y9=c.fetchone()
                    
                    sr8=c.execute('SELECT subject1,subject2,subject3,subject4 from teachertime1 where uid="%s"' %(y9))
                    sr9=c.fetchone()
                    if "break" in y9:
                        self.sslot4=Label(self.studente1,text="12pm-1pm",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sslot4.place(x=400,y=370)
                        self.sslot41=Label(self.studente1,text="break",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sslot41.place(x=620,y=370)
                        
                    if sr9 is not None:
                        for a in w1:
                            for b in sr9:
                                if a==b:
                                    print("slot4 is :",a)
                                    self.sslot4=Label(self.studente1,text="12pm-1pm",font=('arial 16 bold'),fg='white',bg='blue')
                                    self.sslot4.place(x=400,y=370)
                                    self.sslot41=Label(self.studente1,text=a,font=('arial 16 bold'),fg='white',bg='blue')
                                    self.sslot41.place(x=620,y=370)

                    y10=c.execute('SELECT slot6 from sectiontime where name="%s"' %(q1))
                    y11=c.fetchone()
                    print(y11)
                    sr10=c.execute('SELECT subject1,subject2,subject3,subject4 from teachertime1 where uid="%s"' %(y11))
                    sr11=c.fetchone()
                    
                    if "break" in y11:
                        self.sslot6=Label(self.studente1,text="2pm-3pm",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sslot6.place(x=400,y=470)
                        self.sslot61=Label(self.studente1,text="break",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sslot61.place(x=620,y=470)
                    
                    elif sr11 is not None:
                        for a in w1:
                            for b in sr11:
                                if a==b:
                                    print("slot6 is :",a)
                                    self.sslot5=Label(self.studente1,text="2pm-3pm",font=('arial 16 bold'),fg='white',bg='blue')
                                    self.sslot5.place(x=400,y=470)
                                    self.sslot51=Label(self.studente1,text=a,font=('arial 16 bold'),fg='white',bg='blue')
                                    self.sslot51.place(x=620,y=470)
                    else:
                        pass
                                    
                        


                    #print(type(l))
                    self.ssheading1=Label(self.studente1,text="Time Table....",font=('arial 20 bold'),fg='white',bg='blue')
                    self.ssheading1.place(x=250,y=300)
                    self.ssheading=Label(self.studente1,text="Student Details....",font=('arial 20 bold'),fg='white',bg='blue')
                    self.ssheading.place(x=250,y=10)
                    self.ssname=Label(self.studente1,text="Student Name",font=('arial 16 bold'),fg='white',bg='blue')
                    self.ssname.place(x=10,y=80)
                    self.ssname1=Label(self.studente1,text=l[0],font=('arial 16 bold'),fg='white',bg='blue')
                    self.ssname1.place(x=230,y=80)
                    self.ssuid=Label(self.studente1,text="Registration ID",font=('arial 16 bold'),fg='white',bg='blue')
                    self.ssuid.place(x=10,y=130)
                    self.ssuid1=Label(self.studente1,text=l[1],font=('arial 16 bold'),fg='white',bg='blue')
                    self.ssuid1.place(x=230,y=130)
                    self.ssgender=Label(self.studente1,text="Gender",font=('arial 16 bold'),fg='white',bg='blue')
                    self.ssgender.place(x=10,y=180)
                    self.ssgender1=Label(self.studente1,text=l[2],font=('arial 16 bold'),fg='white',bg='blue')
                    self.ssgender1.place(x=230,y=180)
                    self.sssection=Label(self.studente1,text="Section",font=('arial 16 bold'),fg='white',bg='blue')
                    self.sssection.place(x=10,y=230)
                    self.sssection1=Label(self.studente1,text=l[3],font=('arial 16 bold'),fg='white',bg='blue')
                    self.sssection1.place(x=230,y=230)
                    
                    if sr1 is not None and w1[0] in sr1:
                        self.sssubject1=Label(self.studente1,text="Subject1",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject1.place(x=400,y=80)
                        self.sssubject11=Label(self.studente1,text=w1[0],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject11.place(x=620,y=80)
                        self.sssubject12=Label(self.studente1,text="id : "+y1[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject12.place(x=720,y=80)
                        
                    elif sr3 is not None and w1[0] in sr3:
                        self.sssubject1=Label(self.studente1,text="Subject1",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject1.place(x=400,y=80)
                        self.sssubject11=Label(self.studente1,text=w1[0],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject11.place(x=620,y=80)
                        self.sssubject12=Label(self.studente1,text="id : "+y3[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject12.place(x=720,y=80)

                    elif sr5 is not None and w1[0] in sr5:
                        self.sssubject1=Label(self.studente1,text="Subject1",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject1.place(x=400,y=80)
                        self.sssubject11=Label(self.studente1,text=w1[0],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject11.place(x=620,y=80)
                        self.sssubject12=Label(self.studente1,text="id : "+y5[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject12.place(x=720,y=80)
                    elif sr7 is not None and w1[0] in sr7:
                        self.sssubject1=Label(self.studente1,text="Subject1",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject1.place(x=400,y=80)
                        self.sssubject11=Label(self.studente1,text=w1[0],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject11.place(x=620,y=80)
                        self.sssubject12=Label(self.studente1,text="id : "+y7[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject12.place(x=720,y=80)
                    elif sr9 is not None and w1[0] in sr9:
                        self.sssubject1=Label(self.studente1,text="Subject1",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject1.place(x=400,y=80)
                        self.sssubject11=Label(self.studente1,text=w1[0],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject11.place(x=620,y=80)
                        self.sssubject12=Label(self.studente1,text="id : "+y9[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject12.place(x=720,y=80)
                    elif sr11 is not None and w1[0] in sr11:
                        self.sssubject1=Label(self.studente1,text="Subject1",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject1.place(x=400,y=80)
                        self.sssubject11=Label(self.studente1,text=w1[0],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject11.place(x=620,y=80)
                        self.sssubject12=Label(self.studente1,text="id : "+y11[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject12.place(x=720,y=80)

                        
                        

                    if sr1 is not None and w1[1] in sr1:
                        
                        self.sssubject2=Label(self.studente1,text="Subject2",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject2.place(x=400,y=130)
                        self.sssubject21=Label(self.studente1,text=w1[1],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject21.place(x=620,y=130)
                        self.sssubject22=Label(self.studente1,text="id : "+y1[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject22.place(x=720,y=130)
                    elif sr3 is not None and w1[1] in sr3:
                        
                        self.sssubject2=Label(self.studente1,text="Subject2",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject2.place(x=400,y=130)
                        self.sssubject21=Label(self.studente1,text=w1[1],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject21.place(x=620,y=130)
                        self.sssubject22=Label(self.studente1,text="id : "+y3[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject22.place(x=720,y=130)
                    elif sr5 is not None and w1[1] in sr5:
                        
                        self.sssubject2=Label(self.studente1,text="Subject2",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject2.place(x=400,y=130)
                        self.sssubject21=Label(self.studente1,text=w1[1],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject21.place(x=620,y=130)
                        self.sssubject22=Label(self.studente1,text="id : "+y5[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject22.place(x=720,y=130)
                    elif sr7 is not None and w1[1] in sr7:
                        
                        self.sssubject2=Label(self.studente1,text="Subject2",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject2.place(x=400,y=130)
                        self.sssubject21=Label(self.studente1,text=w1[1],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject21.place(x=620,y=130)
                        self.sssubject22=Label(self.studente1,text="id : "+y7[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject22.place(x=720,y=130)
                    elif sr9 is not None and w1[1] in sr9:
                        
                        self.sssubject2=Label(self.studente1,text="Subject2",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject2.place(x=400,y=130)
                        self.sssubject21=Label(self.studente1,text=w1[1],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject21.place(x=620,y=130)
                        self.sssubject22=Label(self.studente1,text="id : "+y9[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject22.place(x=720,y=130)
                    elif sr11 is not None and w1[1] in sr11:
                        
                        self.sssubject2=Label(self.studente1,text="Subject2",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject2.place(x=400,y=130)
                        self.sssubject21=Label(self.studente1,text=w1[1],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject21.place(x=620,y=130)
                        self.sssubject22=Label(self.studente1,text="id : "+y11[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject22.place(x=720,y=130)
                    if sr1 is not None and w1[2] in sr1:               
                    
                        self.sssubject3=Label(self.studente1,text="Subject3",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject3.place(x=400,y=180)
                        self.sssubject31=Label(self.studente1,text=w1[2],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject31.place(x=620,y=180)
                        self.sssubject32=Label(self.studente1,text="id : "+y1[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject32.place(x=720,y=180)
                    elif sr3 is not None and w1[2] in sr3:               
                    
                        self.sssubject3=Label(self.studente1,text="Subject3",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject3.place(x=400,y=180)
                        self.sssubject31=Label(self.studente1,text=w1[2],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject31.place(x=620,y=180)
                        self.sssubject32=Label(self.studente1,text="id : "+y3[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject32.place(x=720,y=180)
                    elif sr5 is not None and w1[2] in sr5:               
                    
                        self.sssubject3=Label(self.studente1,text="Subject3",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject3.place(x=400,y=180)
                        self.sssubject31=Label(self.studente1,text=w1[2],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject31.place(x=620,y=180)
                        self.sssubject32=Label(self.studente1,text="id : "+y5[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject32.place(x=720,y=180)
                    elif sr7 is not None and w1[2] in sr7:               
                    
                        self.sssubject3=Label(self.studente1,text="Subject3",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject3.place(x=400,y=180)
                        self.sssubject31=Label(self.studente1,text=w1[2],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject31.place(x=620,y=180)
                        self.sssubject32=Label(self.studente1,text="id : "+y7[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject32.place(x=720,y=180)
                    elif sr9 is not None and w1[2] in sr9:               
                    
                        self.sssubject3=Label(self.studente1,text="Subject3",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject3.place(x=400,y=180)
                        self.sssubject31=Label(self.studente1,text=w1[2],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject31.place(x=620,y=180)
                        self.sssubject32=Label(self.studente1,text="id : "+y9[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject32.place(x=720,y=180)
                    elif sr11 is not None and w1[2] in sr11:               
                    
                        self.sssubject3=Label(self.studente1,text="Subject3",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject3.place(x=400,y=180)
                        self.sssubject31=Label(self.studente1,text=w1[2],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject31.place(x=620,y=180)
                        self.sssubject32=Label(self.studente1,text="id : "+y11[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject32.place(x=720,y=180)
                           
                    if sr1 is not None and w1[3] in sr1:        
                        self.sssubject4=Label(self.studente1,text="Subject4",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject4.place(x=400,y=230)
                        self.sssubject41=Label(self.studente1,text=w1[3],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject41.place(x=620,y=230)
                        self.sssubject41=Label(self.studente1,text="id : "+y1[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject41.place(x=720,y=230)
                    if sr3 is not None and w1[3] in sr3:        
                        self.sssubject4=Label(self.studente1,text="Subject4",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject4.place(x=400,y=230)
                        self.sssubject41=Label(self.studente1,text=w1[3],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject41.place(x=620,y=230)
                        self.sssubject41=Label(self.studente1,text="id : "+y3[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject41.place(x=720,y=230)
                    if sr5 is not None and w1[3] in sr5:        
                        self.sssubject4=Label(self.studente1,text="Subject4",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject4.place(x=400,y=230)
                        self.sssubject41=Label(self.studente1,text=w1[3],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject41.place(x=620,y=230)
                        self.sssubject41=Label(self.studente1,text="id : "+y5[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject41.place(x=720,y=230)
                    if sr7 is not None and w1[3] in sr7:        
                        self.sssubject4=Label(self.studente1,text="Subject4",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject4.place(x=400,y=230)
                        self.sssubject41=Label(self.studente1,text=w1[3],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject41.place(x=620,y=230)
                        self.sssubject41=Label(self.studente1,text="id : "+y7[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject41.place(x=720,y=230)
                    if sr9 is not None and w1[3] in sr9:        
                        self.sssubject4=Label(self.studente1,text="Subject4",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject4.place(x=400,y=230)
                        self.sssubject41=Label(self.studente1,text=w1[3],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject41.place(x=620,y=230)
                        self.sssubject41=Label(self.studente1,text="id : "+y9[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject41.place(x=720,y=230)
                    if sr11 is not None and w1[3] in sr11:        
                        self.sssubject4=Label(self.studente1,text="Subject4",font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject4.place(x=400,y=230)
                        self.sssubject41=Label(self.studente1,text=w1[3],font=('arial 16 bold'),fg='white',bg='blue')
                        self.sssubject41.place(x=620,y=230)
                        self.sssubject41=Label(self.studente1,text="id : "+y11[0],font=('arial 13 bold'),fg='white',bg='blue')
                        self.sssubject41.place(x=720,y=230)
                        


                    
                    
                    
                else:
                    tkinter.messagebox.showinfo("warning","Invalid Password.")
            
            else:
                tkinter.messagebox.showinfo("warning","User does not exist.")
            
    def student_entry1(self):
        pass


        


root=Tk()
b=Application(root)


root.geometry("1270x720+0+0")


root.resizable(False,False)

root.mainloop()
