import tkinter, os
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



# for i in range(18):
    # button.append(i) = tkinter.Button(mainWindow)

#
# list1 = tkinter.Listbox(mainWindow)                     # CREATE LISTBOX
# list1.grid(row=1,column=0, sticky='nsew', rowspan=2)    # PLACEMENT
# list1.config(border=3, relief='solid')                  # STYLE
# for i in os.listdir('/usr/bin'):                        # lis populated with list of dir...
#     list1.insert(tkinter.END, i)
#
# scroll_list1 = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=list1.yview) # where what act
# scroll_list1.grid(row=1, column=1, sticky='nsw', rowspan=2)
# list1['yscrollcommand'] = scroll_list1.set
#
# # frame for radio buttons
# radioB_frame = tkinter.LabelFrame(mainWindow, text='file details:')
# radioB_frame.grid(row=1, column=2, sticky='ne')
#
# # variable for choice for radio button. all have one variable - that determine 1 choice selection
# # selecting one option deselect previous.
# rbValue = tkinter.IntVar()
# rbValue.set(3)
# # radio buttons:
# radio1 = tkinter.Radiobutton(radioB_frame, text='File', value=1, variable=rbValue)
# radio2 = tkinter.Radiobutton(radioB_frame, text='Path', value=2, variable=rbValue)
# radio3 = tkinter.Radiobutton(radioB_frame, text='Name', value=3, variable=rbValue)
# radio1.grid(row=0, column=0, sticky='w')
# radio2.grid(row=1, column=0, sticky='w')
# radio3.grid(row=2, column=0, sticky='w')
#
#
# # label for result
# resultLabel = tkinter.Label(mainWindow, text='Result')
# resultLabel.grid(row=2, column=2, sticky='nw')
#
# # entry field
# resultEntry = tkinter.Entry(mainWindow)
# resultEntry.grid(row=2, column=2, sticky='sw')
#
# # label frame time
# time_Frame2 = tkinter.LabelFrame(mainWindow, text='Time')
# time_Frame2.grid(row=3, column=0, sticky='new')
#
# # 3 spin boxes inside frame
# hourSpinner = tkinter.Spinbox(time_Frame2, width=2, values=tuple(range(0, 24)))
# minuteSpinner = tkinter.Spinbox(time_Frame2, width=2, from_=0, to=59)
# secondSpinner = tkinter.Spinbox(time_Frame2, width=2, from_=0, to=59)
# hourSpinner.grid(row=0, column=0,)
# tkinter.Label(time_Frame2, text=':').grid(row=0, column=1)
# minuteSpinner.grid(row=0, column=2)
# tkinter.Label(time_Frame2, text=':').grid(row=0, column=3)
# secondSpinner.grid(row=0, column=4)
#
# # Frame for date spinner
# frame3_date = tkinter.Frame(mainWindow)
# frame3_date.grid(row=5, column=0, sticky='new')
# # Data Labels
# dayLabel = tkinter.Label(frame3_date, text='Day')
# monthLabel = tkinter.Label(frame3_date, text='Month')
# yearLabel = tkinter.Label(frame3_date, text='Year')
# dayLabel.grid(row=0, column=0)
# monthLabel.grid(row=0, column=1)
# yearLabel.grid(row=0, column=2)
# # Spinners
# daySpinner = tkinter.Spinbox(frame3_date, width=5, from_=1, to=31)
# monthSpinner = tkinter.Spinbox(frame3_date, width=5, values=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# yearSpinner = tkinter.Spinbox(frame3_date, width=5, from_=1990, to=2099)
# daySpinner.grid(row=0, column=0)
# monthSpinner.grid(row=0, column=1)
# yearSpinner.grid(row=0, column=2)
#
# # Ok and Cancel buttons
# okButton = tkinter.Button(mainWindow, text='Ok')
# cancelButton = tkinter.Button(mainWindow, text='Cancel', command=mainWindow.destroy)
# okButton.grid(row=4, column=3, sticky='e')
# cancelButton.grid(row=4, column=4, sticky='w')


mainWindow.mainloop()
