import tkinter

def parabola(x: int) -> int:
    """Returns y equals x square

    :param x: any int
    :return: y which is x square
    """
    y = x * x
    return y


def draw_axes(canvas) -> None:
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="red")
    canvas.create_line(0, -y_origin, 0, y_origin, fill="red")


mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry('800x600')

canvas = tkinter.Canvas(mainWindow, width=800, height=600)
canvas.grid(row=0, column=0)

draw_axes(canvas)

for x in range(-100, 100):
    y = parabola(x)
    print(y)




mainWindow.mainloop()