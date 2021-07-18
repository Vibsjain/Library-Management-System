# Importing Modules
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
from search_book import *
import sys

# Location of Database
database = "C:/Users/91997/Desktop/FINAL PROJECT/library_data.db"
# Connecting Database
global conn, cur
conn = sqlite3.connect(database)
cur = conn.cursor()

def exit():
	sys.exit()

def go_to_search(a, b):
	if a != "":
		cur.execute("SELECT EXISTS (SELECT 1 FROM Book_data WHERE Book_name = (?))", (a,))
		c = cur.fetchone()[0]
		if c == 1:
			root.destroy()
			search_here(a, 0)
		else:
			root.destroy()
			messagebox.showerror("NOT FOUND", "Book Record Not Found!")
	elif b != "":
		cur.execute("SELECT EXISTS (SELECT 1 FROM Book_data WHERE Author_name = (?))", (b,))
		c = cur.fetchone()[0]
		if c == 1:
			root.destroy()
			search_here(b, 1)
		else:
			root.destroy()
			messagebox.showerror("NOT FOUND", "Book Record Not Found!")
	else:
		messagebox.showerror("INCOMPLETE", "Incomplete information given!")

def search():
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
	login_frame_border.place(relx = 0.265, rely = 0.25, relwidth = 0.5, relheight = 0.4)
	login_frame = Frame(login_frame_border, bg = "black")
	login_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

	by_name = Label(login_frame, text = "Search By Name", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	by_name.place(relx = 0.03, rely = 0.2, relwidth = 0.45, relheight = 0.2)
	by_name_entry = Entry(login_frame, bd = 5, bg = "white", font = ('courier', 20, 'bold'))
	by_name_entry.place(relx = 0.53, relwidth = 0.45, rely = 0.2, relheight = 0.2)

	by_author = Label(login_frame, text = "Search By Author", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	by_author.place(relx = 0.03, rely = 0.6, relwidth = 0.45, relheight = 0.2)
	by_author_entry = Entry(login_frame, bd = 5, bg = "white", font = ('courier', 20, 'bold'))
	by_author_entry.place(relx = 0.53, relwidth = 0.45, rely = 0.6, relheight = 0.2)

	# print(by_name_entry.get(), by_author_entry.get())

	submit = Button(root, text = "Search Book", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = lambda: go_to_search(by_name_entry.get(), by_author_entry.get()))
	submit.place(relx = 0.375, rely = 0.8, relwidth = 0.25, relheight = 0.08)

	main_menu = Button(root, text = "Go To Main Menu", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'))
	main_menu.place(relx = 0.1, rely = 0.8, relwidth = 0.25, relheight = 0.08)

	close = Button(root, text = "Close Application", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = exit)
	close.place(relx = 0.65, rely = 0.8, relwidth = 0.25, relheight = 0.08)

	# Closing Window
	root.mainloop()