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

def check_return(a, b):
	today = date.today()
	cur.execute("SELECT Book_name FROM Book_data WHERE Book_Id = (?)", (a,))
	b_name = str(cur.fetchone()[0])
	s_id = int(b)
	cur.execute("SELECT EXISTS (SELECT 1 FROM Book_1 WHERE Book_name = (?) AND Student_Id = (?))", (b_name, s_id,))
	check = int(cur.fetchone()[0])
	if check == 1:
		cur.execute("SELECT Issue_date, Fine FROM Book_1 WHERE Book_name = (?) AND Student_Id = (?)", (b_name, s_id,))
		data = cur.fetchall()[0]
		fine = float(data[1])
		i_date = str(data[0])
		i_year = int(i_date[:4])
		i_month = int(i_date[5:7])
		i_day = int(i_date[8:])
		last_date = date(i_year, i_month, i_day)
		dif = today - last_date
		dif = int(dif.days)
		if dif <= 15:
			fine += 0
		else:
			fine += dif - 15
		cur.execute("DELETE FROM Book_1 WHERE Book_name = (?) AND Student_Id = (?)", (b_name, s_id,))
		conn.commit()
	else:
		cur.execute("SELECT EXISTS (SELECT 1 FROM Book_2 WHERE Book_name = (?) AND Student_Id = (?))", (b_name, s_id,))
		check = int(cur.fetchone()[0])
		if check == 1:
			cur.execute("SELECT Issue_date, Fine FROM Book_2 WHERE Book_name = (?) AND Student_Id = (?)", (b_name, s_id,))
			data = cur.fetchall()[0]
			fine = float(data[1])
			i_date = str(data[0])
			i_year = int(i_date[:4])
			i_month = int(i_date[5:7])
			i_day = int(i_date[8:])
			last_date = date(i_year, i_month, i_day)
			dif = today - last_date
			dif = int(dif.days)
			if dif <= 15:
				fine += 0
			else:
				fine += dif - 15
			cur.execute("DELETE FROM Book_2 WHERE Book_name = (?) AND Student_Id = (?)", (b_name, s_id,))
			conn.commit()
		else:
			cur.execute("SELECT Issue_date, Fine FROM Book_3 WHERE Book_name = (?) AND Student_Id = (?)", (b_name, s_id,))
			data = cur.fetchall()[0]
			fine = float(data[1])
			i_date = str(data[0])
			i_year = int(i_date[:4])
			i_month = int(i_date[5:7])
			i_day = int(i_date[8:])
			last_date = date(i_year, i_month, i_day)
			dif = today - last_date
			dif = int(dif.days)
			if dif <= 15:
				fine += 0
			else:
				fine += dif - 15
			cur.execute("DELETE FROM Book_3 WHERE Book_name = (?) AND Student_Id = (?)", (b_name, s_id,))
			conn.commit()
	cur.execute("SELECT Fine FROM Student_record WHERE Student_Id = (?)", (s_id,))
	t_fine = float(cur.fetchone()[0])
	t_fine += fine
	cur.execute("UPDATE Student_record SET Fine = (?) WHERE Student_Id = (?)", (t_fine, s_id,))
	conn.commit()
	cur.execute("SELECT Token FROM Student_record WHERE Student_Id = (?)", (s_id,))
	token = int(cur.fetchone()[0])
	token -= 1
	cur.execute("UPDATE Student_record SET Token = (?) WHERE Student_Id = (?)", (token, s_id,))
	conn.commit()
	cur.execute("SELECT Quantity FROM Book_data WHERE Book_Id = (?)", (a,))
	quant = int(cur.fetchone()[0])
	quant += 1
	cur.execute("UPDATE Book_data SET Quantity = (?) WHERE Book_Id = (?)", (quant, a,))
	conn.commit()
	messagebox.showinfo("RETURNED", "Book has been submiited!")
	root.destroy()

def return_frame():
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

	book_id = Label(login_frame, text = "Enter Book Id : ", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	book_id.place(relx = 0.03, rely = 0.2, relwidth = 0.45, relheight = 0.2)
	b_id_entry = Entry(login_frame, bd = 5, bg = "white", font = ('courier', 20, 'bold'))
	b_id_entry.place(relx = 0.53, relwidth = 0.45, rely = 0.2, relheight = 0.2)

	std_id = Label(login_frame, text = "Enter Student Id : ", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	std_id.place(relx = 0.03, rely = 0.6, relwidth = 0.45, relheight = 0.2)
	s_id_entry = Entry(login_frame, bd = 5, bg = "white", font = ('courier', 20, 'bold'))
	s_id_entry.place(relx = 0.53, relwidth = 0.45, rely = 0.6, relheight = 0.2)

	# print(by_name_entry.get(), by_author_entry.get())

	submit = Button(root, text = "Return Book", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = lambda: check_return(int(b_id_entry.get()), int(s_id_entry.get())))
	submit.place(relx = 0.375, rely = 0.8, relwidth = 0.25, relheight = 0.08)

	main_menu = Button(root, text = "Go To Main Menu", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'))
	main_menu.place(relx = 0.1, rely = 0.8, relwidth = 0.25, relheight = 0.08)

	close = Button(root, text = "Close Application", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = exit)
	close.place(relx = 0.65, rely = 0.8, relwidth = 0.25, relheight = 0.08)

	# Closing Window
	root.mainloop()