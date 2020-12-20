from tkinter import *
fields=("Loan Amount","Number of Installments","Rate of Intrest","Installment")

def calculate_installment(entries):
    r=(float(entries[fields[2]].get())/100)/12
    p=float(entries[fields[0]].get())
    n=float(entries[fields[1]].get())
    i=p*r*(1+r)**n /((1+r)**n -1)
    i=("%8.2f"%i).strip()
    entries[fields[3]].delete(0,END)
    entries[fields[3]].config(state=NORMAL)
    entries[fields[3]].insert(0,i)
    entries[fields[3]].config(state=DISABLED)

def makeform(screen,fields):
    entries={}
    for field in fields:
        row=Frame(screen)
        lab=Label(row, width=22,text=field+": ",anchor="w",bg='black',fg='white')
        lab.config(font=('calibri',14))
        ent=Entry(row)
        ent.config(font=("calibri",15))
        ent.insert(0, "0")
        row.pack(side=TOP, fill=X,padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT)
        entries[field]=ent
    entries[field].config(state=DISABLED)
    return entries


if __name__=='__main__':
    screen=Tk()
    screen.title("Loan Calculator")
    screen.config(bg='blue')
    ents=makeform(screen,fields)
    b1=Button(screen, text= " Calculate Installment ", command= (lambda e=ents:calculate_installment(e)))
    b1.config(bg='darkblue',fg='white', borderwidth=2, relief='solid')
    b1.pack(side=TOP, padx=5, pady=5)
    b2=Button(screen, text= "Exit", command=screen.quit)
    b2.config(bg='darkblue',fg='white', borderwidth=2, relief='solid')
    b2.pack(side=BOTTOM, fill=X, padx=5, pady=5)
    screen.mainloop()







