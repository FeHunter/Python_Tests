import tkinter as tk
from pywinauto import Application

# Conecta ao programa alvo
app = Application(backend="uia").connect(title="AudioRelay")
win = app.window(title="AudioRelay")
slider = win.child_window(auto_id="ID_DO_SLIDER", control_type="Slider")

# Funções para alterar
def aumentar():
    valor = slider.get_value()
    slider.set_value(valor + 1)

def diminuir():
    valor = slider.get_value()
    slider.set_value(valor - 1)

# Cria a janela Tkinter
root = tk.Tk()
root.title("Controle Externo")

btn_inc = tk.Button(root, text="Incrementar", command=aumentar)
btn_dec = tk.Button(root, text="Decrementar", command=diminuir)

btn_inc.pack(pady=5)
btn_dec.pack(pady=5)

root.mainloop()
