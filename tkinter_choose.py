from tkinter import *
from tkinter import filedialog

root = Tk()


def tkinter_choose():
    global lab
    global but
    global but1

    def callback():
        global name

        # Получаем путь к файлу
        name = filedialog.askopenfilename()
        if name[-3:] == 'csv' or name[-3:] == 'xls' or name[-4:] == 'xlsx':
            root.quit()  # Выходим из диалогового окна, если файл подходит по условию
        else:
            name = ''
            again()  # Если файл не удовлетворяет, то просим поменять путь в функции again()
            #  в again() мы также можем выйти без ошибок из диалогового окна

    def again():
        global lab
        global but
        global but1
        lab.destroy()
        but.destroy()
        but1.destroy()
        lab = Label(text='Sorry, the path is incorrect. Please, choose the other one', fg='black')
        but = Button(text="Choose", width=15, height=3, bg='gray', fg='white', command=callback)
        but1 = Button(text="Don't choose", width=15, height=3, bg='gray', fg='white', command=quiting)
        lab.pack()
        but1.pack(side='left')
        but.pack(side='right')

    def quiting():
        global name
        name = ''
        root.quit()

    # Создаем диалоговое окно
    root.geometry('360x360')
    lab = Label(text='Choose the path of csv-file', fg='black')
    but = Button(text="Choose", width=15, height=3, bg='gray', fg='white', command=callback)  # Кнопка выбора пути
    but1 = Button(text="Don't choose", width=15, height=3, bg='gray', fg='white', command=quiting)  # Кнопка выхода
    lab.pack()
    but1.pack(side='left')
    but.pack(side='right')
    root.mainloop()
    return name  # Возвращаем файл
