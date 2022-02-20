import tkinter

# print(tkinter.TkVersion)
# tkinter._test()
mainWindow = tkinter.Tk()
mainWindow.title("My first Window")
mainWindow.geometry('800x600-1000-1000') # add +/- to set offset of window

label = tkinter.Label(mainWindow, text="Text visible in Label1")
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.pack(side='left', anchor='n')

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='left', anchor='n', expand=True)

button1 = tkinter.Button(rightFrame, text='Button_1')
button2 = tkinter.Button(rightFrame, text='Button_2')
button3 = tkinter.Button(rightFrame, text='Button_3')
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')


mainWindow.mainloop()
