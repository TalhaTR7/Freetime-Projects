from tkinter import *

#==================================================================================================

turn = 0
Player = ['X', 'O']
Box = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#==================================================================================================
#=========================================== Functions ============================================
#==================================================================================================

def Ask(event = None):

    def Set():
        
        if P2Entry.get() == "" and P1Entry.get()[0] != Player[1]:
            Player[0] = P1Entry.get()[0]
        elif P1Entry.get() == "" and P2Entry.get()[0] != Player[0]:
            Player[1] = P2Entry.get()[0]
        elif P1Entry.get()[0] != P2Entry.get()[0]:
            Player[0] = P1Entry.get()[0]
            Player[1] = P2Entry.get()[0]
        Screen.config(text = (Player[turn] + " ki bari"))
        NewWindow.destroy()

    NewWindow = Toplevel()
    NewWindow.title("Settings")
    NewWindow.geometry("350x150")
    NewWindow.resizable(False, False)
    frameA = Frame(NewWindow)
    frameB = Frame(NewWindow)

    Settings = Label(frameA, text = "Settings", font = ("Metronic Pro Bold Italic", 24))
    P1Label = Label(frameA, text = "Enter P1 character: ", font = ("Metronic Pro Bold", 16))
    P2Label = Label(frameA, text = "Enter P2 character: ", font = ("Metronic Pro Bold", 16))
    P1Entry = Entry(frameA, font = ("Metronic Pro Bold", 16), width = 2, bg = "#DDDDDD")
    P2Entry = Entry(frameA, font = ("Metronic Pro Bold", 16), width = 2, bg = "#DDDDDD")
    Enter = Button(frameB, text = "Enter", command = Set, bg = "#7800B0")
    Cancel = Button(frameB, text = "Cancel", command = lambda: NewWindow.destroy(), bg = "#009E6C")

    Enter["width"] = Cancel["width"] = 15
    Enter["font"] = Cancel["font"] = ("Metronic Pro Bold", 10)
    Enter["fg"] = Cancel["fg"] = "#FFFFFF"

    Settings.grid(row = 0, column = 0)
    P1Label.grid(row = 1, column = 0)
    P2Label.grid(row = 2, column = 0)
    P1Entry.grid(row = 1, column = 1)
    P2Entry.grid(row = 2, column = 1)
    Enter.grid(row = 0, column = 0)
    Cancel.grid(row = 0, column = 1)

    frameA.pack()
    frameB.pack()
    Restart()
    NewWindow.mainloop()

#==================================================================================================

def ChangeTurn():
    
    global turn
    turn += 1
    turn %= 2

#==================================================================================================

def GameOver():

    global Shade

    for row in range(3):
        if Box[row][0]["text"] == Box[row][1]["text"] == Box[row][2]["text"] != "":
            Box[row][0]["bg"], Box[row][0]["fg"] = Shade, "#FFFFFF"
            Box[row][1]["bg"], Box[row][1]["fg"] = Shade, "#FFFFFF"
            Box[row][2]["bg"], Box[row][2]["fg"] = Shade, "#FFFFFF"
            return True

    for column in range(3):
        if Box[0][column]["text"] == Box[1][column]["text"] == Box[2][column]["text"] != "":
            Box[0][column]["bg"], Box[0][column]["fg"] = Shade, "#FFFFFF"
            Box[1][column]["bg"], Box[1][column]["fg"] = Shade, "#FFFFFF"
            Box[2][column]["bg"], Box[2][column]["fg"] = Shade, "#FFFFFF"
            return True

    if Box[0][0]["text"] == Box[1][1]["text"] == Box[2][2]["text"] != "":
        Box[0][0]["bg"] = Box[1][1]["bg"] = Box[2][2]["bg"] = Shade
        Box[0][0]["fg"] = Box[1][1]["fg"] = Box[2][2]["fg"] = "#FFFFFF"
        return True

    elif Box[0][2]["text"] == Box[1][1]["text"] == Box[2][0]["text"] != "":
        Box[0][2]["bg"] = Box[1][1]["bg"] = Box[2][0]["bg"] = Shade
        Box[0][2]["fg"] = Box[1][1]["fg"] = Box[2][0]["fg"] = "#FFFFFF"
        return True

    Blank = 0
    for i in range(3):
        for j in range(3):
            if Box[i][j]["text"] == "":
                Blank += 1

    if Blank == 0:
        for i in range(3):
            for j in range(3):
                Box[i][j]["bg"] = "#FF0066"
                Box[i][j]["fg"] = "#FFFFFF"
                Box[i][j]["activebackground"] = "#CF0053"
                Box[i][j]["activeforeground"] = "#FFFFFF"
        return None

    else: return False

#==================================================================================================

def Play(row, column):

    global Shade
    if turn == 1: Shade = "#7800B0"
    else: Shade = "#009E6C"

    if Box[row][column]["text"] == "" and GameOver() == False:
        Box[row][column]["text"] = Player[turn]
        if GameOver() == False:
            ChangeTurn()
            Screen.config(text = Player[turn] + " ki bari")

    if GameOver() == True:
        Screen.config(text = Player[turn] + " jeet gya")
    elif GameOver() == None:
        Screen.config(text = "Draw hogai")

#==================================================================================================

def Restart(event = None):

    Screen.config(text = Player[turn] + " ki bari")
    DarkMode()
    for i in range(3):
        for j in range(3):
            Box[i][j]["text"] = ""

#==================================================================================================

def DarkMode():

    if Dark.get() == True:
        for i in range(3):
            for j in range(3):
                Box[i][j].config(bg = "#222222",
                                  fg = "#FFFFFF",
                                  activebackground = "#121212",
                                  activeforeground = "#FFFFFF")
    else:
        for i in range(3):
            for j in range(3):
                Box[i][j].config(bg = "#EEEEEE",
                                  fg = "#000000",
                                  activebackground = "#DDDDDD",
                                  activeforeground = "#000000")

#==================================================================================================
#=========================================== Mainframe ============================================
#==================================================================================================

window = Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

Dark = BooleanVar()
Dark.set(True)

#==================================================================================================

MenuBar = Menu(window)
window.config(menu = MenuBar, bg = "#111111")
Game = Menu(MenuBar, tearoff = False)
MenuBar.add_cascade(label = "Game", menu = Game)
Game.add_command(label = "Restart    ", accelerator = "Ctrl+N", command = Restart)
Game.add_command(label = "Settings   ", accelerator = "Ctrl+S", command = Ask)
Game.add_checkbutton(label = "Dark Mode", command = DarkMode, offvalue = Dark.set(False), variable = Dark)
Game.add_separator()
Game.add_command(label = "Exit", command = quit)
window.bind("<Control-n>", Restart)
window.bind("<Control-s>", Ask)

#==================================================================================================

Screen = Label(window, width = 28, height = 3,
                font = ("Burbank Big Cd Bk", 24),
                text = (Player[turn] + " ki bari"),
                bg = "#111111", fg = "#22FF00")
Screen.pack()

Board = Frame(window)
Board.pack()

#==================================================================================================

for i in range(3):
    for j in range(3):
        Box[i][j] = Button(Board, text = "",
                            width = 9, height = 4,
                            bg = "#EEEEEE", fg = "#000000",
                            activebackground = "#DDDDDD",
                            font = ("Burbank Big Cd Bk", 25),
                            command = lambda row = i, column = j: Play(row, column))
        Box[i][j].grid(row = i, column = j)

#==================================================================================================

window.mainloop()
