from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg


loginForm = Tk()
loginForm.title('BMI Calculator')
loginForm.geometry('300x150')
right = int(loginForm.winfo_screenwidth() / 2 - 400 / 2)
down = int(loginForm.winfo_screenheight() / 2 - 200 / 2)
loginForm.geometry('+{}+{}'.format(right, down))
loginForm.resizable(0,0)
#loginForm.iconbitmap('images/login.ico')

#function

def resetForm():
    txtNumber1.set("")
    txtNumber2.set("")


def plus():
    try:
        Number1 = txtNumber1.get()
        Number2 = txtNumber2.get()
        Number2=Number2/100
        result=round(Number1/pow(Number2,2))
        if result < 18.5:
            msg.showinfo(':)',f"your BMI is {result} and you are Underweight")
        elif 18.5 <= result <= 24.9:
            msg.showinfo(':)', f"your BMI is {result} and you are Normal Weight")
        elif 25 <= result <= 29.9:
            msg.showinfo(':)', f"your BMI is {result} and you are Overweight")
        else:
            msg.showinfo(':)', f"your BMI is {result} and you are Obesity")
    except TclError:
        msg.showinfo(':)', "Enter right Number")

    #loginForm.destroy()




lblNumber1=Label(loginForm,text='weight:')
lblNumber1.grid(row=0,column=0,padx=10,pady=10)

txtNumber1=IntVar(value="")
entNumber1=Entry(loginForm,width=20,textvariable=txtNumber1)
entNumber1.grid(row=0,column=1,padx=10,pady=10)

lblNumber2=Label(loginForm,text='height:')
lblNumber2.grid(row=1,column=0,padx=10,pady=10)

txtNumber2=IntVar(value="")
entNumber2=Entry(loginForm,width=20,textvariable=txtNumber2)
entNumber2.grid(row=1,column=1,padx=10,pady=10)

btnlogin=ttk.Button(loginForm,text='Calculate',width=10,command=plus)
btnlogin.grid(row=2,column=1,padx=10,pady=10)



loginForm.mainloop()
