#!/usr/bin/python3

import ftplib

ftp = ftplib.FTP('')
ftp.connect("localhost",8099)
ftp.login()
ftp.cwd("sem6") #replace with your directory
ftp.retrlines("LIST")

def uploadFile():
 filename = "client.py" #replace with your file in your home folder
 ftp.storbinary("STOR "+filename, open(filename, "rb"))
 ftp.quit()

def downloadFile():
 filename = "resume.pdf" #replace with your file in the directory ('directory_name')
 localfile = open(filename, "wb")
 ftp.retrbinary("RETR " + filename, localfile.write, 1024)
 ftp.quit()
 localfile.close()

uploadFile()
# downloadFile()