import tkinter, os

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

list1 = tkinter.Listbox(mainWindow)                     # CREATE LISTBOX
list1.grid(row=1,column=0, sticky='nsew', rowspan=2)    # PLACEMENT
list1.config(border=3, relief='solid')                  # STYLE
for i in os.listdir('/usr/bin'):                        # lis populated with list of dir...
    list1.insert(tkinter.END, i)

scroll_list1 = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=list1.yview) # where what act
scroll_list1.grid(row=1, column=1, sticky='nsw', rowspan=2)
list1['yscrollcommand'] = scroll_list1.set

# frame for radio buttons
radioB_frame = tkinter.LabelFrame(mainWindow, text='file details:')
radioB_frame.grid(row=1, column=2, sticky='ne')

# variable for choice for radio button. all have one variable - that determine 1 choice selection
# selecting one option deselect previous.
rbValue = tkinter.IntVar()
rbValue.set(3)
# radio buttons:
radio1 = tkinter.Radiobutton(radioB_frame, text='File', value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(radioB_frame, text='Path', value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(radioB_frame, text='Name', value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

mainWindow.mainloop()
