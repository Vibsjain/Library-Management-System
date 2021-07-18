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

def del_from_here(b_id):
	b_id = int(b_id)
	cur.execute("SELECT EXISTS (SELECT 1 FROM Book_data WHERE Book_Id = (?))", (b_id,))
	check = cur.fetchone()[0]
	if check == 0:
		messagebox.showerror("NOT FOUND", "Book Record Not Found!")
		root.destroy()
	else:
		cur.execute("DELETE FROM Book_data WHERE Book_Id = (?)", (b_id,))
		conn.commit()
		messagebox.showinfo("DELETED", "Record Deleted!")
		root.destroy()

def del_book():
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
	login_frame_border.place(relx = 0.215, rely = 0.25, relwidth = 0.6, relheight = 0.4)
	login_frame = Frame(login_frame_border, bg = "black")
	login_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

	enter = Label(login_frame, text = "Enter Book Id", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	enter.place(relx = 0, relwidth = 1, rely = 0.2, relheight = 0.2)
	del_entry = Entry(login_frame, bd = 5, bg = "white", font = ('courier', 20, 'bold'))
	del_entry.place(relx = 0.3, rely = 0.5, relwidth = 0.4, relheight = 0.2)

	# Submitting Values
	submit = Button(root, text = "Delete Book", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = lambda: del_from_here(del_entry.get()))
	submit.place(relx = 0.375, rely = 0.8, relwidth = 0.25, relheight = 0.08)

	main_menu = Button(root, text = "Go To Main Menu", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'))
	main_menu.place(relx = 0.1, rely = 0.8, relwidth = 0.25, relheight = 0.08)

	close = Button(root, text = "Close Application", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = exit)
	close.place(relx = 0.65, rely = 0.8, relwidth = 0.25, relheight = 0.08)


	# Closing Window
	root.mainloop()