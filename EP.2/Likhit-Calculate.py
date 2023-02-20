from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title("Likhit - Calculate")
GUI.geometry("350x250")

def calOne():
    val1 = int(E1.get())
    val2 = int(E2.get())
    #L4.config(text = "Result is %s" %(val1+val2))
    text = "Result is = %s" %(val1+val2)
    messagebox.showinfo('Total',text)

def calTwo():
    val1 = int(E1.get())
    val2 = int(E2.get())
    #L4.config(text = "Result is %s" %(val1-val2))
    text = "Result is = %s" %(val1-val2)
    messagebox.showinfo('Total',text)

def calThree():
    val1 = int(E1.get())
    val2 = int(E2.get())
    #L4.config(text = "Result is %s" %(val1*val2))
    text = "Result is = %s" %(val1+val2)
    messagebox.showinfo('Total',text)

def calFour():
    val1 = int(E1.get())
    val2 = int(E2.get())
    #L4.config(text = "Result is %s" %(val1/val2))
    text = "Result is = %s" %(val1/val2)
    messagebox.showinfo('Total',text)
    
L1 = Label(GUI , text = "Calculate" , font = ("Arial", 18), fg= 'green')
L1.pack()

L2 = Label(GUI , text = "Value 1"   , font = ("Arial", 12), fg= 'green')
L2.place(x=30, y=40)

L3 = Label(GUI , text = "Value 2"   , font = ("Arial", 12), fg= 'green')
L3.place(x=30, y=80)

#L4 = Label(GUI , text = "ผลลัพธ์"     , font = ("Arial", 12))
#L4.place(x=125, y=160)

E1 = Entry(GUI)
E1.place(x=120, y=40)

E2 = Entry(GUI)
E2.place(x=120, y=80)

FB1 = Frame(GUI)
FB1.place(x=20, y=80)
#B1 = ttk.Button(FB1 , text = "+", bg="Red",command = calOne)
#B1.pack(ipadx=1, ipady=1)

B1 = Button(GUI , text = "+", bg="Red", fg= "White", font = ("Arial", 9), height = 2, width = 3, command = calOne)
B1.place(x=120, y=110)

B1 = Button(GUI , text = "-", bg="Red", fg= "White", font = ("Arial", 9), height = 2, width = 3, command = calTwo)
B1.place(x=160, y=110)

B1 = Button(GUI , text = "*", bg="Red", fg= "White", font = ("Arial", 9), height = 2, width = 3, command = calThree)
B1.place(x=200, y=110)

B1 = Button(GUI , text = "/", bg="Red", fg= "White", font = ("Arial", 9), height = 2, width = 3, command = calFour)
B1.place(x=240, y=110)

GUI.mainloop()
