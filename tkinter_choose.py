from tkinter import *
from tkinter import filedialog

root = Tk()

def tkinter_choose():

    def callback():
        global name

        name = filedialog.askopenfilename()
        if name[-3:] == 'csv' or name[-3:] == 'xls' or name[-4:] == 'xlsx':
            root.quit()
        else:
            name = ''
            again()

    def again():
        global lab
        global but
        lab.destroy()
        but.destroy()
        lab = Label(text='Sorry, the path is incorrect. Please, choose the other one', fg='black')
        but = Button(text="Choose", width=15, height=3, bg='gray', fg='white', command=callback)
        lab.pack()
        but.pack()
    def quiting():
        global name
        name = ''
        root.quit()
    root.geometry('360x360')
    lab = Label(text='Choose the path of csv-file', fg='black')
    but = Button(text="Choose", width=15, height=3, bg='gray', fg='white', command=callback)
    but1 = Button(text="Quit", width=15, height=3, bg='gray', fg='white', command=quiting)
    lab.pack()
    but1.pack(side='left')
    but.pack(side='right')
    root.mainloop()
    return name
