# Importing Modules
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image 
import sqlite3
from librarian import *
from student import *
from login import *
from password import *
import sys

# Location of Database
database = "C:/Users/91997/Desktop/FINAL PROJECT/library_data.db"
# Connecting Database
global conn, cur
conn = sqlite3.connect(database)
cur = conn.cursor()

def exit():
	sys.exit()

def add_confirm(x_name, x_branch, x_number, token = 0):
	cur.execute("SELECT value FROM Variables WHERE name = 'n'")
	id = int(cur.fetchone()[0])
	fine = 0.0
	cur.execute("INSERT INTO Student_record VALUES (?, ?, ?, ?, ?, ?)", (id, x_name, x_branch, x_number, token, fine,))
	id += 1
	id = str(id)
	cur.execute("UPDATE Variables SET value = (?) WHERE name = 'n'", (id,))
	conn.commit()
	messagebox.showinfo("COMPLETE", "Record Added Successfully! Student id is " + str(int(id) - 1))
	root.destroy()

def check_null(x_name, x_branch, x_number):
	if (x_name == '') or (x_branch == '') or (x_number == ''):
		messagebox.showwarning("INCOMPLETE FIELD", "All fields must be completely filled!")
		root.destroy()
	else:
		add_confirm(x_name, x_branch, x_number)

def add():
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

	# Button Frame
	login_frame_border = Frame(root, bg = "#FFC433", bd = 5)
	login_frame_border.place(relx = 0.215, rely = 0.25, relwidth = 0.6, relheight = 0.5)
	login_frame = Frame(login_frame_border, bg = "black")
	login_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

	name = Label(login_frame, text = "Student Name : ", bg = "black", fg = "white", font = ('courier', 20))
	name.place(relx = 0.1, rely = 0.125, relwidth = 0.3, relheight = 0.15)
	name_entry = Entry(login_frame, bd = 5, bg = "white", font = ('courier', 20, 'bold'))
	name_entry.place(relx = 0.5, rely = 0.125, relwidth = 0.4, relheight = 0.15)

	branches = ['COE', 'IT', 'SE', 'MCE', 'EE', 'ECE', 'MAM', 'BT']
	check = StringVar(root)
	branch = Label(login_frame, text = "Student Branch : ", bg = "black", fg = "white", font = ('courier', 20))
	branch.place(relx = 0.1, rely = 0.375, relwidth = 0.3, relheight = 0.15)
	branch_entry = OptionMenu(login_frame, check, *branches)
	branch_entry.config(bg = "white", fg = "black" , font = ('courier', 20, 'bold'), bd = 5)
	branch_entry.place(relx = 0.5, rely = 0.375, relwidth = 0.4, relheight = 0.15)

	contact = Label(login_frame, text = "Contact Number : ", bg = "black", fg = "white", font = ('courier', 20))
	contact.place(relx = 0.1, rely = 0.625, relwidth = 0.3, relheight = 0.15)
	contact_entry = Entry(login_frame, bd = 5, bg = "white", font = ('courier', 20, 'bold'))
	contact_entry.place(relx = 0.5, rely = 0.625, relwidth = 0.4, relheight = 0.15)

	# Submitting Values
	submit = Button(root, text = "Add Details", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = lambda: check_null(name_entry.get(), check.get(), contact_entry.get()))
	submit.place(relx = 0.375, rely = 0.82, relwidth = 0.25, relheight = 0.08)

	main_menu = Button(root, text = "Go To Main Menu", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = root.destroy)
	main_menu.place(relx = 0.1, rely = 0.82, relwidth = 0.25, relheight = 0.08)

	close = Button(root, text = "Close Application", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = exit)
	close.place(relx = 0.65, rely = 0.82, relwidth = 0.25, relheight = 0.08)

	# Closing Window
	root.mainloop()