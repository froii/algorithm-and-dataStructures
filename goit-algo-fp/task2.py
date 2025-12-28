import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy

PYTHAGORAS_FACTOR = 0.707  # sqrt(2)/2
INITIAL_ANGLE = numpy.pi  # look picture task2_image.jpg
FIGURE_SIZE = (8, 8)


def draw_tree(ax, x, y, size, angle, level):
    if level == 0:
        return

    c, s = numpy.cos(angle), numpy.sin(angle)

    corners = numpy.array([
        [x, y],
        [x + size * c, y + size * s],
        [x + size * c - size * s, y + size * s + size * c],
        [x - size * s, y + size * c]
    ])

    ax.add_patch(patches.Polygon(corners, edgecolor='yellow', facecolor='lightblue', linewidth=2))

    new_size = size * PYTHAGORAS_FACTOR
    draw_tree(ax, corners[3][0], corners[3][1], new_size, angle + numpy.pi / 4, level - 1)

    lx = corners[3][0] + new_size * numpy.cos(angle + numpy.pi / 4)
    ly = corners[3][1] + new_size * numpy.sin(angle + numpy.pi / 4)
    draw_tree(ax, lx, ly, new_size, angle - numpy.pi / 4, level - 1)


try:
    input_value = int(input("Виберіть рівень рекурсії (1-13): "))
    level = min(max(input_value, 1), 13)
except ValueError:
    level = 5

fig, ax = plt.subplots(figsize=FIGURE_SIZE)
fig.patch.set_facecolor("#690505")

ax.set_facecolor('#1a1a1a')
ax.set_aspect('equal')

draw_tree(ax, -50, 0, 100, INITIAL_ANGLE, level)
ax.autoscale()

plt.title(f'Дерево Піфагора (рівень: {level})', color='white')
plt.tight_layout()
plt.show()
