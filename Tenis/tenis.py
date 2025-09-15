import tkinter as tk
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
score = 0
player1_y = 100
player1_width = 20
ball_size = 130
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
    global ball_x, ball_y, ball_dx, ball_dy, player1_width, score
    # update ball pos
    ball_x += ball_dx
    ball_y += ball_dy
    # check wall collision
    if ball_x <= 0 or ball_x + 30 >= SCREEN_WIDTH:
        ball_dx *= -1
    if ball_y <= 0 or ball_y + 30 >= SCREEN_HEIGHT:
        ball_dy *= -1
    # check player collision
    ball_radius = 5
    if (ball_x + ball_radius >= 0 and ball_x - ball_radius <= 0 + player1_width and
        ball_y + ball_radius >= player1_y and ball_y - ball_radius <= player1_y + 100):
            hit_pos = (ball_y - player1_y) / 100
            ball_dy = (hit_pos - 0.5) * 10
            ball_dx = abs(ball_dx) * 1.1
            score += 1
    
    # check if hits the wall
    if (ball_x <= player1_width - 10):
        score = 0
        ball_x, ball_y = SCREEN_WIDTH//2, SCREEN_HEIGHT//2
        ball_dx = random.choice([-5, 5])
        ball_dy = random.choice([-5, 5])
    canvas.coords(ball, ball_x, ball_y, ball_x + 30, ball_y + 30)
    window.after(30, BallMove)

def Score():
    global score
    canvas.itemconfig(scoreLabel, text=f"score: {score}")
    window.after(30, Score)

# window settings
window = tk.Tk()
window.title("Tenis Game")
window.geometry("500x500")

# canvas
canvas = tk.Canvas(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg='white')
canvas.pack()

# elements
player1 = canvas.create_rectangle(0, player1_y, player1_width, player1_y + 100, fill='black')
ball = canvas.create_oval(100, ball_size, ball_size, 100, fill='black')

# Label - score
scoreLabel = canvas.create_text(SCREEN_WIDTH/2, 20, text="0", font=("Arial", 20), fill="black")

# bind
window.bind("<Up>", MoveUp)
window.bind("<Down>", MoveDown)

BallMove()
Score()
window.mainloop()
