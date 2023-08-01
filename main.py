from tkinter import*

calculator=Tk()
calculator.title("SIMPLE Calculator")
calculator.resizable(False,False)
calculator.configure(bg="#0D0D0D")
calculator.geometry("570x600+100+200")
result_section=Label(calculator,width=25,height=2,text="",bg="#F5F5F5",font=("ariel",30))
result_section.pack()

equation=""
def show(value):
    global equation
    equation+=value
    result_section.config(text=equation)

def clear():
    global equation
    equation=""
    result_section.config(text=equation)
def calc():
    global equation
    result = ""
    if equation !="":
        try :
            result=eval(equation)
        except:
            result="INVALID input"
            equation = ""
    result_section.config(text=result)

Button(calculator,text="C",width=5,height=1,fg="#fff",bg="#1E90FF",bd=1,font=("ariel",30,"bold"),command=lambda:clear()).place(x=10,y=100)
Button(calculator,text="/",width=5,height=1,fg="#fff",bg="#545454",bd=1,font=("ariel",30,"bold"),command=lambda:show("/")).place(x=150,y=100)
Button(calculator,text="*",width=5,height=1,fg="#fff",bg="#838B83",bd=1,font=("ariel",30,"bold"),command=lambda:show("*")).place(x=290,y=100)
Button(calculator,text="%",width=5,height=1,fg="#fff",bg="#838B83",bd=1,font=("ariel",30,"bold"),command=lambda:show("%")).place(x=430,y=100)

Button(calculator,text="7",width=5,height=1,fg="#fff",bg="#545454",bd=1,font=("ariel",30,"bold"),command=lambda:show("7")).place(x=10,y=200)
Button(calculator,text="8",width=5,height=1,fg="#fff",bg="#545454",bd=1,font=("ariel",30,"bold"),command=lambda:show("8")).place(x=150,y=200)
Button(calculator,text="9",width=5,height=1,fg="#fff",bg="#838B83",bd=1,font=("ariel",30,"bold"),command=lambda:show("9")).place(x=290,y=200)
Button(calculator,text="+",width=5,height=1,fg="#fff",bg="#838B83",bd=1,font=("ariel",30,"bold"),command=lambda:show("+")).place(x=430,y=200)

Button(calculator,text="4",width=5,height=1,fg="#fff",bg="#545454",bd=1,font=("ariel",30,"bold"),command=lambda:show("4")).place(x=10,y=300)
Button(calculator,text="5",width=5,height=1,fg="#fff",bg="#545454",bd=1,font=("ariel",30,"bold"),command=lambda:show("5")).place(x=150,y=300)
Button(calculator,text="6",width=5,height=1,fg="#fff",bg="#838B83",bd=1,font=("ariel",30,"bold"),command=lambda:show("6")).place(x=290,y=300)
Button(calculator,text="-",width=5,height=1,fg="#fff",bg="#838B83",bd=1,font=("ariel",30,"bold"),command=lambda:show("-")).place(x=430,y=300)

Button(calculator,text="1",width=5,height=1,fg="#fff",bg="#545454",bd=1,font=("ariel",30,"bold"),command=lambda:show("1")).place(x=10,y=400)
Button(calculator,text="2",width=5,height=1,fg="#fff",bg="#545454",bd=1,font=("ariel",30,"bold"),command=lambda:show("2")).place(x=150,y=400)
Button(calculator,text="3",width=5,height=1,fg="#fff",bg="#838B83",bd=1,font=("ariel",30,"bold"),command=lambda:show("3")).place(x=290,y=400)
Button(calculator,text="=",width=5,height=3,fg="#fff",bg="#838B83",bd=1,font=("ariel",30,"bold"),command=lambda:calc()).place(x=430,y=400)

Button(calculator,text="0",width=10,height=1,fg="#fff",bg="#545454",bd=1,font=("ariel",30,"bold"),command=lambda:show("0")).place(x=10,y=500)
Button(calculator,text=".",width=5,height=1,fg="#fff",bg="#545454",bd=1,font=("ariel",30,"bold"),command=lambda:show(".")).place(x=290,y=500)

calculator.mainloop()
