import tkinter as tk
from tkinter import ttk
import repositoryLT as rp
import Util as u

u.showLog(__file__, None, None)


def checkMatchHistory():
    u.showLog(__file__, checkMatchHistory.__name__, None)


def checkTeam():
    u.showLog(__file__, checkTeam.__name__, None)
    rp.saveGameMatchTeamSetting(var.get() for var in FF_ent_list)


def insertUser():
    u.showLog(__file__, insertUser.__name__, None)
    import userSignIn


mainWin = tk.Tk()
mainWin.geometry("1000x500")
mainWin.title("LOL Teams mainPage")
frame = tk.Frame(mainWin)
frame.pack()

frame_teamA = tk.LabelFrame(frame, text="Team A")
frame_teamA.grid(row=0, column=0)

FF_ent_list = []


def setUserList():
    u.showLog(__file__, setUserList.__name__, None)
    userInfoList = rp.getUserList()
    for i in range(1, 6):
        FF_lab = tk.Label(frame_teamA, text="User{}".format(i))
        FF_lab.grid(row=0, column=i)
        FF_combobox = ttk.Combobox(
            frame_teamA, value=userInfoList, state="readonly")
        FF_combobox.grid(row=1, column=i)
        FF_ent_list.append(FF_combobox)
    FF_btn_insert_team = tk.Button(text="출력")
    FF_btn_insert_team.config(command=checkTeam)
    FF_btn_insert_team.pack()


setUserList()

FF_btn_insert_team = tk.Button(text="유저 신규등록")
FF_btn_insert_team.config(command=insertUser)
FF_btn_insert_team.pack()


mainWin.mainloop()
