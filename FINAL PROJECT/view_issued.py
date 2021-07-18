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
import sys

def exit():
	sys.exit()

# Location of Database
database = "C:/Users/91997/Desktop/FINAL PROJECT/library_data.db"
# Connecting Database
global conn, cur
conn = sqlite3.connect(database)
cur = conn.cursor()
global data

def view_issued_books(data):
	label_id = []
	label_name = []
	label_author = []
	label_quantity = []
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
	book_id.place(relx = 0.05, relwidth = 0.1, rely = 0.25, relheight = 0.03)

	book_name = Label(root, text = "Name", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	book_name.place(relx = 0.32, relwidth = 0.1, rely = 0.25, relheight = 0.03)

	book_author = Label(root, text = "Author", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	book_author.place(relx = 0.64, relwidth = 0.1, rely = 0.25, relheight = 0.03)

	book_dep = Label(root, text = "Department", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	book_dep.place(relx = 0.85, relwidth = 0.1, rely = 0.25, relheight = 0.03)

	underscore = Label(root, text = "-" * 300, bg = "black", fg = "white")
	underscore.place(relx = 0, relwidth = 1, rely = 0.28, relheight = 0.03)

	j = 0
	for i in data:
		# print(i)
		label_id.append(Label(root, text = i[0], bg = "black", fg = "white", font = ('courier', 15, 'bold')))
		label_name.append(Label(root, text = i[1], bg = "black", fg = "white", font = ('courier', 15, 'bold')))
		label_author.append(Label(root, text = i[2], bg = "black", fg = "white", font = ('courier', 15, 'bold')))
		label_quantity.append(Label(root, text = i[3], bg = "black", fg = "white", font = ('courier', 15, 'bold')))
		label_id[j].place(relx = 0.05, relwidth = 0.1, rely = 0.34 + j * 0.05, relheight = 0.04)
		label_name[j].place(relx = 0.17, relwidth = 0.4, rely = 0.34 + j * 0.05, relheight = 0.04)
		label_author[j].place(relx = 0.59, relwidth = 0.25, rely = 0.34 + j * 0.05, relheight = 0.04)
		label_quantity[j].place(relx = 0.85, relwidth = 0.1, rely = 0.34 + j * 0.05, relheight = 0.04)
		j += 1
		
	main_menu = Button(root, text = "Go To Main Menu", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'))
	main_menu.place(relx = 0.18, rely = 0.82, relwidth = 0.3, relheight = 0.08)

	close = Button(root, text = "Close Application", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = exit)
	close.place(relx = 0.52, rely = 0.82, relwidth = 0.3, relheight = 0.08)

	# Closing Window
	root.mainloop()

def show_message():
	messagebox.showinfo("NO BOOK", "No Book Issued!")
	root.destroy()

def fetch_issued_books(id):
	data = []
	book = [0, 0, 0]
	cur.execute("SELECT Token FROM Student_record WHERE Student_Id = (?)", (id,))
	token = int(cur.fetchone()[0])
	if token == 0:
		show_message()
	elif token == 1:
		cur.execute("SELECT Book_name FROM Book_1 WHERE Student_Id = (?)", (id,))
		book[0] = cur.fetchone()[0]

	elif token == 2:
		cur.execute("SELECT Book_name FROM Book_1 WHERE Student_Id = (?)", (id,))
		book[0] = cur.fetchone()[0]
		cur.execute("SELECT Book_name FROM Book_2 WHERE Student_Id = (?)", (id,))
		book[1] = cur.fetchone()[0]

	elif token == 3:
		cur.execute("SELECT Book_name FROM Book_1 WHERE Student_Id = (?)", (id,))
		book[0] = cur.fetchone()[0]
		cur.execute("SELECT Book_name FROM Book_2 WHERE Student_Id = (?)", (id,))
		book[1] = cur.fetchone()[0]
		cur.execute("SELECT Book_name FROM Book_3 WHERE Student_Id = (?)", (id,))
		book[2] = cur.fetchone()[0]
	for i in range(token):
		cur.execute('''
			SELECT 
				Book_Id,
				Book_name,
				Author_name,
				Department
			FROM 
				Book_data
			WHERE
				Book_name = (?)
		''', (book[i],))
		data.append(cur.fetchmany()[0])
	view_issued_books(data)