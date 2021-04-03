import cv2
import numpy as np
from win32api import GetSystemMetrics
from engine.physics import Body
import sys


class Planet(Body):
    def __init__(self, mass, starting_speed, starting_position, color, size=11):
        super().__init__(mass, starting_speed, starting_position)
        self.color = color
        self.size = size


class Window:
    def __init__(self, name, size=None):
        self.name = name
        if size is None:
            self.screen = np.zeros((GetSystemMetrics(1), GetSystemMetrics(0), 3), np.uint8)
            cv2.namedWindow(name, cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty(name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        else:
            self.screen = np.zeros((size[1], size[0], 3), np.uint8)

    def erase_body(self, body):
        x = round(body.old_position[0])
        y = round(body.old_position[1])
        position = (x, y)
        self.screen = cv2.circle(self.screen, position, body.size, (0, 0, 0), -1)

    def draw_body(self, body):
        x = round(body.position[0])
        y = round(body.position[1])
        position = (x, y)
        self.screen = cv2.circle(self.screen, position, body.size, body.color, -1)

    def update_screen(self, bodies):
        for body in bodies:
            self.erase_body(body)
            self.draw_body(body)

    def show_screen(self):
        cv2.imshow(self.name, self.screen)


def start_simulation(time_step=0.2, screen_size=None):
    win = Window("Simulation", screen_size)
    while True:
        if cv2.waitKey(1) + 0x00 == ord('q'):
            sys.exit()

        Planet.update_simulation(time_step)
        win.update_screen(Planet.bodies)
        Planet.update_bodies()
        win.show_screen()


if __name__ == "__main__":
    win = Window("window")
    win.show_screen()
    while True:
        if cv2.waitKey() + 0x00 == ord('q'):
            break



