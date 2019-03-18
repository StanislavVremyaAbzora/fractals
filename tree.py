from turtle import *


def tree(d, n):
    if n == 0:
        return
    forward(d)
    right(30)
    tree(d / 2, n - 1)
    left(60)
    tree(d / 2, n - 1)
    right(30)
    backward(d)
 

def main():
    left(90)
    d = int(input('Длинна стороны:'))
    n = int(input('Длинна рекурсии'))
    tree(d,n)
    mainloop()
    
    
if __name__ == '__main__':
    main()
