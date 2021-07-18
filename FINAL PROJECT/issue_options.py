from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image 
from datetime import date
import datetime
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

def check_issue(a, b):
	cur.execute("SELECT EXISTS (SELECT 1 FROM Book_data WHERE Book_Id = (?))", (a,))
	data1 = int(cur.fetchone()[0])
	cur.execute("SELECT EXISTS (SELECT 1 FROM Student_record WHERE Student_Id = (?))", (b,))
	data2 = int(cur.fetchone()[0])
	if (data1 == 1) and (data2 == 1):
		cur.execute("SELECT Token FROM Student_record WHERE Student_Id = (?)", (b,))
		token = int(cur.fetchone()[0])
		cur.execute("SELECT Quantity FROM Book_data WHERE Book_Id = (?)", (a,))
		quan = int(cur.fetchone()[0])

		if token == 3:
			messagebox.showinfo("FULL", "You have already issued maximum number of books!")
			root.destroy()
		elif quan == 0:
			messagebox.showinfo("OUT OF STOCK", "Book is currently unavailable!")
			root.destroy()
		else:
			cur.execute("SELECT Book_name FROM Book_data WHERE Book_Id = (?)", (a,))
			b_name = str(cur.fetchone()[0])
			today = date.today()
			cur.execute("SELECT Student_Id, Student_name FROM Student_record WHERE Student_Id = (?)", (b,))
			data = cur.fetchall()[0]
			s_id = int(data[0])
			s_name = str(data[1])
			reissues = 0
			fine = 0.0
			if token == 0:
				cur.execute("INSERT INTO Book_1 VALUES (?, ?, ?, ?, ?, ?)", (s_id, s_name, b_name, str(today), reissues, fine,))
				conn.commit()
			elif token == 1:
				cur.execute("SELECT EXISTS (SELECT 1 FROM Book_1 WHERE Student_Id = (?))", (s_id,))
				data = int(cur.fetchone()[0])
				if data == 1:
					cur.execute("INSERT INTO Book_2 VALUES (?, ?, ?, ?, ?, ?)", (s_id, s_name, b_name, str(today), reissues, fine,))
					conn.commit()
				else:
					cur.execute("INSERT INTO Book_1 VALUES (?, ?, ?, ?, ?, ?)", (s_id, s_name, b_name, str(today), reissues, fine,))
					conn.commit()
			elif token == 2:
				cur.execute("SELECT EXISTS (SELECT 1 FROM Book_1 WHERE Student_Id = (?))", (s_id,))
				data1 = int(cur.fetchone()[0])
				cur.execute("SELECT EXISTS (SELECT 1 FROM Book_2 WHERE Student_Id = (?))", (s_id,))
				data2 = int(cur.fetchone()[0])
				if data1 == 0:
					cur.execute("INSERT INTO Book_1 VALUES (?, ?, ?, ?, ?, ?)", (s_id, s_name, b_name, str(today), reissues, fine,))
					conn.commit()
				elif data2 == 0:
					cur.execute("INSERT INTO Book_2 VALUES (?, ?, ?, ?, ?, ?)", (s_id, s_name, b_name, str(today), reissues, fine,))
					conn.commit()
				else:
					cur.execute("INSERT INTO Book_3 VALUES (?, ?, ?, ?, ?, ?)", (s_id, s_name, b_name, str(today), reissues, fine,))
					conn.commit()
			token = token + 1
			quan -= 1
			cur.execute("UPDATE Student_record SET Token = (?) WHERE Student_Id = (?)", (token, b,))
			conn.commit()
			cur.execute("UPDATE Book_data SET Quantity = (?) WHERE Book_Id = (?)", (quan, a,))
			conn.commit()
			messagebox.showinfo("ISSUED", "Book Issued Successfully!")
			root.destroy()


	elif data1 != 1:
		messagebox.shoerror("NOT FOUND", "Book Not Found!")
		root.destroy()

	elif data2 != 1:
		messagebox.shoerror("NOT FOUND", "Student Record Not Found!")
		root.destroy()

def issue_book():
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

	submit = Button(root, text = "Issue Book", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = lambda: check_issue(int(b_id_entry.get()), int(s_id_entry.get())))
	submit.place(relx = 0.375, rely = 0.8, relwidth = 0.25, relheight = 0.08)

	main_menu = Button(root, text = "Go To Main Menu", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'))
	main_menu.place(relx = 0.1, rely = 0.8, relwidth = 0.25, relheight = 0.08)

	close = Button(root, text = "Close Application", bg = "#FFC433", fg = "black", bd = 5, font = ('courier', 20, 'bold'), command = exit)
	close.place(relx = 0.65, rely = 0.8, relwidth = 0.25, relheight = 0.08)

	# Closing Window
	root.mainloop()