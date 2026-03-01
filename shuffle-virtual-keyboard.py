#!/bin/python3

import random
import os

from datetime import datetime  # если не импортировано ранее

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.constants import END


# ===============================================================

# def say_hello():
    # print("Hello!")

# Обработчик правого клика
def show_popup(event):
    # Позиция меню будет там, где курсор
    popup.tk_popup(event.x_root, event.y_root)

# Функция для выхода из полноэкранного режима
def exit_fullscreen(event=None):
    root.attributes('-fullscreen', False)


def save_text_to_file(text_widget: Text):
    """
    Сохраняет содержимое виджета Text в файл.
    Диалог выбора файла: имя и путь, формат определяется по расширению.
    """
    # Получаем текст из виджета (убираем финальный перевод строки, если он есть)
    content = text_widget.get("1.0", END)

    # Открываем диалог сохранения файла

    # file_path = filedialog.asksaveasfilename(
        # defaultextension=".txt",
        # filetypes=[
            # ("Text files", "*.txt"),
            # ("All files", "*.*")
        # ],
        # title="Сохранить как..."
    # )

    default_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    file_path = os.path.join(os.getcwd(), default_name)

    if not file_path:
        # Пользователь отменил сохранение
        return

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
    
        # messagebox.showinfo("Сохранено", f"Содержимое сохранено в:\n{file_path}")

    except Exception as e:
        messagebox.showerror("Ошибка сохранения", f"Не удалось сохранить файл:\n{e}")


# ===============================================================

root = Tk()  # Создаем основное окно

root.title("")  # Исправлено: корректный вызов метода

# Установка полноэкранного режима
root.attributes('-fullscreen', True)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"Screen width: {width}px, height: {height}px")


# ===============================================================

# Привязываем клавишу Escape для выхода из полноэкранного режима
# root.bind('<Escape>', exit_fullscreen)
root.bind('<Escape>', lambda event: root.destroy())

# Привязка к правому клику на окне
root.bind("<Button-3>", show_popup)  # Windows/Linux


# ===============================================================

frame1 = Frame(root)
# frame1.pack()
frame1.pack(fill=BOTH, expand=True)  # растягиваем контейнер


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

# Чтобы виджет Text занимал всю доступную ширину окна (соответственно и всей ширины экрана, если окно разворачивается до полного размера), нужно чтобы родительский контейнер expanding и менеджер геометрии растягивали его.

# box = Text(frame1, height=20, font=("arial", 15), wrap=WORD)
box = Text(frame1, height=20, font=("arial", 15), wrap=WORD,
               bg="#2b2b2b", fg="#e0e0e0", insertbackground="white")

# Дополнительно можно настроить подсветку выделения:
# Text.configure(selectbackground="#3e6b8a", selectforeground="white")

# box.pack(fill=BOTH, expand=True)
box.pack(fill=BOTH, expand=True, padx=(10, 10), pady=(10, 0))
# box.grid(row=0, column=0)
# box.grid(row=0, column=0, pady=(20, 0))
# Альтернатива — задать паддинг для frame frame1: frame1.pack(pady=10).

# ===============================================================

# Создаём контекстное меню
popup = Menu(root, tearoff=0)
# popup.add_command(label="Сохранить", command=say_hello)
# popup.add_command(label="Сохранить", command=save_text_to_file(box))
popup.add_command(label="Сохранить", command=lambda: save_text_to_file(box))
popup.add_separator()
popup.add_command(label="Выход", command=root.quit)

# ===============================================================

buttons = [
	'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О',
	'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ы', 'Ъ', 'Ь', 'Э',
	'Ю', 'Я', '.',  ',', ':', ';', '?', '!', 
	'Space', 'Space', 'Space', 'Space', 'Space', 'Space', 'Space', 'Space',
	'Back', 'CLEAR', 'Enter'
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
