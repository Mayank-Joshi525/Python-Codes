import time
import winsound
import win10toast # NEED TO INSTALL AS pip install win10toast
import datetime
def key():
	p = "...WAIT..."
	for a in range(len(p)):
		print(p[a], end="")
		time.sleep(0.2)
print("")
print(format("MJ WHOLESALES",">65"))
timee=str(datetime.datetime.today())
print("")

print(format(f"TIME AND DATE :- {timee}",">120"))
print("")
customer=input("CUSTOMER NAME:-")
number=int(input("ENTER TOTAL ITEMS:"))
net=0
lname={}

f = open("bank_account.txt", "r+") # CREATE BANK ACOOUNT FILE
k = f.read()
if k=="":
	old_money=0
	pass

else:
	old_money = int(k)
	f.close()
f=open("bank_account.txt","w")
for a in range(1,number+1):
	try:
		name = input(f"ENTER ITEM NAME {a} :-")
		qunatity = int(input("ENTER QUANTITY:-"))
		lname[name] = qunatity
		price = float(input("ENTER THE PRICE PER ITEM:-"))
		print("\n*********************** BILL **************************************")
		print("\nItem Name             Item Quantity               Item Price")
		print(name, "                   ", qunatity, "                    ", price)
		print("**************************************************************")
		total = qunatity * price
		net += total
		print("TOTAL AMOUNT TO BE PAID INR", total)
		print("**************************************************************")
	except Exception as e:
		print(e)

print("\n------------------------- NET BILL MJ WHOLESALE ----------------------------------------")
print("\nALL ITEMS")
print("\nITEMS  QUANTITY")
sum=0
for a in lname:
	print(a,"  ",lname[a])
	sum+=lname[a]
print("--------------------------------------")
print("TOTAL ITEMS BROUGHT ARE",sum)
print("-------------------------------------\n")

print("\nTOTAL AMOUNT TO BE PAID BY " ,customer, " IS INR",net)
print("----------------------------------------------------------------------")
print(" ")
print("                                                            PLEASE  VISIT AGAIN !!")
print("----------------------------------------------------------------------")




print("PAYMENT\n")
print("CHOOSE FROM FOLLOWING:-\n"
	  "1:-COD\n"
	  "2:CREDIT/DEBIT CARD\n"
	  "3:-ONLINE PAYMENT\n")

try:
	value=input("ENTER MODE OF PAYMENT:-")
	y=input("EXTRA COST [ y or n ] :-")
	try:
		if y=="y" or y=="Y":
			km=int(input("ENTER THE KILOMETER:-"))
			net_cost=3*km
			print("COST FOR DELIVERY ",net_cost)
		else:
			net_cost=0
	except Exception as e :
		print(e)
	real = "PAYMENT OF INR ", net + net_cost, " SUCCESSFUL!!"
	atlast = int(old_money + net + net_cost)

	if value=="1":
		print("PLEASE PAY INR",net+net_cost)
		winsound.Beep(2630, 15)
		f.write(str(atlast))
	elif value=="2":
		print("CHOOSE \nCREDIT CARD [1]\n DEBIT CARD[2]")
		card=input("CHOOSE CARD:-")
		print("ENTER YOUR CARD TO MACHINE")
		winsound.Beep(2630, 15)
		print("PLEASE WAIT.............")
		time.sleep(5)
		toaster = win10toast.ToastNotifier()
		toaster.show_toast("ALARM", f"{real}", duration=5)
		print("THANK YOU ", customer)
		f.write(str(atlast))
	elif value=="3":
		print("CHOOSE FROM FOLLOWING:-")
		print("1:-PAYTM\n2:-GOOGLE PAY\n3:-PHONE PAY\n4:-OTHERS")
		choice=input("ENTER THE CHOICE:-")
		if choice=="1" or choice=="2" or choice =="3" or choice=="4":
			print("SCAN THE CODE")
			winsound.Beep(2630, 15)
			print("PLEASE WAIT.............")
			time.sleep(5)
			toaster = win10toast.ToastNotifier()
			toaster.show_toast("MJ WHOLESALE", f"{real}", duration=5)
			print("THANK YOU ",customer)
			f.write(str(atlast))
		else:
			pass
	else:
		pass
except Exception as e:
	print(e)

