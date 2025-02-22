from math import pi

shape = input()

if shape == 'square':
    side = float(input())
    square_area = side * side
    print(f'{square_area:.3f}')

elif shape == 'rectangle':
    side_1 = float(input())
    side_2 = float(input())
    rectangle_area = side_1 * side_2
    print(f'{rectangle_area:.3f}')

elif shape == 'circle':
    radius = float(input())
    circle_area = pi * radius * radius
    print(f'{circle_area:.3f}')

elif shape == 'triangle':
    side = float(input())
    height = float(input())
    triangle_area = (side * height) / 2
    print(f'{triangle_area:.3f}')
