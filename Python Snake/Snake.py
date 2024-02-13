from hashlib import new
from tkinter import *
from random  import *
from turtle  import speed

#--------------------------------------------------------------------------------------------------

W = H = 500
SnakeLength = 20
foodColor = "#FF0000"
snakeColor = "#E80083"
Block = 25
Score = 0
Speed = 50
Movements = ["Left", "Right", "Up", "Down"]
shuffle(Movements)
Dir = Movements[0]

#--------------------------------------------------------------------------------------------------

class Food:
    
    def __init__(self, color = foodColor):
        
        x = randint(0, W / Block - 1) * Block
        y = randint(0, H / Block - 1) * Block

        self.Coord = [x, y]

        Board.create_oval(x, y, x + Block, y + Block, fill = color,
                           outline = color, tags = "food")





class Snake:
    
    def __init__(self, color = snakeColor):
        
        self.Length = SnakeLength
        self.Coord = []
        self.Squares = []

        for i in range(SnakeLength):
            self.Coord.append([0, 0])

        for x, y in self.Coord:
            Square = Board.create_rectangle(x, y, x + Block, y + Block, fill = color,
                                             tags = "snake", outline = snakeColor)
            self.Squares.append(Square)

#--------------------------------------------------------------------------------------------------

def Direction(snake, food):

    x, y = snake.Coord[0]

    if Dir == "Up":
        y -= Block
    elif Dir == "Down":
        y += Block
    elif Dir == "Right":
        x += Block
    elif Dir == "Left":
        x -= Block

    snake.Coord.insert(0, (x, y))
    Square = Board.create_rectangle(x, y, x + Block, y + Block, fill = snakeColor,
                                     tags = "snake", outline = snakeColor)
    snake.Squares.insert(0, Square)

    if x == food.Coord[0] and y == food.Coord[1]:
        global Score
        Score += 1
        Screen["text"] = "Score: " + str(Score)
        Board.delete("food")
        food = Food(foodColor)
    else:
        del snake.Coord[-1]
        Board.delete(snake.Squares[-1])
        del snake.Squares[-1]

    if Collision(snake) == True:
        Board.create_text(W / 2, H / 2, text = "Game Over", tags = "text",
                           fill = "#D7FF00" if Dark.get() == True else "#510063",
                           font = ("Burbank Big cd bk", 50))

    else:
        window.after(Speed, Direction, snake, food)

    if x >= W: snake.Coord[0] = [-Block, y]
    elif x < 0: snake.Coord[0] = [W, y]
    if y > H: snake.Coord[0] = [x, -Block]
    elif y < 0: snake.Coord[0] = [x, H]





def ChangeDir(direction):

    global Dir

    if Dir == "Up" and direction != "Down":
        Dir = direction
    elif Dir == "Down" and direction != "Up":
        Dir = direction
    elif Dir == "Left" and direction != "Right":
        Dir = direction
    elif Dir == "Right" and direction != "Left":
        Dir = direction






def Collision(snake):

    x, y = snake.Coord[0]

    for i in snake.Coord[1:]:
        if x == i[0] and y == i[1]:
            return True

    return False






def Restart(event = None):

    global Score, Board, Player

    if Collision(Player) == True:

        Board.delete("snake")
        Board.delete("food")
        Board.delete("text")

        Score = 0
        Screen["text"] = "Score : " + str(Score)

        Apple = Food(foodColor)
        Player = Snake(snakeColor)

        Direction(Player, Apple)






def ChangeColor(obj = None):

    from tkinter import colorchooser
    global snakeColor, foodColor

    Color = colorchooser.askcolor()[1]

    if obj == "Snake": snakeColor = Color
    elif obj == "Food": foodColor = Color    
    elif obj == "Bg": Board.config(bg = Color)

    Restart()






def DarkMode():

    if Dark.get() == False: Board.config(bg = "#CCCCCC")
    else: Board.config(bg = "#222222")
    
    Restart()


#==================================================================================================

window = Tk()
window.title("Snake")
window.resizable(False, False)

#--------------------------------------------------------------------------------------------------

Dark = BooleanVar()
Dark.set(True)

MenuBar = Menu(window)
window.config(menu = MenuBar)

Game = Menu(MenuBar, tearoff = False)
MenuBar.add_cascade(label = "Game", menu = Game)
Game.add_command(label = "Restart       ", accelerator = "< N >", command = Restart)
Game.add_separator()
Game.add_command(label = "Exit", command = quit)

Edit = Menu(MenuBar, tearoff = False)
MenuBar.add_cascade(label = "Edit", menu = Edit)
ColorChange = Menu(Edit, tearoff = False)
Edit.add_cascade(label = "Change Color", menu = ColorChange)
ColorChange.add_command(label = "Snake", command = lambda: ChangeColor("Snake"))
ColorChange.add_command(label = "Food", command = lambda: ChangeColor("Food"))
ColorChange.add_command(label = "Background", command = lambda: ChangeColor("Bg"))
Edit.add_checkbutton(label = "Dark Mode", offvalue = False, variable = Dark, command = DarkMode)

#--------------------------------------------------------------------------------------------------

Screen = Label(window, text = "Score : " + str(Score), font = ("Electroharmonix", ))
Screen.pack()

Board = Canvas(window, width = W, height = H, bg = "#222222")
Board.pack()

#--------------------------------------------------------------------------------------------------

window.update()

windowW = window.winfo_width()
windowH = window.winfo_height()
screenW = window.winfo_screenwidth()
screenH = window.winfo_screenheight()

placementX = int((screenW / 2) - (windowW / 2))
placementY = int((screenH / 2) - (windowH / 2))

window.geometry("{}x{}+{}+{}".format(windowW, windowH, placementX, placementY))

window.bind("<Up>",     lambda event: ChangeDir("Up"))
window.bind("<Down>",   lambda event: ChangeDir("Down"))
window.bind("<Left>",   lambda event: ChangeDir("Left"))
window.bind("<Right>",  lambda event: ChangeDir("Right"))
window.bind("<q>", quit)
window.bind("<n>", Restart)

#--------------------------------------------------------------------------------------------------

Apple = Food()
Player = Snake()

Direction(Player, Apple)

#--------------------------------------------------------------------------------------------------

window.mainloop()