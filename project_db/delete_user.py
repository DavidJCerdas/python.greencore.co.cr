# This script shows a GUI to delete one user from the Postgres DB
from tkinter import *
import psycopg2

window = Tk()
window.title("Remove an existing user")

# DB postgres connector
cnx = psycopg2.connect("dbname=lin_flask")
cur = cnx.cursor()


# function to update the postgres DB
def delete_user():
    try:
        cur.execute("DELETE FROM users WHERE id = %s", (id_entry.get()))
        cnx.commit()
    except Exception as error:
        print("It was not possible to remove the user from the DB.\n" + repr(error))
        cnx.rollback()
    print("User with id: {0} was removed successfully".format(id_entry.get()))
    exit(0)


#  id of the user to be deleted
id_label = Label(window, text="id")
id_label.grid(row=0, column=0)

# Create entries field for each label
id_text = StringVar()
id_entry = Entry(window, textvariable=id_text)
id_entry.grid(row=0, column=1)

# cancel button
cancel_button = Button(window, text="Cancel", width=7)
cancel_button.grid(row=3, column=0)
cancel_button.config(command=exit)

# Button to submit changes
submit_button = Button(window, text="Delete this User", width=18)
submit_button.grid(row=3, column=1)
submit_button.config(command=delete_user)

window.mainloop()
