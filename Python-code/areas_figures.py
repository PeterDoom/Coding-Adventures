import math
figure_input = str(input())
if figure_input == "square":
    side_A = float(input())
    area = side_A **2
    print(area)
if figure_input == "rectangle":
    side_A = float(input())
    side_B = float(input())
    area = side_A * side_B
    print(area)
if figure_input == "triangle":
    side_A =float(input())
    side_B= float(input())
    area = side_A *side_B / 2
    print(area)
if figure_input == "circle":
    side_A = float(input())
    area = side_A**2 *  math.pi
    print(area)
