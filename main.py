import pygame
import sys

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 700
TILE_SIZE = int(SCREEN_WIDTH / 750)
EMPTY_TILE_COLOR = (25,25,25)
FILLED_TILE_COLOR = (255,255,255)

class CellularAutomata:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Cellular Automata')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # if a tile is 0 it's empty, 1 is filled
        self.tiles = []
        self.is_running = True

    def main_loop(self):
        self.init_tiles()

        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            self.update_tiles()
            self.draw_tiles()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                self.is_running = False

            pygame.display.update()

        self.exit()

    def init_tiles(self):
        """
        initialize all tiles to empty
        """
        tiles_across = int(SCREEN_WIDTH / TILE_SIZE)
        tiles_down = int(SCREEN_HEIGHT / TILE_SIZE)

        for i in range(tiles_down):
            row = []
            for j in range(tiles_across):
                row.append(0)
            
            self.tiles.append(row)

        # set the top middle tile to filled and the automata builds off that
        self.tiles[0][int(len(self.tiles[0]) / 2)] = 1

    def update_tiles(self):
        """
        look at the current tile, as well as tiles to the left and right to determine what the tile below should be
        """
        for i in range(len(self.tiles) - 1): # no need to evauluate bottom row
            for j in range(len(self.tiles[i])):
                left_tile = 0 if j == 0 else self.tiles[i][j - 1] # if on left border, left tile is out of bounds so it's empty
                current_tile = self.tiles[i][j]
                right_tile = 0 if j == len(self.tiles[i]) - 1 else self.tiles[i][j + 1]

                configuration = (left_tile, current_tile, right_tile)

                # rule 30
                if configuration == (1,1,1) or configuration == (1,1,0) or configuration == (1,0,1) or configuration == (0,0,0):
                    self.tiles[i + 1][j] = 0
                else:
                    self.tiles[i + 1][j] = 1

    def draw_tiles(self):
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                pygame.draw.rect(
                    self.screen,
                    EMPTY_TILE_COLOR if self.tiles[i][j] == 0 else FILLED_TILE_COLOR, # 0 is empty, 1 is filled
                    (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                )    

    def exit(self):
        pygame.display.quit()
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    cs = CellularAutomata()
    cs.main_loop()
