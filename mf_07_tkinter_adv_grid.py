import tkinter

mainWindow = tkinter.Tk()
mainWindow.title("Advanced Grid")
mainWindow.geometry('800x600-100-100')  # add +/- to set offset of window

label1 = tkinter.Label(mainWindow, text='This is label1 txt')
label1.grid(row=0, column=0, columnspan=3)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)



mainWindow.mainloop()
