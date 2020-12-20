from tkinter import *
screen = Tk()
screen.title("Simple Intrest Calculator")
screen.geometry("500x550")
screen.wm_minsize(width=400, height=300)

def si():
    p=int(e1.get())
    r=float(e2.get())
    t=int(e3.get())
    s= (p * r * t)/100
    tq= p+s
    l5.config(text= "Simple intrest= %d\n\nTotal Amount= %d"%(s,tq))


l1=Label(screen, text= " SIMPLE INTREST CALCULATOR ", fg="white", bg="black")
l1.config(font= ("calibri",14, "bold"), borderwidth=1, relief="solid")
l1.place(x=50, y=20)

l2=Label(screen, text= "Enter Principle Amount", fg="orange")
l2.config(font= ("calibri",13,"bold"))
l2.place(x=30, y=100)

l3=Label(screen, text= "Enter rate of intrest", fg="orange")
l3.config(font= ("calibri",14,"bold"))
l3.place(x=30, y=150)

l4=Label(screen, text= "Enter time_period", fg="orange")
l4.config(font= ("calibri",14,"bold"))
l4.place(x=30, y=200)

e1=Entry(screen, borderwidth=2, relief="solid", font= ("calibri", 13, "bold"))
e2=Entry(screen, borderwidth=2, relief="solid", font= ("calibri", 13, "bold"))
e3=Entry(screen, borderwidth=2, relief="solid", font= ("calibri", 13, "bold"))
e1.place(x=220, y=100)
e2.place(x=220, y=150)
e3.place(x=220, y=200)


b1= Button(screen, text= " Calculate ", command=si)
b1.place(x=50, y=250)

l5= Label(screen, text= "Result will come here", font= ("calibri", 15))
l5.place(x=30, y=300)

l6= Label(screen, text= "Devloped by nirajsoft", bg='Yellow', font=("calibri", 13,))
l6.pack(fill=X)
l6.pack(side=BOTTOM)


screen,mainloop()
