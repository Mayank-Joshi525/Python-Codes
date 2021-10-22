# Author:- 													MAYANK JOSHI

# REMINDER PROGRAMME THAT REMINDS THE PEOPLE ABOUT THE PROMISES THEY MADE

import datetime
import os
import random
from time import sleep

from plyer import notification

date=datetime.datetime.now()
def alarm():
	while (1 == 1):
		if datetime.datetime.now().hour == timee[n][0] and datetime.datetime.now().minute == timee[n][1]:
			music_dir = "C:\\Users\\intex\\Music"
			songs = os.listdir(music_dir)
			a=random.randint(1,105)
			os.startfile(os.path.join(music_dir, songs[a]))

			notification.notify(
				title=f"REMINDER APPLICATION FOR {name}",
				message=timee[n][3],
				timeout=10,app_icon="C:\\Users\intex\\Desktop\\.ico file for python project\\reminder.ico"
			)
			break

timee = []
print(format("REMINDER APP",">70"))
print(format(f"{date}",">120"))
name=str(input("Enter the name:-"))
total_number=int(input("\nEnter your number of remainders for today  :-"))
for a in range(1,total_number+1):
	reason=input(f"\nEnter the reason for reminder {a} :-")
	ti=input('\nEnter the time in H/M/S/AM|PM format like 5/26/AM :-')
	try:
		li=ti.split('/')
		hour=int(li[0])
		real=hour
		minute=int(li[1])
		am_pm=li[2]

	except Exception as e:
		print(e)
		print("ENTER IN VALID FORMAT ")
	if am_pm == "pm" or am_pm=="PM":
		if hour < 12:
			hour = hour + 12
	elif am_pm == "am" or am_pm =="AM":
		hour = hour
	print(f"\nREMINDER {a} is at {real}:{minute}:00:{am_pm}\n")
	l=[hour, minute,am_pm,reason]
	timee.append(l)
	# print(f"{name} has {total_number} reminders for today\n")

for n in range(len(timee)):
	alarm()
	print(f"\nREMINDER {n+1} HAS BEEN DONE")
	sleep(2)
	if total_number>1:
		if total_number==n+1:
			pass
		else:
			print(f"\nREMINDER {n+2} is on it's Way")
			sleep(2)
			notification.notify(
			title=f"\nREMINDER APPLICATION FOR {name}",
			message=f"\nREMINDER {n+2} is on it's Way",app_icon="C:\\Users\intex\\Desktop\\.ico file for python project\\reminder.ico",
			timeout=10)
			alarm()
                                            
	else:
		pass
