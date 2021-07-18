# Importing Modules
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
from login import *
from librarian import *
from student import *
from add_student import *
from password import *
import sys

# Location of Database
database = "C:/Users/91997/Desktop/FINAL PROJECT/library_data.db"

def exit():
	sys.exit()

# Connecting Database
conn = sqlite3.connect(database)
cur = conn.cursor()
root = Tk()
root.title('LIBRARY')
screen_width = root.winfo_screenwidth() 
screen_height = root.winfo_screenheight() 
root.geometry(str(screen_width) + "x" + str(screen_height))

# Setting Background Image
background_image = Image.open("library_image.jpg")
background_image = background_image.resize((screen_width, screen_height), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(screen_width / 2, screen_height / 2,image = img)      
Canvas1.config(bg="white",width = screen_width, height = screen_height)
Canvas1.pack(expand=True,fill=BOTH)

# Creating Heading
heading_frame = Frame(root, bg = "#FFC433", bd = 5)
heading_frame.place(relx=0.215,rely=0.05,relwidth=0.6,relheight=0.15)
heading = Label(heading_frame, text = "Welcome To Library", bg = "black", fg = "white", font = ('courier', 50, 'bold'))
heading.place(relx=0,rely=0, relwidth=1, relheight=1)

# Log In Frame
login_frame_border = Frame(root, bg = "#FFC433", bd = 5)
login_frame_border.place(relx = 0.315, rely = 0.3, relwidth = 0.4, relheight = 0.3)
login_frame = Frame(login_frame_border, bg = "black")
login_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

# Creating Log-in buttons and labels
login_label = Label(login_frame, text = "LOG IN AS", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
login_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.2)
librarian = Button(login_frame, text = "LIBRARIAN", bg = "#FFC433", fg = "Black", font = ('courier', 15, 'bold'), bd = 5, command = lambda: login_fun(1))
librarian.place(relx = 0.35, rely = 0.3, relwidth = 0.31, relheight = 0.2)
student = Button(login_frame, text = "STUDENT", bg = "#FFC433", fg = "Black", font = ('courier', 15, 'bold'), bd = 5, command = lambda: login_fun(0))
student.place(relx = 0.35, rely = 0.6, relwidth = 0.31, relheight = 0.2)

# Close Application Button
close = Button(root, text = "CLOSE APPLICATION", bg = "#FFC433", fg = "black", font = ('courier', 15, 'bold'), bd = 5, command = exit)
close.place(relx = 0.365, rely = 0.8, relwidth = 0.3, relheight = 0.08)

# Ending Window
root.mainloop()