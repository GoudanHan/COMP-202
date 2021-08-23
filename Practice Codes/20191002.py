import turtle

def polygon(n, t, side_length):
    for i in range(n):
        t.fd(side_length)
        t.left()


#leo = turtle.Turtle()

don = turtle.Turtle()
don.color("red")
sides = int(input("Please input the sides you want for the polygon:"))
size = int(input("Please input the side length:"))
polygon(sides, don, size)
