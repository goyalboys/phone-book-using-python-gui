###############################################################################       header files

import back
import start
from Tkinter import *
import sqlite3
from tkMessageBox import *
#from search import *

##############################################################################     created database

con=sqlite3.Connection('phonedirectory10')
cur=con.cursor()
cur.execute('create table if not exists main (mid INTEGER primary key AUTOINCREMENT,fn varchar (20),mn varchar (20),ln varchar(20),company varchar(20),ad varchar(20),city varchar(20),pin number ,ws varchar(20),bd Date )')
cur.execute('create table if not exists ph (mid INTEGER,ct varchar (20), pn number,foreign key(mid) references main(mid)on delete cascade)')
cur.execute('create table if not exists pe(eid INTEGER ,eit varchar(20),ei varchar (20),foreign key (eid) references main (mid)on delete cascade)')


#########################################################################    for save the record
'''def update():
    cur.execute('update main set fn=?,mn=?,ln=?,company=?,ad=?,city=?,pin=?,ws?,bd=? where mid=?',(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),gn))
 '''   
def save():
    if flag==1:
        cur.execute('delete from ph where mid=?',(gn,))
        con.commit()
        cur.execute('delete from pe where eid=?',(gn,))
        con.commit()
        cur.execute('delete from main where mid=?',(gn,))
        con.commit()

    try:
        if type(int(e10.get()))==type(456) :        
            cur.execute('insert into main(fn,mn,ln,company,ad,city,pin,ws,bd) values(?,?,?,?,?,?,?,?,?)',(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get()))
            con.commit()
        cur.execute('select * from main')
        
        x=cur.fetchall()
        if v1.get()==1:
            y='office'
        elif v1.get()==2:
            y='home'
        elif v1.get()==3:
            y='mobile'
        else:
            y=''
        for i in x:  
            for j in i: 
                u=j
                break
        cur.execute('insert into ph values (?,?,?)',(u,y,e10.get()))
        con.commit()
        z=cur.fetchall()
        #print z
        if v2.get()==1:
            y='Office'
        elif v2.get()==2:
            y='Personal'
        else:
            y=' '
        cur.execute('insert into pe values (?,?,?)',(u,y,e11.get()))
        con.commit()        
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
        e11.delete(0,END)
        v1.set(0)
        v2.set(0)
        showinfo('saved','record succesfully saved')
        global flag
        flag=0
    except:
        if e10.get()=='':
            cur.execute('insert into main(fn,mn,ln,company,ad,city,pin,ws,bd) values(?,?,?,?,?,?,?,?,?)',(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get()))
            con.commit()
            cur.execute('select * from main')
            
            x=cur.fetchall()
            if v1.get()==1:
                y='office'
            elif v1.get()==2:
                y='home'
            elif v1.get()==3:
                y='mobile'
            else:
                y=''
            for i in x:  
                for j in i: 
                    u=j
                    break
            cur.execute('insert into ph values (?,?,?)',(u,y,e10.get()))
            con.commit()
            z=cur.fetchall()
            if v2.get()==1:
                y='Office'
            elif v2.get()==2:
                y='Personal'
            else:
                y=' '
            cur.execute('insert into pe values (?,?,?)',(u,y,e11.get()))
            con.commit()        
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            e5.delete(0,END)
            e6.delete(0,END)
            e7.delete(0,END)
            e8.delete(0,END)
            e9.delete(0,END)
            e10.delete(0,END)
            e11.delete(0,END)
            v1.set(0)
            v2.set(0)
            showinfo('saved','record succesfully saved')
            global flag
            flag=0
        else:
            showinfo('sorry','you entered wrong data')
    if flag==0:
        Button(root1,text='  Save  ',command=save).grid(row=f,column=0)
        Button(root1,text='Search',command=search).grid(row=f,column=1)
        Button(root1,text='Close',command=close).grid(row=f,column=2)
        Button(root1,text='Edit',command=search).grid(row=f,column=3)    


    
    
