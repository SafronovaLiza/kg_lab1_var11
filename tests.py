import unittest
from tkinter import *

from circle import MovingCircleApp


class TestMovingCircleApp(unittest.TestCase):
    def test_initial_circle(self):
        app = MovingCircleApp()
        self.assertEqual(app.circle_center_x, app.canvas_width // 2)
        self.assertEqual(app.circle_center_y, app.canvas_height // 2)
        self.assertEqual(app.circle_radius, 30)

    def test_move_circle(self):
        app = MovingCircleApp()
        app.move_circle()

    def test_change_color(self):
        app = MovingCircleApp()
        initial_color_index = app.circle_color_index
        app.change_color(None)
        self.assertNotEqual(app.circle_color_index, initial_color_index)

    def setUp(self):
        self.root = Tk()

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()