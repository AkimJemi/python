from tkinter import *
from tkinter import filedialog as fd


def open_file():
    result = fd.askopenfile(initialfile="/", title="test", filetypes=(("txt files", ".txt"), ("all files", "*.*")))
    print(f"file name : {result.name}")


# path: str = fd.askopenfilename()
# print(path)
root = Tk()

button = Button(root, text="open file", command=open_file)
button.pack()
root.geometry("300x300")
root.mainloop()
# f = open("C:/Users/wowp1/Desktop/test.txt", "r")
# print(f)
# from tkinter import *
# from tkinter import filedialog
# from tkinter import ttk
#
#
# def button1_clicked():
#     file = filedialog.askopenfile(initialdir='~/')
#     if file:
#         v1.set(file.name)
#         contents = file.read()
#         print(contents)
#         file.close()
#
#
# def button2_clicked():
#     file_name = filedialog.askopenfilename(initialdir='~/')
#     if file_name:
#         v2.set(file_name)
#
#
# if __name__ == "__main__":
#     root = Tk()
#     root.title('Dialogs')
#     root.columnconfigure(0, weight=1)
#     root.rowconfigure(0, weight=1)
#
#     frame = ttk.Frame(root, padding=10)
#     frame.columnconfigure(0, weight=1)
#     frame.rowconfigure(0, weight=1)
#     frame.grid(sticky=(N, W, S, E))
#
#     # Open File
#     b1 = ttk.Button(
#         frame, text='Open File', width=15,
#         command=button1_clicked)
#     b1.grid(row=0, column=0, sticky=(W))
#     v1 = StringVar()
#     l1 = ttk.Label(frame, textvariable=v1)
#     l1.grid(row=0, column=1)
#
#     # Open File
#     b2 = ttk.Button(
#         frame, text='Open Filename', width=15,
#         command=button2_clicked)
#     b2.grid(row=1, column=0, sticky=(W))
#     v2 = StringVar()
#     l2 = ttk.Label(frame, textvariable=v2)
#     l2.grid(row=1, column=1)
#
#     root.mainloop()