# coding: utf-8

import rhinoscriptsyntax as rs
from grid import Grid

# variable
x_num = 5
y_num = 5
z_num = 5

x_span = 100
y_span = 100
z_span = 100


def draw_grid_info(_origin_pt, _x_span, _y_span, _z_span, obj_layer):
    text = "X{0}Y{1}Z{2}".format(_x_span, _y_span, _z_span)
    place_point = [_origin_pt[0], _origin_pt[1] - 10, _origin_pt[2]]
    text_height = x_span / 10
    font = "Arial"
    font_style = 0  # 0: normal 1: bold 2: italic 3: bold and italic
    justification = 2

    obj_text = rs.AddText(text, place_point, text_height, font, font_style, justification)

    rs.ObjectLayer(obj_text, obj_layer)


rs.EnableRedraw(False)

# grid layer(parent)
grid_layer = rs.AddLayer("Grid", [0, 0, 0], True, False, None)

# text layer
text_layer = rs.AddLayer("Text", [0, 0, 0], True, False, grid_layer)

# point layer
point_layer = rs.AddLayer("Point", [0, 0, 0], True, False, grid_layer)

# line along the x-axis layer
line_x_axis_layer = rs.AddLayer("Line_x-axis", [0, 0, 0], True, False, grid_layer)

# line along the y-axis layer
line_y_axis_layer = rs.AddLayer("Line_y-axis", [0, 0, 0], True, False, grid_layer)

# line along the z-axis layer
line_z_axis_layer = rs.AddLayer("Line_z-axis", [0, 0, 0], True, False, grid_layer)

for i in range(x_num):
    for j in range(y_num):
        for k in range(z_num):
            origin_pt = [i * x_span, j * y_span, k * z_span]

            pts_of_grid = [
                origin_pt,  # pt1
                [origin_pt[0], origin_pt[1] + y_span, origin_pt[2]],  # pt2
                [origin_pt[0] + x_span, origin_pt[1] + y_span, origin_pt[2]],  # pt3
                [origin_pt[0] + x_span, origin_pt[1], origin_pt[2]],  # pt4
                [origin_pt[0], origin_pt[1], origin_pt[2] + z_span],  # pt5
                [origin_pt[0], origin_pt[1] + y_span, origin_pt[2] + z_span],  # pt6
                [origin_pt[0] + x_span, origin_pt[1] + y_span, origin_pt[2] + z_span],  # pt7
                [origin_pt[0] + x_span, origin_pt[1], origin_pt[2] + z_span],  # pt8
            ]

            # grid instance
            grid = Grid(pts_of_grid)

            # draw lines of the grid
            grid.draw_lines_along_x_grid(line_x_axis_layer)
            grid.draw_lines_along_y_grid(line_y_axis_layer)
            grid.draw_lines_along_z_grid(line_z_axis_layer)

            # draw grid information
            draw_grid_info(origin_pt, i, j, k, text_layer)

            if i == x_num - 1:
                place_pt = [origin_pt[0] + x_span, origin_pt[1], origin_pt[2]]
                draw_grid_info(place_pt, i + 1, j, k, text_layer)
            if j == y_num - 1:
                place_pt = [origin_pt[0], origin_pt[1] + y_span, origin_pt[2]]
                draw_grid_info(place_pt, i, j + 1, k, text_layer)
            if k == z_num - 1:
                place_pt = [origin_pt[0], origin_pt[1], origin_pt[2] + z_span]
                draw_grid_info(place_pt, i, j, k + 1, text_layer)
            if i == x_num - 1 and j == y_num - 1:
                place_pt = [origin_pt[0] + x_span, origin_pt[1] + y_span, origin_pt[2]]
                draw_grid_info(place_pt, i + 1, j + 1, k, text_layer)

rs.EnableRedraw(True)
