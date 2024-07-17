# myList = [0, 1, 20, 40, 55, 12, 78]

# print(myList.sort())   
# print(myList)   

# myList = [10, 1, 2, 8, 20, 43, 15]
# print(sorted(myList))
# print(myList)

# import sup

# import time

# sup.hello()

# time.sleep(5)

# sup.sum(10, 20)

# class Adil:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age 

#     def hello(self):
#         print(f"привет Меня зовут {self.name}!")


# one_person = Adil("adil", 20)
# print(one_person.age)
# print(one_person.name)
# one_person.hello()

# two_person = Adil("adil", 33)
# print(two_person.age)
# print(two_person.name)



from tkinter import *

# def get_entry():
#     value = entry.get()
#     txt["text"] = value

def swith_color():
    root.configure(bg="#e716fa")
    tittle["bg"] = "#e716fa"
    frame["bg"] = "#e716fa"

def swith_color2():
    root.configure(bg="#0af21d")
    tittle["bg"] = "#0af21d"
    frame["bg"] = "#0af21d"


root = Tk()
root.title("App")
root.geometry("400x400")
root.configure(bg="#5b8f72")

tittle = Label(root, text="suuuuuuu", bg="#0c14f0", fg="#5b8f72", font=("Comic Sans MS", 16, 'bold'))
tittle.pack()


frame = Frame(root)
frame.pack(anchor="center")


btn1 = Button(frame, text="btn1", bg="#0c14f0", fg="#5b8f72", command=swith_color, font=("Comic Sans MS", 12, 'bold'))
btn2 = Button(frame, text="btn2", bg="#0c14f0", fg="#5b8f72", command=swith_color2, font=("Comic Sans MS", 12, 'bold'))
btn3 = Button(frame, text="btn3", bg="#0c14f0", fg="#5b8f72", font=("Comic Sans MS", 12, 'bold'))
btn4 = Button(frame, text="btn4", bg="#0c14f0", fg="#5b8f72", font=("Comic Sans MS", 12, 'bold'))

btn1.grid(row=0, column=0, pady=10, padx=10)
btn2.grid(row=0, column=1, pady=10, padx=10)
btn3.grid(row=0, column=2, pady=10, padx=10)
btn4.grid(row=0, column=3, pady=10, padx=10)


root.mainloop()






