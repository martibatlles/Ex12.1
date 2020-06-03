import pygame

class Goku:
    """Una classe que crea i impimeix una imatge en una finestra"""

    def __init__(self):
        """Inicialitza la finestra i crea atributs"""
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 563))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Son Goku")



    def _update_screen(self):
        self.screen.fill((255, 255, 255))
        self.blit_background()
        self.blit_goku()
        pygame.display.flip()


    def blit_background(self):
        self.background = pygame.image.load("background.bmp")
        self.rect_background = self.background.get_rect()
        self.rect_background.center = self.screen_rect.center
        self.screen.blit(self.background, self.rect_background)


    def blit_goku(self):
        """Dibuixa la imatge a la pantalla"""
        self.goku = pygame.image.load("Goku.bmp")
        self.rect_goku = self.goku.get_rect()
        self.rect_goku.center = self.screen_rect.center
        self.screen.blit(self.goku, self.rect_goku)


    def run(self):
        while True:
            self.blit_background()
            self.blit_goku()
            self._update_screen()
def main():
    goku = Goku()
    goku.run()

if __name__ == "__main__":
    main()
