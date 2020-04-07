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

        
        










        
        self.left=Frame(master,width=1250,height=720,bg='lightgreen')
        self.left.pack(side=LEFT)


        #LABELS=======

        self.heading=Label(self.left,text="Section Details",font=('arial 30 bold'),fg='black',bg='lightgreen')
        self.heading.place(x=0,y=0)

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
        else:
            #c.execute("create table appointments1(id integer primary key autoincrement,name text,age integer,gender text,location text,scheduled_time text,phone integer)")

            sql="INSERT INTO 'sectiontime' (name,day,slot1,slot2,slot3,slot4,slot5,slot6,subject1,subject2,subject3,subject4) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"
            c.execute(sql, (self.val1,self.val2,self.val3,self.val4,self.val5,self.val6,self.val7,self.val8,self.val9,self.val10,self.val11,self.val12))
            '''c.execute('select * from appointments1')
            
            for row in c.execute('select * from appointments1'):
                print(row)'''
            conn.commit()
            tkinter.messagebox.showinfo("Success"," Details of section " +str(self.val1) +" has been created ")


           # self.box.insert(END,'\nAppintment fixed for ' + str(self.val1) + ' at ' + str(self.val5) )


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
            
            







root=Tk()
b=Application(root)


root.geometry("1200x720+0+0")


root.resizable(False,False)

root.mainloop()
