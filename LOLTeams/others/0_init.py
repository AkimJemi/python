from bs4 import BeautifulSoup
import requests
from datetime import datetime
import sys
from tkinter import *


def alert():
    print(datetime.now())
    ent_p()


win = Tk()
win.geometry("1000x500")
win.title("LOL Teams")
req = requests.get(url="https://python.bakyeono.net/chapter-1-3.html")
soup = BeautifulSoup(req.text, "html.parser")


def ent_p():
    a = ent.get()
    print(a)


# Label
lab = Label(win)
img = PhotoImage(
    file="C:/Users/wowp1/Desktop/laptop_github/ufc/img/download.png", master=win)
lab.config(image=img)
lab.pack()
result = soup.find("div", attrs={"class", "draft-warning"}).text
print(result)
ent = Entry(win)
ent2 = Entry(win)
ent2.config(show="*")


def clear(event):
    ent2.delete(0, ent2.get())


ent2.insert(0, "temp@naver.com")
ent2.delete(0, 3)
ent2.bind("<Button-1>", clear)
ent2.pack()

# win.option_add("*Font", "맑은고 25")
btn = Button(win, text="입장", width=10, height=3,)
btn.config(command=alert)


ent.pack()
btn.pack()
win.mainloop()
