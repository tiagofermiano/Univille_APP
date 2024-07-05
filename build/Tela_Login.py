from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Label

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\tiago\univille_app\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_home_screen():
    home_screen = Toplevel(window)
    home_screen.geometry("428x626")
    home_screen.configure(bg="#FFFFFF")
    Label(home_screen, text="Bem-vindo à Tela Home", font=("Inter SemiBold", 24), bg="#FFFFFF").pack(pady=20)

def check_credentials():
    username = entry_1.get()
    password = entry_2.get()
    if username == "aluno" and password == "123":
        open_home_screen()
    else:
        print("Credenciais inválidas")

window = Tk()
window.geometry("428x626")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 626,
    width = 428,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    428.0,
    626.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    199.0,
    230.0,
    anchor="nw",
    text="Login",
    fill="#000000",
    font=("Inter SemiBold", 24 * -1)
)

canvas.create_text(
    91.0,
    322.0,
    anchor="nw",
    text="Nome",
    fill="#000000",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    91.0,
    387.0,
    anchor="nw",
    text="Senha",
    fill="#000000",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    103.0,
    351.0,
    anchor="nw",
    text="Escreva seu nome",
    fill="#000000",
    font=("Inter ExtraLight", 10 * -1)
)

canvas.create_text(
    103.0,
    412.0,
    anchor="nw",
    text="Digite sua senha",
    fill="#000000",
    font=("Inter ExtraLight", 10 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=check_credentials,
    relief="flat"
)
button_1.place(
    x=97.0,
    y=471.0,
    width=234.0,
    height=32.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=97.0,
    y=518.0,
    width=234.0,
    height=32.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    213.0,
    360.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=95.0,
    y=343.0,
    width=236.0,
    height=32.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    213.0,
    421.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=95.0,
    y=404.0,
    width=236.0,
    height=32.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    175.0,
    243.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()
