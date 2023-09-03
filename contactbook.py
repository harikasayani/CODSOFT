from tkinter import *
window=Tk()
window.geometry("700x500")
window.config(bg="lightblue")
frame=Frame(window)
name2=StringVar()
email2=StringVar()
phone2=StringVar()
address2=StringVar()
value=StringVar()
search2=StringVar()
def add():
    global list1
    
    list1=Listbox(window,width=75,height=20)
    name1=Message(window,text="Name :",width=50).place(x=50,y=75)
    name=Entry(window,textvariable=name2).place(x=50,y=100)
    email1=Message(window,text="Email :",width=50).place(x=50,y=125)
    email=Entry(window,textvariable=email2).place(x=50,y=150)
    phone1=Message(window,text="Phone no :",width=75).place(x=50,y=175)
    phone=Entry(window,textvariable=phone2).place(x=50,y=200)
    address1=Message(window,text="Address :",width=50).place(x=50,y=225)
    address=Entry(window,textvariable=address2).place(x=50,y=250)
    list1.place(x=200,y=60)
    submit=Button(window,text="Submit",command=lambda:Submit()).place(x=50,y=325)
def Submit():
    d1=name2.get()
    list1.insert(END,"Name : "+d1)
    d2=email2.get()
    d3=phone2.get()
    list1.insert(END,"Phone no : "+d3)
    list1.insert(END,"-------------------------------------------------------------------------------------------------------------------------")
    d4=address2.get()
    name2.set(" ")
    email2.set(" ")
    phone2.set(" ")
    address2.set(" ")
def search():
    search=Message(window,text="search :",width=50).place(x=50,y=275)
    search1=Entry(window,textvariable=search2).place(x=50,y=300)
    
def searchcontact():
    enter2="Name : "+search2.get()
    index=list1.get(0,"end")
    for i in index:
        if enter2==i:
            print("YES")
            break
        else:
             print("NO")
def delete():
    select=list1.curselection()
    list1.delete(select)
label=Label(window,text="CONTACT BOOK",fg="red",width=20).place(x=270,y=40)
button=Button(window,text="add contact",command=lambda:add()).place(x=50,y=400)
button1=Button(window,text="search contact",command=lambda:searchcontact()).place(x=150,y=400)
button2=Button(window,text="delete contact",command=lambda:delete()).place(x=250,y=400)
button3=Button(window,text="search",command=lambda:search()).place(x=350,y=400)
window.mainloop()