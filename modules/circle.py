from tkinter import *
import random

root = Tk()
root.title("Moving Circle")

# Задаем холст
canvas_width = 600
canvas_height = 400
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Задаем круг
circle_radius = 30
circle_center_x = canvas_width // 2
circle_center_y = canvas_height // 2
circle_color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
circle_color_index = 0
circle_color = circle_color_list[circle_color_index]
circle = canvas.create_oval(circle_center_x - circle_radius, circle_center_y - circle_radius,
                            circle_center_x + circle_radius, circle_center_y + circle_radius,
                            fill=circle_color)

# Задаем шаг при перемещении и направления
step_size = 10
x_direction = 0
y_direction = 0


# Функция для перемещения круга
def move_circle():
    global circle_center_x, circle_center_y

    new_x = circle_center_x + x_direction * step_size
    new_y = circle_center_y + y_direction * step_size

    # Проверка, достиг ли круг границ холста, если достиг - движение не происходит
    if new_x - circle_radius >= 0 and new_x + circle_radius <= canvas_width:
        circle_center_x = new_x
    if new_y - circle_radius >= 0 and new_y + circle_radius <= canvas_height:
        circle_center_y = new_y

    canvas.coords(circle, circle_center_x - circle_radius, circle_center_y - circle_radius,
                  circle_center_x + circle_radius, circle_center_y + circle_radius)

    root.after(50, move_circle)
move_circle()


# Функция для изменения образца закраски круга
def change_color(event):
    global circle_color_index, circle_color

    # Циклическое изменение образца
    circle_color_index = (circle_color_index + 1) % len(circle_color_list)
    circle_color = circle_color_list[circle_color_index]

    # Изменяем образец закраски круга
    canvas.itemconfig(circle, fill=circle_color)


# Привязка кнопок PgUp и PgDn к функции change_color
root.bind("<Prior>", change_color)
root.bind("<Next>", change_color)


# Настройка привязок клавиш для перемещения
def move_left(event):
    global x_direction
    x_direction = -1


def move_right(event):
    global x_direction
    x_direction = 1


def move_up(event):
    global y_direction
    y_direction = -1


def move_down(event):
    global y_direction
    y_direction = 1


def stop_move(event):
    global x_direction, y_direction
    x_direction = 0
    y_direction = 0


# Привязываем функции к событиям клавиатуры
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)
root.bind("<KeyRelease>", stop_move)


# Выход из программы при нажатии esc
def exit_program(event):
    root.destroy()


root.bind("<Escape>", exit_program)

# Изменение радиуса
radius_label = Label(root, text="Радиус:")
radius_label.pack(side=LEFT, padx=5, pady=5)
radius_entry = Entry(root)
radius_entry.pack(side=LEFT, padx=5, pady=5)


def apply_radius():
    global circle_radius
    try:
        new_radius = int(radius_entry.get())
        if new_radius > 0:
            circle_radius = new_radius
            canvas.coords(circle, circle_center_x - circle_radius, circle_center_y - circle_radius,
                          circle_center_x + circle_radius, circle_center_y + circle_radius)
    except ValueError:
        pass


apply_button = Button(root, text="Применить", command=apply_radius)
apply_button.pack(side=LEFT, padx=5, pady=5)

root.mainloop()