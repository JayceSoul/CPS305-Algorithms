#Jonathan Ong
import turtle
import random as ran
import math
#--------------<Exercise 1>---------------
def tree(branchLen,t):
    r = ran.randint(5,15)
    r2 = ran.randint(20,35)
    if branchLen > 5:
        t.width(branchLen/5)
        t.color("brown")
        if branchLen <= 20:
            t.color("green")
        t.forward(branchLen)
        t.right(r2)
        tree(branchLen-r,t)
        t.width(int(branchLen/5))
        t.left(r2*2)
        tree(branchLen-r,t)
        t.width(int(branchLen/5))
        t.right(r2)
        if branchLen >= 15:
            t.color("brown")
        t.backward(branchLen)

def drawTree():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(0)
    t.tracer(10)
    t.left(90)
    t.up()
    t.color("brown")
    t.backward(100)
    t.down()
    tree(75,t)
    myWin.exitonclick()


#--------------<Exercise 2>---------------

#---------<Q1>----------
#acc must be 1
def power(x,n,acc):
    if n == 0:
        return acc
    else:
        return power(x, n-1 ,acc*x)

#---------<Q2>----------
def powerH(x,n):
    if n == 0:
        return 1
    elif n <= 1:
        return x
    elif n%2 == 0:
        return powerH(x,int(n/2)) * powerH(x,int(n/2))
    else:
        return powerH(x,int(n/2)) * powerH(x,int(n/2)) * x

#---------<Q3>----------
def binoCo(n,k):
    if k == 0 or n == k:
        return 1
    elif k > n:
        return 0
    elif k > 0:
        return binoCo(n-1,k) + binoCo(n-1,k-1)
    else:
        return 1


#runs the program
drawTree()
#print(power(2,6,1))
#print(powerH(2,6))
#print(binoCo(6,4))