import tkinter as tk
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
player1_y = 100
ball_y = 200
ball_x = 200
ball_dx = random.choice([-5, 5])
ball_dy = random.choice([-5, 5])

def MoveUp(event):
    global player1_y
    if (player1_y > 0):
        player1_y -= 10
    canvas.coords(player1, 0, player1_y, 20, player1_y + 100)

def MoveDown(event):
    global player1_y
    if (player1_y < SCREEN_HEIGHT - 100): # 100 is the size of the player
        player1_y += 10
    canvas.coords(player1, 0, player1_y, 20, player1_y + 100)

def BallMove():
    global ball_x, ball_y, ball_dx, ball_dy
    # update ball pos
    ball_x += ball_dx
    ball_y += ball_dy
    # check collision
    if ball_x <= 0 or ball_x + 30 >= SCREEN_WIDTH:
        ball_dx *= -1
    if ball_y <= 0 or ball_y + 30 >= SCREEN_HEIGHT:
        ball_dy *= -1
    canvas.coords(ball, ball_x, ball_y, ball_x + 30, ball_y + 30)
    window.after(30, BallMove)

# window settings
window = tk.Tk()
window.title("Tenis Game")
window.geometry("500x500")

# canvas
canvas = tk.Canvas(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg='white')
canvas.pack()

# elements
player1 = canvas.create_rectangle(0, player1_y, 20, player1_y + 100, fill='black')
ball = canvas.create_oval(100, 130, 130, 100, fill='black')

# bind
window.bind("<Up>", MoveUp)
window.bind("<Down>", MoveDown)

BallMove()
window.mainloop()
