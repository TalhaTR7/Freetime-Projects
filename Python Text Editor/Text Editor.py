from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import filedialog
import os
from tkinter import font

#==================================================================================================

FontFamily = ["Agency FB",
              "BadaBoom BB",
              "Burbank Big Cd Bk",
              "Burbank Big Cd Bd",
              "Electroharmonix",
              "FC Liverpool  Club 2019",
              "liverpool Cup 2023",
              "Ninja Naruto",
              "Metronic Pro Bold",
              "Metronic Pro Bold Italic",
              "Most Wazted",
              "Real Madrid",
              "Real Madrid 15/16",
              "Rea Madrid 2021 UCL",
              "TT Lakes Condensed Bold DEMO",
              "TT Lakes Neue Condensed Black I",
              "TT Lakes Neue Condensed ExtraBo"]

HelpText = """
Levi has short, straight black hair styled in an undercut, as well as narrow,
intimidating steel blue eyes with dark circles under them and a deceptively
youthful face. He is quite short, but his physique is well-developed in
musculature from extensive omni-directional mobility gear usage. He is usually
either frowning or expressionless; that, plus his extremely calm demeanor, often
makes it difficult for others to guess what he is thinking.
    
He is most often seen in his Scout Regiment uniform, with a light gray button-up
shirt underneath along with his trademark white ascot, though since the
coup d'etat, he has lef it off. When embarking on expeditions outside the Walls,
he also wears the Scout Regiment's green-hooded cloak; like the rest of the Scouts
who traveled and fought against the Marleyan troops, Levi wore the new all black
variant of the Scout Regiment's uniform. Wh en forced to take leave from his duties
due to injury, Levi was seen in a black suit, plain white shirt, ascot, and dress
shoes.
"""

#==================================================================================================
#========================================== Functions =============================================
#==================================================================================================

def ChangeColor():
    TextColor.set(colorchooser.askcolor()[1])
    TextArea.config(fg = TextColor.get())
#------------------------------------------------
def ChangeFont(*font):
    font
    TextArea.config(font = (TextFont.get(), TextSize.get()))
#------------------------------------------------
def ChangeSize():
    TextArea.config(font = (TextFont.get(), TextSize.get()))

#==================================================================================================

NewFile = lambda event = None: TextArea.delete("1.0", END)
#------------------------------------------------
def OpenFile(event = None):
    Path = filedialog.askopenfilename(title = "Open",
                                      initialfile = "Untitled",
                                      initialdir = "E:\\Levi PY",
                                      defaultextension = ".txt",
                                      filetypes = (("Text File", "*.txt"),
                                                   ("HTML File", ["*.html", "*.htm"]),
                                                   ("PDF", "*.pdf"),
                                                   ("Python File", "*.py"),
                                                   ("All Files", "*.*")))
    if Path == "": return
    else:
        try:
            window.title(os.path.basename(Path))
            NewFile()
            file = open(Path, "r")
            TextArea.insert("1.0", file.read())
        except Exception:
            messagebox.showerror(title = "Error", message = "File did not found")
        finally:
            file.close()
#------------------------------------------------
def SaveFile(event = None):
    Path = filedialog.asksaveasfilename(title = "Save as",
                                        confirmoverwrite = True,
                                        initialdir = "E:\\Levi PY",
                                        initialfile = "Untitled",
                                        defaultextension = ".txt",
                                        filetypes = (("Text file", "*.txt"),
                                                     ("Web Page", ["*.html", "*.htm"]),
                                                     ("PDF", "*.pdf"),
                                                     ("Python File", "*.py"),
                                                     ("All files", "*.*")))
    if Path == "": return
    else:
        try:
            file = open(Path, "w")
            file.write(TextArea.get("1.0", END))
        except Exception:
            messagebox.showerror(title = "Error", message = "Something went wrong")
        finally:
            file.close()

#==================================================================================================

CutText = lambda event = None: TextArea.event_generate("<<Cut>>")
CopyText = lambda event = None: TextArea.event_generate("<<Copy>>")
PasteText = lambda event = None: TextArea.event_generate("<<Paste>>")

#==================================================================================================

def Help(event = None):
    HelpWindow = Tk()
    HelpWindow.title("Help")
    Label(HelpWindow, text = "Help", font = (FontFamily[2], 25)).pack(pady = 10)
    Label(HelpWindow, text = HelpText[1:-1], justify = "left", font = (FontFamily[-3], 12)).pack(padx = 10)
    Close = Button(HelpWindow, text = "close", command = HelpWindow.destroy, relief = None)
    Close.pack(padx = 10, pady = 10, side = "right")
    HelpWindow.mainloop()
