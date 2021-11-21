import smtplib

print("Enter your Email ID : ")
mo=input()
print("Enter Your Password : \n")
passw = input()
print("Enter receiver's mail ID : ")
sml = input()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(mo, passw)
server.sendmail(mo, sml, "Hi there, how's your day going?")



