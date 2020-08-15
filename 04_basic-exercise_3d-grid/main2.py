# coding: utf-8

import rhinoscriptsyntax as rs
from System.Drawing import Color

# variable
x_num = 5
y_num = 5
z_num = 5

x_span = 100
y_span = 100
z_span = 100


def draw_grid_info(_origin_pt, _x_span, _y_span, _z_span, layer):
    text = "X{0}Y{1}Z{2}".format(_x_span, _y_span, _z_span)
    place_point = [_origin_pt[0], _origin_pt[1] - 10, _origin_pt[2]]
    text_height = x_span / 10
    font = "Arial"
    font_style = 0  # 0: normal 1: bold 2: italic 3: bold and italic
    justification = 2

    text_id = rs.AddText(text, place_point, text_height, font, font_style, justification)
    rs.ObjectLayer(text_id, layer)


def draw_grid_line(_start_pt, _end_pt, layer):
    line_id = rs.AddLine(_start_pt, _end_pt)
    rs.ObjectLayer(line_id, layer)


def draw_grid_point(_pt, layer):
    point_id = rs.AddPoint(_pt)
    rs.ObjectLayer(point_id, layer)


rs.EnableRedraw(False)

# grid layer(parent)
grid_layer = rs.AddLayer("Grid", [0, 0, 0], True, False, None)

# text layer
text_layer = rs.AddLayer("Text", [0, 0, 0], True, False, grid_layer)

# point layer
point_layer = rs.AddLayer("Point", [0, 0, 0], True, False, grid_layer)

# line along the x-axis layer
line_x_axis_layer = rs.AddLayer("Line_x-axis", [255, 0, 0], True, False, grid_layer)

# line along the y-axis layer
line_y_axis_layer = rs.AddLayer("Line_y-axis", [0, 255, 0], True, False, grid_layer)

# line along the z-axis layer
line_z_axis_layer = rs.AddLayer("Line_z-axis", [0, 0, 255], True, False, grid_layer)

for i in range(x_num):
    for j in range(y_num):
        for k in range(z_num):
            origin_pt = [i * x_span, j * y_span, k * z_span]

            # draw grid point
            draw_grid_point(origin_pt, point_layer)

            # draw grid lines
            if i < x_num - 1:
                start_pt = origin_pt
                end_pt = [(i + 1) * x_span, j * y_span, k * z_span]
                draw_grid_line(start_pt, end_pt, line_x_axis_layer)

            if j < y_num - 1:
                start_pt = origin_pt
                end_pt = [i * x_span, (j + 1) * y_span, k * z_span]
                draw_grid_line(start_pt, end_pt, line_y_axis_layer)

            if k < z_num - 1:
                start_pt = origin_pt
                end_pt = [i * x_span, j * y_span, (k + 1) * z_span]
                draw_grid_line(start_pt, end_pt, line_z_axis_layer)

            # draw grid information
            draw_grid_info(origin_pt, i, j, k, text_layer)

rs.EnableRedraw(True)
