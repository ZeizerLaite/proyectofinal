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
    #Draw the two vertical lines.
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)

    #Draw the two horizontal lines.
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    #Set the color and width for X.
    color('blue')
    width(8)

    #Leave a margin to keep X centered inside the square.
    margin = 25

    #Draw the first diagonal.
    up()
    goto(x + margin, y + margin)
    down()
    goto(x + 133 - margin, y + 133 - margin)

    #Draw the second diagonal.
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

    #Draw the centered circle.
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

    #Convert the coordinates into a position from 0 to 8.
    column = positions.index(square_x)
    row = positions.index(square_y)

    return row * 3 + column


state = {
    #Store the current player.
    'player': 0,

    #Store the contents of the nine squares.
    #None means that the square is available.
    'board': [None] * 9,

    #Indicate whether the game has already finished.
    'finished': False,
}


#Associate each player with its drawing function.
players = [drawx, drawo]


def check_winner():
    """Return winning player or None."""
    board = state['board']

    #Store every possible winning combination.
    winning_lines = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )

    #Check every possible winning combination.
    for a, b, c in winning_lines:
        if (
            board[a] is not None
            and board[a] == board[b]
            and board[b] == board[c]
        ):
            return board[a]

    #Return None when nobody has won.
    return None


def board_is_full():
    """Return True if all squares are occupied."""
    #Check that every square contains a move.
    return all(square is not None for square in state['board'])


def show_message(text):
    """Display game result."""
    #Move above the board to display the result.
    up()
    goto(0, 205)
    color('black')

    #Write the result centered above the board.
    write(
        text,
        align='center',
        font=('Arial', 16, 'bold'),
    )

    update()


def tap(x, y):
    """Draw X or O in tapped square."""
    #Ignore clicks after the game has finished.
    if state['finished']:
        return

    #Get the selected board position.
    index = square_index(x, y)

    #Ignore clicks outside the board.
    if index is None:
        return

    #Prevent players from selecting an occupied square.
    if state['board'][index] is not None:
        return

    #Convert the click to the square origin.
    x = floor(x)
    y = floor(y)

    #Get the current player and drawing function.
    player = state['player']
    draw = players[player]

    #Draw the current player's symbol.
    draw(x, y)

    #Store the move in the selected square.
    state['board'][index] = player

    update()

    #Check whether the current move created a winner.
    winner = check_winner()

    if winner is not None:
        #Stop the game after detecting a winner.
        state['finished'] = True

        #Player 0 represents X and player 1 represents O.
        if winner == 0:
            show_message('X wins!')
        else:
            show_message('O wins!')

        return

    #End the game in a draw if every square is occupied.
    if board_is_full():
        state['finished'] = True
        show_message('Draw!')
        return

    #Change turns only after a valid move.
    state['player'] = not player


#Use a taller window to leave room for the result.
setup(420, 460, 370, 0)

#Hide the turtle cursor.
hideturtle()

#Disable automatic screen updates.
tracer(False)

#Draw the board.
grid()
update()

#Call tap whenever the player clicks the screen.
onscreenclick(tap)

#Keep the game window open.
done()
