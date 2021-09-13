# Author :- Mayank Joshi

# todo 								CREATING A FEEDBACK FORM

from tkinter import * # pre installed
import pyautogui # need too install as pip install pyautogui
import datetime # pre- installed
def simple():
	# pyautogui.alert("THANK YOU,YOUR FEEDBACK HAS BEEN SUBMITTED.","FEDDBACK FORM")
	name = entry_1.get()
	email = entry_2.get()
	gender = var.get()
	if gender == 1:
		gender = "MALE"
	else:
		gender = "FEMALE"
	country = c.get()
	rate = va.get()
	date = datetime.datetime.now()
	feedback = text_editor.get(1.0, "end")
	print(f"DATE:-{date}\nNAME:-{name}\nEMAIL:-{email}\nGENDER:-{gender}\n"
		  f"COUNTRY:-{country}\nRATE:-{rate}\nFEEDBACK:-{feedback}")

root=Tk()
root.geometry('1200x1000')
root.title("FEEDBACK FORM")

label_0 = Label(root, text="FEEDBACK FORM", width=20, font=("bold", 35), bg="yellow", fg="red")
label_0.place(x=620, y=5)

label_1 = Label(root, text="Full Name", width=20, font=("bold", 25), bg="orange")
label_1.place(x=670, y=150)

entry_1 = Entry(root, font="bold 25")
entry_1.place(x=1200, y=150)

label_2 = Label(root, text="Email", width=20, font=("bold", 25), bg="white", fg="dark blue")
label_2.place(x=670, y=220)

entry_2 = Entry(root, font="bold 25")
entry_2.place(x=1200, y=220)

label_3 = Label(root, text="Gender", width=20, font=("bold", 25), bg="green")
label_3.place(x=670, y=280)
var = IntVar()
Radiobutton(root, text="Male", padx=5, variable=var, value=1, font=("bold", 15)).place(x=1500, y=280)
Radiobutton(root, text="Female", padx=20, variable=var, value=2, font=("bold", 15)).place(x=1200, y=280)

label_4 = Label(root, text="Country", width=20, font=("bold", 25), bg="orange")
label_4.place(x=670, y=350)

list1 = ['Afganisthan', 'Bangladesh', 'Canada', 'China', 'France', 'Germany', 'India', 'Mexico', 'Malaysia'
	, 'Nepal', 'Pakistan', 'Switzerland', 'USA'];
c = StringVar()
droplist = OptionMenu(root, c, *list1)
droplist.config(width=15, font=("bold", 15))
c.set('Select your country')
droplist.place(x=1200, y=350)

label_5 = Label(root, text="RATE US", width=20, font=("bold", 25), bg="green")
label_5.place(x=670, y=450)
va = Scale(root, from_=0, to=5, orient=HORIZONTAL, font="Algerian 35 bold")
va.place(x=1200, y=450)
va.set(0)

Button(root, text='Submit', width=20, bg='brown', fg='white', font=("bold", 15),command=simple).place(x=850, y=620)

status_bars = Label(root, text="Status bar", font="lucida 15 bold", bg="yellow", fg="blue")
status_bars.pack(side=BOTTOM)

Label(root, text="ENTER YOUR VALUABLE FEEDBACK :)", font="lucida 15 bold").place(x=80, y=30)
text_editor = Text(root, font="lucida 11", pady=50)
text_editor.config(wrap="word", relief=SUNKEN)
text_editor.place(x=14, y=65)

Button(root, text='DEVELOPER', width=20, bg='red', fg='green', font=("bold", 25)) \
.place(x=1120, y=730)

text_change = False

def change_word(event=None):
		global text_change
		if text_editor.edit_modified():
			text_change = True
			word = len(text_editor.get(1.0, "end-1c").split())
			chararcter = len(text_editor.get(1.0, "end-1c").replace(" ", ""))
			status_bars.config(text=f"Character :{chararcter} Word :{word}")
		text_editor.edit_modified(False)

text_editor.bind("<<Modified>>", change_word)
text_change = False

root.mainloop()
quit()




