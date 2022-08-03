from mysql import connector
from tkinter import *
from tkinter import messagebox
def database():
    conn=connector.connect(
        user='root',
        password='root',
        host='127.0.0.1',
        port='3306',
        database='formdb')
    mycursor=conn.cursor()
    mycursor.execute("insert into input values (%s,%s,%s,%s,%s,%s)",(ent1.get(),ent2.get(),ent3.get(),ent4.get(),c.get(),var.get()))
    messagebox.showinfo("INFO","Registered")
    conn.commit()

reg=Tk()
reg.geometry("400x500")
reg.resizable(0,0)
reg.title("Registration Form")

head=Label(reg,text='Register Here!!!',fg='White',bg='black',width=15,height=1,bd=2,highlightbackground='black', highlightcolor='black', highlightthickness=1)
head.place(x=150,y=50)

lab1=Label(reg,text='Sr_No.:',fg='white',bg='black',width=15,height=1,bd=2,highlightbackground='black', highlightcolor='black', highlightthickness=1)
lab1.place(x=90,y=100)
ent1=Entry(reg,width=15,bd=2,highlightbackground='black', highlightcolor='black', highlightthickness=1)
ent1.place(x=220,y=100)

lab2=Label(reg,text='Name:',fg='white',bg="black",width=15,height=1,bd=2,highlightbackground='black', highlightcolor='black', highlightthickness=1)
lab2.place(x=90,y=150)
ent2=Entry(reg,width=15,bd=2,highlightbackground='black', highlightcolor='black', highlightthickness=1)
ent2.place(x=220,y=150)

lab3=Label(reg,text='Roll no.:',fg='white',bg="black",width=15,height=1,bd=2,highlightbackground='black', highlightcolor='black', highlightthickness=1)
lab3.place(x=90,y=200)
ent3=Entry(reg,width=15,bd=2,highlightbackground='black', highlightcolor='black', highlightthickness=1)
ent3.place(x=220,y=200)

lab4=Label(reg,text='Address:',fg='white',bg="black",width=15,height=1,bd=2,highlightbackground='black', highlightcolor='black', highlightthickness=1)
lab4.place(x=90,y=250)
ent4=Entry(reg,width=15,bd=2,highlightbackground='black', highlightcolor='black', highlightthickness=1)
ent4.place(x=220,y=250)

lab5=Label(reg,text='Branch:',fg='white',bg="black",width=15,height=1,bd=2,highlightbackground='black', highlightcolor='black', highlightthickness=1)
lab5.place(x=90,y=300)
list_of_branches=["CSE","IT","ECE","ME","CIVIL","OTHER"]
c=StringVar()
droplist=OptionMenu(reg,c,*list_of_branches)
droplist.config(width=9,bd=2,highlightbackground='black', highlightcolor='black', highlightthickness=1)
c.set("Select...",)
droplist.place(x=220,y=300)

lab6=Label(reg,text='Gender:',fg='white',bg="black",width=15,height=1,bd=2,highlightbackground='black', highlightcolor='black', highlightthickness=1)
lab6.place(x=90,y=350)
var=IntVar()
Radiobutton(reg,text="Male",padx=2,variable=var,value=1).place(x=220,y=350)
Radiobutton(reg,text="Female",padx=2,variable=var,value=2).place(x=280,y=350)

log=Button(reg,text='Register',fg='Black',bg='light blue',command=database,width=15,height=1,bd=2,highlightbackground='black', highlightcolor='black', highlightthickness=1)
log.place(x=150,y=400)

reg.mainloop()
