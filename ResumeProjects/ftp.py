import ftplib
import shutil

FTP_HOST = "192.68.228.70"
FTP_USER = "xeroxts"
FTP_PASS = "efi4XEROX"

# connect to the FTP server
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
# force UTF-8 encoding
ftp.encoding = "utf-8"
# the name of file you want to download from the FTP server
filename = "120.57_.pdf"
with open(filename, "wb") as file:
    # use FTP's RETR command to download the file
    ftp.retrbinary(f"RETR {filename}", file.write)
# quit and close the connection
ftp.quit()

Source = r'C:\Users\karthikb\PycharmProjects\ResumeProjects\120.57_.pdf'
Destination = r'\\basqa\basqa\My_Space\Karthik\Sample'
shutil.copy(Source, Destination)
