# AUTHOR :- MAYANK JOSHI
# 							TODO LIST
# SHOULD HAVE A TEXT FILE AS TODO.TXT AOR WITH OTHER NAME
import datetime
today=datetime.datetime.today().date()
f=open("todo.txt","r+")
a=f.readlines()
f.seek(0,0)
f.write(format(f" TODO LIST of MAYANK on {today}\n", ">70"))
print(format(f"TODO LIST OF {today}",">70"))
print("\nTHE WORK FOR YOU TODAY IS :-\n")
for line in range(len(a)):
	if line==0:
		pass
	else:
		print(a[line])
deleted=[]

if len(a)==0 or len(a)==1:
	print("NOTHING TO SHOW YOU !!\n")
else:
	answer = input("\nDO YOU WANT TO CLEAN YOUR TODO LIST [Y or y ] :-")
	if answer=="Y" or answer=="y":
		print("CHOOSE FROM THE FOLLOWING:-\n"
			  " c|C - TO CLEAN ENTIRE LIST \n"
			  " o|O - TO CLEN A PARTICULAR ITEM ")
		clean=input("ENTER THE ABOVE CHOICES:-")
		if clean=="c" or clean=="C":
			f1=open("todo.txt","w")
			f1.write("")
			f.flush()
			f1.close()
		elif clean=="o" or clean=="O":
			for l in range(len(a)):
				if l==0:
					pass
				else:
					print(f"{l}:- {a[l]}")
			i=int(input("ENTER LINE TO BE DELETED:- "))
			if i>len(a):
				print("INVALID ENTRY !! ")
			elif i==0:
				pass
			else:
				if i:
					for item in range(len(a)):
						if item==0 or item==i:
							pass
						else:
							deleted.append(a[item])
				with open("todo.txt","w") as f2:
					f2.writelines("")
				f3=open("todo.txt","a")
				f3.seek(f.tell(),0)
				f3.writelines(deleted)
	else:
		pass
ans=input("DO YOU WANT TO ADD SOMETHING TO YOUR TODO LIST [Y or y ] :-")
f4=open("todo.txt","a")
i=1
while (ans=="y" or ans=="Y"):
	work=input(f"ENTER THE WORK {i} :-")
	f4.write(f"{work} \n")
	ans=input("ENTER Y or y TO CONTINUE :-")
	print("    ADDED  \n")
	i+=1

f.close()
f4.close()
