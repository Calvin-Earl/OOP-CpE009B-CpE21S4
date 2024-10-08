from tkinter import *


class MyWindow:
    def __init__(self, win):

        self.Label1 = Label(win, fg="Blue", text="Calculator")
        self.Label1.place(x=150, y=70)

        self.Label2 = Label(win, text="Number 1")
        self.Label2.place(x=70, y=150)

        self.Label3 = Label(win, text="Number 2")
        self.Label3.place(x=70, y=180)

        self.Label4 = Label(win, fg="Green", text="Result")
        self.Label4.place(x=70, y=210)

        self.Entry1 = Entry(win, bd=2)
        self.Entry1.place(x=140, y=150)

        self.Entry2 = Entry(win, bd=2)
        self.Entry2.place(x=140, y=180)

        self.Entry3 = Entry(win, bd=2)
        self.Entry3.place(x=140, y=210)

        self.Button1 = Button(win, fg="Green", text="Add", command=self.add)
        self.Button1.place(x=80, y=250)

        self.Button2 = Button(win, fg="Orange", text="Subtract", command=self.sub)
        self.Button2.place(x=120, y=250)

        self.Button3 = Button(win, fg="Navy Blue", text="Multiply", command=self.mul)
        self.Button3.place(x=180, y=250)

        self.Button4 = Button(win, fg="Red", text="divide", command=self.div)
        self.Button4.place(x=240, y=250)

    def add(self):
        self.Entry3.delete(0, "end")
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 + num2
        self.Entry3.insert(END, str(result))

    def sub(self):
        self.Entry3.delete(0, "end")
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 - num2
        self.Entry3.insert(END, str(result))

    def mul(self):
        self.Entry3.delete(0, "end")
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 * num2
        self.Entry3.insert(END, str(result))

    def div(self):
        self.Entry3.delete(0, "end")
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 / num2
        self.Entry3.insert(END, str(result))


window = Tk()
MyWin = MyWindow(window)
window.geometry("400x300+10+10")
window.title("Standard Calculator")
window.configure(bg="Gray")
window.mainloop()