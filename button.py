import pygame
import global_button_config as conf
import timer
from texture import Texture

class Button:
    def __init__(self, name, pos, path="", extension="png", scales=(1,1,1), wait_time=conf.wait_time, offsets=conf.offsets):
        self.name = name
        self.path = path
        self.extension = extension
        self.scales = scales
        self.pos = pos

        self.timer = timer.Timer()
        self.wait_time = wait_time

        self.inactive = Texture(name + "_inactive", offset=offsets[0], scale=scales[0], path=path, extension=extension)
        self.hover = Texture(name + "_hover", offset=offsets[1], scale=scales[1], path=path, extension=extension)
        self.clicked = Texture(name + "_clicked", offset=offsets[2], scale=scales[2], path=path, extension=extension)

        self.inactive_rect = self.inactive.image.get_rect()
        self.hover_rect = self.hover.image.get_rect()
        self.clicked_rect = self.clicked.image.get_rect()

        self.inactive_rect.center = (self.pos[0] + self.inactive.offset[0], self.pos[1] + self.inactive.offset[1])
        self.hover_rect.center = (self.pos[0] + self.hover.offset[0], self.pos[1] + self.hover.offset[1])
        self.clicked_rect.center = (self.pos[0] + self.clicked.offset[0], self.pos[1] + self.clicked.offset[1])

        self.active = False
        self.is_clicked = False
        self.is_hover = False

    def rescale(self, scales):
        self.scales = scales

        self.inactive.rescale(self.scales[0])
        self.hover.rescale(self.scales[1])
        self.clicked.rescale(self.scales[2])

        self.inactive_rect = self.inactive.image.get_rect()
        self.hover_rect = self.hover.image.get_rect()
        self.clicked_rect = self.clicked.image.get_rect()

        self.inactive_rect.center = (self.pos[0] + self.inactive.offset[0], self.pos[1] + self.inactive.offset[1])
        self.hover_rect.center = (self.pos[0] + self.hover.offset[0], self.pos[1] + self.hover.offset[1])
        self.clicked_rect.center = (self.pos[0] + self.clicked.offset[0], self.pos[1] + self.clicked.offset[1])

    def update(self, button):
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()

        if self.inactive_rect.collidepoint(mouse_pos):
            self.is_hover = True

            if mouse_buttons[button]:
                if not self.is_clicked:
                    self.timer.startTimer()

                self.is_clicked = True

                self.active = self.timer.getTimer() > self.wait_time and self.timer.getTimer() < self.wait_time + 0.1

            else:
                self.is_clicked = False
                self.active = False

        else:
            self.is_hover = False
            self.is_clicked = False
            self.active = False

    def get_active_texture(self):
        if self.is_clicked:
            return self.clicked.image
        elif self.is_hover:
            return self.hover.image
        return self.inactive.image

    def get_active_rect(self):
        if self.is_clicked:
            return self.clicked_rect
        elif self.is_hover:
            return self.hover_rect
        return self.inactive_rect