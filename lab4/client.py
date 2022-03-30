#!/usr/bin/python3

import ftplib

ftp = ftplib.FTP('')
ftp.connect("localhost",8099)
ftp.login()
ftp.cwd(".") # current directory in the FTP server
ftp.retrlines("LIST")

# upload exapmle1.txt to the FTP server
filename = "example1.txt" # upload this file from current directory
ftp.storbinary("STOR " + filename, open(filename, "rb"))

# download example2.txt from the FTP server
filename = "example2.txt" # downlod this file from cwd in the FTP server
localfile = open(filename, "wb")
ftp.retrbinary("RETR " + filename, localfile.write, 1024)
ftp.quit()
localfile.close()