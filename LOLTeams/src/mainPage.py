import tkinter as tk
from tkinter import ttk
import repositoryLT as rp


def checkMatchHistory():
    print("checkMatchHistory")


def checkTeam():
    rp.saveGameMatchTeamSetting(FF_ent_list)


mainWin = tk.Tk()
mainWin.geometry("1000x500")
mainWin.title("LOL Teams mainPage")
frame = tk.Frame(mainWin)
frame.pack()

first_frame = tk.LabelFrame(frame, text="Team A")
first_frame.grid(row=0, column=0)

FF_ent_list = []
userInfoList = rp.getUserList()
for i in range(1, 6):
    FF_lab = tk.Label(first_frame, text="User{}".format(i))
    FF_lab.grid(row=0, column=i)
    FF_combobox = ttk.Combobox(first_frame, value=userInfoList)
    FF_combobox.grid(row=1, column=i)
    # FF_ent = tk.Entry(first_frame)
    # FF_ent.grid(row=1, column=i)
    FF_ent_list.append(FF_combobox)


FF_btn_insert_team = tk.Button(text="출력")
FF_btn_insert_team.config(command=checkTeam)
FF_btn_insert_team.pack()


def insertUser():
    import userSignIn


FF_btn_insert_team = tk.Button(text="유저 신규등록")
FF_btn_insert_team.config(command=insertUser)
FF_btn_insert_team.pack()


mainWin.mainloop()
