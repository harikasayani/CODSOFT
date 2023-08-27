from tkinter import *
my_page=Tk()
my_page.geometry("313x335")
my_page.title("Calculator")
x=" "
d=StringVar()
def result(num):
    global x
    x=x+num
    d.set(x)
    
def clears():
    global x
    x=" "
    user_exp.delete(0,END)
    
def equals():
    y=str(eval(x))
    d.set(y)
    

user_exp=Entry(my_page,textvariable=d,font=('Arial',20),justify=RIGHT,fg="blue",bg="whitesmoke")
user_exp.grid(row=0,column=0,columnspan=4,pady=20)


button0=Button(my_page,text="0",padx=30,pady=25,command=lambda:result('0'),bg="bisque")
button0.grid(row=4,column=0)

button1=Button(my_page,text="1",padx=30,pady=20,command=lambda:result('1'),bg="bisque")
button1.grid(row=3,column=0)

button2=Button(my_page,text="2",padx=30,pady=20,command=lambda:result('2'),bg="bisque")
button2.grid(row=3,column=1)

button3=Button(my_page,text="3",padx=33,pady=20,command=lambda:result('3'),bg="bisque")
button3.grid(row=3,column=2)

button4=Button(my_page,text="4",padx=30,pady=20,command=lambda:result('4'),bg="bisque")
button4.grid(row=2,column=0)

button5=Button(my_page,text="5",padx=30,pady=20,command=lambda:result('5'),bg="bisque")
button5.grid(row=2,column=1)

button6=Button(my_page,text="6",padx=33,pady=20,command=lambda:result('6'),bg="bisque")
button6.grid(row=2,column=2)

button7=Button(my_page,text="7",padx=30,pady=20,command=lambda:result('7'),bg="bisque")
button7.grid(row=1,column=0)

button8=Button(my_page,text="8",padx=30,pady=20,command=lambda:result('8'),bg="bisque")
button8.grid(row=1,column=1)

button9=Button(my_page,text="9",padx=33,pady=20,command=lambda:result('9'),bg="bisque")
button9.grid(row=1,column=2)

div=Button(my_page,text="/",padx=30,pady=20,command=lambda:result('10'),bg="bisque")
div.grid(row=2,column=3)

add=Button(my_page,text="+",padx=32,pady=20,command=lambda:result('+'),bg="bisque")
add.grid(row=3,column=3)

sub=Button(my_page,text="-",padx=32,pady=20,command=lambda:result('-'),bg="bisque")
sub.grid(row=2,column=3)

mul=Button(my_page,text="x",padx=32,pady=20,command=lambda:result('*'),bg="bisque")
mul.grid(row=1,column=3)

equal=Button(my_page,text="=",padx=30,pady=25,command=equals,bg="bisque")
equal.grid(row=4,column=1)

clear=Button(my_page,text="clear",padx=21,pady=25,font=('Arial',10),command=clears,bg="bisque")
clear.grid(row=4,column=3)

mod=Button(my_page,text="%",padx=30,pady=25,command=lambda:result('%'),bg="bisque")
mod.grid(row=4,column=2)

my_page.mainloop()