##########################################################            for search function
def search():
    def fun():
        t=askyesno('close','you are really want to close it')
        if t==1: 
            root.destroy()
        ######################################################
        

    
    def select(event):
        def detail():
            
            root.destroy()

            
            def fun():
                t=askyesno('close','you are really want to close it')
                if t==1:
                    root2.destroy()
                #############################
            def delete():
                showinfo('sucess',str(h[0][1])+'  record'+ '  deleted')
                root2.destroy()
                #print h[0][0]
                cur.execute('delete from ph where mid=?',(contactid,))
                con.commit()
                cur.execute('delete from pe where eid=?',(contactid,))
                con.commit()
                cur.execute('delete from main where mid=?',(contactid,))
                con.commit()
                #############################
            def edit():
                
                e1.insert(0,h[0][1])
                global gn
                global flag
                gn=h[0][0]
                e2.insert(0,h[0][2])
                e3.insert(0,h[0][3])
                e4.insert(0,h[0][4])
                e5.insert(0,h[0][5])
                e6.insert(0,h[0][6])
                e7.insert(0,h[0][7])
                e8.insert(0,h[0][8])
                e9.insert(0,h[0][9])
                try:
                    if p[0][1]=='office':
                        v1.set(1)
                    elif p[0][1]=='home':
                        v1.set(2)
                    elif p[0][1]=='mobile':
                        v1.set(3)
                    else: 
                        v1.set(0)
                except:
                    v1.set(0)
                try: 
                    if g[0][1]=='Office':
                        v2.set(1)
                    elif g[0][1]=='Personal':
                        v2.set(2)
                    else:
                        v2.set(0)
                except:
                    v2.set(0)
                try:
                    e10.insert(0,p[0][2])
                except:
                    e10.insert(0,'')
                try:
                    e11.insert(0,g[0][2])
                except:
                    e11.insert(0,'')
                flag=1
                root2.destroy()
                Button(root1,text='update',command=save).grid(row=14,column=0)
                Label(root1,text='               ',bg='light blue').grid(row=14,column=1)
                Label(root1,text='                 ',bg='light blue').grid(row=14,column=3)
                
                

            root2=Tk()
            root2['bg']='orange'
            cur.execute('select * from main where mid=?',(contactid,))
            h=cur.fetchall()
            cur.execute('select * from ph where mid=?',(contactid,))
            p=cur.fetchall()
            cur.execute('select * from pe where eid=?',(contactid,))
            g=cur.fetchall()
            Label(root2,text="details of "+str(h[0][1]),font="times 20 bold",fg='white',bg='orange').grid(row=0,column=0,columnspan=2)
            Label(root2,text='first name   :',font='times 15 italic',bg='orange').grid(row=2,column=0)
            try:
                Label(root2,text=h[0][1],font='times 15 italic',bg='orange').grid(row=2,column=1)
            except:
                Label(root2,text=' ',font='times 15 italic',bg='orange').grid(row=2,column=1)
            
            Label(root2,text='middle name  :',font='times 15 italic',bg='orange').grid(row=3,column=0)
            try:
                Label(root2,text=h[0][2],font='times 15 italic',bg='orange').grid(row=3,column=1)
            except:
                Label(root2,text=' ',font='times 15 italic',bg='orange').grid(row=3,column=1)
            Label(root2,text='last name    :',font='times 15 italic',bg='orange').grid(row=4,column=0)
            try:
                Label(root2,text=h[0][3],font='times 15 italic',bg='orange').grid(row=4,column=1)
            except:
                Label(root2,text=' ',font='times 15 italic',bg='orange').grid(row=4,column=1)
            Label(root2,text='company      :',font='times 15 italic',bg='orange').grid(row=5,column=0)
            try:
                Label(root2,text=h[0][4],font='times 15 italic',bg='orange').grid(row=5,column=1)
            except:
                Label(root2,text=' ',font='times 15 italic',bg='orange').grid(row=5,column=1)
            Label(root2,text='address      :',font='times 15 italic',bg='orange').grid(row=6,column=0)
            try:
                Label(root2,text=h[0][5],font='times 15 italic',bg='orange').grid(row=6,column=1)
            except:
                Label(root2,text=' ',font='times 15 italic',bg='orange').grid(row=6,column=1)
            Label(root2,text='city         :',font='times 15 italic',bg='orange').grid(row=7,column=0)
            try:
                Label(root2,text=h[0][6],font='times 15 italic',bg='orange').grid(row=7,column=1)
            except:
                Label(root2,text=' ',font='times 15 italic',bg='orange').grid(row=7,column=1)
            Label(root2,text='pincode      :',font='times 15 italic',bg='orange').grid(row=8,column=0)
            try:
                Label(root2,text=h[0][7],font='times 15 italic',bg='orange').grid(row=8,column=1)
            except:
                Label(root2,text=' ',font='times 15 italic',bg='orange').grid(row=8,column=1)
            Label(root2,text='website url  :',font='times 15 italic',bg='orange').grid(row=9,column=0)
            try:
                Label(root2,text=h[0][8],font='times 15 italic',bg='orange').grid(row=9,column=1)
            except:
                Label(root2,text=' ',font='times 15 italic',bg='orange').grid(row=9,column=1)
            Label(root2,text='date of birth :',font='times 15 italic',bg='orange').grid(row=10,column=0)
            try:
                Label(root2,text=h[0][9],font='times 15 italic',bg='orange').grid(row=10,column=1)
            except:
                Label(root2,text=' ',font='times 15 italic',bg='orange').grid(row=10,column=1)
            Label(root2,text='phone details :',font='times 15 italic',bg='orange',fg='blue').grid(row=11,column=0)
            try:
                Label(root2,text=p[0][1],font='times 15 italic',bg='orange').grid(row=12,column=0)
            except:
                Label(root2,text=' ',font='times 15 italic',bg='orange').grid(row=12,column=0) 
            try:
                Label(root2,text=p[0][2],font='times 15 italic',bg='orange').grid(row=12,column=1)
            except:
                Label(root2,text=' ',font='times 15 italic',bg='orange').grid(row=12,column=1)

            
            Label(root2,text='email address :',font='times 15 italic',bg='orange',fg='blue').grid(row=13,column=0)
            try:
                Label(root2,text=g[0][1],font='times 15 italic',bg='orange').grid(row=14,column=0)
            except:
                Label(root2,text=' ',font='times 15 italic',bg='orange').grid(row=14,column=0)
            try:
                Label(root2,text=g[0][2],font='times 15 italic',bg='orange').grid(row=14,column=1)
            except:
                Label(root2,text=' ',font='times 15 italic',bg='orange').grid(row=14,column=1)
            
            Button(root2,text='Close',command=fun).grid(row=16,column=1)
            Button(root2,text='DELETE',command=delete).grid(row=16,column=0)
            Button(root2,text='Edit',command=edit).grid(row=16,column=2)


            
        widget=event.widget   
        selection=widget.curselection()
        contactid=str(dic.get(selection[0]))
        detail()
    def typei(e=1):
        e14.delete('0','end')
        cur.execute("select mid,fn,mn,ln from main where fn like ? or mn like ? or ln like ? order by fn",('%'+e12.get()+'%','%'+e12.get()+'%','%'+e12.get()+'%',))
        e13=cur.fetchall()
        k=0
        dic.clear()
        for i in e13:
            dic.update({k:i[0]})
            e14.insert(END,str(i[1])+' '+str(i[2])+' '+str(i[3]))
            k+=1
        root.bind('<<ListboxSelect>>',select)
    root=Tk()
    Button(root,text='Close',command=close).grid(row=3,column=1)
    Label(root,text="enter your",font="times 20 bold",bg='light blue',fg='light blue').grid(row=0,column=0)
    Label(root,text="searching Phone Book",font="times 20 bold",bg='light blue').grid(row=0,column=1)
    Label(root,text='enter your Name',font='times 13').grid(row=1,column=0)
    e14=Listbox(root,height=20,width=60,xscrollcommand=7,yscrollcommand=9)
    e14.grid(row=2,column=0,columnspan=2)
    e12=Entry(root)
    e12.grid(row=1,column=1)
    cur.execute("select mid,fn,mn,ln from main where fn like ? or mn like ? or ln like ? order by fn",('%'+e12.get()+'%','%'+e12.get()+'%','%'+e12.get()+'%',))
    data=cur.fetchall()
    k=0
    dic={}
    for i in data:
        dic.update({k:i[0]})
        e14.insert(END,str(i[1])+' '+str(i[2])+' '+str(i[3]))
        k+=1
    root.bind('<KeyPress>',typei)
    root.bind('<<ListboxSelect>>',select)
    root.mainloop()
