# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 17:04:47 2019

@author: User
"""

#%%
import mysql.connector as msc
import tkinter as tk
from tkinter import *
import webbrowser


a=msc.connect(host='localhost',user='root',password='1234',database='')
a.autocommit
b=a.cursor(buffered=True)
b.execute('create database if not exists project;')
b.execute('use project;')
b.execute('''create table if not exists Uni
          (AccessCode varchar(20) primary key,
          Universities  varchar(100)  not null,
          Ranks int)''')
b.execute('''create table if not exists yourlist
          (name varchar(30),
          University varchar(50),
          course  varchar(20)  not null,
          effective_fees int)''')
a.commit()

def samplespace():
    b.execute('''insert into uni
              values('SBPN001','Symbiosis Pune',60),
              ('JJSA123','JJ School of Art',12),
              ('ITB007','IIT Bombay',1),
              ('IMI014','IIM Indore',5),
              ('IMA015','IIM Ahmedabad',4)''')
    a.commit()
    
l=[]
b.execute('select * from uni')
for i in b:
    l.append(i)
    
if len(l)==0:
    samplespace()
    b.execute('select * from uni')
    for i in b:
        l.append(i)
else:
    b.execute('select * from uni')
    for i in b:
        l.append(i)
        
for i in l:
    s='''create table if not exists `%s`
        (Courses varchar(20) not null,
        Criteria_percentage int(5),
        Fees int not null,
        MinScholarship int(5),
        MaxScholarship int(5),
        AcceptanceRate decimal(5,2));'''
    x=s.replace('%s',i[1])
    b.execute(x)
    a.commit()
    
b.execute("select * from `symbiosis pune`")
l2=[]
for i in b:
    l2.append(i)
if len(l2)==0:
    b.execute('''insert into `Symbiosis Pune`
              values('LLB',87,400000,10,60,23),
              ('BBA',80,350000,15,45,50),
              ('BA',84,375000,10,30,45)''')
    a.commit() 
    
b.execute("select * from `JJ School of Art`")
l2=[]
for i in b:
    l2.append(i)
if len(l2)==0:
     b.execute('''insert into `JJ School of Art`
              values('Architecture',90,500000,20,60,40),
              ('BBA',80,400000,10,40,60),
              ('BA',85,350000,20,30,50)''')
     a.commit()
    
b.execute("select * from `IIT Bombay`")
l2=[]
for i in b:
    l2.append(i)
if len(l2)==0:
     b.execute('''insert into `IIT Bombay`
                  values('Btech',95,400000,50,100,5),
                  ('B.eng CS',96,380000,30,70,3),
                  ('Majors Math',90,300000,25,50,15)''')
     a.commit()

b.execute("select * from `IIM Indore`")
l2=[]
for i in b:
    l2.append(i)
if len(l2)==0:
     b.execute('''insert into `IIM Indore`
                  values('MBA',85,500000,10,60,20),
                  ('PGP',80,350000,15,40,30),
                  ('FPM',84,300000,12,38,25)''')
     a.commit()

b.execute("select * from `IIM Ahmedabad`")
l2=[]
for i in b:
    l2.append(i)
if len(l2)==0:
    b.execute('''insert into `IIM Ahmedabad`
                  values('MBA',95,400000,10,100,10),
                  ('PGP',90,300000,15,50,15),
                  ('FPM',93,300000,10,60,25)''')
    a.commit()

#GUI                                      
    
def about(): 
    helpmaster=tk.Tk(className='about')
    helpmaster.geometry("1500x1500")
    s='''Terms and Conditions 
    Introduction
    These Standard Terms and Conditions written on this webpage shall manage your use of our software, accessible right here.
    
    These Terms will be applied fully and affect to your use of this software. 
    By using this software, you agreed to accept all terms and conditions written in here. 
    You must not use this software if you disagree with any of these software Standard Terms and Conditions.
    
    Restrictions
    You are specifically restricted from all of the following:
    
    publishing any software material in any other media;
    selling, sublicensing and/or otherwise commercializing any software material;
    publicly performing and/or showing any software material;
    using this software in any way that is or may be damaging to this software;
    using this software in any way that impacts user access to this software;
    using this software contrary to applicable laws and regulations, or in any way may cause harm to the software, or to any person or business entity;
    engaging in any data mining, data harvesting, data extracting or any other similar activity in relation to this software;
    using this software to engage in any advertising or marketing.
    Certain areas of this software are restricted from being access by you and KAK may further restrict access by you to any areas of this software, at any time, in absolute discretion.
    Any user ID and password you may have for this software are confidential and you must maintain confidentiality as well.
    
    No warranties
    This software is provided "as is", with all faults, and KAK express no representations or warranties, of any kind related to this software or the materials contained on this software.
    Also, nothing contained on this software shall be interpreted as advising you.
    
    Limitation of liability
    In no event shall KAK, nor any of its officers, directors and employees, shall be held liable for anything arising out of or in any way connected with your use of this software whether such liability is under contract.
    KAK, including its officers, directors and employees shall not be held liable for any indirect, consequential or special liability arising out of or in any way related to your use of this software.
    
    Severability
    If any provision of these Terms is found to be invalid under any applicable law, such provisions shall be deleted without affecting the remaining provisions herein.
    
    Variation of Terms
    KAK is permitted to revise these Terms at any time as it sees fit, and by using this software you are expected to review these Terms on a regular basis.
    
    Assignment
    The KAK is allowed to assign, transfer, and subcontract its rights and/or obligations under these Terms without any notification.
    However, you are not allowed to assign, transfer, or subcontract any of your rights and/or obligations under these Terms.
    
    Entire Agreement
    These Terms constitute the entire agreement between KAK and you in relation to your use of this software, and supersede all prior agreements and understandings.'''
    
    tk.Label(helpmaster,text=s).pack()

    
def tnew():        
    def chk():
        def tadd():
            def addflds():
                varr1=en1.get()
                varr2=en2.get()
                varr3=en3.get()
                varr4=en4.get()
                varr5=en5.get()
                varr6=en6.get()
                en1.delete(0,END)
                en2.set(0)
                en3.delete(0,END)
                en4.set(0)
                en5.set(0)
                en6.set(0)
                if varr1=='' or varr2==0 or varr3=='' or varr4==0 or varr5==0 or varr6==0:
                    tk.Label(master2,text="please fill all fields correctly").grid(row=10)
                else:
                    s='''create table if not exists `%s`
                        (Courses varchar(20) not null,
                        Criteria_percentage int(5),
                        Fees int not null,
                        MinScholarship int(5),
                        MaxScholarship int(5),
                        AcceptanceRate decimal(5,2));'''
                    x=s.replace('%s',var1)
                    b.execute(x)
                    a.commit()
                    s2='''insert into `%s2`
                    values(%s,%s,%s,%s,%s,%s)'''
                    x2=s2.replace('%s2',var1)
                    data=(varr1,varr2,varr3,varr4,varr5,varr6)
                    b.execute(x2,data)
                    a.commit()
                    tk.Label(master2,text="Course details uploaded sucessfully. Add another?").grid(row=10)
                
                
            var1=e1.get()
            var2=e2.get()
            var3=e3.get()
            s="insert into uni values(%s,%s,%s)"
            data=(var2,var1,var3)
            b.execute(s,data)
            a.commit()            
            master.destroy()
            master2=tk.Tk()
            master2.title(var1 + " further details")
            master2.geometry("500x500") 
            tk.Label(master2, 
                     text="NOTE: fields are case sensitive").grid(row=0)
            tk.Label(master2, 
                     text="Course").grid(row=1)
            tk.Label(master2, 
                     text="Criteria(%)").grid(row=2)
            tk.Label(master2, 
                     text="Fees").grid(row=3)
            tk.Label(master2, 
                     text="Minimum Scholarship").grid(row=4)
            tk.Label(master2, 
                     text="Maximum Scholarship").grid(row=5)
            tk.Label(master2, 
                     text="Acceptance rate").grid(row=6)
            tk.Button(master2, 
                      text='Quit', 
                      command=master2.destroy).grid(row=9, 
                                                column=2, 
                                                sticky=tk.W, 
                                                pady=4)
            tk.Button(master2, 
                      text='Add Fields',
                      command=addflds).grid(row=8, 
                                                column=1, 
                                                sticky=tk.W, 
                                                pady=4)
            
            en1 = tk.Entry(master2)
            en1.grid(row=1, column=1)
            en2 = tk.Scale(master2, from_=0, to=100, orient=HORIZONTAL)
            en2.grid(row=2, column=1)
            en3 = tk.Entry(master2)
            en3.grid(row=3, column=1)
            en4 = tk.Scale(master2, from_=0, to=100, orient=HORIZONTAL)
            en4.grid(row=4, column=1)
            v=en4.get()
            en5 = tk.Scale(master2, from_=v, to=100, orient=HORIZONTAL)
            en5.grid(row=5, column=1)
            en6 = tk.Scale(master2, from_=0, to=100, orient=HORIZONTAL)
            en6.grid(row=6, column=1)
            
        var=e1.get()
        varr=e2.get()
        try:
            varrr=int(e3.get())
        except:
            e3.delete(0,END)
            tk.Label(master, 
             text="Rank should be an integer").grid(row=4,column=1)
        if var !='' and varr !='' and varrr !='' and type(varrr)==int:
            tk.Button(master, 
                  text='Continue',
                  command=tadd).grid(row=5,column=1,sticky=tk.W,pady=4)
        else:
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            tk.Label(master, 
             text="FILL ALL FIELDS").grid(row=4)
            

    master = tk.Tk(className='new teacher account')
    master.geometry("350x200") 
    tk.Label(master, 
             text="NOTE: fields are case sensitive").grid(row=0)
    tk.Label(master, 
             text="University").grid(row=1)
    tk.Label(master, 
             text="Access code").grid(row=2)
    tk.Label(master, 
             text="National Rank(int)").grid(row=3)
    tk.Button(master, 
              text='Quit', 
              command=master.destroy).grid(row=6,column=2,sticky=tk.W,pady=4)
    tk.Button(master, 
                  text='Check',
                  command=chk).grid(row=5,column=1,sticky=tk.W,pady=4)
    
    e1 = tk.Entry(master)
    e1.grid(row=1, column=1)
    e2 = tk.Entry(master,show="*")
    e2.grid(row=2, column=1)
    e3 = tk.Entry(master)
    e3.grid(row=3, column=1)
    
    

def tlogin():
    def tconf():
        def homeof():
            
            def deluniv():
                master21.destroy()
                mainmaster.destroy()
                d="drop table `%s`"
                de=d.replace("%s",var1)
                b.execute(de)
                d2="delete from uni where universities like '%s'"
                de2=d2.replace("%s",var1)
                b.execute(de2)
                a.commit()
                print("University-",var1,"dropped")
            
            master21 = tk.Tk()
            master21.title(var1)
            master21.geometry("300x200")
            tk.Label(master21, 
                 text=("Welcome to the home of " + var1)).grid(row=1,column=1)
            tk.Button(master21,text="continue")
            menu = Menu(master21) 
            master21.config(menu=menu) 
            loginmenu = Menu(menu) 
            menu.add_cascade(label='UPDATE', menu=loginmenu) 
            loginmenu.add_command(label='Update existing',command=update_existing) 
            loginmenu.add_command(label='Add Course',command=addcourse)
            createmenu = Menu(menu) 
            menu.add_cascade(label='DELETE', menu=createmenu)  
            createmenu.add_command(label='Course',command=delcourse)
            createmenu.add_command(label='University',command=deluniv)
        
        def addcourse():
            def addfinal():
                varr1=en1.get()
                varr2=en2.get()
                varr3=en3.get()
                varr4=en4.get()
                varr5=en5.get()
                varr6=en6.get()
                en1.delete(0,END)
                en3.delete(0,END)
                s2='''insert into `%s2`
                values(%s,%s,%s,%s,%s,%s)'''
                x2=s2.replace('%s2',var1)
                data=(varr1,varr2,varr3,varr4,varr5,varr6)
                b.execute(x2,data)
                a.commit()
                
            master2=tk.Tk()
            master2.title("add course- " + var1)
            master2.geometry("500x500") 
            tk.Label(master2, 
                     text="NOTE: fields are case sensitive").grid(row=0)
            tk.Label(master2, 
                     text="Course").grid(row=1)
            tk.Label(master2, 
                     text="Criteria(%)").grid(row=2)
            tk.Label(master2, 
                     text="Fees").grid(row=3)
            tk.Label(master2, 
                     text="Minimum Scholarship").grid(row=4)
            tk.Label(master2, 
                     text="Maximum Scholarship").grid(row=5)
            tk.Label(master2, 
                     text="Acceptance rate").grid(row=6)
            tk.Button(master2, 
                      text='Quit', 
                      command=master2.destroy).grid(row=9, 
                                                column=2, 
                                                sticky=tk.W, 
                                                pady=4)
            tk.Button(master2, 
                      text='Add Fields',
                      command=addfinal).grid(row=8, 
                                                column=1, 
                                                sticky=tk.W, 
                                                pady=4)
            en1 = tk.Entry(master2)
            en1.grid(row=1, column=1)
            en2 = tk.Scale(master2, from_=0, to=100, orient=HORIZONTAL)
            en2.grid(row=2, column=1)
            en3 = tk.Entry(master2)
            en3.grid(row=3, column=1)
            en4 = tk.Scale(master2, from_=0, to=100, orient=HORIZONTAL)
            en4.grid(row=4, column=1)
            v=en4.get()
            en5 = tk.Scale(master2, from_=v, to=100, orient=HORIZONTAL)
            en5.grid(row=5, column=1)
            en6 = tk.Scale(master2, from_=0, to=100, orient=HORIZONTAL)
            en6.grid(row=6, column=1)
            
            
        def delcourse():
            def delfinalc():
                varcrse=e1.get()
                if varcrse in l:
                    s='''delete from `%s` where courses like %t'''
                    x=s.replace('%s',var1)
                    xx=x.replace('%t','"' + varcrse + '"')
                    b.execute(xx)
                    a.commit()
                else:
                    tk.Label(master,text="INVALID course name").grid(row=2)
                    
                    
            s='''select courses from %s'''
            x=s.replace('%s','`'+ var1 + '`')
            b=a.cursor(buffered=True)
            b.execute(x)
            l=[]
            for i in b:
                l.append(i[0])
            master = Tk() 
            lb=Listbox(master)
            for j in l:
                lb.insert(l.index(j),j)
            e1=tk.Entry(master)
            e1.grid(row=1)
            tk.Label(master,text="Avalible courses").grid(row=2)
            lb.grid(row=4)
            btn=tk.Button(master,text='Delete',command=delfinalc)
            btn.grid(row=2,column=1)
            
        def update_existing():
            def updatefur():
                def update():
                    a=msc.connect(host='localhost',user='root',password='1234',database='project')
                    b=a.cursor(buffered=True)
                    varr1=en1.get()
                    varr2=en2.get()
                    varr3=en3.get()
                    varr4=en4.get()
                    varr5=en5.get()
                    varr6=en6.get()
                    s='''delete from `%s` where courses like %t'''
                    x=s.replace('%s',var1)
                    xx=x.replace('%t','"' + var_1 + '"')
                    b.execute(xx)
                    a.commit()
                    s2='''insert into `%s2`
                    values(%s,%s,%s,%s,%s,%s)'''
                    x2=s2.replace('%s2',var1)
                    data=(varr1,varr2,varr3,varr4,varr5,varr6)
                    b.execute(x2,data)
                    a.commit()
    
                var_1=e1.get()
                if var_1 in l:
                    master2= Tk()
                    master2.title("further details")
                    master2.geometry("500x500") 
                    tk.Label(master2, 
                             text="NOTE: fields are case sensitive").grid(row=0)
                    tk.Label(master2, 
                             text="Course").grid(row=1)
                    tk.Label(master2, 
                             text="Criteria(%)").grid(row=2)
                    tk.Label(master2, 
                             text="Fees").grid(row=3)
                    tk.Label(master2, 
                             text="Minimum Scholarship").grid(row=4)
                    tk.Label(master2, 
                             text="Maximum Scholarship").grid(row=5)
                    tk.Label(master2, 
                             text="Acceptance rate").grid(row=6)
                    tk.Button(master2, 
                              text='Quit', 
                              command=master2.destroy).grid(row=9, 
                                                        column=2, 
                                                        sticky=tk.W, 
                                                        pady=4)
                    tk.Button(master2, 
                              text='Update',command=update).grid(row=8, 
                                                        column=1, 
                                                        sticky=tk.W, 
                                                        pady=4)
                    en1 = tk.Entry(master2)
                    en1.grid(row=1, column=1)
                    en1.insert(END,var_1)
                    en2 = tk.Scale(master2, from_=0, to=100, orient=HORIZONTAL)
                    en2.grid(row=2, column=1)
                    en3 = tk.Entry(master2)
                    en3.grid(row=3, column=1)
                    en4 = tk.Scale(master2, from_=0, to=100, orient=HORIZONTAL)
                    en4.grid(row=4, column=1)
                    v=en4.get()
                    en5 = tk.Scale(master2, from_=v, to=100, orient=HORIZONTAL)
                    en5.grid(row=5, column=1)
                    en6 = tk.Scale(master2, from_=0, to=100, orient=HORIZONTAL)
                    en6.grid(row=6, column=1)
                    
                else:
                    tk.Label(master,text="Invalid course").grid(row=3)
                
            s='''select courses from %s'''
            x=s.replace('%s','`'+ var1 + '`')
            b=a.cursor(buffered=True)
            b.execute(x)
            l=[]
            for i in b:
                l.append(i[0])
            master = Tk(className='avalible courses') 
            lb=Listbox(master)
            for j in l:
                lb.insert(l.index(j),j)
            e1=tk.Entry(master)
            e1.grid(row=1)
            tk.Label(master,text="Avalible courses").grid(row=2)
            lb.grid(row=4)
            b=tk.Button(master,text='continue',command=updatefur)
            b.grid(row=2,column=1)
            
            
        var1=e1.get()
        var2=e2.get()
        s='select universities from uni where accesscode like %s'
        x=s.replace('%s','"'+var2+'"')
        b.execute(x)
        l=[]
        for i in b:
            for j in i:
                l.append(j)
                
        unil=[]
        b.execute("select universities from uni;")
        textlab=tk.Label(mainmaster,text="")
        textlab.grid(row=3,column=0)
        textlab2=tk.Label(mainmaster,text="")
        textlab2.grid(row=4,column=0)
        for i in b:
            for j in i:
                unil.append(j)
        
        if var1=='' or var2=='':
            textlab.config(text="please fill all fields")
            
        elif var2=='administrator' and var1 in unil:
            confbtn.destroy()
            textlab.config(text="____________Welcome user___________")
            textlab2.config(text="______Press login to continue______")
            tk.Button(mainmaster, 
                      text='Login',
                      command=homeof).grid(row=4,column=1,sticky=tk.W,pady=4)
        
        elif var1 in l:
            confbtn.destroy()
            textlab.config(text="____________Welcome user___________")
            textlab2.config(text="______Press login to continue______")
            tk.Button(mainmaster, 
                      text='Login',
                      command=homeof).grid(row=4,column=1,sticky=tk.W,pady=4)
            
            
        elif var1 not in unil:
            textlab.config(text="Entered university isn't registered.")
            textlab2.config(text="Consider adding it to our database")
            tk.Button(mainmaster, 
              text='Add New', 
              command=tnew).grid(row=5,column=1,sticky=tk.W,pady=4)
            
        elif len(l)==0 and var2!='administrator':
            e1.delete(0, END)
            e2.delete(0, END)
            textlab.config(text="INVALID ENTRIES")
            tk.Button(mainmaster, 
              text='Add New', 
              command=tnew).grid(row=5,column=1,sticky=tk.W,pady=4)
            
        
    def clear_fields():
        e1.delete(0,END)
        e2.delete(0,END)
        
    
    mainmaster = tk.Tk(className='teacher login')
    mainmaster.geometry("400x300") 
    tk.Label(mainmaster, 
             text="NOTE: fields are case sensitive").grid(row=0)
    tk.Label(mainmaster, 
             text="University").grid(row=1)
    tk.Label(mainmaster, 
             text="Access code").grid(row=2)
    tk.Button(mainmaster, 
              text='Quit', 
              command=mainmaster.destroy).grid(row=5,column=2,sticky=tk.W,pady=4)
    confbtn=tk.Button(mainmaster, 
              text='Confirm',
              command=tconf)
    confbtn.grid(row=4,column=1,sticky=tk.W,pady=4)
    tk.Button(mainmaster, 
              text='Clear fields',
              command=clear_fields).grid(row=4,column=2,sticky=tk.W,pady=4)
    
    e1 = tk.Entry(mainmaster)
    e1.grid(row=1, column=1)
    e2 = tk.Entry(mainmaster,show="*")
    e2.grid(row=2, column=1)




def slogin():
    def sgetuniv():
        def sshowuniv():
            
            
            def bycourse():
                def shwdeets():
                    def chkforsch_crse():
                        def addtoyourlist():
                            s=('''insert into yourlist
                                      values(%s,%s,%s,%s)''')
                            data=(student_name,colg,crse,fees)
                            b.execute(s,data)
                            a.commit()
                            tk.Label(smaster4,text="Query OK, 1 row affected").grid(row=9,column=0)
                            addtol.destroy()
                            dbtn.destroy()
                            
                        mins=fin[3]
                        maxs=fin[4]
                        minmar=fin[1]
                        dbtn.destroy()
                        maxmar=100
                        div_r=(maxs-mins)/(maxmar-minmar)
                        scholarship=(mins + div_r*(percnt-minmar))//1
                        fees=((fin[2])*((100-scholarship)/100))//1
                        tk.Label(smaster4,text='Avalible scholarship: ').grid(row=5,column=0)
                        tk.Label(smaster4,text='Effective fees(Rs.): ').grid(row=6,column=0)
                        tk.Label(smaster4,text=str(scholarship)+'%').grid(row=5,column=1)
                        tk.Label(smaster4,text=str(fees)).grid(row=6,column=1)
                        addtol=tk.Button(smaster4,text='Add to your list',command=addtoyourlist)
                        addtol.grid(row=8,column=2)
                        
                    colg=col.get()
                    for i in acctocrse:
                        if i==colg:
                            fin=acctocrse[colg][0]
                            smaster4=tk.Tk()
                            smaster4.title('details-'+crse+' in '+colg)
                            smaster4.geometry("300x300")
                            tk.Label(smaster4,text='Course: ').grid(row=0,column=0)
                            tk.Label(smaster4,text='Fees(Rs.): ').grid(row=1,column=0)
                            tk.Label(smaster4,text='Min. Scholarship(%): ').grid(row=2,column=0)
                            tk.Label(smaster4,text='Max. Scholarship(%): ').grid(row=3,column=0)
                            tk.Label(smaster4,text='Acceptance rate: ').grid(row=4,column=0)
                            tk.Label(smaster4,text=fin[0]).grid(row=0,column=1)
                            tk.Label(smaster4,text=fin[2]).grid(row=1,column=1)
                            tk.Label(smaster4,text=fin[3]).grid(row=2,column=1)
                            tk.Label(smaster4,text=fin[4]).grid(row=3,column=1)
                            tk.Label(smaster4,text=fin[5]).grid(row=4,column=1)
                            dbtn=tk.Button(smaster4,text='Calculate scholarship',command=chkforsch_crse)
                            dbtn.grid(row=7,column=2)
                            bkbtn=tk.Button(smaster4,text='Back',command=smaster4.destroy)
                            bkbtn.grid(row=8,column=1)
                            
                            
                        else:
                            tk.Label(smaster3,text='Please select an option').grid(row=2,column=0)
                        
                crse=coursesel.get()
                if crse!='':
                    smaster3=tk.Tk()
                    smaster3.title('Universities offering '+crse)
                    smaster3.geometry("400x300")
                    b.execute("select universities from uni")
                    ul=[]
                    acctocrse={}
                    for i in b:
                        ul.append(i[0])
                    for u in ul:
                        z="select * from `univ` where criteria_percentage <= percnt and courses like 'crse';"
                        z=z.replace('univ',u)
                        z=z.replace('percnt',str(percnt))
                        z=z.replace('crse',crse)
                        b.execute(z)
                        for i in b:
                            temp=[]
                            temp.append(i)
                            acctocrse[u]=temp
                    cl=[]
                    for i in acctocrse:
                        cl.append(i)
                    optns=tuple(cl)
                    col=tk.StringVar(smaster3)
                    coloptnmenu = tk.OptionMenu(smaster3,
                                 col,*optns)
                    tk.Label(smaster3,text='Universities offering '+crse).grid(row=0,column=0)
                    coloptnmenu.grid(row=1,column=1)
                    tk.Label(smaster3,text='Select university: ').grid(row=1,column=0)
                    ubtn=tk.Button(smaster3,text='Show details',command=shwdeets)
                    ubtn.grid(row=2,column=2)
                    
                    
                        
                        
                else:
                    tk.Label(smaster2,text='Please select a field').grid(row=2,column=2)
                    
                
            def bycolleage():
                def showdetails():
                    def chkforsch_col():
                        def addtoyourlist():
                            s=('''insert into yourlist
                                      values(%s,%s,%s,%s)''')
                            data=(student_name,colg,cr,fees)
                            b.execute(s,data)
                            a.commit()
                            tk.Label(smaster4,text="Query OK, 1 row affected").grid(row=9,column=0)
                            addtol.destroy()
                            schbtn.destroy()
                            
     
                        mins=details[3]
                        maxs=details[4]
                        minmar=details[1]
                        maxmar=100
                        div_r=(maxs-mins)/(maxmar-minmar)
                        schbtn.destroy()
                        scholarship=(mins + div_r*(percnt-minmar))//1
                        fees=((details[2])*((100-scholarship)/100))//1
                        tk.Label(smaster4,text='Avalible scholarship: ').grid(row=5,column=0)
                        tk.Label(smaster4,text='Effective fees(Rs.): ').grid(row=6,column=0)
                        tk.Label(smaster4,text=str(scholarship)+'%').grid(row=5,column=1)
                        tk.Label(smaster4,text=str(fees)).grid(row=6,column=1)
                        addtol=tk.Button(smaster4,text='Add to your list',command=addtoyourlist)
                        addtol.grid(row=8,column=2)
                        bkbtn=tk.Button(smaster4,text='Back',command=smaster4.destroy)
                        bkbtn.grid(row=8,column=1)
                        
                    
                    cr=selectedcourse.get()
                    if cr!='':                        
                        for i in range(len(acctocolg[colg])):
                            if acctocolg[colg][i][0]==cr:
                                details=acctocolg[colg][i]
                                smaster4=tk.Tk()
                                smaster4.title("details- "+cr+' in '+colg)
                                smaster4.geometry("300x300")
                                tk.Label(smaster4,text="Course: ").grid(row=0,column=0)
                                tk.Label(smaster4,text="Fees(Rs.): ").grid(row=1,column=0)
                                tk.Label(smaster4,text="Min. Scholarship(%): ").grid(row=2,column=0)
                                tk.Label(smaster4,text="Max. Scholarship(%): ").grid(row=3,column=0)
                                tk.Label(smaster4,text="Acceptance Rate(%): ").grid(row=4,column=0)
                                tk.Label(smaster4,text=str(details[0])).grid(row=0,column=1)
                                tk.Label(smaster4,text=str(details[2])).grid(row=1,column=1)
                                tk.Label(smaster4,text=str(details[3])).grid(row=2,column=1)
                                tk.Label(smaster4,text=str(details[4])).grid(row=3,column=1)
                                tk.Label(smaster4,text=str(details[5])).grid(row=4,column=1)
                                schbtn=tk.Button(smaster4,text='Check for scholarships',command=chkforsch_col)
                                tk.Label(smaster4,text='').grid(row=7,column=2)
                                schbtn.grid(row=8,column=0)
                    else:
                        tk.Label(smaster3,text='Please select a field').grid(row=1,column=3)
                            
                colg=colsel.get()
                if colg!='':
                    smaster3=tk.Tk()
                    smaster3.title('avalible courses in '+colg)
                    smaster3.geometry("400x300")
                    acctocolg={}
                    acctocolg[colg]=(studentdict[colg])
                    lis=[]
                    for i in range(len(acctocolg[colg])):
                        lis.append(acctocolg[colg][i][0])
                    options=tuple(lis)
                    selectedcourse=tk.StringVar(smaster3)
                    selector=tk.OptionMenu(smaster3,selectedcourse,*options)
                    selector.grid(row=1,column=1)
                    tk.Label(smaster3,text='Select a course').grid(row=0,column=0)
                    tk.Label(smaster3,text="in "+colg).grid(row=1,column=0)
                    tk.Label(smaster3,text="that you're interested in").grid(row=2,column=0)
                    deets=tk.Button(smaster3,text="Show details",command=showdetails)
                    deets.grid(row=4,column=2)
                    bkbtn=tk.Button(smaster3,text='Back',command=smaster3.destroy)
                    bkbtn.grid(row=7,column=1)
                else:
                    tk.Label(smaster2,text='Please select a field').grid(row=2,column=2)
                
                
                
                
            smaster.destroy()
            smaster2=Tk(className='criteria')
            smaster2.geometry("400x300")
            collist=[]
            crslist=[]
            for i in studentdict:
                collist.append(i)
                for j in range(len(studentdict[i])):
                    crslist.append(studentdict[i][j][0])
                    
            crslist = list(dict.fromkeys(crslist))
            coursesel = tk.StringVar(smaster2)
            crsoptions = tuple(crslist) 
            crsoptionmenu = tk.OptionMenu(smaster2,
                                 coursesel,*crsoptions)
            crsoptionmenu.grid(row=3,column=1)
            tk.Label(smaster2,text='Courses:').grid(row=3,column=0)
            
            colsel= tk.StringVar(smaster2)
            coloptions = tuple(collist) 
            coloptionmenu = tk.OptionMenu(smaster2,
                                 colsel,*coloptions)
            coloptionmenu.grid(row=1,column=1)
            tk.Label(smaster2,text='Colleages:').grid(row=1,column=0)
            tk.Button(smaster2,text="get by colleage",command=bycolleage).grid(row=1,column=2)
            tk.Button(smaster2,text="get by course",command=bycourse).grid(row=3,column=2)
            tk.Label(smaster2,text='OR').grid(row=2,column=0)
            tk.Label(smaster2,text='').grid(row=0,column=0)
            
            
            
            
        percnt=ent.get()
        student_name=ent_2.get()
        if student_name=='':
            iterlabel.config(text='please enter your name')
        else:
            b.execute("select universities from uni")
            btn.destroy()
            iterlabel.destroy()
            ent.config(state=DISABLED)
            l=[]
            studentdict={}
            for i in b:
                l.append(i[0])
            for j in l:
                st="select * from `var` where criteria_percentage < in"
                st=st.replace('var',j)
                st=st.replace('in',str(percnt))
                b.execute(st)
                courselist=[]
                for val in b:
                    courselist.append(val)
                    studentdict[j]=courselist
            nuniv=len(studentdict)
            ncr=0
            for i in studentdict:
                ncr=ncr+(len(studentdict[i]))
            if ncr==0 or nuniv==0:
                x1=tk.Label(smaster,text="....Sorry, no universities found :/....")
                x1.grid(row=4,column=1)
                awwbtn=tk.Button(smaster,text='Go back',command=smaster.destroy)
                awwbtn.grid(row=5,column=2)
            else:            
                x2=tk.Label(smaster,text=str(ncr)+' course(s) found in '+str(nuniv)+' colleage(s)')
                x2.grid(row=4,column=1)
                cntbtn=tk.Button(smaster,text="Next Step",command=sshowuniv)
                cntbtn.grid(row=5,column=2)
            
    smaster= tk.Tk(className='welcome student!')
    smaster.geometry("400x150")
    ent = tk.Scale(smaster, from_=0, to=100, orient=HORIZONTAL)
    ent.grid(row=2, column=1)
    ent_2 = tk.Entry(smaster) 
    ent_2.grid(row=3,column=1)
    tk.Label(smaster,text="12th board percentage:").grid(row=2,column=0)
    tk.Label(smaster,text="Name:").grid(row=3,column=0)
    btn=tk.Button(smaster,text="Get universities!",command=sgetuniv)
    btn.grid(row=4,column=1)
    iterlabel=tk.Label(smaster)
    iterlabel.grid(row=5,column=1)
    
    
def callback(url):
    webbrowser.open_new(url)
    
def student_check():
    
    def student_sql():

            
        name=entry.get()
        if name=='':
            tk.Label(checkmaster,text='please enter your name').grid(row=3,column=1)
        else:
            command="select * from yourlist where name like '%s'"
            command=command.replace('%s',name)
            univlist=[]
            b.execute(command)
            checkmaster.destroy()
            for i in b:
                univlist.append(i)
                
            if univlist==[]:
                checkmaster_new_acc=tk.Tk(className="new user")
                tk.Label(checkmaster_new_acc,text="it looks like you're a new user.").grid(row=0,column=0)
                tk.Label(checkmaster_new_acc,text="click here to use the software and add universities").grid(row=1,column=0)
                buttn=tk.Button(checkmaster_new_acc,text='new user',command=lambda:[slogin(),checkmaster_new_acc.destroy()])
                buttn.grid(row=2,column=0)
            else:    
                checkmaster2=tk.Tk(className="selected universities")
                checkmaster2.geometry("350x250")
                rng=len(univlist)
                tk.Label(checkmaster2,text='University').grid(row=0,column=0)
                tk.Label(checkmaster2,text='Course').grid(row=0,column=1)
                tk.Label(checkmaster2,text='Effective fees').grid(row=0,column=2)
                
                universities=[]
                
                for k in range(rng):
                    uname=univlist[k][1]
                    universities.append(uname)
                    tk.Label(checkmaster2,text=uname).grid(row=k+1,column=0)
                    tk.Label(checkmaster2,text=univlist[k][2]).grid(row=k+1,column=1)
                    tk.Label(checkmaster2,text=univlist[k][3]).grid(row=k+1,column=2)
                    

                    
                lastbtn=tk.Button(checkmaster2,text='back',command=checkmaster2.destroy)
                lastbtn.grid(row=rng+1,column=3)
                tk.Label(checkmaster2,text='Related Websites:').grid(row=rng+2,column=1)
                
                if 'Symbiosis Pune' in universities:
                    linkbtn1= tk.Label(checkmaster2, text="Symbiosis Pune", fg="blue", cursor="hand2")
                    linkbtn1.grid(row=rng+2,column=2)
                    linkbtn1.bind("<Button-1>", lambda e: callback("http://www.sibm.edu"))
                    
                if 'IIT Bombay' in universities:
                    linkbtn1= tk.Label(checkmaster2, text="IIT Bombay", fg="blue", cursor="hand2")
                    linkbtn1.grid(row=rng+3,column=2)
                    linkbtn1.bind("<Button-1>", lambda e: callback("http://www.iitb.ac.in"))
                    
                if 'IIM Indore' in universities:
                    linkbtn1= tk.Label(checkmaster2, text="IIM Indore", fg="blue", cursor="hand2")
                    linkbtn1.grid(row=rng+4,column=2)
                    linkbtn1.bind("<Button-1>", lambda e: callback("http://www.iimidr.ac.in"))
                    
                if 'IIM Ahmedabad' in universities:
                    linkbtn1= tk.Label(checkmaster2, text="IIM Ahmedabad", fg="blue", cursor="hand2")
                    linkbtn1.grid(row=rng+5,column=2)
                    linkbtn1.bind("<Button-1>", lambda e: callback("http://www.iima.ac.in"))
                
                if 'JJ School of Art' in universities:
                    linkbtn1= tk.Label(checkmaster2, text="JJ School of Art", fg="blue", cursor="hand2")
                    linkbtn1.grid(row=rng+6,column=2)
                    linkbtn1.bind("<Button-1>", lambda e: callback("http://www.sirjjschoolofart.in"))
                
        
        
    checkmaster =tk.Tk(className="login")
    checkmaster.geometry("300x100")
    entry=tk.Entry(checkmaster)
    entry.grid(row=1,column=1)
    tk.Label(checkmaster,text='enter your name:').grid(row=1,column=0)
    butn=tk.Button(checkmaster,text='continue',command=student_sql)
    butn.grid(row=2,column=2)
    

master = Tk(className="home")
master.geometry("500x100")
menu = Menu(master) 
master.config(menu=menu) 
loginmenu = Menu(menu) 
usemenu=Menu(menu)
menu.add_cascade(label='Use Program', menu=usemenu)
usemenu.add_command(label='Student', command=slogin)
menu.add_cascade(label='Login', menu=loginmenu) 
loginmenu.add_command(label='Student',command=student_check) 
loginmenu.add_command(label='Teacher', command=tlogin)
createmenu = Menu(menu) 
menu.add_cascade(label='Create account', menu=createmenu)  
createmenu.add_command(label='Teacher', command=tnew)
exitmenu= Menu(menu)
menu.add_cascade(label="Exit", menu=exitmenu)
exitmenu.add_command(label="Exit", command=master.destroy) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About', command=lambda : about())    
  

mainloop()















