#!/bin/python3

import random
import os

from datetime import datetime  # если не импортировано ранее

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.constants import END


# ===============================================================

def load_file_into_text(text_widget, filepath=None, encoding='utf-8'):
    """
    Загружает содержимое файла в указанный текстовый виджет (tk.Text).

    Args:
        text_widget: объект tkinter.Text — существующее текстовое поле.
        filepath: str | None — путь к файлу. Если None, откроется диалог выбора файла.
        encoding: str — кодировка файла (по умолчанию 'utf-8').
    """
    path = filepath
    if not path:
        path = filedialog.askopenfilename()
        if not path:
            return  # пользователь отменил выбор

    try:
        with open(path, 'r', encoding=encoding) as f:
            content = f.read()
    except Exception as e:
        text_widget.delete("1.0", END)
        text_widget.insert(END, f"Ошибка загрузки файла:\n{e}")
        return

    text_widget.delete("1.0", END)
    text_widget.insert(END, content)
    
 
# def show_notification(title, text, duration=3000):
def show_notification(text, duration=5000):
    pop = Toplevel(root)
    pop.wm_overrideredirect(True)  # без рамки окна
    pop.attributes("-topmost", True)

    # Размер и позиция попапа (обычно внизу справа)
    width, height = 320, 100
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    x = screen_w - width - 20
    # y = screen_h - height - 60
    y = 40
    pop.geometry(f"{width}x{height}+{x}+{y}")

    frame = Frame(pop, relief="raised", borderwidth=1)
    frame.pack(fill="both", expand=True)

    # Label(frame, text=title, font=("TkDefaultFont", 12, "bold")).pack(anchor="w", padx=10, pady=(8,0))
    Label(frame, text=text, wraplength=300).pack(anchor="w", padx=10, pady=(0,8))

    # Закрыть через duration миллисекунд
    pop.after(duration, pop.destroy)

# Обработчик правого клика
def show_popup(event):
    # Позиция меню будет там, где курсор
    popup.tk_popup(event.x_root, event.y_root)

# Функция для выхода из полноэкранного режима
def exit_fullscreen(event=None):
    root.attributes('-fullscreen', False)

def copy_all_text_to_clipboard(text_widget):
    """
    Копирует всё содержимое Text виджета в буфер обмена.
    text_widget: tkinter.Text
    """
    root = text_widget.winfo_toplevel()  # получить корневой/top-level виджет
    content = text_widget.get("1.0", "end-1c")  # весь текст без завершающего переноса
    root.clipboard_clear()
    root.clipboard_append(content)
    root.update()  # обновить буфер обмена



def flash_color():
    # Сохраняем исходный цвет фона окна
    global original_bg
    original_bg = root.cget("bg")

    # Меняем цвет главного окна
    root.config(bg="orange")  # любой нужный цвет
    # Через 3000 мс вернуть исходный цвет
    root.after(3000, restore_color)

def restore_color():
    root.config(bg=original_bg)
    
    
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

    flash_color()
    show_notification("Сохранено")
    # show_notification("Новое уведомление", "Произошло событие и здесь ваше сообщение.")


# ===============================================================

root = Tk()  # Создаем основное окно

root.title("")  # Исправлено: корректный вызов метода

# Установка полноэкранного режима
root.attributes('-fullscreen', True)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"Screen width: {width}px, height: {height}px")


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
popup.add_command(label="Копировать", command=lambda: copy_all_text_to_clipboard(box))
popup.add_command(label="Открыть", command=lambda: load_file_into_text(box))
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

# ===============================================================

# Привязываем клавишу Escape для выхода из полноэкранного режима
# root.bind('<Escape>', exit_fullscreen)
root.bind('<Escape>', lambda event: root.destroy())

# Привязка к правому клику на окне
root.bind("<Button-3>", show_popup)  # Windows/Linux

# Ctrl+C копирование всего текста
root.bind("<Control-c>", lambda e: copy_all_text_to_clipboard(box))

# Ctrl+S сохранить
# root.bind("<Control-s>", lambda e, w=box: save_text_to_file(w))
root.bind("<Control-s>", lambda e: save_text_to_file(box))

root.bind("<Control-o>", lambda e: load_file_into_text(box))

# ===============================================================

root.mainloop()
