from tkinter import *

class MyWindow:
    
    def __init__(self, window):
        self.button = Button(window, text="Click to change color", command=self.changecolor)
        self.button.place(relx=0.5, rely=0.5, anchor=CENTER)
        
    def changecolor(self):
        self.button.config(bg="yellow")


window = Tk()
MyWin = MyWindow(window)
window.title("Special Midterm Exam in OOP")
window.geometry("300x300+10+10")
window.mainloop()
