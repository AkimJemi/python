import tkinter as tk
from tkinter import messagebox as msg
from PIL import ImageTk, Image
import Util as u


u.showLog(__file__, None, None)


def checkExecutionCode():
    u.showLog(__file__, checkExecutionCode.__name__, None)
    password = initEnt.get()
    if (password.__eq__("")):
        msg.showinfo(title='log-in succeed', message='Welcome to LOL Teams')
        initWin.destroy()

        import mainPage
    else:
        msg.showerror(title='log-in fail',
                      message='The entered password is incorrect')
        print('The entered password is : {}'.format(password))


initWin = tk.Tk()
initWin.geometry("450x550")
initWin.title("LOL Teams")
frame = tk.Frame(initWin)

init_img_frame = tk.LabelFrame(frame, text="test")
init_img_frame.grid(row=0, column=0)

img = ImageTk.PhotoImage(Image.open("img/img001.jpg"))
initLab1 = tk.Label(initWin, image=img)
initLab1.place(x=-2, y=-2)
initLab1.pack(fill="both", expand="yes", pady=10)

initLab2 = tk.Label(text="실행코드")
initLab2.pack()
initEnt = tk.Entry(width=10)
initEnt.place(x=10, y=10)
initEnt.pack()
initBtn = tk.Button(text="입장", width=5, height=2)


initBtn.config(command=checkExecutionCode)
initBtn.pack()
initWin.mainloop()
