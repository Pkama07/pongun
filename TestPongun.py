import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))
running = True


def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def draw_text(text, size, place, color, font):
    font = pygame.font.Font(font, size)
    text_surf, text_rect = text_objects(text, font, color)
    text_rect.center = place
    win.blit(text_surf, text_rect)


main = True
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.draw.rect(win, (255, 255, 255), (150, 300, 200, 100))
    draw_text("PonGun", 75, (250, 100), (255, 0, 0), 'Walkway_UltraBold.ttf')
    draw_text("A Game by PyKam", 40, (250, 200), (255, 255, 255), 'Walkway_UltraBold.ttf')
    draw_text("Play", 35, (250, 350), (0, 0, 0), 'Walkway_Oblique_Bold.ttf')
    if pygame.mouse.get_pressed()[0] and 150 <= pygame.mouse.get_pos()[0] <= 350 and 300 <= pygame.mouse.get_pos()[1] <= 400:
        main = False
    pygame.display.update()
pygame.quit()
