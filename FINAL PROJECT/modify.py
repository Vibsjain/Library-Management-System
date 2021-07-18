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
from librarian import *
from add_book import *
from delete_book import *
import sys

def exit():
	sys.exit()

# Location of Database
database = "C:/Users/91997/Desktop/FINAL PROJECT/library_data.db"
# Connecting Database
global conn, cur
conn = sqlite3.connect(database)
cur = conn.cursor()

def mod_icons():
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
	login_frame_border.place(relx = 0.315, rely = 0.25, relwidth = 0.4, relheight = 0.3)
	login_frame = Frame(login_frame_border, bg = "black")
	login_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

	# Creating Buttons
	add = Button(login_frame, text = "Add New Book", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = add_details)
	add.place(relx = 0.15, rely = 0.150, relwidth = 0.7, relheight = 0.3)

	delete = Button(login_frame, text = "Delete Book", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = del_book)
	delete.place(relx = 0.15, rely = 0.5, relwidth = 0.7, relheight = 0.3)

	main_menu = Button(root, text = "Go To Main Menu", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'))
	main_menu.place(relx = 0.18, rely = 0.8, relwidth = 0.3, relheight = 0.08)

	close = Button(root, text = "Close Application", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = exit)
	close.place(relx = 0.52, rely = 0.8, relwidth = 0.3, relheight = 0.08)

	# Closing Window
	root.mainloop()