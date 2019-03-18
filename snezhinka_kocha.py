from turtle import *

def snezhinka_kocha(order, size):
    koch(order, size)
    right(120)
    koch(order, size)
    right(120)
    koch(order, size)


def koch(order, size):
    if order == 0:
        forward(size)
    else:
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)
        right(120)
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)

def main():
    speed(0)
    up()
    goto(-100,0)
    down()
    n = int(input('Глубина рекурсии:'))
    d = int(input('Общая длинна:'))
    snezhinka_kocha(n, d)
    mainloop()

if __name__ == '__main__':
    main()
