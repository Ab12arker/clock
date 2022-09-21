import datetime
import time

from tkinter import*
screen = Tk()
screen.title("Digital Clock")
screen.geometry('560x250')
screen.configure(background='white')

#name = "This application Developer by Partho Sarker"

def clock():
   t1 = time.strftime('%H:%M:%S %p')
   t2 = Label(screen,text=t1,font=('ds-Digital',70,'bold'),fg='red',bg = 'white')
   t2.after(180,clock)
   t2.place(x=40,y=100)
   t3 = datetime.date.today()

   d1 = Label(screen, text=t3.day, font=('ds-Digital', 35, 'bold'), fg='green', bg='white').place(x=120, y=0)
   d2 = Label(screen, text=t3.month, font=('ds-Digital', 35, 'bold'), fg='green', bg='white').place(x=220, y=0)
   d3 = Label(screen, text=t3.year, font=('ds-Digital', 35, 'bold'), fg='green', bg='white').place(x=300, y=0)
   date = Label(screen, text='Date', font=('ds-Digital', 10, 'bold'), fg='green', bg='white').place(x=130, y=50)
   month = Label(screen, text='Month', font=('ds-Digital', 10, 'bold'), fg='green', bg='white').place(x=212, y=50)
   year = Label(screen, text='Year', font=('ds-Digital', 10, 'bold'), fg='green', bg='white').place(x=335, y=50)



   hour = Label(screen, text='Hour', font=('ds-Digital', 15, 'bold'), fg='green', bg='white').place(x=70, y=200)
   mint = Label(screen, text='Min', font=('ds-Digital', 15, 'bold'), fg='green', bg='white').place(x=215, y=200)
   sec = Label(screen, text='Sec', font=('ds-Digital', 15, 'bold'), fg='green', bg='white').place(x=330, y=200)



clock()
screen.mainloop()

#nameLabel = Label(screen, font=("Calibri bold",10),bg="yellow")
#nameLabel.grid(row=3, sticky="W", padx=30)
