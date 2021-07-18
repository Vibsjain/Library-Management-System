from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image 
import sqlite3
from view_books import *
import sys

def exit():
	sys.exit()

# Location of Database
database = "C:/Users/91997/Desktop/FINAL PROJECT/library_data.db"
# Connecting Database
global conn, cur, data, datalist
conn = sqlite3.connect(database)
cur = conn.cursor()
datalist = []

cur.execute("SELECT DISTINCT Department FROM Book_data ORDER BY Department")
data = cur.fetchall()

for i in data:
	datalist.append(i[0])

def go_to_view(a):
	root.destroy()
	fetch_data(a)

def show_dep():
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
	login_frame_border.place(relx = 0.265, rely = 0.25, relwidth = 0.5, relheight = 0.3)
	login_frame = Frame(login_frame_border, bg = "black")
	login_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

	choose_dep = Label(login_frame, text = "CHOOSE DEPARTMENT", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	choose_dep.place(relx = 0, rely = 0.2, relwidth = 1, relheight = 0.2)

	check = StringVar(root)
	dep = OptionMenu(login_frame, check, *datalist)
	dep.config(text = check.get(), bg = "white", fg = "black" , font = ('courier', 20, 'bold'), bd = 5)
	dep.place(relx = 0.25, rely = 0.5, relwidth = 0.5, relheight = 0.2)

	# dep_place = Label(login_frame, text = check.get(), bg = "black", fg = "white", font = ('courier', 20, 'bold'))

	submit = Button(root, text = "View Books", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = lambda: go_to_view(check.get()))
	submit.place(relx = 0.375, rely = 0.8, relwidth = 0.25, relheight = 0.08)

	main_menu = Button(root, text = "Go To Main Menu", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'))
	main_menu.place(relx = 0.1, rely = 0.8, relwidth = 0.25, relheight = 0.08)

	close = Button(root, text = "Close Application", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = exit)
	close.place(relx = 0.65, rely = 0.8, relwidth = 0.25, relheight = 0.08)

	# Closing Window
	root.mainloop()