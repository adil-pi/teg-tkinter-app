from tkinter import *
import os
import webbrowser

def open_paint():
    os.system("mspaint")

def open_youtube():
    webbrowser.open("https://www.youtube.com/")



root = Tk()
root.title("mortis song tutorial")
root.geometry("400x300")


btn1 = Button(text="Открыть Paint", command=open_paint)
btn2 = Button(text="Открыть Youtube", command=open_youtube)

btn1.pack(pady=10)
btn2.pack(pady=10)

root.mainloop()