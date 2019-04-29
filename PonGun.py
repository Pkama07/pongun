# PyKam
import pygame
pygame.init()
win_x = 500
win_y = 500
win = pygame.display.set_mode((win_x, win_y))
pygame.display.set_caption("PonGun")
ship1 = pygame.image.load('preview_player.gif')
ship2 = pygame.transform.flip(ship1, True, False)
bullets = [pygame.transform.scale(pygame.image.load('bullet1.png'), (20, 20)),
           pygame.transform.scale(pygame.image.load('bullet2.png'), (20, 20)),
           pygame.transform.scale(pygame.image.load('bullet3.png'), (20, 20))]


class Player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.score = 0


class Bullet(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = False
        self.count = 0
        self.can = False


def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def draw_text(text, size, place, color, font):
    font = pygame.font.Font(font, size)
    text_surf, text_rect = text_objects(text, font, color)
    text_rect.center = place
    win.blit(text_surf, text_rect)


# main menu mainloop
main = True
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.draw.rect(win, (255, 255, 255), (150, 300, 200, 100))
    draw_text("PonGun", 75, (250, 100), (255, 0, 0), 'Walkway_UltraBold.ttf')
    draw_text("By Pradyun Kamaraju", 40, (250, 200), (255, 255, 255), 'Walkway_UltraBold.ttf')
    draw_text("Play", 35, (250, 350), (0, 0, 0), 'Walkway_Oblique_Bold.ttf')
    if pygame.mouse.get_pressed()[0] and 150 <= pygame.mouse.get_pos()[0] <= 350 and 300 <= pygame.mouse.get_pos()[1] <= 400:
        main = False
    pygame.display.update()
running = True
player1 = Player(125, 250)
player2 = Player(375, 250)
bullet1 = Bullet(player1.x, player1.y)
bullet2 = Bullet(player2.x, player2.y)


def check_bullet():
    if bullet1.state:
        if bullet1.x < 500:
            bullet1.x = bullet1.x + 5
            win.blit(bullets[bullet1.count], (bullet1.x, bullet1.y))
            bullet1.count = bullet1.count + 1
            if bullet1.count > 2:
                bullet1.count = 0
            if player2.x < bullet1.x < player2.x + 60 and player2.y < bullet1.y < player2.y + 40:
                player1.score = player1.score + 1
                bullet1.state = False
        else:
            bullet1.count = 0
            bullet1.state = False
    if bullet2.state:
        if bullet2.x > 0:
            bullet2.x = bullet2.x - 5
            win.blit(bullets[bullet2.count], (bullet2.x, bullet2.y))
            bullet2.count = bullet2.count + 1
            if bullet2.count > 2:
                bullet2.count = 0
            if player1.x < bullet2.x < player1.x + 60 and player1.y < bullet2.y < player1.y + 40:
                player2.score = player2.score + 1
                bullet2.state = False
        else:
            bullet2.count = 0
            bullet2.state = False


def draw_window():
    win.fill((0, 0, 0))
    pygame.draw.line(win, (255, 255, 255), (250, 0), (250, 500), 5)
    win.blit(ship1, (player1.x, player1.y))
    win.blit(ship2, (player2.x, player2.y))
    check_bullet()
    draw_text(str(player1.score), 50, (125, 100), (255, 255, 255), 'Walkway_Bold.ttf')
    draw_text(str(player2.score), 50, (375, 100), (255, 255, 255), 'Walkway_Bold.ttf')

    pygame.display.update()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
# player1 actions
    if keys[pygame.K_w] and player1.y >= 0:
        player1.y = player1.y - 5
    elif keys[pygame.K_w]:
        player1.y = -15
    if keys[pygame.K_s] and player1.y+40 < 500:
        player1.y = player1.y + 5
    elif keys[pygame.K_s]:
        player1.y = 500 - 40
    if keys[pygame.K_d] and player1.x+60 < 250:
        player1.x = player1.x + 5
    elif keys[pygame.K_d]:
        player1.x = 250 - 60
    if keys[pygame.K_a] and player1.x > 0:
        player1.x = player1.x - 5
    elif keys[pygame.K_a]:
        player1.x = 0
    if keys[pygame.K_f] and not bullet1.state:
        bullet1.state = True
        bullet1.x = player1.x + 43
        bullet1.y = player1.y + 25
# player2 actions
    if keys[pygame.K_UP] and player2.y >= 0:
        player2.y = player2.y - 5
    elif keys[pygame.K_UP]:
        player2.y = -15
    if keys[pygame.K_DOWN] and player2.y+40 < 500:
        player2.y = player2.y + 5
    elif keys[pygame.K_DOWN]:
        player2.y = 500 - 40
    if keys[pygame.K_LEFT] and player2.x > 250:
        player2.x = player2.x - 5
    elif keys[pygame.K_LEFT]:
        player2.x = 250
    if keys[pygame.K_RIGHT] and player2.x+60 < 500:
        player2.x = player2.x + 5
    elif keys[pygame.K_RIGHT]:
        player2.x = 500 - 60
    if keys[pygame.K_SLASH] and not bullet2.state:
        bullet2.state = True
        bullet2.x = player2.x + 17
        bullet2.y = player2.y + 25
    draw_window()
    if player1.score == 10 or player2.score == 10:
        running = False
# end game mainloop
end = True
while end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    win.fill((0, 0, 0))
    if player1.score == 10:
        draw_text("Player 1 Wins!", 75, (250, 250), (255, 255, 255), 'Walkway_Black.ttf')
    else:
        draw_text("Player 2 Wins!", 75, (250, 250), (255, 255, 255), 'Walkway_Black.ttf')
    pygame.display.update()


