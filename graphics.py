"""
1. Write the lines of code that would import
and create a turtle named 'Pong'.
"""
import turtle
pong = turtle.Turtle()


"""
2.  Draw a square with Pong of length 100
"""
for i in range(4):
  pong.fd(100)
  pong.right(90)


"""
3.  Write a function that will allow the user
to input the length of a square and then draw
a square of that length.
"""
def sqr():
  x = int(input())
  for i in range(4):
    pong.fd(x)
    pong.rihgt(90)

"""
4.  Draw a series of squares with different sizes
that share the same corner.
"""





"""
5.  Repeat the question above but change the color
each time it draws a square.
"""
