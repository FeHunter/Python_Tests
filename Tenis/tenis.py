import tkinter as tk

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
player1_y = 100

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

# window settings
window = tk.Tk()
window.title("Tenis Game")
window.geometry("500x500")

# canvas
canvas = tk.Canvas(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg='gray')
canvas.pack()

# cria a raquete do player1 uma vez
player1 = canvas.create_rectangle(0, player1_y, 20, player1_y + 100, fill='blue')

# bind das teclas
window.bind("<Up>", MoveUp)
window.bind("<Down>", MoveDown)

window.mainloop()
