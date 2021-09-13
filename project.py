#TODO												 READING A PDF FILE

import pyttsx3 # need to install
import PyPDF2 # need to install
speaker=pyttsx3.init()
speaker.setProperty("rate",-2)
book=open(r"jess404.pdf","rb") # Can be a pdf file or word document
reader=PyPDF2.PdfFileReader(book)
pages=reader.numPages
print("Total Pages ::- ",pages)
print()
for num in range(1,pages):
	page=reader.getPage(num)
	text=page.extractText()
	print(text)
	speaker.say(text)
	speaker.runAndWait()









quit()

# source code for covid managment system

print(
	"******************************************************************************************************************************************")
print(
	"*                                                                                                                                         *")
print(
	"*                                              Welcome  To  COVID-19  management  System                                                   *")
print(
	"*                                                                                                                                         *")
print(
	"*******************************************************************************************************************************************")
import pymysql

mydb = pymysql.connect(host="localhost", user="root", password='mayankjoshi')
mycursor = mydb.cursor()
mycursor.execute("create database if not exists covid_management")
mycursor.execute("use covid_management")
mycursor.execute(
	"create table if not exists staff(sno varchar(25) not null,name varchar(25) not null,age varchar(25) not null,gender char(5) not null,post varchar(25) not null,salary varchar(25) not null)")
mycursor.execute(
	"create table if not exists patients(sno varchar(25) not null,name varchar(25) not null,age varchar(25) not null,gender char(5) not null,date date not null)")
mycursor.execute("create table if not exists login(admin varchar(25) not null,password varchar(25) not null)")
mycursor.execute("create table if not exists sno(patient varchar(25) not null,staff varchar(25) not null)")
mycursor.execute("select * from sno")
z = 0
for i in mycursor:
	z = 1
if z == 0:
	mycursor.execute("insert into sno values('0','0')")
mydb.commit()
j = 0
mycursor.execute("select * from login")

for i in mycursor:
	j = 1
if (j == 0):
	mycursor.execute("insert into login values('admin','ng')")
	mydb.commit()
