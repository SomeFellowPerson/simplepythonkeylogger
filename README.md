# simplepythonkeylogger
A simple python keylogger script that features a black- and whitelist and an auto-mailer.

In the "CREDS.txt" file you define the e-mail and credentials as well as the mailing delay in minutes and the associated SMTP server:\
From "CREDS.txt":

Email:test@gmail.com\
Password:securepassword123\
Server:smtp.someserver.com\
Delay:20



Instructions for the other files are contained within themselves.\
The "mail.ps1" file is merely the script that will be used to mail the logger file to the email.\
The email will be the recipient as well as the sender, it is effectively emailing it self the logger file.\
The "Keylogger.py" file does not take any arguments.\
The gmail smtp server is smtp.gmail.com for other services just google it\
The required pip installations are:

-pip install pynput\
-pip install threading\
-pip install regex\
-pip install colorama
