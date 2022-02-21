import tkinter
# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry('900x900+100+100')  # add +/- to set offset of window
mainWindow['padx'] = 8


for i in range(6):
    mainWindow.columnconfigure(i, weight=1)
# mainWindow.columnconfigure(1, weight=1)
# mainWindow.columnconfigure(2, weight=1)
# mainWindow.columnconfigure(3, weight=1)

for i in range(8):
    mainWindow.rowconfigure(i, weight=1)
# mainWindow.rowconfigure(1, weight=1)
# mainWindow.rowconfigure(2, weight=1)
# mainWindow.rowconfigure(3, weight=1)
# mainWindow.rowconfigure(4, weight=1)
# mainWindow.rowconfigure(6, weight=1)

resultEntry = tkinter.Entry(mainWindow)
resultEntry.grid(row=0, column=0, columnspan=4, sticky='nsew')

buttonC = tkinter.Button(mainWindow, text='C')
buttonCe = tkinter.Button(mainWindow, text='Ce')
button0 = tkinter.Button(mainWindow, text='0')
button1 = tkinter.Button(mainWindow, text='1')
button2 = tkinter.Button(mainWindow, text='2')
button3 = tkinter.Button(mainWindow, text='3')
button4 = tkinter.Button(mainWindow, text='4')
button5 = tkinter.Button(mainWindow, text='5')
button6 = tkinter.Button(mainWindow, text='6')
button7 = tkinter.Button(mainWindow, text='7')
button8 = tkinter.Button(mainWindow, text='8')
button9 = tkinter.Button(mainWindow, text='9')
button_plus = tkinter.Button(mainWindow, text='=')
button_minus = tkinter.Button(mainWindow, text='-')
button_asterix = tkinter.Button(mainWindow, text='*')
button_division = tkinter.Button(mainWindow, text='/')
button_equal = tkinter.Button(mainWindow, text='=')
buttonC.grid(row=1, column=0, sticky='nsew')
buttonCe.grid(row=1, column=1, sticky='nsew')
button0.grid(row=5, column=0, sticky='nsew')
button1.grid(row=4, column=0, sticky='nsew')
button2.grid(row=4, column=1, sticky='nsew')
button3.grid(row=4, column=2, sticky='nsew')
button4.grid(row=3, column=0, sticky='nsew')
button5.grid(row=3, column=1, sticky='nsew')
button6.grid(row=3, column=2, sticky='nsew')
button7.grid(row=2, column=0, sticky='nsew')
button8.grid(row=2, column=1, sticky='nsew')
button9.grid(row=2, column=2, sticky='nsew')
button_plus.grid(row=2, column=3, sticky='nsew')
button_minus.grid(row=3, column=3, sticky='nsew')
button_asterix.grid(row=4, column=3, sticky='nsew')
button_division.grid(row=5, column=3, sticky='nsew')
button_equal.grid(row=5, column=1, sticky='nsew', columnspan=2)


mainWindow.mainloop()
