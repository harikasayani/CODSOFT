from tkinter import *
import random
my_page=Tk()
my_page.geometry("400x400")
my_page.config(bg="lightpink")

data2=StringVar()
data1=StringVar()
score_user=0
score_computer=0

def Input(val):
    if val=='ROCK':
        data1.set(val)
    if val=='SCISSOR':
        data1.set(val)
    if val =='PAPER':
        data1.set(val)
    
def Submit():
    global score_user
    global score_computer
    user_input=data1.get()
    computer_input=data2.get()
    if user_input=='ROCK' and computer_input=='SCISSOR':
        score_user=score_user+1
        label1=Label(my_page,text="USER WINS").pack()
    if user_input=='ROCK' and computer_input=='PAPER':
        score_computer=score_computer+1
        label1=Label(my_page,text="COMPUTER WINS").pack()
    if user_input=='PAPER' and computer_input=='ROCK':
        score_user=score_user+1
        label1=Label(my_page,text="USER WINS").pack()
    if user_input=='PAPER' and computer_input=='SCISSOR':
        score_computer=score_computer+1
        label1=Label(my_page,text="COMPUTER WINS").pack()
    if user_input=='SCISSOR' and computer_input=='ROCK':
        score_computer=score_computer+1
        label1=Label(my_page,text="COMPUTER WINS").pack()
    if user_input=='SCISSOR' and computer_input=='PAPER':
        score_user=score_user+1
        label1=Label(my_page,text="USER WINS").pack()
    if user_input==computer_input:
        label1=Label(my_page,text="TIE").pack()
    print("score_user",score_user)
    print("score_computer",score_computer)
    data1.set(" ")
    data2.set(" ")

def  Playagain():
    data1.set(" ")
    data2.set(" ")
    enter=random.choice(['ROCK','PAPER','SCISSOR'])
    data2.set(enter)
    

main_label=Label(my_page,text="ROCK PAPER SCISSOR GAME").pack(padx=3,pady=3)

user_label=Label(my_page,text="COMPUTER").pack(padx=3,pady=3)

user_entry=Entry(my_page,textvariable=data2).pack(padx=3,pady=3)

computer_label=Label(my_page,text="USER").pack(padx=3,pady=3)

computer_entry=Entry(my_page,textvariable=data1).pack(padx=3,pady=3)

rock_button=Button(my_page,text="ROCK ",command=lambda:Input('ROCK')).pack(padx=20,side=LEFT)

paper_button=Button(my_page,text="PAPER",command=lambda:Input('PAPER')).pack(padx=20,side=RIGHT)

submit_result=Button(my_page,text="SUBMIT",command=Submit).pack(pady=20)

play_again=Button(my_page,text="PLAYAGAIN",command=Playagain).pack(padx=3,pady=3)

scissor_button=Button(my_page,text="SCISSSOR ",command=lambda:Input('SCISSOR'),padx=18).pack(padx=30,pady=23)

enter=random.choice(['ROCK','PAPER','SCISSOR'])
data2.set(enter)

my_page.mainloop()
