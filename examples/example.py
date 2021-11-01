import easycanvas

canvas = easycanvas.canvas("Game", "white", 400, 250)
canvas.canvas.create_rectangle(10, 10, 50, 50, fill="black", outline="black")

while True:
    canvas.update()