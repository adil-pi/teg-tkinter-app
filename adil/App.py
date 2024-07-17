from tkinter import *

def get_entry():
    value = int(entry.get())
    value2 = int(entry2.get())
    txt["text"] = value + value2
    




root = Tk()
root.title("dynomike song tutorial")
root.geometry("400x400")


entry = Entry()
entry.pack()

entry2 = Entry()
entry2.pack()



txt = Label(text="New text...")
txt.pack()

btn = Button(text="Click me!", command=get_entry)
btn.pack()





root.mainloop()

