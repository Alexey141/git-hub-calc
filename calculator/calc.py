from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("calculator")

def calc(Key):

    if Key == "=":
        str2 = "-+0123456789.*/)("                 # Разрешенные символы и цифры для ввода.
        if calc_entry.get()[0] not in str2:
            calc_entry.insert(END, " Error!")
            messagebox.showerror(" Ошибка!","Не верный ввод")
# Счёт
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" +str(result))
        except:
            calc_entry.insert(END, "!")
            messagebox.showerror(" Ошибка", "Проверьте правильность данных")

# Кнопка очистить поле ввода
    elif Key == "C":
        calc_entry.delete(0, END)

    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, Key)

# Создание кнопок в окне calculator.
bttn_list = [
    "7", "8", "9", "C",
    "4", "5", "6", "/",
    "1", "2", "3", "*",
    ".", "0", "+", "-",
    "="
    ]

r = 1
c = 0

for i in bttn_list:
    rel = ""
    cmd=lambda x=i:calc(x)
    ttk.Button(root, text=i, command=cmd).grid(row=r, column=c)
    c += 1
    if c>3:
        c=0
        r += 1

calc_entry = Entry(root, width=30)
calc_entry.grid(row=0, column=0, columnspan=5)

root.mainloop()
