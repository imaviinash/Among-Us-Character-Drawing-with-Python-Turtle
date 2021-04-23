'''Among Us Character Drawing with Python Turtle

Explanation:

First Part:
a. First, import the turtle module. Then, set the value of a variable “color1” as “yellow”,”color2″ as “”, “color3” as “sky-blue” and “color4” as “”. Likewise, create an instance of the turtle and store it in “t”. Create a screen for the turtle and store it in “s”.

The Body as Jiu() function:
a. Create a function named jiu(). Inside this function, set the pen size of the turtle as 20. Fill the color as in “color1” and begin the fill.
b. Set the turtle right at an angle of 90 degrees and move the turtle forward at an angle of 50 units. Set the turtle right at an angle of 180 degrees and create a circle with the arguments (40, -180).
c. Again, set the turtle right at an angle of 180 degrees and forward at 200 units.
d. Set the turtle right at an angle of 180 degrees and create another circle with the arguments (100, -180)
e. Move the turtle backward at 20 units and set it left at an angle of 15 degrees. Create a circle with the arguments (500, -20) and move it backward at 20 units.
f. Similarly, create another circle at 40, -180 and set it left at an angle of 7 degrees. Move the turtle backward at 50 units.
g. Now, set the turtle up and left at 90 degrees. Move it forward at 10 units and right at 90 degrees. Call the down() method.
h. Set the turtle right at 240 degrees and create a circle as in 50, -70 and end the fill.

The glasses as glass() function:
a. Call the up() method and set the turtle right at an angle of 230 degrees. Move the turtle forward at an angle of 100 degrees and set it left at an angle of 90 degrees. Move it forward at 20 units and again set it right at 90 degrees.
b. Call the down() method and fill the color as in “color3” and begin the fill.
c. Set the turtle right at an angle of 150 degrees and create a circle of 90, -55.
d. Move the turtle right at an angle of 180 degrees and move it forward at 1 unit. Again, set the turtle right at an angle of 180 and create a circle as 10, -65. Right at 180 degrees and forward at 110 degrees and again right at 180 degrees.
e. Accordingly, create another circle as 50, -190 and set the turtle right at 170 degrees and forward at 80 units.
f. Likewise, set it right at 180 degrees and draw a circle as 45, -30 and end the fill.

The Bag as jhola() function:
a. Move the turtle up and set it right at 90 degrees. Move it forward at 30 units and right at 255 degrees. Start to fill the color as in “color1” and begin the fill.
b. Set the turtle down, forward at 30 units, and right at 255 degrees.
c. Draw a circle as 300, -30 and set it right at 260 degrees and forward at 30 units. End the fill.

Last Part:
a. Lastly, call all the function which are jiu(), glass() and jhola().
b. End the code with the turtle.done() method.'''


import turtle

color1 = 'red'
color2 = ''
color3 = 'skyblue'
color4 = ''

s = turtle.getscreen()
t = turtle.Turtle()


def jiu():
    t.pensize(20)

    t.fillcolor(color1)
    t.begin_fill()

    t.right(90)
    t.forward(50)
    t.right(180)
    t.circle(40, -180)
    t.right(180)
    t.forward(200)

    t.right(180)
    t.circle(100, -180)

    t.backward(20)
    t.left(15)
    t.circle(500, -20)
    t.backward(20)

    t.circle(40, -180)
    t.left(7)
    t.backward(50)

    t.up()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.down()

    t.right(240)
    t.circle(50, -70)

    t.end_fill()


def glass():
    t.up()

    t.right(230)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.right(90)

    t.down()
    t.fillcolor(color3)
    t.begin_fill()

    t.right(150)
    t.circle(90, -55)

    t.right(180)
    t.forward(1)
    t.right(180)
    t.circle(10, -65)
    t.right(180)
    t.forward(110)
    t.right(180)

    t.circle(50, -190)
    t.right(170)
    t.forward(80)

    t.right(180)
    t.circle(45, -30)

    t.end_fill()


def jhola():
    t.up()
    t.right(60)
    t.forward(100)
    t.right(90)
    t.forward(75)

    t.fillcolor(color1)
    t.begin_fill()

    t.down()
    t.forward(30)
    t.right(255)

    t.circle(300, -30)
    t.right(260)
    t.forward(30)

    t.end_fill()


jiu()
glass()
jhola()

turtle.done()
