from tkinter import*
# import tkinter as tk
import random

k_app = Tk()
# конструктор класса Tk, который создает основное окно приложения. Это окно будет служить контейнером для всех других виджетов (элементов интерфейса), которые вы добавите в ваше приложение.
# похоже на     
	# root = Tk()									# Создаем основное окно
		# =то же самое
		
k_app.title = ""
k_app.config(bg = "white")
# k_app.wm_iconbitmap(math.ico)
k_app.resizable(0,0)

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



# appname=Label(k_app, text="klv",
				# font=("arial", 20, "bold"), bg="green", fg="white")

# appname.grid(row=0, columnspan=15)

box = Text(k_app, width=50, height=20, font = ("arial", 15), wrap = WORD)
box.grid(row=1, columnspan=40)

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

for button in buttons:
	command = lambda x = button: select(x)
	if varRow !=8:
		Button(k_app, text=button, width=5, bg="black", fg="white",
					command=command).grid(row=varRow,column=varColumn)
	if varRow ==8:
		tk.Button(k_app, text=button, width=100, bg="black", fg="white",
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
		
		

mainloop()