#################################################################      for close
def close():
    t=askyesno('close','you are really want to close it')
    if t==1: 
        root1.destroy()

#################################################################      for  user interface
def anc():
    global f
    Label(root1,text='Select Phone Type:',font='times 15 bold',fg='blue',bg='light blue').grid(row=f,column=0)
    v1=IntVar()
    Radiobutton(root1,text='Office',variable=v1,value=1,bg='light blue').grid(row=f,column=1)
    Radiobutton(root1,text='Home',variable=v1,value=2,bg='light blue').grid(row=f,column=2)
    Radiobutton(root1,text='Mobile',variable=v1,value=3,bg='light blue').grid(row=f,column=3)
    Label(root1,text='Phone Number',font='times 13 ',bg='light blue').grid(row=f+1,column=0)
    e10=Entry(root1)
    e10.grid(row=f+1,column=1)
    Button(root1,text='+',).grid(row=f+1,column=2)
    f+=2
    '''Label(root1,text='Select Email Type:',font='times 15 bold ',fg='blue',bg='light blue').grid(row=f,column=0)
    v2=IntVar()
    Radiobutton(root1,text='Office',variable=v2,value=1,bg='light blue').grid(row=f,column=1)
    Radiobutton(root1,text='Personal',variable=v2,value=2,bg='light blue').grid(row=f,column=2)
    Label(root1,text='Email id',font='times 13 ',bg='light blue').grid(row=f,column=0)
    e11=Entry(root1)
    e11.grid(row=f,column=1)
    Button(root1,text='+',command=anc).grid(row=f,column=2)'''
