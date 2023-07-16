import tkinter as tk
from tkinter import ttk
import repositoryLT as rp
import Util as u
u.showLog(__file__, None, None)


mainWin = tk.Tk()
mainWin.geometry("1000x500")
mainWin.title(u.getTitle(__file__))
frame = tk.Frame(mainWin)
frame.pack()


def checkMatchHistory():
    u.showLog(__file__, checkMatchHistory.__name__, None)


def setUserList(teamName, num):
    frame_team = tk.LabelFrame(frame, text=teamName)
    frame_team.grid(row=num-1, column=1)
    FF_ent_list = []
    u.showLog(__file__, setUserList.__name__, None)
    userInfoList = rp.getUserList()
    for i in range(1, 6):
        FF_lab = tk.Label(frame_team, text="User{}".format(i))
        FF_lab.grid(row=num*2-1, column=i)
        FF_combobox = ttk.Combobox(
            frame_team, value=userInfoList, state="readonly")
        FF_combobox.grid(row=num*2, column=i)
        FF_ent_list.append(FF_combobox)

    def checkTeam():
        u.showLog(__file__, checkTeam.__name__, None)
        rp.saveGameMatchTeamSetting([var.get() for var in FF_ent_list])
    FF_btn_insert_team = tk.Button(frame_team, text="출력")
    FF_btn_insert_team.grid(row=num*2, column=7)
    FF_btn_insert_team.config(command=checkTeam)


setUserList(teamName="Team A", num=1)
setUserList(teamName="Team B", num=2)


def insertUser():
    mainWin.destroy()
    u.showLog(__file__, insertUser.__name__, None)
    import userSignIn as user


frame_team_leftside = tk.LabelFrame(frame, text="Label")
frame_team_leftside.grid(row=0, column=2)
FF_btn_insert_team = tk.Button(frame_team_leftside, text="신규등록")
FF_btn_insert_team.grid(row=1, column=1)
FF_btn_insert_team.config(command=insertUser)


def initializeDB():
    from initializeDB import initializeDB
    initializeDB()
    mainWin.destroy()
    import mainPage


FF_btn_initialize_DB = tk.Button(frame_team_leftside, text="정보 초기화")
FF_btn_initialize_DB.grid(row=2, column=1)
FF_btn_initialize_DB.config(command=initializeDB)

mainWin.mainloop()
