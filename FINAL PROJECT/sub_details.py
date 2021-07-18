from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image 
import sqlite3
from datetime import date 
import datetime
import sys

def exit():
	sys.exit()

# Location of Database
database = "C:/Users/91997/Desktop/FINAL PROJECT/library_data.db"
# Connecting Database
global conn, cur
conn = sqlite3.connect(database)
cur = conn.cursor()

def cal_fine(data, a):
	global today
	today = date.today()
	cur.execute("SELECT Fine FROM Student_record WHERE Student_Id = (?)", (int(a), ))
	t_fine = float(cur.fetchone()[0])
	for i in data:
		t_fine += float(i[2])
		i_year = int(i[1][:4])
		i_month = int(i[1][5:7])
		i_day = int(i[1][8:])
		last_date = date(i_year, i_month, i_day)
		dif = today - last_date
		dif = int(dif.days)
		if dif <= 15:
			fine = 0
		else:
			fine = dif - 15
		t_fine += fine
	return t_fine

def show_sub(data, b):
	book = []
	i_d = []
	r_d = []
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
	book_name = Label(root, text = "Book Name", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	book_name.place(relx = 0.02, relwidth = 0.5, rely = 0.25, relheight = 0.03)

	i_date = Label(root, text = "Issue Date", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	i_date.place(relx = 0.55, relwidth = 0.15, rely = 0.25, relheight = 0.03)

	r_date = Label(root, text = "Submission Date", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	r_date.place(relx = 0.73, relwidth = 0.18, rely = 0.25, relheight = 0.03)

	underscore = Label(root, text = "-" * 300, bg = "black", fg = "white")
	underscore.place(relx = 0, relwidth = 1, rely = 0.28, relheight = 0.03)

	j = 0
	for i in data:
		book.append(Label(root, text = i[0], bg = "black", fg = "white", font = ('courier', 15, 'bold')))
		i_d.append(Label(root, text = i[1], bg = "black", fg = "white", font = ('courier', 15, 'bold')))
		r_d.append(Label(root, text = i[3], bg = "black", fg = "white", font = ('courier', 15, 'bold')))
		book[j].place(relx = 0.02, relwidth = 0.5, rely = 0.34 + j * 0.05, relheight = 0.04)
		i_d[j].place(relx = 0.55, relwidth = 0.15, rely = 0.34 + j * 0.05, relheight = 0.04)
		r_d[j].place(relx = 0.73, relwidth = 0.18, rely = 0.34 + j * 0.05, relheight = 0.04)
		j += 1

	fine_label = Label(root, text = "Total Fine", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	fine_label.place(relx = 0, relwidth = 1, rely = 0.6, relheight = 0.03)
	print_price = Label(root, text = b, bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	print_price.place(relx = 0, relwidth = 1, rely = 0.65, relheight = 0.03)

	main_menu = Button(root, text = "Go To Main Menu", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'))
	main_menu.place(relx = 0.18, rely = 0.82, relwidth = 0.3, relheight = 0.08)

	close = Button(root, text = "Close Application", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = exit)
	close.place(relx = 0.52, rely = 0.82, relwidth = 0.3, relheight = 0.08)

	# Closing Window
	root.mainloop()

def fetch_d(a):
	cur.execute("SELECT Token FROM Student_record WHERE Student_Id = (?)", (int(a),))
	token = int(cur.fetchone()[0])
	data = []
	if token == 0:
		messagebox.showinfo("NO BOOKS", "No Books Issued")
		root.destroy()
	if token >= 1:
		cur.execute("SELECT Book_name, Issue_date, Fine FROM Book_1 WHERE Student_Id = (?)", (int(a), ))
		data.append(list(cur.fetchall()[0]))
	if token >= 2:
		cur.execute("SELECT Book_name, Issue_date, Fine FROM Book_2 WHERE Student_Id = (?)", (int(a), ))
		data.append(list(cur.fetchall()[0]))
	if token == 3:
		cur.execute("SELECT Book_name, Issue_date, Fine FROM Book_3 WHERE Student_Id = (?)", (int(a), ))
		data.append(list(cur.fetchall()[0]))
	for i in range(len(data)):
		d = data[i][1]
		i_year = int(d[:4])
		i_month = int(d[5:7])
		i_day = int(d[8:])
		l_d = date(i_year, i_month, i_day)
		l_d += datetime.timedelta(days = 15)
		data[i].append(str(l_d))

	t_fine = cal_fine(data, a)
	show_sub(data, t_fine)