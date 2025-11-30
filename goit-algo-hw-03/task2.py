import turtle


def koch_curve(t, size, level):
    if level == 0:
        t.forward(size)
    else:
        size /= 3
        for angle in [60, -120, 60, 0]:
            koch_curve(t, size, level - 1)
            t.left(angle)


def koch_snowflake(size, level):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(111)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    for _ in range(3):
        koch_curve(t, size, level)
        t.right(120)

    window.mainloop()


level = int(input("Введіть рівень рекурсії (0-5):"))
koch_snowflake(500, level=level)

# 1. Код виконується. Програма візуалізує фрактал «сніжинка Коха».
# 2. Користувач має можливість вказати рівень рекурсії.
