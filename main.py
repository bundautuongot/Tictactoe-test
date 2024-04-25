import Game

game = Game.Game()

while game.run:
    game.draw_grid()
    game.handle_events()
    game.update()

