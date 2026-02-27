#!/bin/python3

from tkinter import*
# AI_разные способы import_ python.html

import random

root = Tk()			# Создаем основное окно
# конструктор класса Tk, который создает основное окно приложения. Это окно будет служить контейнером для всех других виджетов (элементов интерфейса), которые вы добавите в ваше приложение.

		
root.title = ""
# root.config(bg = "white")
# root.config(bg = "white")
	# root.title(""); root.config(bg="white")

	# (lambda: (root.title(""), root.config(bg="white")))()

# # Устанавливаем полноэкранный режим
root.attributes('-fullscreen', True)

# # Если нужно, добавьте кнопку для выхода из полноэкранного режима
def exit_fullscreen(event=None):
    root.attributes('-fullscreen', False)

# # Привязываем клавишу Escape для выхода из полноэкранного режима
root.bind('<Escape>', exit)
	
# root.wm_iconbitmap(math.ico)
#root.resizable(0,0)
	# метод устанавливает возможность изменения размера окна.

    # Первый аргумент (0) отвечает за возможность изменения размера окна по горизонтали (ширине).
    # Второй аргумент (0) отвечает за возможность изменения размера окна по вертикали (высоте).

	# Таким образом, вызов root.resizable(0, 0) делает окно фиксированным, то есть пользователь не сможет изменять его размеры ни по ширине, ни по высоте. Если вы хотите разрешить изменение размера, вы можете установить значения в 1 (например, root.resizable(1, 1)).


frame1 = Frame(root)
frame1.pack()



def select(value):
	if value == "Space":
		box.insert(INSERT, '')
	elif value == "Enter":
		box.insert(INSERT, '\n')
	elif value == "Tab":
		box.insert(INSERT, '    ')
	elif value == "Back space":
		box.delete(1.0, END)
	else:
		box.insert(INSERT, value)



# appname=Label(root, text="klv",
				# font=("arial", 20, "bold"), bg="green", fg="white")

# appname.grid(row=0, columnspan=15)

	# Настройка grid для растягивания
# root.columnconfigure(0, weight=1)  # Устанавливаем вес для первого столбца
# Устанавливает вес для первого столбца, что позволяет ему растягиваться при изменении размера окна.

# label2 = tk.Label(frame2, text="Это Label в Frame с grid")
# label2.grid(row=0, column=0)


# box = Text(root, width=50,  font = ("arial", 15), wrap = WORD)
# box = Text(root, font = ("arial", 15), wrap = WORD)
# box = Text(frame1, height=40, font = ("arial", 15), wrap = WORD)
box = Text(frame1, height=20, font = ("arial", 15), wrap = WORD)
# # box.grid(row=1, columnspan=80)
box.grid(row=0, column=0)
# box.grid(row=0, columnspan=0)

	# # Создаем объект Text
	# text = tk.Text(root, wrap='word')
# box.grid(sticky='ew')  # Растягиваем по всем направлениям


	# # Настройка строк и столбцов для растягивания
# root.rowconfigure(0, weight=1)  # Устанавливаем вес для первой строки


buttons = [
	# '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Back space', '*',   
	'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О',
	'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ы', 'Ъ', 'Ь', 'Э',
	'Ю', 'Я', 'Space'
]
#print(buttons)
random.shuffle(buttons)
# print(buttons)
# список
# exit
varRow=4
varColumn=0

frame2 = Frame(root)
frame2.pack()


for button in buttons:
	command = lambda x = button: select(x)
		# создает анонимную функцию (лямбда-функцию), которая будет вызвана при определенном событии, например, при нажатии кнопки.
		
		# lambda x = button: это определение лямбда-функции, которая принимает один аргумент x. Значение по умолчанию для x — это переменная button. Это означает, что если при вызове функции не будет передано значение, то x будет равно button.
		
		# select(x): это вызов функции select, передавая ей аргумент x. Таким образом, когда лямбда-функция будет вызвана, она передаст значение button в функцию select.
		
	if varRow != 8:
		Button(frame2, text=button, width=5, font = ("arial", 10), bg="black", fg="white",
					command=command).grid(row=varRow,column=varColumn)
	if varRow == 8:
		Button(frame2, text=button, width=100, bg="black", fg="white",
					command=command).grid(columnspan=40, row=varRow,column=varColumn)
	
	varColumn+=1
	
	if varColumn > 14 and varRow == 4:
		varColumn = 0
		varRow+=1
	if varColumn > 14 and varRow == 5:
		varColumn = 0
		varRow+=1
	if varColumn > 14 and varRow == 6:
		varColumn = 0
		varRow+=1
	if varColumn > 14 and varRow == 7:
		varColumn = 0
		varRow+=1

#	print(varColumn)

mainloop()
