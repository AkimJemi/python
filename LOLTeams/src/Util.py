from datetime import datetime as date
from pathlib import Path as path
from inspect import currentframe as cf

init = "init"
sheetnames = ['saveGameMatchTeamSetting', 'saveUserInfo']


def showLog(py, method, msg,):
    if method == None:
        method = init
    if msg == None:
        msg = ''
    print("{} : {}. {} {}".format(date.now(), py.split('\\')[-1], method, msg))


def getPythonFileName():
    showLog(__file__, getPythonFileName.__name__, None)
    return path(__file__).name


def getCurrentMethod():
    showLog(__file__, getCurrentMethod.__name__, None)
    return cf().f_code.co_name
