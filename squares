from turtle import *

def k(d,n):
    if n == 0:
        return
    up()
    speed(4)
    right(10)
    forward(d//8)
    down()
    for i in range(4):
        forward(d)
        right(90)
    return k(d*0.9, n-1)



def main():
    left(10)
    k(int(input()), int(input()))
    mainloop()


if __name__ == '__main__':
    main()
