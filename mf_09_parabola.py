import tkinter


def parabola(canvas, size):
    # parabola(numb: int) -> float:
    """
    Returns y equals x square
    :param canvas: any int
    :param size:
    """
    for x in range(size):
        y = x * x / size
        draw_plot(canvas, x, y)
        draw_plot(canvas, -x, y)

    # numb_square = numb * numb / 50
    # return numb_square


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
    canvas.create_line(x, -y, x + 1, -y + 1, fill="red")


mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry('800x600')

canvas1 = tkinter.Canvas(mainWindow, width=800, height=600)
canvas1.grid(row=0, column=0)

draw_axes(canvas1)
parabola(canvas1, 100)
parabola(canvas1, 50)

mainWindow.mainloop()
