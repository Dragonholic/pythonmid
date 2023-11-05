import turtle as t
import time
wn = t.Screen()  # create a window for the turtle to draw on
wn.title("Turtle Demo")  # the title to show at the top of the window
WINDOW_WIDTH = 500  # size constants for easy changing
WINDOW_HEIGHT = 500
wn.setup(WINDOW_WIDTH, WINDOW_HEIGHT, 200, 10)  # specify window size (width, height)
user_input = t.numinput(title='Line graph', prompt='How many data points:')
x_max = user_input
# print(userInput)
# graph window
x_min = 0
y_min = 0
y_max = 5
# tick info
t_l = 0.1
x_t_space = 1
y_t_space = 1
wn.setworldcoordinates(x_min, y_min, x_max, y_max)
# Draw x-axis
t.tracer(10)
t.hideturtle()
t.up()
t.goto(x_min, 0)
t.down()
t.goto(user_input, 0.0)
t.up()
# Draw the y-axis
t.goto(0.0, y_min)
t.down()
t.goto(0.0, y_max)
t.up()
# Draw the x tick marks
n_x_ticks = int((x_max - x_min) / x_t_space) + 1
for tick in range(n_x_ticks):
    loc = x_min + tick * x_t_space
    t.up()
    t.goto(loc, -t_l * 0.4)
    t.down()
    t.goto(loc, t_l * 0.4)
    t.up()
    t.write(tick)

# Draw the y tick marks
y_label = range(0, 21, 4)

n_y_ticks = int((y_max - y_min) / y_t_space) + 1
for tick in range(n_y_ticks):
    loc = y_min + tick * y_t_space
    t.up()
    t.goto(-t_l * 0.4, loc)
    t.down()
    t.goto(t_l * 0.4, loc)
    for i in y_label:
        tick = i
        print(tick)
        t.write(tick, align="left", font=("Arial", 8, "normal"))
# get user input and plot the y value as long as user needed.
# the below code marks the value in the x-axis itself, that is not what I want.
#I want the value to get plotted outside the axis as in the normal line chart
t.backward
t.goto(0, 0)
t.tiltangle(45)
user_value = t.numinput(title='Line graph', prompt='Enter the first value:')
t.shape("square")
t.stamp()
t.forward(user_value)
user_value = t.numinput(title='Line graph', prompt='Enter the next value:')
t.shape("square")
t.stamp()
t.forward(user_value)
user_value = t.numinput(title='Line graph', prompt='Enter the next value:')
t.shape("square")
t.stamp()
t.forward(user_value)