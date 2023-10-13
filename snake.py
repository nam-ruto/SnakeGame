# Import Tkinter library
from tkinter import *
import random

# Constant variable
WIDTH = 600
HEIGHT = 600
SPEED = 50
SPACE_SIZE = 10
SNAKE_PART = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

# Initial figure
score = 0
direction = "down"

class Snake:
    pass

class Food:
    pass

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

    window.mainloop()