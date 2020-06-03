import pygame

class Goku:
    """Una classe que crea i impimeix una imatge en una finestra"""

    def __init__(self):
        """Inicialitza la finestra i crea atributs"""
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 666))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Son Goku")



    def _update_screen(self):
        self.screen.fill((255, 255, 255))
        self.blitme()
        pygame.display.flip()

    def blitme(self):
        """Dibuixa la imatge a la pantalla"""
        self.image = pygame.image.load("Goku.bmp")
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.screen.blit(self.image, self.rect)


    def run(self):
        while True:
            self.blitme()
            self._update_screen()
def main():
    goku = Goku()
    goku.run()

if __name__ == "__main__":
    main()
