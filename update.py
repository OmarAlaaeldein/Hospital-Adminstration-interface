# update the appointments
from tkinter import *
import tkinter.messin_carebox 
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

class Application:
    def __init__(self, master):
        self.master = master
        # heading label
        self.heading = Label(master, text="Update Appointments",  fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=150, y=0)

        # search criteria -->ID 
        self.ID = Label(master, text="Enter Patient's ID", font=('arial 18 bold'))
        self.ID.place(x=0, y=60)

        # entry for  the ID
        self.IDnet = Entry(master, width=30)
        self.IDnet.place(x=280, y=62)

        # search button
        self.search = Button(master, text="Search", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=350, y=102)
    # function to search
    def search_db(self):
        self.input = self.IDnet.get()
        # execute sql 

        sql = "SELECT * FROM appointments WHERE ID LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.ID1 = self.row[1]
            self.in_care = self.row[2]
            self.ven = self.row[3]
            self.max_bed = self.row[4]
            self.max_bed = self.row[6]
            self.phone = self.row[5]
        # creating the update form
        self.uID = Label(self.master, text="Patient's ID", font=('arial 18 bold'))
        self.uID.place(x=0, y=140)

        self.uin_care = Label(self.master, text="in_care", font=('arial 18 bold'))
        self.uin_care.place(x=0, y=180)

        self.uven = Label(self.master, text="ven", font=('arial 18 bold'))
        self.uven.place(x=0, y=220)

        self.umax_bed = Label(self.master, text="max_bed", font=('arial 18 bold'))
        self.umax_bed.place(x=0, y=260)

        self.umax_bed = Label(self.master, text="Appointment max_bed", font=('arial 18 bold'))
        self.umax_bed.place(x=0, y=300)

        self.uphone = Label(self.master, text="Phone Number", font=('arial 18 bold'))
        self.uphone.place(x=0, y=340)

        # entries for each labels==========================================================
        # ===================filling the search result in the entry box to update
        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=300, y=140)
        self.ent1.insert(END, str(self.ID1))

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=180)
        self.ent2.insert(END, str(self.in_care))

        self.ent3 = Entry(self.master, width=30)
        self.ent3.place(x=300, y=220)
        self.ent3.insert(END, str(self.ven))


        self.ent5 = Entry(self.master, width=30)
        self.ent5.place(x=300, y=300)
        self.ent5.insert(END, str(self.max_bed))

        # self.ent6 = Entry(self.master, width=30)
        # self.ent6.place(x=300, y=340)
        # self.ent6.insert(END, str(self.phone))

        # button to execute update
        self.update = Button(self.master, text="Update", width=20, height=2, bg='lightblue', command=self.update_db)
        self.update.place(x=400, y=380)

        # button to delete
        self.delete = Button(self.master, text="Delete", width=20, height=2, bg='red', command=self.delete_db)
        self.delete.place(x=150, y=380)
    def update_db(self):
        # declaring the variables to update
        self.var1 = self.ent1.get() #updated ID
        self.var2 = self.ent2.get() #updated in_care
        self.var3 = self.ent3.get() #updated ven
        self.var4 = self.ent4.get() #updated max_bed
        self.var5 = self.ent5.get() #updated phone
        self.var6 = self.ent6.get() #updated max_bed

        query = "UPDATE appointments SET ID=?, in_care=?, ven=?, max_bed=?, phone=?, scheduled_max_bed=? WHERE ID LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.IDnet.get(),))
        conn.commit()
        tkinter.messin_carebox.showinfo("Updated", "Successfully Updated.")
    def delete_db(self):
        # delete the appointment
        sql2 = "DELETE FROM appointments WHERE ID LIKE ?"
        c.execute(sql2, (self.IDnet.get(),))
        conn.commit()
        tkinter.messin_carebox.showinfo("Success", "Deleted Successfully")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()
        self.ent6.destroy()
# creating the object
root = Tk()
b = Application(root)
root.geometry("1200x720+0+0")
root.resizable(False, False)
root.mainloop()
