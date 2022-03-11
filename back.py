from Tkinter import *
def close(e=1):
    root.destroy()
root=Tk()
root.title('phonebook')
a=PhotoImage(file='pb1.gif')
Label(root,image=a).pack()
root.after(1000,close)
root.mainloop()
