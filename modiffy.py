if (board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != '0'):
    return board[0][0]
if (board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != '0'):
    return board[1][0]
if (board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != '0'):
    return board[2][0]

    # Check verticals
if (board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != '0'):
    return board[0][0]
if (board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != '0'):
    return board[0][1]
if (board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != '0'):
    return board[0][2]

    # Check diagonals
if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != '0'):
    return board[1][1]
if (board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != '0'):
    return board[1][1]

    # Check if draw
draw_flag = 0
for i in range(3):
    for j in range(3):
        if board[i][j] == '0':
            draw_flag = 1
if draw_flag == 0:
    return None

return None