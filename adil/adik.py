# Импортируем tkinter в проект
from tkinter import *

def calk():
    val1 = entry1.get()
    val2 = entry2.get()
    val3 = entry3.get()
    print(val1, val2, val3)

    if val1 == '' or val2 == '' or val3 == '':
        txt["text"] = 'Заполните все поля!'
        txt['bg'] = '#f51111'
        return
    else:
        if val2 != '+' and val2 != "/" and val2 != '*' and val2 != "-":
            txt["text"] = "Неверная операция!"
            txt["bg"] = '#bda668'
        else:
            if val2 == '+':
                txt["text"] = float(val1) + float(val3)
                txt["bg"] = '#33f511'
            elif val2 == '-':
                txt["text"] = float(val1) - float(val3)
                txt["bg"] = '#33f511'
            elif val2 == '/':
                txt["text"] = float(val1) - float(val3)
                txt["bg"] = '#33f511'
            elif val2 == '+':
                txt["text"] = float(val1) - float(val3)
                txt["bg"] = '#33f511'


root = Tk()
root.title("dynomike song tutorial")
root.geometry("495x300")
root.configure(bg="#ffffff")

frame = Frame(root)
frame.pack(anchor="center")



lab1 = Label(frame, text='Число', font=('Comic Sans MS', 12))
lab2 = Label(frame, text='Операция', font=('Comic Sans MS', 12))
lab3 = Label(frame, text='Число', font=('Comic Sans MS', 12))
entry1 = Entry(frame, font=('Comic Sans MS', 12), width=14)
entry2 = Entry(frame, font=('Comic Sans MS', 12), width=14)
entry3 = Entry(frame, font=('Comic Sans MS', 12), width=14)
btn = Button(frame, text="Вычислить", font=('Comic Sans MS', 12), bg="#84e8d7", fg="#f5050d",  command=calk)
txt = Label(frame, text="")


lab1.grid(row=0, column=0, padx=10, pady=10)
lab2.grid(row=0, column=1, padx=10, pady=10)
lab3.grid(row=0, column=2, padx=10, pady=10)

entry1.grid(row=1, column=0, padx=10, pady=10)
entry2.grid(row=1, column=1, padx=10, pady=10)
entry3.grid(row=1, column=2, padx=10, pady=10)
btn.grid(row=2, columnspan=3, sticky='we', padx=10, pady=10)
txt.grid(row=3, columnspan=3, sticky='we', padx=10, pady=10)




root.mainloop()