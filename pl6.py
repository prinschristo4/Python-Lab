import smtplib

fromaddr = "b.prince.christopher98@gmail.com"
toaddr = "princebommaji@gmail.com"

msg = "Hello this is my mail by python"

server = smtplib.SMTP("smtp.gmail.com:985")
server.starttls()
server.login(fromaddr, "Chin2bro")
server.sendmail(fromaddr, toaddr, msg)
