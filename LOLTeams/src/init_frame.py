import tkinter as tk
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import sys
from PIL import ImageTk, Image



def checkExecutionCode():
    if (initEnt.get().__eq__("")):
        initWin.destroy()
        import mainPage
    else:
        print(False)


print("init")
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


# def mainPage():
# mainWin = tk.Tk()
# mainWin.geometry("1000x500")
# mainWin.title("LOL Teams mainPage")
# tk.Label(text="시작").pack()
# ent = tk.Entry(width=10)
# ent.pack()
# btn = tk.Button(text="입장", width=10, height=3)
# btn.config(command=checkMatchHistory)
# btn.pack()
# mainWin.mainloop()


# MainPage
# class mainPage:
#     mainWin = tk.Tk()
#     mainWin.geometry("1000x500")
#     mainWin.title("LOL Teams mainPage")
#     tk.Label(text="시작").pack()
#     ent = tk.Entry(width=10)
#     ent.pack()
#     btn = tk.Button(text="입장", width=10, height=3)
#     btn.config(command=checkMatchHistory)
#     btn.pack()
#     mainWin.mainloop()


# Button(text="입장").grid(column=1, row=1, pady=10, padx=20)


# req = requests.get(url="https://python.bakyeono.net/chapter-1-3.html")
# soup = BeautifulSoup(req.text, "html.parser")


# def ent_p():
#     a = ent.get()
#     print(a)


# # Label
# lab = Label(win)
# img = PhotoImage(
#     file="C:/Users/wowp1/Desktop/laptop_github/ufc/img/download.png", master=win)
# lab.config(image=img)
# lab.pack()
# result = soup.find("div", attrs={"class", "draft-warning"}).text
# print(result)
# ent = Entry(win)
# ent2 = Entry(win)
# ent2.config(show="*")


# def clear(event):
#     ent2.delete(0, ent2.get())


# ent2.insert(0, "temp@naver.com")
# ent2.delete(0, 3)
# ent2.bind("<Button-1>", clear)
# ent2.pack()

# # win.option_add("*Font", "맑은고 25")
# btn = Button(win, text="입장", width=10, height=3,)
# btn.config(command=alert)


# ent.pack()
# btn.pack()
