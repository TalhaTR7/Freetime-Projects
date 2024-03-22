from tkinter import *

class button:

    def __init__(self, W, H, R, C, BG, T, Press, Cs = 1, Rs = 1):
        self.B = Button(frame,
                        font = ("Metronic Pro Bold",),
                        width = W,
                        height = H,
                        bg = BG,
                        fg = "#FFFFFF",
                        activebackground = "#111111",
                        activeforeground = "#FFFFFF",
                        text = T,
                        command = Press,
                        border = None,
                        bd = None,
                        relief = None)
        self.B.grid(row = R, column = C,
                    columnspan = Cs,
                    rowspan = Rs)

def Press(number, event = None):
    global eqText
    eqText = eqText + str(number)
    eqLabel.set(eqText)

def Solve(event = None):
    global eqText
    try: Total = str(eval(eqText))
    except:
        Total = "Invalid syntax"
        import time
    eqLabel.set(Total)
    eqText = Total

def Clear():
    global eqText
    eqText = ""
    eqLabel.set("")

window = Tk()
window.config(bg = "#000000")
window.title("Calculator")
window.resizable(False, False)

eqText = ""
eqLabel = StringVar()

screen = Label(window, height = 3, width = 26,
               font = ("Metronic Pro Bold",18),
               bg = "#000000", fg = "#00FF00",
               textvariable = eqLabel).pack()

frame = Frame(window, width = 32, height = 20)

Button1 = button(9, 4, 3, 0, "#333333", 1, lambda: Press(1))
Button2 = button(9, 4, 3, 1, "#333333", 2, lambda: Press(2))
Button3 = button(9, 4, 3, 2, "#333333", 3, lambda: Press(3))
Button4 = button(9, 4, 2, 0, "#333333", 4, lambda: Press(4))
Button5 = button(9, 4, 2, 1, "#333333", 5, lambda: Press(5))
Button6 = button(9, 4, 2, 2, "#333333", 6, lambda: Press(6))
Button7 = button(9, 4, 1, 0, "#333333", 7, lambda: Press(7))
Button8 = button(9, 4, 1, 1, "#333333", 8, lambda: Press(8))
Button9 = button(9, 4, 1, 2, "#333333", 9, lambda: Press(9))
Button0 = button(9, 4, 4, 0, "#333333", 0, lambda: Press(0))

ButtonD = button(9, 4, 1, 3, "#222222", '/', lambda: Press('/'))
ButtonM = button(9, 4, 2, 3, "#222222", '*', lambda: Press('*'))
ButtonS = button(9, 4, 3, 3, "#222222", '-', lambda: Press('-'))
ButtonA = button(9, 4, 4, 3, "#222222", '+', lambda: Press('+'))
ButtonP = button(9, 4, 4, 1, "#222222", '.', lambda: Press('.'))
ButtonE = button(9, 4, 4, 2, "#222222", '=', Solve)

ButtonX = button(19, 2, 0, 0, "#111111",  'Exit', quit, 2)
ButtonC = button(19, 2, 0, 2, "#111111", 'Clear', Clear, 2)

window.bind("1", lambda event: Press(1))
window.bind("2", lambda event: Press(2))
window.bind("3", lambda event: Press(3))
window.bind("4", lambda event: Press(4))
window.bind("5", lambda event: Press(5))
window.bind("6", lambda event: Press(6))
window.bind("7", lambda event: Press(7))
window.bind("8", lambda event: Press(8))
window.bind("9", lambda event: Press(9))
window.bind("0", lambda event: Press(0))

window.bind("<slash>", lambda event: Press('/'))
window.bind("<asterisk>", lambda event: Press('*'))
window.bind("<minus>", lambda event: Press('-'))
window.bind("<plus>", lambda event: Press('+'))
window.bind("<period>", lambda event: Press('.'))
window.bind("<Return>", Solve)




frame.pack()

window.mainloop()
