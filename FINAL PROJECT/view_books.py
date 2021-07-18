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

def fetch_data(a):
	global data
	cur.execute('''
		SELECT 
				Book_Id,
				Book_name,
				Author_name,
				Quantity
			FROM 
				Book_data
			WHERE
				Department = (?)
		''', (a,))
	data = cur.fetchall()
	view_book_for(data)

def view_book_for(data):
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

		# Creating Heading for Book Search
	book_id = Label(root, text = "Book Id", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	book_id.place(relx = 0.05, relwidth = 0.1, rely = 0.02, relheight = 0.03)

	book_name = Label(root, text = "Name", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	book_name.place(relx = 0.32, relwidth = 0.1, rely = 0.02, relheight = 0.03)

	book_author = Label(root, text = "Author", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	book_author.place(relx = 0.64, relwidth = 0.1, rely = 0.02, relheight = 0.03)

	book_quantity = Label(root, text = "Quantity", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	book_quantity.place(relx = 0.85, relwidth = 0.1, rely = 0.02, relheight = 0.03)

	underscore = Label(root, text = "-" * 300, bg = "black", fg = "white")
	underscore.place(relx = 0, relwidth = 1, rely = 0.05, relheight = 0.03)

	j = 0
	for i in data:
		# print(i)
		label_id.append(Label(root, text = i[0], bg = "black", fg = "white", font = ('courier', 15, 'bold')))
		label_name.append(Label(root, text = i[1], bg = "black", fg = "white", font = ('courier', 15, 'bold')))
		label_author.append(Label(root, text = i[2], bg = "black", fg = "white", font = ('courier', 15, 'bold')))
		label_quantity.append(Label(root, text = i[3], bg = "black", fg = "white", font = ('courier', 15, 'bold')))
		label_id[j].place(relx = 0.05, relwidth = 0.1, rely = 0.1 + j * 0.03, relheight = 0.02)
		label_name[j].place(relx = 0.17, relwidth = 0.4, rely = 0.1 + j * 0.03, relheight = 0.02)
		label_author[j].place(relx = 0.59, relwidth = 0.25, rely = 0.1 + j * 0.03, relheight = 0.02)
		label_quantity[j].place(relx = 0.85, relwidth = 0.1, rely = 0.1 + j * 0.03, relheight = 0.02)
		j += 1

	main_menu = Button(root, text = "Go To Main Menu", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'))
	main_menu.place(relx = 0.18, rely = 0.82, relwidth = 0.3, relheight = 0.08)

	close = Button(root, text = "Close Application", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = exit)
	close.place(relx = 0.52, rely = 0.82, relwidth = 0.3, relheight = 0.08)

	# Closing Window
	root.mainloop()