f=12
gn=0
flag=0
root1=Tk()
root1.title('phonebook')
root1['bg']='light blue'
a=PhotoImage(file='pb.gif')
Label(root1,image=a).grid(row=0,column=1)
Label(root1,text='First Name',font='times 13',bg='light blue').grid(row=1,column=0)
e1=Entry(root1)
e1.grid(row=1,column=1)
Label(root1,text='Middle Name',font='times 13',bg='light blue').grid(row=2,column=0)
e2=Entry(root1)
e2.grid(row=2,column=1)
Label(root1,text='Last Name',font='times 13',bg='light blue').grid(row=3,column=0)
e3=Entry(root1)
e3.grid(row=3,column=1)
Label(root1,text='Company Name',font='times 13 ',bg='light blue').grid(row=4,column=0)
e4=Entry(root1)
e4.grid(row=4,column=1)
Label(root1,text='Address',font='times 13',bg='light blue').grid(row=5,column=0)
e5=Entry(root1)
e5.grid(row=5,column=1)
Label(root1,text='City',font='times 13',bg='light blue').grid(row=6,column=0)
e6=Entry(root1)
e6.grid(row=6,column=1)
Label(root1,text='Pincode',font='times 13 ',bg='light blue').grid(row=7,column=0)
e7=Entry(root1)
e7.grid(row=7,column=1)
Label(root1,text='Website URl',font='times 13 ',bg='light blue').grid(row=8,column=0)
e8=Entry(root1)
e8.grid(row=8,column=1)
Label(root1,text='Date of Birth',font='times 13',bg='light blue').grid(row=9,column=0)
e9=Entry(root1)
e9.grid(row=9,column=1)
Label(root1,text='Select Phone Type:',font='times 15 bold',fg='blue',bg='light blue').grid(row=10,column=0)
v1=IntVar()
Radiobutton(root1,text='Office',variable=v1,value=1,bg='light blue').grid(row=10,column=1)
Radiobutton(root1,text='Home',variable=v1,value=2,bg='light blue').grid(row=10,column=2)
Radiobutton(root1,text='Mobile',variable=v1,value=3,bg='light blue').grid(row=10,column=3)
Label(root1,text='Phone Number',font='times 13 ',bg='light blue').grid(row=11,column=0)
e10=Entry(root1)
e10.grid(row=11,column=1)
Button(root1,text='+',command=anc).grid(row=11,column=2)
Label(root1,text='Select Email Type:',font='times 15 bold ',fg='blue',bg='light blue').grid(row=f+2,column=0)
v2=IntVar()
Radiobutton(root1,text='Office',variable=v2,value=1,bg='light blue').grid(row=f+2,column=1)
Radiobutton(root1,text='Personal',variable=v2,value=2,bg='light blue').grid(row=f+2,column=2)
Label(root1,text='Email id',font='times 13 ',bg='light blue').grid(row=f+3,column=0)
e11=Entry(root1)
e11.grid(row=f+3,column=1)
Button(root1,text='+').grid(row=f+3,column=2)
Button(root1,text='Save',command=save).grid(row=f+4,column=0)
Button(root1,text='Search',command=search).grid(row=f+4,column=1)
Button(root1,text='Close',command=close).grid(row=f+4,column=2)
Button(root1,text='Edit',command=search).grid(row=f+4,column=3)    
root1.mainloop()

