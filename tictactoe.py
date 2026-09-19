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


def square_index(x, y):
    """Return board index for tapped coordinates."""
    #Convert the click to the square origin.
    square_x = floor(x)
    square_y = floor(y)

    #Store the three valid positions for rows and columns.
    positions = (-200, -67, 66)

    #Ignore clicks outside the board.
    if square_x not in positions or square_y not in positions:
        return None

    #Convert the square coordinates into a position from 0 to 8.
    column = positions.index(square_x)
    row = positions.index(square_y)

    return row * 3 + column


state = {
    'player': 0,

    #Store the contents of the nine squares.
    #None means that the square is available.
    'board': [None] * 9,
}

players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    #Get the selected board position.
    index = square_index(x, y)

    #Ignore clicks outside the board.
    if index is None:
        return

    #Prevent players from selecting an occupied square.
    if state['board'][index] is not None:
        return

    x = floor(x)
    y = floor(y)

    player = state['player']
    draw = players[player]

    draw(x, y)

    #Store the move in the selected square.
    state['board'][index] = player

    update()

    #Change turns only after a valid move.
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
