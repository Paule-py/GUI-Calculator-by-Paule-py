import tkinter
import time

top = tkinter.Tk("GUICalc")
top.geometry("300x400")
top.resizable(width=False, height=False)
top.title("GUI Calc PW")

header = tkinter.Text("", height=3, width=18, bg="lightblue")
header.place(x=50, y=50)

v = ""

def clear():
    global v
    header.delete(1.0, tkinter.END)
    v = ""
def calculate():
    global v
    print("Calculation complete.")
    try:
        eval(v)
    except:
        clear()
        header.insert(tkinter.END, "ERROR")
    solution = eval(v)
    clear()
    print(solution)
    header.insert(tkinter.END, solution)
    v = str(solution)
def one():
    global v
    header.insert(tkinter.END, "1")
    v= v + "1"
def two():
    global v
    header.insert(tkinter.END, "2")
    v= v + "2"
def three():
    global v
    header.insert(tkinter.END, "3")
    v= v + "3"
def four():
    global v
    header.insert(tkinter.END, "4")
    v= v + "4"
def five():
    global v
    header.insert(tkinter.END, "5")
    v= v + "5"
def six():
    global v
    header.insert(tkinter.END, "6")
    v= v + "6"
def seven():
    global v
    header.insert(tkinter.END, "7")
    v= v + "7"
def eight():
    global v
    header.insert(tkinter.END, "8")
    v= v + "8"
def nine():
    global v
    header.insert(tkinter.END, "9")
    v= v + "9"
def zero():
    global v
    header.insert(tkinter.END, "0")
    v= v + "0"
def add():
    global v
    header.insert(tkinter.END, "+")
    v = v + "+"
def sub():
    global v
    header.insert(tkinter.END, "-")
    v = v + "-"
def mul():
    global v
    header.insert(tkinter.END, "*")
    v = v + "*"
def div():
    global v
    header.insert(tkinter.END, "/")
    v = v + "/"
def kom():
    global v
    header.insert(tkinter.END, ".")
    v = v + "."


b1 = tkinter.Button(top, text="1", background="blue", fg="white", width=5, height=2, command=one, highlightbackground="lightblue")
b2 = tkinter.Button(top, text="2", background="blue", fg="white", width=5, height=2, command=two, highlightbackground="lightblue")
b3 = tkinter.Button(top, text="3", background="blue", fg="white", width=5, height=2, command=three, highlightbackground="lightblue")
b4 = tkinter.Button(top, text="4", background="blue", fg="white", width=5, height=2, command=four, highlightbackground="lightblue")
b5 = tkinter.Button(top, text="5", background="blue", fg="white", width=5, height=2, command=five, highlightbackground="lightblue")
b6 = tkinter.Button(top, text="6", background="blue", fg="white", width=5, height=2, command=six, highlightbackground="lightblue")
b7 = tkinter.Button(top, text="7", background="blue", fg="white", width=5, height=2, command=seven, highlightbackground="lightblue")
b8 = tkinter.Button(top, text="8", background="blue", fg="white", width=5, height=2, command=eight, highlightbackground="lightblue")
b9 = tkinter.Button(top, text="9", background="blue", fg="white", width=5, height=2, command=nine, highlightbackground="lightblue")
b0 = tkinter.Button(top, text="0", background="blue", fg="white", width=5, height=2, command=zero, highlightbackground="lightblue")
be = tkinter.Button(top, text="=", background="orange", width=5, height=2, command=calculate, highlightbackground="lightblue")
ba = tkinter.Button(top, text="+", background="grey", width=5, height=2, command=add, highlightbackground="lightblue")
bs = tkinter.Button(top, text="-", background="grey", width=5, height=2, command=sub, highlightbackground="lightblue")
bm = tkinter.Button(top, text="*", background="grey", width=5, height=2, command=mul, highlightbackground="lightblue")
bd = tkinter.Button(top, text="/", background="grey", width=5, height=2, command=div, highlightbackground="lightblue")
bc = tkinter.Button(top, text="C", background="red", width=5, height=2, command=clear, highlightbackground="lightblue")
bk = tkinter.Button(top, text=",", background="grey", width=5, height=2, command=kom, highlightbackground="lightblue")


ba.place(x=200,y=150)
bs.place(x=200,y=200)
bm.place(x=200,y=250)
bd.place(x=200,y=300)
bc.place(x=200,y=50)

b7.place(x=200-150, y=300-150)
b8.place(x=250-150, y=300-150)
b9.place(x=300-150, y=300-150)
b4.place(x=200-150, y=350-150)
b5.place(x=250-150, y=350-150)
b6.place(x=300-150, y=350-150)
b1.place(x=200-150, y=400-150)
b2.place(x=250-150, y=400-150)
b3.place(x=300-150, y=400-150)
b0.place(x=250-150, y=450-150)
be.place(x=300-150, y=450-150)
bk.place(x=50, y=300)
top.mainloop()