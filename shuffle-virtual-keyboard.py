#!/bin/python3

from tkinter import *
import random

root = Tk()  # Создаем основное окно

root.title("")  # Исправлено: корректный вызов метода

# Установка полноэкранного режима
root.attributes('-fullscreen', True)

# Функция для выхода из полноэкранного режима
def exit_fullscreen(event=None):
    root.attributes('-fullscreen', False)

# Привязываем клавишу Escape для выхода из полноэкранного режима
# root.bind('<Escape>', exit_fullscreen)
root.bind('<Escape>', lambda event: root.destroy())

frame1 = Frame(root)
frame1.pack()
# frame1 = Frame(root): создаёт новый контейнер-виджет Frame, который является дочерним к окну root. Он служит для группирования других виджетов внутри окна.
# frame1.pack(): размещает этот Frame в окне с помощью геометрического менеджера pack, т. е. добавляет его в окно и выстраивает в доступном пространстве (по умолчанию сверху вниз, по порядку вызова).

def select(value):
    if value == "Space":
        box.insert(INSERT, ' ')
    elif value == "Enter":
        box.insert(INSERT, '\n')
    elif value == "Tab":
        box.insert(INSERT, '    ')
    elif value == "CLEAR":
        box.delete("1.0", END)
    elif value in ("Backspace", "Back"):
        # Удаление символа слева от курсора (как клавиша Backspace)
        box.delete("insert-1c", "insert")
    else:
        box.insert(INSERT, value)

box = Text(frame1, height=20, font=("arial", 15), wrap=WORD)
box.grid(row=0, column=0)
# box.grid(row=0, column=0, pady=(20, 0))
# Альтернатива — задать паддинг для frame frame1: frame1.pack(pady=10).

buttons = [
'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О',
'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ы', 'Ъ', 'Ь', 'Э',
'Ю', 'Я', '.',  ',', ':', ';', '?', '!', 'Space', 'Back', 'CLEAR'
]

random.shuffle(buttons)

frame2 = Frame(root)
frame2.pack()

varRow = 4
varColumn = 0

for button in buttons:
    command = lambda x=button: select(x)
    if varRow != 8:
        Button(frame2, text=button, width=5, font=("arial", 10, "bold"),
               bg="black", fg="white", command=command).grid(row=varRow, column=varColumn)
    else:
        Button(frame2, text=button, width=100, bg="black", fg="white",
               command=command).grid(columnspan=40, row=varRow, column=varColumn)

    varColumn += 1

    if varColumn > 14 and varRow == 4:
        varColumn = 0
        varRow += 1
    if varColumn > 14 and varRow == 5:
        varColumn = 0
        varRow += 1
    if varColumn > 14 and varRow == 6:
        varColumn = 0
        varRow += 1
    if varColumn > 14 and varRow == 7:
        varColumn = 0
        varRow += 1

root.mainloop()
