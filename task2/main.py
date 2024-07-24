import turtle


def rotate_triangle(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        rotate_triangle(t, length, level - 1)
        t.left(60)
        rotate_triangle(t, length, level - 1)
        t.right(120)
        rotate_triangle(t, length, level - 1)
        t.left(60)
        rotate_triangle(t, length, level - 1)


def snowflake(t, length, level):
    for _ in range(3):
        rotate_triangle(t, length, level)
        t.right(120)


def main():
    level = int(input("Рівень рекурсії: "))
    length = 200

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-length / 2, length / 3)
    t.pendown()
    snowflake(t, length, level)
    turtle.done()


if __name__ == "__main__":
    main()
