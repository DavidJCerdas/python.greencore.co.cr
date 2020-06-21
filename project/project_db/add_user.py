# This script shows a GUI to add a user to the Postgres DB
from tkinter import *
import psycopg2

window = Tk()
window.title("Add a new user")

# DB postgres connector
cnx=psycopg2.connect("dbname=lin_flask")
cur=cnx.cursor()

# function to update the postgres DB
def add_user():
    print("id:{0}|name:{1}|last name:{2}|age:{3}|address:{4}|phone:{5}".format(id_entry.get(), name_entry.get(),
                                                                               last_name_entry.get(), age_entry.get(),
                                                                               address_entry.get(), phone_entry.get()))
    try:
        cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s)", (id_entry.get(),name_entry.get(),
                                                                               last_name_entry.get(), age_entry.get(),
                                                                               address_entry.get(), phone_entry.get()))
        cnx.commit()
    except Exception as error:
        print("It was not possible to insert into the DB.\n" + repr(error))
        cnx.rollback()
    print("User was added successfully")
    exit(0)


#  tkinter Labels for each DB field
id_label = Label(window, text="id")
name_label = Label(window, text="name")
last_name_label = Label(window, text="last_name")
age_label = Label(window, text="age")
address_label = Label(window, text="address")
phone_label = Label(window, text="phone")
# Put each label in the grid
id_label.grid(row=0, column=0)
name_label.grid(row=1, column=0)
last_name_label.grid(row=2, column=0)
age_label.grid(row=3, column=0)
address_label.grid(row=4, column=0)
phone_label.grid(row=5, column=0)

# Create entries field for each label
id_text = StringVar()
id_entry = Entry(window, textvariable=id_text)
name_text = StringVar()
name_entry = Entry(window, textvariable=name_text)
last_name_text = StringVar()
last_name_entry = Entry(window, textvariable=last_name_text)
age_text = StringVar()
age_entry = Entry(window, textvariable=age_text)
address_text = StringVar()
address_entry = Entry(window, textvariable=address_text)
phone_text = StringVar()
phone_entry = Entry(window, textvariable=phone_text)
# Put each entry in the grid
id_entry.grid(row=0, column=1)
name_entry.grid(row=1, column=1)
last_name_entry.grid(row=2, column=1)
age_entry.grid(row=3, column=1)
address_entry.grid(row=4, column=1)
phone_entry.grid(row=5, column=1)

cancel_button = Button(window, text="Cancel", width=7)
cancel_button.grid(row=7, column=0)
cancel_button.config(command=exit)

# Button to submit changes
submit_button = Button(window, text="Submit", width=8)
submit_button.grid(row=7, column=1)
submit_button.config(command=add_user)

window.mainloop()
