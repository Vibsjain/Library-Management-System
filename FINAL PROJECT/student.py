# Importing Modules
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
# from main import *
from login import *
from librarian import *
from add_student import *
from password import *
from search_by import *
from dep_booklist import *
from view_books import *
from view_issued import *
from sub_details import *
import sys

def exit():
	sys.exit()

# Location of database
database = "C:/Users/91997/Desktop/FINAL PROJECT/library_data.db"
# Connecting Database
global conn, cur
conn = sqlite3.connect(database)
cur = conn.cursor()

def student_choices(id):
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
	login_frame_border.place(relx = 0.315, rely = 0.25, relwidth = 0.4, relheight = 0.4)
	login_frame = Frame(login_frame_border, bg = "black")
	login_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

	# Creating Buttons
	booklist = Button(login_frame, text = "View Booklist", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = show_dep)
	booklist.place(relx = 0.15, rely = 0.2, relwidth = 0.7, relheight = 0.15)

	search_book = Button(login_frame, text = "Search Book", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = search)
	search_book.place(relx = 0.15, rely = 0.38, relwidth = 0.7, relheight = 0.15)

	issued_book = Button(login_frame, text = "View Issued Books", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = lambda: fetch_issued_books(id))
	issued_book.place(relx = 0.15, rely = 0.55, relwidth = 0.7, relheight = 0.15)

	submission = Button(login_frame, text = "View Submission Details", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = lambda: fetch_d(int(id)))
	submission.place(relx = 0.15, rely = 0.73, relwidth = 0.7, relheight = 0.15)

	main_menu = Button(root, text = "Go To Main Menu", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'),command = root.destroy)
	main_menu.place(relx = 0.18, rely = 0.82, relwidth = 0.3, relheight = 0.08)

	close = Button(root, text = "Close Application", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = exit)
	close.place(relx = 0.52, rely = 0.82, relwidth = 0.3, relheight = 0.08)

	# Closing Window
	root.mainloop()