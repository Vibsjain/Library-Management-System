# Importing Modules
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
from login import *
from librarian import *
from student import *
from add_student import *
from password import *
import sys

# Location of Database
database = "C:/Users/Vibhu/Desktop/FINAL PROJECT/library_data.db"

def exit():
	sys.exit()

# Connecting Database
conn = sqlite3.connect(database)
cur = conn.cursor()

class MainGUI:
	def __init__(self, master):
		self.master = master
		master.title("Library")

	# screen_width = master.winfo_screenwidth() 
	# screen_height = master.winfo_screenheight() 
	# master.geometry(str(screen_width) + "x" + str(screen_height))

	# # Setting Background Image
	# background_image = Image.open("library_image.jpg")
	# background_image = background_image.resize((screen_width, screen_height), Image.ANTIALIAS)
	# img = ImageTk.PhotoImage(background_image)
	# Canvas1 = Canvas(master)
	# Canvas1.create_image(screen_width / 2, screen_height / 2,image = img)      
	# Canvas1.config(bg="white",width = screen_width, height = screen_height)
	# Canvas1.pack(expand=True,fill=BOTH)

	# Creating Heading
	self.heading_frame = Frame(master, bg = "#FFC433", bd = 5)
	self.heading_frame.place(relx=0.215,rely=0.05,relwidth=0.6,relheight=0.15)
	self.heading = Label(heading_frame, text = "Welcome To Library", bg = "black", fg = "white", font = ('courier', 50, 'bold'))
	self.heading.place(relx=0,rely=0, relwidth=1, relheight=1)

	# Log In Frame
	self.login_frame_border = Frame(master, bg = "#FFC433", bd = 5)
	self.login_frame_border.place(relx = 0.315, rely = 0.3, relwidth = 0.4, relheight = 0.3)
	self.login_frame = Frame(login_frame_border, bg = "black")
	self.login_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

	# Creating Log-in buttons and labels
	self.login_label = Label(login_frame, text = "LOG IN AS", bg = "black", fg = "white", font = ('courier', 20, 'bold'))
	self.login_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.2)
	self.librarian = Button(login_frame, text = "LIBRARIAN", bg = "#FFC433", fg = "Black", font = ('courier', 15, 'bold'), bd = 5, command = lambda: login_fun(1))
	self.librarian.place(relx = 0.35, rely = 0.3, relwidth = 0.31, relheight = 0.2)
	self.student = Button(login_frame, text = "STUDENT", bg = "#FFC433", fg = "Black", font = ('courier', 15, 'bold'), bd = 5, command = lambda: login_fun(0))
	self.student.place(relx = 0.35, rely = 0.6, relwidth = 0.31, relheight = 0.2)

	# Close Application Button
	self.close = Button(master, text = "CLOSE APPLICATION", bg = "#FFC433", fg = "black", font = ('courier', 15, 'bold'), bd = 5, command = exit)
	self.close.place(relx = 0.365, rely = 0.8, relwidth = 0.3, relheight = 0.08)

root = Tk()
main_gui = MainGUI(root)
root.mainloop()

from tkinter import Tk, Label, Button, StringVar

class MyFirstGUI:
    LABEL_TEXT = [
        "This is our first GUI!",
        "Actually, this is our second GUI.",
        "We made it more interesting...",
        "...by making this label interactive.",
        "Go on, click on it again.",
    ]
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set(self.LABEL_TEXT[self.label_index])
        self.label = Label(master, textvariable=self.label_text)
        self.label.bind("<Button-1>", self.cycle_label_text)
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def cycle_label_text(self, event):
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT) # wrap around
        self.label_text.set(self.LABEL_TEXT[self.label_index])

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()