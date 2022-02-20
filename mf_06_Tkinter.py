import tkinter

print(tkinter.TkVersion)

# tkinter._test()
mainWindow = tkinter.Tk()
mainWindow.title("My frirst Window")
mainWindow.geometry('640x480-1000-1000') # add +/- to set offset of window
mainWindow.mainloop()
