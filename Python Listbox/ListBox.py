from tkinter import *
from tkinter import filedialog, messagebox, colorchooser, ttk

food = ["Pizza", "Biryani", "Burger", "Shawarma", "Chicken"]
drinks = ["Lemonade", "Coke", "Coffee", "Tea"]
custom = "Metronic Pro Bold"
haram = False
Save = []


#--------------------------------------------------------------------------------------------------
#-------------------------------------- Functions -------------------------------------------------
#--------------------------------------------------------------------------------------------------


def OpenFile(event = None):
    path = filedialog.askopenfilename(initialdir = "E:\\Levi",
                                      title = "Open a file",
                                      defaultextension = ".txt",
                                      filetypes = (("Text file", "*.txt"),
                                                   ("HTML file", "*.html"),
                                                   ("All files", "*.*")))
    if path == "":
        return
    file = open(path, "r")
    print(file.read())
    file.close()



def SaveFile(event = None):
    path = filedialog.asksaveasfile(initialdir = "E:\\Levi",
                                    title = "Save at location",
                                    defaultextension = ".txt",
                                    filetypes = (("Text file", "*.txt"),
                                                 ("HTML file", "*.html"),
                                                 ("All files", "*.*")))
    if path is None: return
    else:
        for i in Save: path.write("  {}\n".format(i))
        path.write("------------------------")
        path.close()




def Haram():
    global haram
    if haram == True:
        messagebox.showerror(title = "Watch it",
                             message = "You cannot add any haram item")
    elif haram == False:
        messagebox.showinfo(title = "Smart",
                            message = "You did well with you decision")
    elif haram == None:
        messagebox.showwarning(title = "Beware",
                               message = "Don't think anything stupid")


def Place():
    for i in menuF.curselection():
        print(menuF.get(i))
        Save.append(menuF.get(i))
    for i in menuD.curselection():
        print(menuD.get(i))
        Save.append(menuD.get(i))


def Add():
    if name.get() != "":
        if name.get() == "Pork":
            global haram
            haram = messagebox.askyesnocancel(title = "Think again",
                                              message = "Do you want to add 'Pork'?")
            Haram()
        else: menuF.insert(menuF.size(), name.get())
    menuF.config(height = menuF.size())


def Remove():
    if menuF.curselection():
        for i in reversed(menuF.curselection()):
            menuF.delete(i)
    elif menuD.curselection():
        for i in reversed(menuD.curselection()):
            menuD.delete(i)
    menuF.config(height = menuF.size())
    menuD.config(height = menuD.size())



def ColorMenu():
    color_bg = colorchooser.askcolor(title = "Background")
    color_fg = colorchooser.askcolor(title = "Foreground")
    menuF.config(bg = color_bg[1],
                fg = color_fg[1])


def Manual(event = None):
    Message = """
    1. Select your products from a tab
    2. Before switching tabs, place the selected products
    3. Do the same for other tabs
    4. Finally save the order

    You understand?
    """
    Ans = messagebox.askyesno(title = "Manual", message = Message[1:])
    if Ans == True: pass
    elif Ans == False: Manual()
    else: Manual()


def About():
    Message = """
    Made by:    Legend
    Version:      7.12.03
    """
    messagebox.showinfo(title = "About", message = Message[1:])


#--------------------------------------------------------------------------------------------------
#------------------------------------ Menu Bar ----------------------------------------------------
#--------------------------------------------------------------------------------------------------


window = Tk()

MenuBar = Menu(window)
window.config(menu = MenuBar, bg = "#333333")
window.title("Restaurant")

fileMenu = Menu(MenuBar, tearoff = 0)
MenuBar.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label = "Open     ", accelerator = "Ctrl+O", command = OpenFile)
fileMenu.add_command(label = "Save     ", accelerator = "Ctrl+S", command = SaveFile)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = quit)

editMenu = Menu(MenuBar, tearoff = 0)
MenuBar.add_cascade(label = "Edit", menu = editMenu)
editMenu.add_command(label = "Color", command = ColorMenu)
editMenu.add_separator()
lengthMenu = Menu(editMenu, tearoff = 0)
editMenu.add_cascade(label = "Length", menu = lengthMenu)
lengthMenu.add_command(label = "Width")
lengthMenu.add_command(label = "Height")

helpMenu = Menu(MenuBar, tearoff = 0)
MenuBar.add_cascade(label = "Help",  menu = helpMenu)
helpMenu.add_command(label = "Manual", command = Manual)
helpMenu.add_command(label = "About", command = About)

window.bind("<Control-s>", SaveFile)
window.bind("<Control-o>", OpenFile)
window.bind("<Escape>", quit)
window.bind("<Control-m>", Manual)


#--------------------------------------------------------------------------------------------------
#------------------------------------ User Interface ----------------------------------------------
#--------------------------------------------------------------------------------------------------


NoteBook = ttk.Notebook(window)

tab1 = Frame(window)
tab2 = Frame(window)

NoteBook.add(tab1, text = "Food")
NoteBook.add(tab2, text = "Drinks")




menuF = Listbox(tab1,
                font = (custom, 18),
                width = 30,
                selectmode = MULTIPLE,)

menuD = Listbox(tab2,
                font = (custom, 18),
                width = 30,
                selectmode = MULTIPLE,)


for i in range(len(food)):
    menuF.insert(i, food[i])
for i in range(len(drinks)):
    menuD.insert(i, drinks[i])




frame = Frame(window)

place = Button(frame, 
               text = "Place",
               font = (custom, 18),
               command = Place,
               fg = "White",
               bg = "red").pack(side = 'left')

add = Button(frame,
             text = "Add",
             font = (custom, 18),
             command = Add,
             fg = "white",
             bg = "green").pack(side = 'left')

remove = Button(frame, 
                text = "Remove",
                font = (custom, 18),
                command = Remove,
                fg = "white",
                bg = "purple").pack(side = 'left')

name = Entry(window,
             font = (custom, 18),
             bg = "#222222",
             fg = "#FFFFFF",
             width = menuF["width"])


menuF.config(height = menuF.size())
menuD.config(height = menuF.size())

#-------------------------------------- Packing ---------------------------------------------------

frame.pack()
name.pack()

menuF.pack()
menuD.pack()
NoteBook.pack(expand = True, fill = "both")

window.mainloop()
