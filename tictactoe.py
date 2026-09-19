"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    #Set the color and width for X.
    color('blue')
    width(8)

    #Leave a margin to keep X centered inside the square.
    margin = 25

    up()
    goto(x + margin, y + margin)
    down()
    goto(x + 133 - margin, y + 133 - margin)

    up()
    goto(x + margin, y + 133 - margin)
    down()
    goto(x + 133 - margin, y + margin)
    up()


def drawo(x, y):
    """Draw O player."""
    #Set the color and width for O.
    color('red')
    width(8)

    #Calculate the center of the selected square.
    radius = 42
    center_x = x + 66.5
    center_y = y + 66.5

    #Move to the bottom point of the circle.
    up()
    goto(center_x, center_y - radius)
    setheading(0)
    down()
    circle(radius)
    up()


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
