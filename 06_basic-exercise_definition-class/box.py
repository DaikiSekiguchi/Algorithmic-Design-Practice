# coding: utf-8

import rhinoscriptsyntax as rs


class Box:

    def __init__(self, origin, width, depth, height):
        self.origin = origin
        self.width = width
        self.depth = depth
        self.height = height

    def draw_box(self):
        pts = [
            [self.origin[0], self.origin[1], self.origin[2]],
            [self.origin[0] + self.width, self.origin[1], self.origin[2]],
            [self.origin[0] + self.width, self.origin[1] + self.depth, self.origin[2]],
            [self.origin[0], self.origin[1] + self.depth, self.origin[2]],
            [self.origin[0], self.origin[1], self.origin[2] + self.height],
            [self.origin[0] + self.width, self.origin[1], self.origin[2] + self.height],
            [self.origin[0] + self.width, self.origin[1] + self.depth, self.origin[2] + self.height],
            [self.origin[0], self.origin[1] + self.depth, self.origin[2] + self.height],
        ]

        # drawing a box based on pts
        rs.AddBox(pts)

    def draw_box_info(self):
        text = "w: {0} d: {1} h: {2}".format(self.width, self.depth, self.height)
        place_point = [self.origin[0], self.origin[1] - 100, self.origin[2]]
        text_height = 50
        font = "Arial"
        font_style = 0  # 0: normal 1: bold 2: italic 3: bold and italic
        justification = None

        rs.AddText(text, place_point, text_height, font, font_style, justification)
