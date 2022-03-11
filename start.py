from Tkinter import *
def close(e=1):
    root.destroy()
root=Tk()
root.title('phonebook')
root.geometry('700x600')
root['bg']='blue'
#root.configure('blue')
Label(root,text='Project Title :PhoneBook',font='times 20 bold',bg='blue').place(x=50,y=100)
Label(root,text='Project of Python and database',font='times 20 bold',bg='blue').place(x=150,y=200)
Label(root,text='Developed By : vineet goyal',font='times 20 bold ',fg='green',bg='blue').place(x=250,y=300)
Label(root,text='---------------',font='times 20 bold ',fg='red',bg='blue').place(x=350,y=400)
Label(root,text='Make mouse movement over the screen to close',font='times 13 bold ',fg='red',bg='blue').place(x=300,y=500)
root.bind('<Motion>',close)
root.mainloop()