#------------------------------------------------
def Customize():
    ask = messagebox.askyesno(title = "Customize",
                              message = "Do you want to cutomize your text editor?")
    if ask == True:
        messagebox.showerror(title = "Error",
                             message = "This feature is not available yet")
#------------------------------------------------
def DarkMode():
    if DarkBool.get() == True:
        TextArea.config(bg = "#111111", fg = "#FFFFFF")
        Color.config(state = "disabled")
    else:
        TextArea.config(bg = "#FFFFFF", fg = TextColor.get())
        Color.config(state = "active")
#------------------------------------------------
def About():
    AboutText = """
    The Text Editor
    Made by:\tA Legend
    Version:\t07.12.03
    """
    messagebox.showinfo(title = "About", message = AboutText[1:-1])

#==================================================================================================
#======================================== GUI Framework ===========================================
#==================================================================================================

window = Tk()

windowW = 500
windowH = 500
screenW = window.winfo_screenwidth()
screenH = window.winfo_screenheight()
x = int((window.winfo_screenwidth() / 2) - (windowW / 2))
y = int((window.winfo_screenheight() / 2) - (windowH / 2))

DarkBool = BooleanVar()
DarkBool.set(True)

TextFont = StringVar()
TextFont.set("Metronic Pro Bold")

TextSize = IntVar()
TextSize.set(12)

TextColor = StringVar()
TextColor.set("#000000")

FileName = StringVar()
FileName.set("Untitled - Text Editor")

window.geometry("{}x{}+{}+{}".format(windowW, windowH, x, y))
window.title(FileName.get())
window.rowconfigure(0, weight = 1)
window.columnconfigure(0, weight = 1)

TextArea = Text(window, font = (TextFont.get(), TextSize.get()), fg = TextColor.get())
Scroll = Scrollbar(TextArea)
TextArea.grid(sticky = E + W + N + S)
Scroll.pack(side = RIGHT, fill = Y)
TextArea.config(yscrollcommand = Scroll.set(0.0, 1.0))

#==================================================================================================
#============================================= Menu ===============================================
#==================================================================================================

MenuBar = Menu(window)
window.config(menu = MenuBar)
#================================================
File = Menu(MenuBar, tearoff = False)
MenuBar.add_cascade(menu = File, label = "File")
File.add_command(label = "New                 ", accelerator = "Ctrl + N", command = NewFile)
File.add_command(label = "Open                ", accelerator = "Ctrl + O", command = OpenFile)
File.add_command(label = "Save                ", accelerator = "Ctrl + S", command = SaveFile)
File.add_separator()
File.add_command(label = "Exit                ", accelerator = "        ", command = quit)
#------------------------------------------------
Edit = Menu(MenuBar, tearoff = False)
MenuBar.add_cascade(menu = Edit, label = "Edit")
Edit.add_command(label = "Cut                 ", accelerator = "Ctrl + X", command = CutText)
Edit.add_command(label = "Copy                ", accelerator = "Ctrl + C", command = CopyText)
Edit.add_command(label = "Paste               ", accelerator = "Ctrl + V", command = PasteText)
#------------------------------------------------
Options = Menu(MenuBar, tearoff = False)
MenuBar.add_cascade(menu = Options, label = "Options")
Options.add_command(label = "Help             ", accelerator = "Ctrl + H", command = Help)
Options.add_command(label = "Customize...", command = Customize)
Options.add_checkbutton(label = "Dark Mode",
                        variable = DarkBool,
                        offvalue = DarkBool.set(False),
                        command = DarkMode)
Options.add_separator()
Options.add_command(label = "About", command = About)

#==================================================================================================

window.bind("<Control-n>", NewFile)
window.bind("<Control-o>", OpenFile)
window.bind("<Control-s>", SaveFile)
window.bind("<Escape>"   , quit)
#------------------------------------------------
window.bind("<Control-x>", CutText)
window.bind("<Control-c>", CopyText)
window.bind("<Control-v>", PasteText)
#------------------------------------------------
window.bind("<Control-h>", Help)

#==================================================================================================
#============================================ Frames ==============================================
#==================================================================================================

frame = Frame(window)
frame.grid()
#================================================
Color = Button(frame, text = "Color", command = ChangeColor)
Font = OptionMenu(frame, TextFont, *FontFamily, command = ChangeFont)
Size = Spinbox(frame, textvariable = TextSize, from_ = 1, to = 100, command = ChangeSize)
#------------------------------------------------
Color.grid(row = 0, column = 0)
Font.grid(row = 0, column = 1)
Size.grid(row = 0, column = 2)

#==================================================================================================

window.mainloop()
