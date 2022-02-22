import tkinter


def parabola(numb: int) -> int:
    """
    Returns y equals x square
    :param numb: any int
    :return: y which is x square
    """
    numb_square = numb * numb / 50
    return numb_square


def draw_axes(canvas) -> None:
    """
    Draw axes x y
    :param canvas:
    :return:
    """
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canvas.create_line(0, -y_origin, 0, y_origin, fill="black")


def draw_plot(canvas, x: int, y: int) -> None:
    canvas.create_line(x, y, x + 1, y + 1, fill="red")


mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry('800x600')

canvas1 = tkinter.Canvas(mainWindow, width=800, height=600)
canvas1.grid(row=0, column=0)

draw_axes(canvas1)


for x in range(-100, 100):
    y = parabola(x)
    draw_plot(canvas1, x, -y)




mainWindow.mainloop()