loop1 = 'y'
while (loop1 == 'y' or loop1 == 'Y'):
	print("--------------------------------")
	print("1.admin")
	print("2.patient")
	print("3.exit")
	print("-------------------------------")
	ch1 = int(input("enter your choice: "))
	if (ch1 == 1):
		pas = input("enter your password: ")
		mycursor.execute("select * from login")
		for i in mycursor:
			username, password = i
		if (pas == password):
			loop2 = 'n'
			while (loop2 == 'n' or loop2 == 'N'):
				print("--------------------------------")
				print("1.Add patients")
				print("2.Add staff")
				print("3.Display patients record")
				print("4.Display staff record")
				print("5.Change password")
				print("6.Remove patients")
				print("7.Remove staff")
				print("8.logout")
				print("-------------------------------")
				ch2 = int(input("enter your choice: "))
				if ch2 == 1:
					loop3 = 'y'
					while (loop3 == 'y' or loop3 == 'Y'):
						name = input("enter patients name: ")
						age = input("enter patients age: ")
						gender = input("enter patients gender(m/f): ")
						date = input("enter date of conformation of covid: ")
						mycursor.execute("select * fron sno")
						for i in mycursor:
							patient, staff = i
							patient = int(patient) + 1
						mycursor.execute("insert into patients values('" + str(
							patient) + "','" + name + "','" + age + "','" + gender + "','" + date + "')")

						mycursor.execute("update sno set patients='" + str(patient) + "'")
						mydb.commit()
						print("data of patient has been saved sucessfully............")
						mycursor.execute("select * from patients")
						t = 0
						for i in mycursor:
							t += 1
							t_id1, name1, age1, gender1, date1 = i
						print(u"total number of corona infected patients-->{patient}")
						print(u"active corona cases--> {t}")
						print(u"this patient with id {t_id} will be quarantine upto 14 days from (date1)")

						loop3 = input("do you want to add more patients(y/n): ")
					loop2 = input("do you want to logout(y/n): ")
				elif (ch2 == 2):
					loop3 = 'y'
					while (loop3 == 'y' or loop3 == 'Y'):
						name = input("enter new staff name: ")
						age = input("enter age: ")
						gender = input("enter gender(m/f): ")
						post = input("enter his/her post: ")
						salary = input("enter his/her salary: ")

						mycursor.execute("select * from sno")
						for i in mycursor:
							patient, staff = i
							staff = int(staff) + 1

						mycursor.execute("insert into staff values('" + str(
							staff) + "'),'" + name + "','" + age + "','" + gender + "','" + post + "','" + salary + "')")
						mycursor.execute("update sno set staff='" + str(staff) + "'")
						mydb.commit()
						print(u"staff with id{staff} has been saved sucessfully.............")

						mycursor.execute("select * from staff")
						t = 0
						for i in mycursor:
							t += 1

						print(u"Active staff members--> {t}")

						loop3 = input("do you want to enter more staff data(y/n): ")
					loop2 = input("do you want to logout(y/n): ")
				elif (ch2 == 3):
					idd = input("enter patient's ID: ")
					t_id2, name2, age2, gender2, date2 = ["", "", "", "", ""]
					mycursor.execute("select * from patients where sno='" + idd + "'")
					for i in mycursor:
						t_id2, name2, age2, gender2, date2 = i
					print("/ ID / NAME / AGE / GENDER / CORONA POSITIVE DATE /")
					print(u"/ {t_id2} / {name2} / {age2} / {gender2} / {date2} /")
				elif (ch2 == 4):
					idd = input("enter staff ID: ")
					t_id3, name3, age3, gender3, post3, salary3 = ["", "", "", "", ""]
					mydb.commit()
					mycursor.execute("select * from staff where sno='" + idd + "'")
					for i in mycursor:
						t_id3, name3, age3, gender3, post3, salary3 = i
					print("/ ID / NAME / AGE / GENDER / POST / SALARY/")
					print(u"/ {t_id3} / {name3} / {age3} / {gender3} / {POST} / {SALARY} /")
				elif (ch2 == 5):
					pas = input("enter old password: ")
					mycursor.execute("select * from login")
					for i in mycursor:
						username, password = i
					if (pas == password):
						npas = input("enter new password")
						mycursor.execute("update login set password='" + npas + "'")
						mydb.commit()
					else:
						print("wrong password.....")
				elif (ch2 == 6):
					loop3 = 'y'
					while (loop3 == 'y' or loop3 == 'Y'):
						idd = input("Enter patient ID: ")
						mycursor.execute("delete from patients where sno='" + idd + "'")
						mydb.commit()
						print("patient has been removed sucessfully")
						loop3 = input("do you want to remove more patients(y/n): ")

				elif (ch2 == 7):
					loop3 = 'y'
					while (loop3 == 'y' or loop3 == 'Y'):
						idd = input("Enter staff ID: ")
						mycursor.execute("delete from staff where sno='" + idd + "'")
						mydb.commit()
						print("staff has been removed sucessfully ")
						loop3 = input("do you want to remove more staff(y/n): ")
				elif (ch2 == 8):
					break
	elif (ch1 == 2):
		print("Thank you for coming forward for you COVID-19 test...... ")
		icough = input("Are you feeling cough?(y/n): ").lower()  # Y-->y or N-->n
		dry_cough = 'n'
		cough = 'n'
		if (icough == 'y' or icough == 'Y'):
			dry_cough = input("are you feeling dry cough (y/n): ").lower()
			cough = input("Are you feeling normal cough(y/n): ").lower()

		sneeze = input("Are you feeling sneeze?(y/n): ").lower()
		pain = input("Are you feeling body pain?(y/n): ").lower()
		weakness = input("Are you feeling weekness?(y/n): ").lower()
		mucus = input("Are you feeling any mucus?(y/n): ").lower()
		itemp = int(input("Please enter you temperature: "))
		if (itemp <= 100):
			temp = 'low'
		else:
			temp = 'high'
		breath = input("Are you having difficulty in breathing?(y/n): ").lower()
		if (
				dry_cough == 'y' and sneeze == 'y' and pain == 'y' and weakness == 'y' and temp == 'high' and breath == 'y'):
			print("Sorry to say but according to us you are suffering from corona virus.......:( ")
			name = input("Enter your name: ")
			age = input("Enter you age: ")
			gender = input("Enter your gender: ")

			mycursor.execute("select * from sno")
			for i in mycursor:
				patient, staff = i
				patient = int(patient) + 1
			mycursor.execute("insert into patients values('" + str(
				patient) + "','" + name + "','" + age + "','" + gender + "',now())")
			mycursor.execute("update sno set patient='" + str(patient) + "'")
			mydb.commit()
			print("Data of patient has been saved sucessfully....")
			print(u"total number of corona infected patient-->{patient}")
			mycursor.execute("select * from patients")
			t = 0
			for i in mycursor:
				t += 1
			print(u"Active corona cases--> {t}")
			mycursor.execute("select * from patients")
			for i in mycursor:
				t_id5, name5, age5, gender5, date5 = i
			print(u"this patient with id{t_id5} will be quarantine upto 14 days from {date5}")
		elif (
				dry_cough == 'y' and sneeze == 'y' and pain == 'n' and weakness == 'n' and temp == 'low' and breath == 'n'):
			print("nothing to worry,its just common cold...")
		else:
			print("you are not corona infiected ,if you are feeling something wrong you just need to take rest....")
			print("if then also you can't feel better, please consult to your doctor.")
	elif (ch1 == 3):
		break

