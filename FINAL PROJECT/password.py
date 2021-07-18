from tkinter import *
from PIL import ImageTk, Image 
from tkinter import messagebox
import sqlite3
from librarian import *
from student import *
from add_student import *
from login import *
import sys

# Location of Database
database = "C:/Users/91997/Desktop/FINAL PROJECT/library_data.db"
# Connecting Database
global conn, cur
conn = sqlite3.connect(database)
cur = conn.cursor()

def exit():
	sys.exit()

def confirm_password(a, b):
	if (a == b) and a != "":
		cur.execute("UPDATE Variables SET value = (?) WHERE name = 'password'", (a,))
		conn.commit()
		messagebox.showinfo("CHANGED", "Password Changed Successfully!")
		root.destroy()
		login_fun(1)
	else:
		messagebox.showerror("INCOMPLETE", "Passwords Do Not Match!")
		root.destroy()
		librarian_choices()

def change_password():
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

	new_pass = Label(login_frame, text = "Enter New Password", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	new_pass.place(relx = 0.07, rely = 0.2, relwidth = 0.45, relheight = 0.2)
	new_pass_entry = Entry(login_frame, bd = 5, bg = "white", font = ('courier', 20, 'bold'))
	new_pass_entry.place(relx = 0.57, relwidth = 0.35, rely = 0.2, relheight = 0.2)

	confirm_pass = Label(login_frame, text = "Confirm New Password", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	confirm_pass.place(relx = 0.07, rely = 0.6, relwidth = 0.45, relheight = 0.2)
	confirm_pass_entry = Entry(login_frame, bd = 5, bg = "white", font = ('courier', 20, 'bold'))
	confirm_pass_entry.place(relx = 0.57, relwidth = 0.35, rely = 0.6, relheight = 0.2)

	submit = Button(root, text = "Change Password", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = lambda: confirm_password(new_pass_entry.get(), confirm_pass_entry.get()))
	submit.place(relx = 0.375, rely = 0.8, relwidth = 0.25, relheight = 0.08)

	main_menu = Button(root, text = "Go To Main Menu", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'))
	main_menu.place(relx = 0.1, rely = 0.8, relwidth = 0.25, relheight = 0.08)

	close = Button(root, text = "Close Application", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = exit)
	close.place(relx = 0.65, rely = 0.8, relwidth = 0.25, relheight = 0.08)

	# Closing Window
	root.mainloop()