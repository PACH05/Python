import pywhatkit

print("Enter Mobile number :")
nmob=input()
mob= '+91'+ nmob
print("Enter message : ")
msg= input()
print("Enter sending Time in 24 hrs format separately using Enter key :");
hrs=int(input())
min=int(input())

pywhatkit.sendwhatmsg(mob,msg,hrs,min, 10)
