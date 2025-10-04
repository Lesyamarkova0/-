import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon
import numpy as np

def is_point_in_triangle(x, y, vertices):
    x1, y1 = vertices[0]
    x2, y2 = vertices[1]
    x3, y3 = vertices[2]
    
    inside = (y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)
    a = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / inside
    b = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / inside
    c = 1 - a - b
    
    return 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1

def rain(size):
    triangle_side = 4
    triangle_height = triangle_side * np.sqrt(3) / 2
    triangle_area = (triangle_side * triangle_height) / 2
    circle_area = triangle_area / 2
    R = np.sqrt(circle_area / np.pi)
    vertices = np.array([
        [triangle_side / 2, triangle_height], #верхняя вершина
        [0, 0],# левая нижняя
        [triangle_side, 0] #правая вершина
    ])

    x0, y0 = triangle_side / 2, triangle_height / 3
    
    
    fig, ax = plt.subplots(figsize=(8, 8))
    plt.axis('equal')
    ax.add_patch(Polygon(vertices,facecolor='lightcoral'))
    ax.add_patch(Circle((x0, y0), R, facecolor='c'))
    
    X, Y = [], []
    while len(X) < size:
        x_candidate = np.random.uniform(0, triangle_side)
        y_candidate = np.random.uniform(0, triangle_height)
        if is_point_in_triangle(x_candidate, y_candidate, vertices):
            X.append(x_candidate)
            Y.append(y_candidate)
    
    X = np.array(X)
    Y = np.array(Y)
    
    plt.scatter(X, Y, marker='o', c='orange')
    
    inside = len([d for d in (X - x0)**2 + (Y - y0)**2 if d <= R**2])
    prob = inside / size
    
    plt.show()
    print(f'В круглую клумбу из {size} капель дождя попало {inside}. Доля попавших капель составляет {prob}')

rain(1000)
