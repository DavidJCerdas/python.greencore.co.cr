# This script shows a GUI to list all users from the Postgres DB
from tkinter import *
import psycopg2
import csv
import datetime

window = Tk()
window.title("List users of the DB")

# DB postgres connector
cnx = psycopg2.connect("dbname=lin_flask")
cur = cnx.cursor()


# function to update the postgres DB
def list_users():
    try:
        cur.execute("SELECT * FROM users;")
        for user_x in cur.fetchall():
            print("{0}".format(list(user_x)))
            with open('users_'+str(datetime.date.today())+'.csv', mode='+a', encoding='utf-8') as users_csv:
                users_csv = csv.writer(users_csv, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                users_csv.writerow(list(user_x))
    except Exception as error:
        print("It was not possible to list the users in the DB.\n" + repr(error))
        cnx.rollback()
    exit(0)


# cancel button
cancel_button = Button(window, text="Cancel", width=7)
cancel_button.grid(row=3, column=0)
cancel_button.config(command=exit)

# Button to submit changes
submit_button = Button(window, text="Export as users.csv", width=19)
submit_button.grid(row=3, column=1)
submit_button.config(command=list_users)

window.mainloop()
