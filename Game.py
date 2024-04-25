import copy
import pygame

class Game:
    SCREEN_WIDTH = SCREEN_HEIGHT = 1500
    SIZE = 3
    BACKGROUND_COLOR = (255, 255, 255)
    GRID_COLOR = (0, 0, 0)
    X_COLOR = (0, 255, 0)
    O_COLOR = (255, 0, 0)
    CHARACTERS = 3
    LINE_WIDTH = 5
    MARKERS_WIDTH = 10
    MAX_DEPTH = 11
    player = 1
    run = True
    click = False
    markers = []
    pos = []
    bestMove = None

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    countMoves = 0

    def __init__(self):
        pygame.init()
        for i in range(self.SIZE):
            row = [0] * self.SIZE
            self.markers.append(row)
            pygame.display.set_caption('Tic tac toe')

    def draw_grid(self):
        self.screen.fill(self.BACKGROUND_COLOR)
        for i in range(self.SIZE - 1):
            i = i + 1
            pygame.draw.line(self.screen,
                             self.GRID_COLOR,
                             (i * self.SCREEN_WIDTH / self.SIZE, 0),
                             (i * self.SCREEN_WIDTH / self.SIZE, self.SCREEN_WIDTH),
                             self.LINE_WIDTH)
            pygame.draw.line(self.screen,
                             self.GRID_COLOR,
                             (0, i * self.SCREEN_HEIGHT / self.SIZE),
                             (self.SCREEN_HEIGHT, i * self.SCREEN_HEIGHT / self.SIZE),
                             self.LINE_WIDTH)
            self.draw_markers()

    def draw_markers(self):
        for x in range(self.SIZE):
            for y in range(self.SIZE):
                if self.markers[x][y] == 1:
                    pygame.draw.line(self.screen,
                                     self.X_COLOR,
                                     (x * self.SCREEN_WIDTH / self.SIZE + 10, y * self.SCREEN_HEIGHT / self.SIZE + 10),
                                     (x * self.SCREEN_WIDTH / self.SIZE + self.SCREEN_WIDTH / self.SIZE - 10,
                                      y * self.SCREEN_HEIGHT / self.SIZE + self.SCREEN_HEIGHT / self.SIZE - 10),
                                     self.MARKERS_WIDTH)
                    pygame.draw.line(self.screen,
                                     self.X_COLOR,
                                     (x * self.SCREEN_WIDTH / self.SIZE + 10,
                                      y * self.SCREEN_HEIGHT / self.SIZE + self.SCREEN_HEIGHT / self.SIZE - 10),
                                     (x * self.SCREEN_WIDTH / self.SIZE + self.SCREEN_WIDTH / self.SIZE - 10,
                                      y * self.SCREEN_HEIGHT / self.SIZE + 10),
                                     self.MARKERS_WIDTH)
                elif self.markers[x][y] == -1:
                    pygame.draw.circle(self.screen,
                                       self.O_COLOR,
                                       (x * self.SCREEN_WIDTH / self.SIZE + self.SCREEN_WIDTH / (2 * self.SIZE),
                                        y * self.SCREEN_HEIGHT / self.SIZE + self.SCREEN_HEIGHT / (2 * self.SIZE)),
                                       self.SCREEN_WIDTH / (2 * self.SIZE) - 5,
                                       self.MARKERS_WIDTH)

    def handle_events(self):
        if self.player == -1:
            self.botMove()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.player == 1:
                    self.pos = pygame.mouse.get_pos()
                    cell_x = self.pos[0]
                    cell_y = self.pos[1]
                    if self.markers[int(cell_x // (self.SCREEN_WIDTH / self.SIZE))][
                        int(cell_y // (self.SCREEN_WIDTH / self.SIZE))] == 0:
                        self.markers[int(cell_x // (self.SCREEN_WIDTH / self.SIZE))][
                            int(cell_y // (self.SCREEN_WIDTH / self.SIZE))] = self.player
                        self.player *= -1
                        self.countMoves += 1

    def update(self):
        pygame.display.update()

    def getAllAvailableMove(self, board):
        availableMoves = []
        for row in range(self.SIZE):
            for col in range(self.SIZE):
                if board[row][col] == 0:
                    availableMoves.append((row, col))
        return availableMoves

    def isEndGame(self, board):
        for y in range(self.SIZE):
            for x in range(self.SIZE - self.CHARACTERS + 1):
                if sum(board[y][x:x + self.CHARACTERS]) == self.CHARACTERS:
                    return 'X'
                if sum(board[y][x:x + self.CHARACTERS]) == -self.CHARACTERS:
                    return 'O'

        for x in range(self.SIZE):
            for y in range(self.SIZE - self.CHARACTERS + 1):
                if sum(board[y + i][x] for i in range(self.CHARACTERS)) == self.CHARACTERS:
                    return 'X'
                if sum(board[y + i][x] for i in range(self.CHARACTERS)) == -self.CHARACTERS:
                    return 'O'

        for y in range(self.SIZE - self.CHARACTERS + 1):
            for x in range(self.SIZE - self.CHARACTERS + 1):
                if sum(board[y + k][x + k] for k in range(self.CHARACTERS)) == self.CHARACTERS:
                    return 'X'
                if sum(board[y + k][x + k] for k in range(self.CHARACTERS)) == -self.CHARACTERS:
                    return 'O'

        for y in range(self.SIZE - self.CHARACTERS + 1):
            for x in range(self.SIZE - 1, self.CHARACTERS - 1, -1):
                if sum(board[y + k][x - k] for k in range(self.CHARACTERS)) == self.CHARACTERS:
                    return 'X'
                if sum(board[y + k][x - k] for k in range(self.CHARACTERS)) == -self.CHARACTERS:
                    return 'O'
        return 'D'

    def isFull(self, board):
        for row in board:
            if 0 in row:
                return False
        return True

    def minimax(self, board, alpha, beta, depth, maximizingPlayer):
        state = self.isEndGame(board)
        if depth == 0:
            return 10
        if state == 'X':
            return 500
        if state == 'O':
            return -500
        if self.isFull(board):
            return 0
        availableMoves = self.getAllAvailableMove(board)
        if maximizingPlayer:
            maxVal = -1000
            for (row, col) in availableMoves:
                new_board = copy.deepcopy(board)
                new_board[row][col] = 1
                val = self.minimax(new_board, alpha, beta, depth - 1, False)
                alpha = max(alpha, val)
                maxVal = max(maxVal, val)
                if beta < alpha:
                    break
            return maxVal
        else:
            minVal = 1000
            for (row, col) in availableMoves:
                new_board = copy.deepcopy(board)
                new_board[row][col] = -1
                val = self.minimax(new_board, alpha, beta, depth - 1, True)
                if val <= minVal and depth == self.MAX_DEPTH:
                    self.best_move = (row, col)
                print(val)
                beta = min(beta, val)
                minVal = min(minVal, val)
                if alpha > beta:
                    break
            return minVal

    def botMove(self):
        self.minimax(self.markers, -1000, 1000, self.MAX_DEPTH, False)
        row, col = self.best_move
        self.markers[row][col] = -1
        self.player *= -1
        self.countMoves += 1
