# coding: utf-8

import rhinoscriptsyntax as rs


def euclidean(num1, num2):
    if num2 > num1:
        a = num2
        b = num1
    else:
        a = num1
        b = num2

    # 商と余りを求める
    q, mod = divmod(a, b)

    while True:
        if mod == 0:
            print("Greatest common divisor is {0}".format(b))
            break

        a = b
        b = mod
        q, mod = divmod(a, b)


def draw_euclidean(num1, num2):
    if num2 > num1:
        a = num2
        b = num1
    else:
        a = num1
        b = num2

    # 商と余りを求める
    q, mod = divmod(a, b)

    origin_pt = (0, 0, 0)
    count = 0

    while True:

        for _ in range(q):
            p1 = origin_pt
            p2 = (origin_pt[0] + b, origin_pt[1], origin_pt[2])
            p3 = (origin_pt[0] + b, origin_pt[1] - b, origin_pt[2])
            p4 = (origin_pt[0], origin_pt[1] - b, origin_pt[2])

            # draw rectangle
            rs.AddPolyline([p1, p2, p3, p4, p1])

            # update origin point
            if count % 2 == 0:  # even number
                origin_pt = p2
            else:  # odd number
                origin_pt = p4

        # Processing end judgment
        if mod == 0:
            print("Greatest common divisor of {0} and {1} is {2}".format(num1, num2, b))
            break

        # update variable
        a = b
        b = mod
        q, mod = divmod(a, b)
        count += 1


if __name__ == "__main__":
    draw_euclidean(48, 20)
