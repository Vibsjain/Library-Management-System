from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image 
import sqlite3
import sys

def exit():
	sys.exit()

# Location of Database
database = "C:/Users/91997/Desktop/FINAL PROJECT/library_data.db"
# Connecting Database
global conn, cur
conn = sqlite3.connect(database)
cur = conn.cursor()

def add_book_here(name, author, quantity, department):
	cur.execute("SELECT value FROM Variables WHERE name = 'b'")
	id = int(cur.fetchone()[0])
	if (name == "") or (author == "") or (quantity == "") or (department == ""):
		messagebox.showerror("INCOMPLETE", "All Fields are required!")
	else:
		cur.execute("INSERT INTO Book_data VALUES (?, ?, ?, ?, ?)", (id, name, author, int(quantity), department,))
		id += 1
		id = str(id)
		cur.execute("UPDATE Variables SET value = (?) WHERE name = 'b'", (id,))
		conn.commit()
		messagebox.showinfo("COMPLETE", "Book Added Successfully! Book id is " + str(int(id) - 1))
		root.destroy()

def add_details():
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

	book_name = Label(login_frame, text = "Name of Book : ", bg = "black", fg = "white", font = ('courier', 20))
	book_name.place(relx = 0.05, rely = 0.1, relwidth = 0.4, relheight = 0.18)
	name_entry = Entry(login_frame, bd = 5, bg = "white", font = ('courier', 20, 'bold'))
	name_entry.place(relx = 0.55, rely = 0.1, relwidth = 0.4, relheight = 0.18)

	author_name = Label(login_frame, text = "Name of Author : ", bg = "black", fg = "white", font = ('courier', 20))
	author_name.place(relx = 0.05, rely = 0.3, relwidth = 0.4, relheight = 0.18)
	author_entry = Entry(login_frame, bd = 5, bg = "white", font = ('courier', 20, 'bold'))
	author_entry.place(relx = 0.55, rely = 0.3, relwidth = 0.4, relheight = 0.18)

	quan = Label(login_frame, text = "Quantity : ", bg = "black", fg = "white", font = ('courier', 20))
	quan.place(relx = 0.05, rely = 0.5, relwidth = 0.4, relheight = 0.18)
	quan_entry = Entry(login_frame, bd = 5, bg = "white", font = ('courier', 20, 'bold'))
	quan_entry.place(relx = 0.55, rely = 0.5, relwidth = 0.4, relheight = 0.18)

	dep = Label(login_frame, text = "Department : ", bg = "black", fg = "white", font = ('courier', 20))
	dep.place(relx = 0.05, rely = 0.7, relwidth = 0.4, relheight = 0.18)
	dep_entry = Entry(login_frame, bd = 5, bg = "white", font = ('courier', 20, 'bold'))
	dep_entry.place(relx = 0.55, rely = 0.7, relwidth = 0.4, relheight = 0.18)

	# Submitting Values
	submit = Button(root, text = "Add Book", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = lambda: add_book_here(name_entry.get(), author_entry.get(), quan_entry.get(), dep_entry.get()))
	submit.place(relx = 0.375, rely = 0.82, relwidth = 0.25, relheight = 0.08)

	main_menu = Button(root, text = "Go To Main Menu", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'))
	main_menu.place(relx = 0.1, rely = 0.82, relwidth = 0.25, relheight = 0.08)

	close = Button(root, text = "Close Application", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = exit)
	close.place(relx = 0.65, rely = 0.82, relwidth = 0.25, relheight = 0.08)

	# Closing Window
	root.mainloop()