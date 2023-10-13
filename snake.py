# Import Tkinter library
from tkinter import *
import random

# Constant variable
WIDTH = 600
HEIGHT = 600
SPEED = 50
SPACE_SIZE = 20
SNAKE_PART = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

# Initial figure
score = 0
direction = "down"

class Snake:
    def __init__(self, canvas):
        self.snake_size = SNAKE_PART
        self.coordinates = []
        self.blocks = []
    
        for i in range(0, SNAKE_PART):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            block = canvas.create_rectangle(x, y, x + SPACE_SIZE, y  + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
            self.blocks.append(block)

class Food:
    def __init__(self, canvas):
        x = random.randint(0, (WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags="food")

def moving():
    pass

def changeDirection():
    pass

def gameOver():
    pass

# Main function
if __name__ == "__main__":
    window = Tk()
    window.title("Snake game")

    label = Label(window, text="Score: {}".format(score), font=("Arial", 30))
    label.pack()

    canvas = Canvas(window, bg=BACKGROUND_COLOR, width=WIDTH, height=HEIGHT)
    canvas.pack()

    window.update()

    snake = Snake(canvas)
    food = Food(canvas)

    window.mainloop()