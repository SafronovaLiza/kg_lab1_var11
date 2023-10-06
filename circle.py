from tkinter import *

class MovingCircleApp:
    def __init__(self):
        """
        Инициализация приложения MovingCircleApp.

        Создает главное окно и устанавливает начальные значения для свойств холста и круга.
        Привязывает функции к событиям клавиатуры и настраивает изменение радиуса.

        Параметры:
            Нет.

        """
        self.root = Tk()
        self.root.title("Moving Circle")

        self.canvas_width = 600
        self.canvas_height = 400
        self.canvas = Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        self.circle_radius = 30
        self.circle_center_x = self.canvas_width // 2
        self.circle_center_y = self.canvas_height // 2
        self.circle_color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.circle_color_index = 0
        self.circle_color = self.circle_color_list[self.circle_color_index]
        self.circle = self.canvas.create_oval(
            self.circle_center_x - self.circle_radius, self.circle_center_y - self.circle_radius,
            self.circle_center_x + self.circle_radius, self.circle_center_y + self.circle_radius,
            fill=self.circle_color
        )

        self.step_size = 10
        self.x_direction = 0
        self.y_direction = 0

        self.move_circle()

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<KeyRelease>", self.stop_move)
        self.root.bind("<Escape>", self.exit_program)
        self.root.bind("<Prior>", self.change_color)
        self.root.bind("<Next>", self.change_color)

        self.radius_label = Label(self.root, text="Радиус:")
        self.radius_label.pack(side=LEFT, padx=5, pady=5)
        self.radius_entry = Entry(self.root)
        self.radius_entry.pack(side=LEFT, padx=5, pady=5)

        self.apply_button = Button(self.root, text="Применить", command=self.apply_radius)
        self.apply_button.pack(side=LEFT, padx=5, pady=5)

    def move_circle(self):
        """
        Перемещает круг по холсту с заданным шагом и направлением.

        При каждом перемещении проверяет, не достиг ли круг границы холста.
        Если достиг, то перемещение не происходит.

        Параметры:
            Нет.

        """
        new_x = self.circle_center_x + self.x_direction * self.step_size
        new_y = self.circle_center_y + self.y_direction * self.step_size

        if new_x - self.circle_radius >= 0 and new_x + self.circle_radius <= self.canvas_width:
            self.circle_center_x = new_x
        if new_y - self.circle_radius >= 0 and new_y + self.circle_radius <= self.canvas_height:
            self.circle_center_y = new_y

        self.canvas.coords(self.circle, self.circle_center_x - self.circle_radius, self.circle_center_y - self.circle_radius,
                    self.circle_center_x + self.circle_radius, self.circle_center_y + self.circle_radius)

        self.root.after(50, self.move_circle)

    def change_color(self, event):
        """
        Изменяет цвет круга при каждом вызове функции.

        Перебирает список доступных цветов и изменяет цвет круга на следующий цвет из списка.

        Параметры:
            event: объект события. Игнорируется.

        """
        self.circle_color_index = (self.circle_color_index + 1) % len(self.circle_color_list)
        self.circle_color = self.circle_color_list[self.circle_color_index]

        self.canvas.itemconfig(self.circle, fill=self.circle_color)

    def move_left(self, event):
        """
        Устанавливает направление движения круга влево.

        Параметры:
            event: объект события. Игнорируется.

        """
        self.x_direction = -1

    def move_right(self, event):
        """
        Устанавливает направление движения круга вправо.

        Параметры:
            event: объект события. Игнорируется.

        """
        self.x_direction = 1

    def move_up(self, event):
        """
        Устанавливает направление движения круга вверх.

        Параметры:
            event: объект события. Игнорируется.

        """
        self.y_direction = -1

    def move_down(self, event):
        """
        Устанавливает направление движения круга вниз.

        Параметры:
            event: объект события. Игнорируется.

        """
        self.y_direction = 1

    def stop_move(self, event):
        """
        Останавливает движение круга.

        Параметры:
            event: объект события. Игнорируется.

        """
        self.x_direction = 0
        self.y_direction = 0

    def exit_program(self, event):
        """
        Завершает работу программы при нажатии клавиши Esc.

        Параметры:
            event: объект события. Игнорируется.

        """
        self.root.destroy()

    def apply_radius(self):
        """
        Применяет новый радиус круга.

        Получает новый радиус из текстового поля ввода и применяет его, если он больше нуля.

        Параметры:
            Нет.

        """
        try:
            new_radius = int(self.radius_entry.get())
            if new_radius > 0:
                self.circle_radius = new_radius
                self.canvas.coords(self.circle, self.circle_center_x - self.circle_radius,
                                   self.circle_center_y - self.circle_radius,
                                   self.circle_center_x + self.circle_radius, self.circle_center_y + self.circle_radius)
        except ValueError:
            pass

    def start(self):
        """
        Запускает главный цикл приложения.

        Параметры:
            Нет.

        """
        self.root.mainloop()


app = MovingCircleApp()
app.start()
