from tkinter import *
from tkinter import messagebox
import pymysql

# Database credentials
mypass = "root"
mydatabase = "db"

try:
    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()
except Exception as e:
    messagebox.showerror("Database Error", f"Connection failed: {e}")

# Table names
issueTable = "books_issued"
bookTable = "books"

def issue():
    bid = inf1.get().strip()
    issueto = inf2.get().strip()

    if not bid or not issueto:
        messagebox.showwarning("Input Error", "Both fields are required.")
        return

    try:
        # Check if book exists
        cur.execute("SELECT status FROM " + bookTable + " WHERE bid = %s", (bid,))
        result = cur.fetchone()

        if not result:
            messagebox.showerror("Error", "Book ID not found.")
            return

        status = result[0]

        if status == "issued":
            messagebox.showinfo("Unavailable", "Book is already issued.")
            return

        # Issue the book
        cur.execute("INSERT INTO " + issueTable + " (bid, issuedto) VALUES (%s, %s)", (bid, issueto))
        cur.execute("UPDATE " + bookTable + " SET status = 'issued' WHERE bid = %s", (bid,))
        con.commit()

        messagebox.showinfo("Success", "Book issued successfully.")
        root.destroy()

    except Exception as e:
        con.rollback()
        messagebox.showerror("Error", f"Failed to issue book: {e}")

def issueBook():
    global inf1, inf2, root

    root = Tk()
    root.title("Library")
    root.geometry("600x500")

    Canvas1 = Canvas(root, bg="#D6ED17")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID
    lb1 = Label(labelFrame, text="Book ID:", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Issued To
    lb2 = Label(labelFrame, text="Issued To:", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    # Buttons
    issueBtn = Button(root, text="Issue", bg='#d1ccc0', fg='black', command=issue)
    issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
