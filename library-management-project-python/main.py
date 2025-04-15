from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from AddBook import addBook
from DeleteBook import delete
from ViewBooks import View
from IssueBook import issueBook
from ReturnBook import returnBook
import os

# MySQL credentials
mypass = "root"
mydatabase = "db"

# Try to connect to the database
try:
    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()
except Exception as e:
    messagebox.showerror("Database Connection Error", f"Could not connect to database:\n{e}")

# Create main window
root = Tk()
root.title("Library")
root.minsize(width=400, height=400)
root.geometry("600x500")

# Background image setup
same = True
n = 0.25

# Check if the image exists
image_path = "lib.jpg"
if not os.path.isfile(image_path):
    messagebox.showerror("Image Error", f"Background image '{image_path}' not found.")
    root.destroy()
else:
    background_image = Image.open(image_path)
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth * n)
    newImageSizeHeight = int(imageSizeHeight * n) if same else int(imageSizeHeight / n)

    # Use Resampling.LANCZOS for modern PIL
    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)
    Canvas1.create_image(300, 340, image=img)
    Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill=BOTH)

    # Title Frame
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingLabel = Label(headingFrame1, text="Welcome to \n DataFlair Library", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Buttons
    btn1 = Button(root, text="Add Book Details", bg='black', fg='white', command=addBook)
    btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    btn2 = Button(root, text="Delete Book", bg='black', fg='white', command=delete)
    btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

    btn3 = Button(root, text="View Book List", bg='black', fg='white', command=View)
    btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

    btn4 = Button(root, text="Issue Book to Student", bg='black', fg='white', command=issueBook)
    btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

    btn5 = Button(root, text="Return Book", bg='black', fg='white', command=returnBook)
    btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

    root.mainloop()

