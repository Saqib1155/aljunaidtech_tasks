from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

# Database credentials
mypass = "root"
mydatabase = "db"

try:
    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()
except Exception as e:
    messagebox.showerror("Database Error", f"Could not connect to database:\n{e}")
    exit()

# Table names
issueTable = "books_issued"
bookTable = "books"

def deleteBook():
    bid = bookInfo1.get().strip()

    if not bid:
        messagebox.showwarning("Input Error", "Please enter a Book ID.")
        return

    try:
        # First delete from issue table
        cur.execute(f"DELETE FROM {issueTable} WHERE bid = %s", (bid,))
        con.commit()

        # Then delete from books table
        cur.execute(f"DELETE FROM {bookTable} WHERE bid = %s", (bid,))
        con.commit()

        if cur.rowcount == 0:
            messagebox.showinfo("Not Found", "No book found with that ID.")
        else:
            messagebox.showinfo("Success", "Book record deleted successfully.")
        bookInfo1.delete(0, END)
        root.destroy()

    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete book.\n\nError: {e}")

def delete():
    global bookInfo1, Canvas1, root

    root = Tk()
    root.title("Library - Delete Book")
    root.geometry("600x500")
    root.minsize(width=400, height=400)

    Canvas1 = Canvas(root, bg="#006B38")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID input
    lb2 = Label(labelFrame, text="Book ID :", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Buttons
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=deleteBook)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
