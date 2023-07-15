import tkinter as tk
import repositoryLT as rp
import Util as u

u.showLog(__file__, None, None)


def saveUser():
    u.showLog(__file__, saveUser.__name__, None)
    rp.saveUserInfo(info=[FF_ent.get(), FF_ent2.get(), FF_ent3.get()])


userSiginWin = tk.Tk()
userSiginWin.geometry("400x300")
userSiginWin.title("LOL Teams userSignIn")
frame = tk.Frame(userSiginWin)
frame.pack()

first_frame = tk.LabelFrame(frame, text="User Info")
first_frame.grid(row=0, column=0)

FF_lab = tk.Label(first_frame, text="유저 이름")
FF_lab.grid(row=0, column=0)

FF_ent = tk.Entry(first_frame)
FF_ent.grid(row=0, column=1)

FF_lab2 = tk.Label(first_frame, text="유저 닉네임")
FF_lab2.grid(row=1, column=0)

FF_ent2 = tk.Entry(first_frame)
FF_ent2.grid(row=1, column=1)

FF_lab3 = tk.Label(first_frame, text="유저 비밀번호")
FF_lab3.grid(row=2, column=0)

FF_ent3 = tk.Entry(first_frame)
FF_ent3.config(show="*")
FF_ent3.grid(row=2, column=1)

FF_userSignIn_insert_btn = tk.Button(first_frame, text="출력")
FF_userSignIn_insert_btn.config(command=saveUser)
FF_userSignIn_insert_btn.grid(row=3, column=1)

userSiginWin.mainloop()
