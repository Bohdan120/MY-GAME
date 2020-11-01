from tkinter import *
window = Tk()
def jump(event):
    jump_action()

def jump_action():
    global ball_x
    global ball_y
    global dx
    global dy
    ball_y = ball_y + dy
    if ball_y > 140 or ball_y < 0:
        dy = - dy
    canvas.coords(ball, ball_x, ball_y, ball_x + 50, ball_y + 50)
    window.after(40, jump_action)
    if ball_y > 140 or ball_y < 0:
        dy = 0



def draw_triangles(count_rows):
    global rects
    triangle_y = 0
    for i in range(count_rows):
        triangle_x = 0
        while triangle_x + 60 <= 600:
            triangle = canvas.create_polygon(triangle_x, triangle_y, triangle_x + 60, triangle_y, triangle_x, triangle_y, fill="red", width="3", outline="red")
            triangles.append(triangle)
            triangle_x = triangle_x + 60
        triangle_y = triangle_y + 30
canvas = Canvas(window, width=600, height=200, bg="orange")
canvas.pack()
dy = 10
dx = 10
ball_x = 0
ball_y = 0
triangles = []
draw_triangles(1)
ball = canvas.create_oval(ball_x, ball_y, ball_x + 50, ball_y + 50, fill="yellow", outline= "yellow")

window.bind("<Up>", jump)
window.mainloop()







'''
def draw_rects(count_rows):
    global rects
    rect_y = 0
    for i in range(count_rows):
        rect_x = 0
        while rect_x + 60 <= 600:
            rect = canvas.create_rectangle(rect_x, rect_y, rect_x + 60, rect_y + 30, fill="pink", width="3", outline="blue")
            rects.append(rect)
            rect_x = rect_x + 60
        rect_y = rect_y + 30

rects = []

draw_rects(1)
'''


