quit()
import pymysql
mydb=pymysql.connect(password="mayankjoshi",host="localhost",user="root")
mycursor=mydb.cursor()
mycursor.execute("create database student")
quit()
# todo PROGRAMM TO CONNECT PYTHON AND MYSQL AND CREATE TABLE
import pymysql
mydb=pymysql.connect(password="mayankjoshi",host="localhost",user="root",database="CLASS_12")
mycursor=mydb.cursor()
mycursor.execute("create table STUDENT_INFO (ROLL_NO INT auto_increment not null unique,ADM_NO char(12) primary key "
				 ",NAME varchar(10),FEES char(8) DEFAULT 'PAID')")

import pyttsx3
import PyPDF2
speaker=pyttsx3.init()
speaker.setProperty("rate",165)
book=open("G:\\ALL PDF's\\CHEMISTRY BOOK CLASS 12\\lech101.pdf","rb")
reader=PyPDF2.PdfFileReader(book)
pages=reader.numPages
print(pages)
for num in range(1,pages):
	page=reader.getPage(num)
	text=page.extractText()
	print(text)
	speaker.say(text)
	speaker.runAndWait()

quit()
import pickle

f=open("file.dat","wb")
data={"Employee":"Mukesh","Id":1201,"Age":48}
pickle.dump(data,f)
quit()
f=open("C:\\Users\\intex\\Desktop\\N.txt","r")
k=f.readlines()
print(k)
longest=k[0]
for a in k:
	a.rstrip("\n")
	if len(a)>len(longest):
		longest=a
	else:
		pass
print("longest line is",longest,"with length of ",len(a))
quit()
import pickle
f=open("binary.dat","wb")
d={"name":"Mohit","Class":"12","Marks":"48"}
pickle.dump(d,f)
quit()

import pickle
f=open("binary.dat","rb")
s=pickle.load(f)
print("DATA IN YOUR BINARY FILE")
quit()
import pickle
f=open("binary.dat","wb")
d={"name":"Mohit","Class":12,"Marks":48}
pickle.dump(d,f)
quit()
print("OPENING YOUR WEBSITE")




import urllib.request
data=urllib.request.urlopen("https://timesofindia.indiatimes.com/")
# k=data.read()
print(data.getcode())
quit()


quit()
import mysql.connector as mq
mydb=mq.connect(password="mayankjoshi",host="localhost",user="root",database="student")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists CLASS_12")


quit()
import pymysql
mydb=pymysql.connect(password="mayankjoshi",host="localhost",user="root",database="class_12")
mycursor=mydb.cursor()
mycursor.execute("select student_info.Roll_no,name,Attend from student_info,Attendance "
				 "where Attendance.Roll_no=student_info.Roll_no")
d=mycursor.fetchall()
print(d)


quit()