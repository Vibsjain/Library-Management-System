from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image 
import sqlite3
from reissue import *
from issue_options import *
from return_book import *
import sys

def exit():
	sys.exit()

# Location of Database
database = "C:/Users/91997/Desktop/FINAL PROJECT/library_data.db"
# Connecting Database
global conn, cur
conn = sqlite3.connect(database)
cur = conn.cursor()

def show_option():
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
	issue = Button(login_frame, text = "Issue Book", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = issue_book)
	issue.place(relx = 0.15, rely = 0.18, relwidth = 0.7, relheight = 0.2)

	reissue = Button(login_frame, text = "Reissue Book", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = reissue_here)
	reissue.place(relx = 0.15, rely = 0.40, relwidth = 0.7, relheight = 0.2)

	ret = Button(login_frame, text = "Return Book", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = return_frame)
	ret.place(relx = 0.15, rely = 0.62, relwidth = 0.7, relheight = 0.2)

	main_menu = Button(root, text = "Go To Main Menu", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'))
	main_menu.place(relx = 0.18, rely = 0.82, relwidth = 0.3, relheight = 0.08)

	close = Button(root, text = "Close Application", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = exit)
	close.place(relx = 0.52, rely = 0.82, relwidth = 0.3, relheight = 0.08)

	# Closing Window
	root.mainloop()