from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import sys

# Location of Database
database = "C:/Users/91997/Desktop/FINAL PROJECT/library_data.db"
# Connecting Database
global conn, cur
conn = sqlite3.connect(database)
cur = conn.cursor()

def exit():
	sys.exit()

def search_by_author(a):
	global data
	cur.execute('''
			SELECT 
				Book_Id,
				Book_name,
				Author_name,
				Quantity,
				Department
			FROM 
				Book_data
			WHERE
				Author_name = (?)
		''', (a,))
	data = cur.fetchmany()[0]

def search_by_name(b):
	global data
	cur.execute('''
			SELECT 
				Book_Id,
				Book_name,
				Author_name,
				Quantity,
				Department
			FROM 
				Book_data
			WHERE
				Book_name = (?)
		''', (b,))
	data = cur.fetchmany()[0]

def search_here(a, n):
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

	# Creating Heading for Book Search
	book_id = Label(root, text = "Book Id", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	book_id.place(relx = 0.01, relwidth = 0.1, rely = 0.25, relheight = 0.03)

	book_name = Label(root, text = "Name", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	book_name.place(relx = 0.28, relwidth = 0.1, rely = 0.25, relheight = 0.03)

	book_author = Label(root, text = "Author", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	book_author.place(relx = 0.60, relwidth = 0.1, rely = 0.25, relheight = 0.03)

	book_quantity = Label(root, text = "Quantity", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	book_quantity.place(relx = 0.77, relwidth = 0.1, rely = 0.25, relheight = 0.03)

	book_dep = Label(root, text = "Department", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	book_dep.place(relx = 0.89, relwidth = 0.1, rely = 0.25, relheight = 0.03)

	underscore = Label(root, text = "-" * 300, bg = "black", fg = "white")
	underscore.place(relx = 0, relwidth = 1, rely = 0.3, relheight = 0.03)

	if n == 1:
		search_by_author(a)
	elif n == 0:
		search_by_name(a)

	id_book = Label(root, text = data[0], bg = "black", fg = "white", font = ('courier', 15, 'bold'))
	id_book.place(relx = 0.01, relwidth = 0.1, rely = 0.4, relheight = 0.03)

	name_book = Label(root, text = data[1], bg = "black", fg = "white", font = ('courier', 15, 'bold'))
	name_book.place(relx = 0.13, relwidth = 0.4, rely = 0.4, relheight = 0.03)

	author_book = Label(root, text = data[2], bg = "black", fg = "white", font = ('courier', 15, 'bold'))
	author_book.place(relx = 0.54, relwidth = 0.22, rely = 0.4, relheight = 0.03)

	quantity = Label(root, text = data[3], bg = "black", fg = "white", font = ('courier', 15, 'bold'))
	quantity.place(relx = 0.77, relwidth = 0.1, rely = 0.4, relheight = 0.03)

	dep = Label(root, text = data[4], bg = "black", fg = "white", font = ('courier', 15, 'bold'))
	dep.place(relx = 0.89, relwidth = 0.1, rely = 0.4, relheight = 0.03)

	main_menu = Button(root, text = "Go To Main Menu", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'))
	main_menu.place(relx = 0.18, rely = 0.8, relwidth = 0.3, relheight = 0.08)

	close = Button(root, text = "Close Application", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = exit)
	close.place(relx = 0.52, rely = 0.8, relwidth = 0.3, relheight = 0.08)

	# Closing Window
	root.mainloop()