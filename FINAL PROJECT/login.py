# Importing Modules
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image 
import sqlite3
# from main import *
from librarian import *
from student import *
from add_student import *
from password import *

global library_password
# Location of Database
database = "C:/Users/91997/Desktop/FINAL PROJECT/library_data.db"
# Connecting Database
global conn, cur
conn = sqlite3.connect(database)
cur = conn.cursor()
cur.execute("SELECT value FROM Variables WHERE name = 'password'")
library_password = str(cur.fetchone()[0])

# n = 0 for student and 1 for librarian

def check_pass(string):
	if string == library_password:
		root.destroy()
		librarian_choices()
	else:
		messagebox.showwarning("PASSWORD", "Invalid Password")
		root.destroy()

def check_id(number):
	cur.execute("SELECT EXISTS (SELECT 1 FROM Student_record WHERE Student_Id = (?))", (number,))
	conn.commit()
	data=cur.fetchone()[0]
	if data == 1:
		root.destroy()
		student_choices(number)
	elif data == 0:
		messagebox.showerror("STUDENT", "Student record not found!")
		root.destroy()

# Log In As Admin
def login_admin():
	# Log In Frame
	login_frame_border = Frame(root, bg = "#FFC433", bd = 5)
	login_frame_border.place(relx = 0.315, rely = 0.3, relwidth = 0.4, relheight = 0.3)
	login_frame = Frame(login_frame_border, bg = "black")
	login_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

	# Entering values
	enter = Label(login_frame, text = "ENTER PASSWORD", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	enter.place(relx = 0, rely = 0.2, relwidth = 1, relheight = 0.2)
	entry = Entry(login_frame, bg = "white", bd = 5, show = "*", font = ('courier', 15))
	entry.place(relx = 0.35, rely = 0.6, relwidth = 0.31, relheight = 0.2)

	# Submit Button
	submit = Button(root, text = "LOG IN", bg = "#FFC433", fg = "black", font = ('courier', 15, 'bold'), bd = 5, command = lambda: check_pass(entry.get()))
	submit.place(relx = 0.42, rely = 0.7, relwidth = 0.2, relheight = 0.08)

def login_student():
	login_frame_border = Frame(root, bg = "#FFC433", bd = 5)
	login_frame_border.place(relx = 0.315, rely = 0.3, relwidth = 0.4, relheight = 0.3)
	login_frame = Frame(login_frame_border, bg = "black")
	login_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

	# Entering values
	enter = Label(login_frame, text = "ENTER ID", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	enter.place(relx = 0, rely = 0.2, relwidth = 1, relheight = 0.2)
	entry = Entry(login_frame, bg = "white", bd = 5, font = ('courier', 15))
	entry.place(relx = 0.35, rely = 0.6, relwidth = 0.31, relheight = 0.2)

	# Submit Button
	submit = Button(root, text = "LOG IN", bg = "#FFC433", fg = "black", font = ('courier', 15, 'bold'), bd = 5, command = lambda: check_id(entry.get()))
	submit.place(relx = 0.42, rely = 0.7, relwidth = 0.2, relheight = 0.08)

# Creating main function 
def login_fun(n):
	
	# Creating Window
	global root
	global Canvas1
	root = Tk()
	root.title('LIBRARY')
	screen_width = root.winfo_screenwidth() 
	screen_height = root.winfo_screenheight() 
	root.geometry(str(screen_width) + "x" + str(screen_height))

	Canvas1 = Canvas(root)      
	Canvas1.config(bg="black",width = screen_width, height = screen_height)
	Canvas1.pack(expand=True,fill=BOTH)

	# Creating Heading
	heading_frame = Frame(root, bg = "#FFC433", bd = 5)
	heading_frame.place(relx=0.215,rely=0.05,relwidth=0.6,relheight=0.15)
	heading = Label(heading_frame, text = "Welcome To Library", bg = "black", fg = "white", font = ('courier', 50, 'bold'))
	heading.place(relx=0,rely=0, relwidth=1, relheight=1)

	# Log In As Student Or Librarian
	if n == 1:
		login_admin()
	elif n == 0:
		login_student()

	# Main Menu
	main_menu = Button(root, text = "Go To Main Menu", bg = "#FFC433", fg = "black", font = ('courier', 15, 'bold'), bd = 5, command = root.destroy)
	main_menu.place(relx = 0.365, rely = 0.8, relwidth = 0.3, relheight = 0.08)

	# Closing Window
	root.mainloop()