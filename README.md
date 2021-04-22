# simplepythonkeylogger
A simple python keylogger script that features a black- and whitelist and an auto-mailer.

In the "useList.txt" file you define if you are gonna use a black or whitelist. The chosen option should be written in between the hashtags:
From useList.txt:

Using:           
#########
blacklist
#########
(Replace blacklist with whitelist if you want to use whitelist and vice versa)

OR

Using:           
#########
whitelist
#########
(Replace blacklist with whitelist if you want to use whitelist and vice versa)




In the "whitelist.txt" or "blacklist.txt" file you define what keys you want to be concerned:
From "whitelist.txt":

IF THIS LIST IS CHOSEN ONLY THE KEYS IN THIS LIST WILL BE LOGGED. USE FORMAT: Key.code (e.g. Key.esc or a or z) AND A NEW LINE FOR EACH KEY --> https://pynput.readthedocs.io/en/latest/keyboard.html
###########################################################################################################################################################################################
Key.esc
Key.alt
a
z
c
h
b
n
d
Key.ctrl_r



In the "CREDS.txt" file you define the e-mail and credentials as well as the mailing delay in minutes and the associated SMTP server:
From "CREDS.txt":

Email:test@gmail.com
Password:securepassword123
Server:smtp.someserver.com
Delay:20



The "mail.ps1" file is merely the script that will be used to mail the logger file to the email.
The email will be the recipient as well as the sender, it is effectively emailing it self the logger file.
The "Keylogger.py" file does not take any arguments.
