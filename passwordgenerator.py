from tkinter import *
import random,string

my_page=Tk()
my_page.geometry("450x500")

my_page.title("Password Generator")

password=StringVar()
def generatepassword():
    global  set_password
    combination=string.ascii_letters+string.digits
    set_password=" "
    my_len=int(passwordlength_entry.get())
    if my_len>=8:
        for i in range(my_len):
            set_password=set_password+random.choice(combination)
        password.set(set_password)
    else:
        label1=Label(my_page,text="!enter valid length which is greater than or equal to 8",font=('Arial',12),fg='red').pack()
    
def print_password():
    print("Password  : ",set_password)
    my_password.delete(0,END)
    passwordlength_entry.delete(0,END)

password_len=Label(my_page,text=" ENTER YOUR PASSWORD LENGTH",fg="blue",bg="pink",font=("Arial",12))
password_len.pack(padx=50,pady=50)

passwordlength_entry=Entry(my_page,width=15,font=("Arial",12))
passwordlength_entry.pack(padx=30,pady=30)

generator=Button(my_page,text="GENERATE PASSWORD",command=generatepassword,fg="blue",bg="pink",font=("Arial",12))
generator.pack(padx=30,pady=30)

my_password=Entry(my_page,textvariable=password,width=20,font=("Arial",12))
my_password.pack(padx=30,pady=30)

submit=Button(my_page,text="Submit",command=print_password,font=("Arial",12),bg="pink",fg="blue")
submit.pack(padx=30,pady=30)

my_page.mainloop()
