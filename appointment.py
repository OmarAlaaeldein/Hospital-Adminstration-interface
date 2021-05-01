from tkinter import *
import sqlite3
import pyttsx3
from tkinter import messagebox
#import tkinter.messagebox
# connect to the databse.
conn = sqlite3.connect('database.db')
# cursor to move around the databse
c = conn.cursor()

# empty list to later append the ids from the database
ids = []

# tkinter window
class Application:
    def __init__(self, master):
        self.master = master

        # creating the frames in the master
        self.left = Frame(master, width=800, height=720, bg='cyan')
        self.bg = PhotoImage(file = 'bg.png')
        self.label = Label(self.left, image = self.bg)
        self.label.place(x=0, y=225, relwidth = 1, relheight = 1)
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side=RIGHT)
        
           
        # labels for the window
        self.heading = Label(self.left, text="Hospital Admins", font=('arial 40 bold'), fg='black', bg='cyan')
        self.heading.place(x=0, y=0)
        # patients ID
        self.ID = Label(self.left, text="Hospital ID", font=('arial 18 bold'), fg='black', bg='cyan')
        self.ID.place(x=0, y=100)

        # in_care
        self.in_care = Label(self.left, text="Bed in intensive care", font=('arial 18 bold'), fg='black', bg='cyan')
        self.in_care.place(x=0, y=140)

        # ven
        self.ven = Label(self.left, text="Used Ventilators", font=('arial 18 bold'), fg='black', bg='cyan')
        self.ven.place(x=0, y=180)

        # max_bed
        self.max_bed = Label(self.left, text="Max bed", font=('arial 18 bold'), fg='black', bg='cyan')
        self.max_bed.place(x=0, y=220)

        # appointment max_ven
        self.max_ven = Label(self.left, text="Max ven", font=('arial 18 bold'), fg='black', bg='cyan')
        self.max_ven.place(x=0, y=260)

        # date
        self.date = Label(self.left, text="Date (dd,mm,yyyy)", font=('arial 18 bold'), fg='black', bg='cyan')
        self.date.place(x=0, y=300)

        # Entries for all labels============================================================
        self.ID_ent = Entry(self.left, width=30)
        self.ID_ent.place(x=280, y=100)

        self.in_care_ent = Entry(self.left, width=30)
        self.in_care_ent.place(x=280, y=140)
    
        self.ven_ent = Entry(self.left, width=30)
        self.ven_ent.place(x=280, y=180)

        self.max_bed_ent = Entry(self.left, width=30)
        self.max_bed_ent.place(x=280, y=220)

        self.max_ven_ent = Entry(self.left, width=30)
        self.max_ven_ent.place(x=280, y=260)

        self.date = Entry(self.left, width=30)
        self.date.place(x=280, y=300)


        # button to perform a command
        self.submit = Button(self.left, text="Add", width=20, height=4, bg='steelblue', command=self.add_appointment)
        self.submit.place(x=300, y=340)
    
        # getting the number of appointments fixed to view in the log
        sql2 = "SELECT ID FROM appointments "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)
        
        self.unique=[i[0] for i in c.execute("SELECT date FROM appointments ")]

        
        # ordering the ids
        self.new = sorted(ids)
        self.final_id = self.new[len(ids)-1]
        # displaying the logs in our right frame
        self.logs = Label(self.right, text="Logs", font=('arial 28 bold'), fg='white', bg='steelblue')
        self.logs.place(x=0, y=0)

        self.box = Text(self.right, width=50, height=40)
        self.box.place(x=20, y=60)
        self.box.insert(END, "Last Information Regsitered for ID  " + str(self.final_id))
    # funtion to call when the submit button is clicked
    def add_appointment(self):
        # getting the user inputs
        self.val1 = self.ID_ent.get()
        self.val2 = self.in_care_ent.get()
        self.val3 = self.ven_ent.get()
        self.val4 = self.max_bed_ent.get()
        self.val5 = self.max_ven_ent.get()
        self.val6 = self.date.get()

        # checking if the user input is empty
        print(self.unique)
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '' or self.val6== '':
            messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        # check if ID and Date is repeated for the smae entry
        elif int(self.val1) in ids and self.val6 in self.unique:
            messagebox.showinfo("Warning","Already registered for the same date and hospital ID")
        else:
            # now we add to the database
            sql = "INSERT INTO 'appointments' (ID, in_care_ent, ven_ent, max_bed_ent, max_ven_ent, date) VALUES(?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            conn.commit()
            messagebox.showinfo("Success", "Information at " +str(self.val6) + " has been created" )
            self.box.insert(END, 'information' + str(self.val1) + ' at ' + str(self.val6+'\n'))

# creating the object
root = Tk()
b = Application(root)

# resolution of the window
root.geometry("1200x720+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()
