from turtle import *


def minkovsky(n, d):
    if n == 0:
        forward(d)
    else:
        minkovsky(n-1, d/3)
        left(90)
        mink(n-1, d/3)
        right(90)
        mink(n-1, d/3)
        right(90)
        mink(n-1, d/3*2)
        left(90)
        mink(n-1, d/3)
        left(90)
        mink(n-1, d/3)
        right(90)
        mink(n-1, d/3)


def main():
  up()
  goto(-100,0)
  down()
  n = int(input('Глубина рекурсии:'))
  a = int(input('Ощая длина:'))
  minkovsky(n, a)


if __name__ == '__main__':
    main()
