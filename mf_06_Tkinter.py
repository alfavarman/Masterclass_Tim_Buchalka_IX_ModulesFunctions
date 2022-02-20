import tkinter

# print(tkinter.TkVersion)
# tkinter._test()
mainWindow = tkinter.Tk()
mainWindow.title("My first Window")
mainWindow.geometry('800x600-1000-1000') # add +/- to set offset of window

# label = tkinter.Label(mainWindow, text="Text visible in Label1")
# label.pack(side='top')
#
# leftFrame = tkinter.Frame(mainWindow)
# leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)
#
# canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
# canvas.pack(side='left', anchor='n')
#
# rightFrame = tkinter.Frame(mainWindow)
# rightFrame.pack(side='left', anchor='n', expand=True)
#
# button1 = tkinter.Button(rightFrame, text='Button_1')
# button2 = tkinter.Button(rightFrame, text='Button_2')
# button3 = tkinter.Button(rightFrame, text='Button_3')
# button1.pack(side='top')
# button2.pack(side='top')
# button3.pack(side='top')

label = tkinter.Label(mainWindow, text="Text visible in Label1")
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky='n')

button1 = tkinter.Button(rightFrame, text='Button_1')
button2 = tkinter.Button(rightFrame, text='Button_2')
button3 = tkinter.Button(rightFrame, text='Button_3')
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# CONFIGURE COLUMNS
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

rightFrame.columnconfigure(0, weight=1)
button3.grid(sticky='ew')               # won't work until column weigh is set

mainWindow.mainloop()
