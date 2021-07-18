# Importing Modules
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
from login import *
from student import *
from add_student import *
from password import *
from search_by import *
from dep_booklist import *
from view_books import *
from modify import *
from issue_books import *
import sys

# Location of Database
database = "C:/Users/91997/Desktop/FINAL PROJECT/library_data.db"
# Connecting Database
global conn, cur
conn = sqlite3.connect(database)
cur = conn.cursor()

def exit():
	sys.exit()

def add_s():
	root.destroy()
	add()

def change_p():
	root.destroy()
	change_password()

def librarian_choices():
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
	login_frame_border.place(relx = 0.315, rely = 0.25, relwidth = 0.4, relheight = 0.5)
	login_frame = Frame(login_frame_border, bg = "black")
	login_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

	# Creating Buttons
	booklist = Button(login_frame, text = "View Booklist", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = show_dep)
	booklist.place(relx = 0.2, rely = 0.05, relwidth = 0.6, relheight = 0.14)

	search_book = Button(login_frame, text = "Search Book", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = search)
	search_book.place(relx = 0.2, rely = 0.21, relwidth = 0.6, relheight = 0.14)

	modify_book = Button(login_frame, text = "Modify/Add/Delete Book", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 15, 'bold'), command = mod_icons)
	modify_book.place(relx = 0.2, rely = 0.37, relwidth = 0.6, relheight = 0.14)

	issue_book = Button(login_frame, text = "Issue Book", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = show_option)
	issue_book.place(relx = 0.2, rely = 0.53, relwidth = 0.6, relheight = 0.14)

	add_student = Button(login_frame, text = "Add Student", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = add_s)
	add_student.place(relx = 0.2, rely = 0.69, relwidth = 0.6, relheight = 0.14)

	change_password = Button(login_frame, text = "Change Password", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = change_p)
	change_password.place(relx = 0.2, rely = 0.85, relwidth = 0.6, relheight = 0.14)

	main_menu = Button(root, text = "Go To Main Menu", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = root.destroy)
	main_menu.place(relx = 0.18, rely = 0.82, relwidth = 0.3, relheight = 0.08)

	close = Button(root, text = "Close Application", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = exit)
	close.place(relx = 0.52, rely = 0.82, relwidth = 0.3, relheight = 0.08)

	# Closing Window
	root.mainloop()