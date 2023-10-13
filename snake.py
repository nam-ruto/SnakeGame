# Import Tkinter library
from tkinter import *
import random

# Constant variable
WIDTH = 600
HEIGHT = 600
SPEED = 50
SPACE_SIZE = 20
SNAKE_PART = 30
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"
GAME_OVER_COLOR = "red"

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

    def snakeMoving(self, canvas, snake, food):
        x, y = self.coordinates[0]
        #-------Set the snake's movement (add head delete tail)------#
        if direction == "up":
            y -= SPACE_SIZE
        elif direction == "down":
            y += SPACE_SIZE
        elif direction == "right":
            x += SPACE_SIZE
        elif direction == "left":
            x -= SPACE_SIZE

        snake.coordinates.insert(0, (x, y))
        block = canvas.create_rectangle(x, y, x + SPACE_SIZE, y  + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
        snake.blocks.insert(0, block)

        del self.coordinates[-1]
        canvas.delete(self.blocks[-1])
        del self.blocks[-1]
        #-------Set the snake's movement (add head delete tail)------#

        # Eat food and generate new ones
        if(x == food.getCoordinatesX() and y == food.getCoordinatesY()):
            global score
            score += 1
            label.config(text="Score: {}".format(score))
            canvas.delete("food")
            food = Food(canvas)

        # Check collisions (itself and the screen sides)
        if(self.snakeCollisions(snake, canvas)):
            gameOver(canvas)
            
        # Keep moving
        else:
            window.after(SPEED, self.snakeMoving, canvas, snake, food)

    def snakeCollisions(self, snake, canvas):
        x, y = self.coordinates[0]

        if(x < 0 or x >= WIDTH):
            return True
        elif(y < 0 or y >= HEIGHT):
            return True
        for body_part in self.coordinates[1:]:
            if(x == body_part[0] and y == body_part[1]):
                return True
        return False


class Food:
    def __init__(self, canvas):
        x = random.randint(0, (WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags="food")
    def getCoordinatesX(self):
        return self.coordinates[0]
    def getCoordinatesY(self):
        return self.coordinates[1]


def changeDirection(new_direction):
    global direction

    if(new_direction == "left"):
        if(direction != "right"):
            direction = new_direction

    elif(new_direction == "right"):
        if(direction != "left"):
            direction = new_direction

    elif(new_direction == "up"):
        if(direction != "down"):
            direction = new_direction

    elif(new_direction == "down"):
        if(direction != "up"):
            direction = new_direction 


def gameOver(canvas):
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("Ariel", 60), text="GAME OVER" , fill=GAME_OVER_COLOR, tags="gameover")

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
    snake.snakeMoving(canvas, snake, food)

    window.bind("<Left>", lambda event: changeDirection("left"))
    window.bind("<Right>", lambda event: changeDirection("right"))
    window.bind("<Up>", lambda event: changeDirection("up"))
    window.bind("<Down>", lambda event: changeDirection("down"))

    window.mainloop()