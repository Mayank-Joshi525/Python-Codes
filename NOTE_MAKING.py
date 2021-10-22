import datetime
today = datetime.datetime.today().date()
timestamp = datetime.datetime.now()
print(format(f"SHORT NOTE-MAKING    											DATE:- {today}", ">80"))
f = open("note_making.txt", "r+")
f.write(format("MAYANK's Short Notes", ">70"))
j=f.tell()
f.close()
ans = "y"
file = open("note_making.txt", "a")
file.seek(j, 0)
while ans == "y" or ans == "Y":
    note = input("ENTER THE NOTE :-")
    net = note + " AT :- " + str(timestamp)
    file.write(f" \n {net}")
    ans = input("ENTER Y or y:-")
    print("CHECk THE FILE FOR YOUR NOTES IN THE [NOTE_MAKING.TXT]")
