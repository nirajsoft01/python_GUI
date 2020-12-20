from tkinter import *
screen= Tk()
screen.title("Login")
screen.wm_minsize(width=700, height=700)
screen.geometry("700x700")
screen.config(bg= "black")
def login():
 x= e1.get()
 y= e2.get()

 if x== "Mohit" and y=="computer123":
     screen1= Tk()
     screen1.geometry("1000x1000")
     screen1.title("Manhattan")
 else:
     l3.config(text= "Invalid Username or Password")

l1=Label(screen, text= " LOG IN ", fg="white", bg="black")
l1.config(font= ("calibri",35), borderwidth=1, relief="solid")
l1.place(x=100, y=200)

l2=Label(screen, text= "  Username ", fg="white", bg="black")
l2.config(font= ("calibri",18), borderwidth=1, relief="solid")
l2.place(x=120, y=300)

e1=Entry(screen, borderwidth=2, relief="solid", font= ("calibri", 17, "bold"))
e1.place(x=130, y=340)

l2=Label(screen, text= "  Password ", fg="white", bg="black")
l2.config(font= ("calibri",18), borderwidth=1, relief="solid")
l2.place(x=120, y=400)

e2=Entry(screen, show="*", borderwidth=2, relief="solid", font= ("calibri", 17, "bold"))
e2.place(x=130, y=440)

b1= Button(screen, text= " Login ", command= login)
b1.config(borderwidth=0.5, relief="solid",width=20, height=2,bg="blue", fg="white")
b1.place(x=360, y=520)

l3=Label(screen, text= "", fg="white", bg="black")
l3.config(font= ("calibri",10), borderwidth=1, relief="solid")
l3.place(x=130, y=480)

screen.mainloop()

"""a= input("Set Username")
b= input("Set Password")

while(True):
 x= input("Please enter ur username")
 y= input("Please enter ur password")
 if x== a and y==b:
    print("Welcome to the future")
 else:
    print("Invalid Username or Password")"""



    




