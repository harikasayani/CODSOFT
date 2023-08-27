from tkinter import *
my_page=Tk()
my_page.geometry("800x400")
my_page.title("To_Do_List")
my_page.config(bg="burlywood")

def Add():
    data=entry.get()
    listbox.insert(END,data)
    entry.delete(0,END)
    
def Remove():
    select=listbox.curselection()
    listbox.delete(select)

def Delete():
    listbox.delete(0,END)

label=Label(my_page,text="TO DO LIST",font=("Arial",15))
label.grid(padx=10,pady=10)

entry=Entry(my_page,width=40,font=("Arial",15))
entry.grid(padx=10,pady=10)

listbox=Listbox(my_page,width=40,font=("Arial",15))
listbox.grid(padx=40,pady=5,rowspan=3)

add_button=Button(my_page,text="ADD",width=20,padx=20,pady=10,command=lambda:Add())
add_button.grid(row=2,column=1)

remove_button=Button(my_page,text="REMOVE",width=20,padx=20,pady=10,command=lambda:Remove())
remove_button.grid(row=3,column=1)

delete_button=Button(my_page,text="DELETE ALL",width=20,padx=20,pady=10,command=lambda: Delete())
delete_button.grid(row=4,column=1)
my_page.mainloop()
