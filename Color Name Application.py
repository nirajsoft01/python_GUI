from tkinter import *
screen = Tk()
screen.title("PaintName")
screen.geometry("440x340")
screen.wm_maxsize(width=440, height=340)
screen.wm_minsize(width=440, height=340)

#Defining Function
def setColor():
    c=['black','red','green','blue']
    v.get()
    e1.config(fg= c[v.get()])


l1=Label(screen, text= "Select Your Color", font=("calibri",15, "bold"))
l1.place(x=50, y=40)

#RadioButton Creation
v=IntVar()
v.set(0)
rb10= Radiobutton(screen, text=" Default BLACK",fg= 'black', variable=v, value=0, command= setColor)
rb10.config(borderwidth=2, relief= "solid")
rb1= Radiobutton(screen, text="RED",fg= 'red', variable=v, value=1, command= setColor)
rb2= Radiobutton(screen, text="GREEN",fg= 'green', variable=v, value=2, command= setColor)
rb3= Radiobutton(screen, text="BLUE",fg= 'blue', variable=v, value=3, command= setColor)
rb10.place(x=150, y=120, width= 120)
rb1.place(x=50, y=80, width= 80)
rb2.place(x=150, y=80, width= 80)
rb3.place(x=250, y=80, width= 80)

l2=Label(screen, text= "Enter Your Name", font=("calibri",15, "bold"))
l2.place(x=50, y=150)

e1=Entry(screen, font=("calibri",25))
e1.insert(0,'     ')
e1.place(x=50, y=200, width= 330, height= 100)


screen.mainloop()
