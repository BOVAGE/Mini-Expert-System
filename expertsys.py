import tkinter as tk
from tkinter import messagebox, simpledialog

class App():
    def __init__(self, window, textfile):
        self.textfile = textfile
        self.window = window
        window.withdraw()

    def readFromFile(self):
        with open(self.textfile) as file:
            contents = file.readlines()
            stecapdict = {}
            for line in contents:
                line = line.rstrip("\n")
                state, capital = line.split('/')
                stecapdict.setdefault(state.title(), capital.title())
##                print(f"{state} and {capital}")
            return stecapdict


    def appendToFile(self, state, capital):
        with open(self.textfile, "a") as file:
            file.write(f"\n{state}/{capital}")

    def result(self):
        self.questionBox = simpledialog.askstring("State", "Type the name of a state\
 in Nigeria")
        answer = self.readFromFile().get(self.questionBox.title(), "IDK")
        if answer != "IDK":
            messageBox = messagebox.showinfo("Capital", message = f"The capital city\
 of {self.questionBox.title()} is {answer}")
            print(answer)
        else:
            teacherBox = simpledialog.askstring("Teach Me", f"I don't know.\
 What is the capital?")
            self.appendToFile(self.questionBox, teacherBox)

        retry = messagebox.askretrycancel("Ask again", "Do you want to ask again")
        if retry:
            self.result()
        else:
            self.window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Nigeria States Expert")
    App(root, "expertfile.txt").result()
    root.mainloop()
