from datetime import datetime as date
from pathlib import Path as path
from inspect import currentframe as cf
from tkinter import messagebox as msg

init = "init"
dbFileName = "db/db.xlsx"
sheetnames = ['saveGameMatchTeamSetting', 'saveUserInfo']


def showinfo(title, message):
    msg.showinfo(title=title, message=message)


def showerror(title, message):
    msg.showerror(title=title, message=message)


def showLog(py, method, msg,):
    if method == None:
        method = init
    if msg == None:
        msg = ''
    print("{} : {} . {} {}".format(
        date.now(), py.split('\\')[-1], "{}()".format(method), msg))


def getTitle(file):
    return file.split('\\')[-1].split('.')[0]


def getPythonFileName():
    showLog(__file__, getPythonFileName.__name__, None)
    return path(__file__).name


def getCurrentMethod():
    showLog(__file__, getCurrentMethod.__name__, None)
    return cf().f_code.co_name
