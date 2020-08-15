# coding: utf-8

import rhinoscriptsyntax as rs


class Grid:

    def __init__(self, pts):
        self.pts = pts
        self.lines_along_x_grid = []
        self.lines_along_y_grid = []
        self.lines_along_z_grid = []

    # draw lines along the x-axis
    def draw_lines_along_x_grid(self, obj_layer):
        line1 = rs.AddLine(self.pts[0], self.pts[3])
        line2 = rs.AddLine(self.pts[1], self.pts[2])
        line3 = rs.AddLine(self.pts[4], self.pts[7])
        line4 = rs.AddLine(self.pts[5], self.pts[6])

        self.lines_along_x_grid += [line1, line2, line3, line4]

        rs.ObjectLayer(self.lines_along_x_grid, obj_layer)

    # draw lines along the y-axis
    def draw_lines_along_y_grid(self, obj_layer):
        line1 = rs.AddLine(self.pts[0], self.pts[1])
        line2 = rs.AddLine(self.pts[3], self.pts[2])
        line3 = rs.AddLine(self.pts[4], self.pts[5])
        line4 = rs.AddLine(self.pts[7], self.pts[6])

        self.lines_along_y_grid += [line1, line2, line3, line4]

        rs.ObjectLayer(self.lines_along_y_grid, obj_layer)

    # draw lines along the z-axis
    def draw_lines_along_z_grid(self, obj_layer):
        line1 = rs.AddLine(self.pts[0], self.pts[4])
        line2 = rs.AddLine(self.pts[1], self.pts[5])
        line3 = rs.AddLine(self.pts[2], self.pts[6])
        line4 = rs.AddLine(self.pts[3], self.pts[7])

        self.lines_along_z_grid += [line1, line2, line3, line4]

        rs.ObjectLayer(self.lines_along_z_grid, obj_layer)
