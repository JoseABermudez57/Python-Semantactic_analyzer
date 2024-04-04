from pathlib import Path
from operations.syntactic_analyzer import analyze_syntax
from operations.lexical_analyzer.lexer import Lexer

from tkinter import Tk, Canvas, Text, Button, PhotoImage, END, NORMAL, DISABLED

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/main_frame")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("850x650")
window.configure(bg="#FFFFFF")


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=650,
    width=850,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    425.0,
    325.0,
    image=image_image_1
)


def insert_syntactic_result_text():
    entry_2.config(state=NORMAL)
    entry_2.delete('1.0', END)
    result = []
    result_show = []
    lexer = Lexer(entry_1.get(1.0, END))
    token = lexer.next_token()
    t, lexeme = token
    format_token = f'TOKEN: {t} - LEXEMA: {lexeme}'
    while t is not None and lexeme is not None:
        result_show.append(format_token)
        result.append((t, lexeme))
        token = lexer.next_token()
        t, lexeme = token
        format_token = f'TOKEN: {t} - LEXEMA: {lexeme}'
    result_syntactic = analyze_syntax(result)
    result_show.insert(0, result_syntactic)
    entry_2.insert(END, "\n".join(map(str, result_show)))
    entry_2.config(state=DISABLED)


def insert_code_result_text():
    entry_3.config(state=NORMAL)
    entry_3.insert(END, "Texto insertado desde el código\n")
    entry_3.config(state=DISABLED)


def clean_text_areas():
    entry_2.config(state=NORMAL)
    entry_3.config(state=NORMAL)
    entry_1.delete(1.0, END)
    entry_2.delete(1.0, END)
    entry_3.delete(1.0, END)
    entry_2.config(state=DISABLED)
    entry_3.config(state=DISABLED)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=insert_syntactic_result_text,
    relief="flat"
)
button_1.place(
    x=37.0,
    y=584.0,
    width=137.0,
    height=36.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=clean_text_areas,
    relief="flat"
)
button_2.place(
    x=200.0,
    y=584.0,
    width=166.25196838378906,
    height=36.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    202.5,
    360.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#000000",
    fg="#FFFFFF",
    insertbackground='#FFFFFF',
    highlightthickness=0
)
entry_1.place(
    x=55.0,
    y=173.0,
    width=295.0,
    height=373.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    628.0,
    206.5,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#000000",
    fg="#FFFFFF",
    insertbackground='#FFFFFF',
    state='disabled',
    highlightthickness=0
)
entry_2.place(
    x=457.0,
    y=112.0,
    width=342.0,
    height=187.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    628.0,
    480.5,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#000000",
    fg="#FFFFFF",
    insertbackground='#FFFFFF',
    state='disabled',
    highlightthickness=0
)
entry_3.place(
    x=457.0,
    y=406.0,
    width=342.0,
    height=147.0
)


def run_app():
    window.title("Semantic Analizer")
    window.resizable(False, False)
    window.mainloop()
