import Game

game = Game.Game()

while game.run:
    game.draw_grid()
    game.handle_events()
    game.update()
    if game.isEndGame(game.markers) == -1 or game.isEndGame(game.markers) == 1:
        print(1)
        game.waitUntilKeyPress()