import pygame

from network import Network

WIDTH = 700
HEIGHT = 600

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")


class Window:
    def __init__(self, window_display):
        self._window = window_display

    @property
    def window(self):
        return self._window

    def draw_window(self, player, list_players):
        self.window.fill((255, 255, 255))  # Fill the screen with white
        player.draw(self.window)
        for player_index in list_players:
            player_to_draw = list_players[player_index]
            player_to_draw.draw(self.window)
        pygame.display.update()


def main():
    win = Window(window)
    n = Network()
    clock = pygame.time.Clock()
    player = n.player
    while True:
        clock.tick(60)
        list_players = n.send(player)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        player.move()
        win.draw_window(player, list_players)


if __name__ == '__main__':
    main()
