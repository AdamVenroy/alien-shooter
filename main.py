import pygame
from classes import Player, Bullet

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images/ufo.png')
pygame.display.set_icon(icon)

SPEED = 10
X_BOUNDARY = 769
Y_BOUNDARY = 550

def move_and_shoot(player_rect, bullets, mouse_x, mouse_y):
    active_key = pygame.key.get_pressed()
    if active_key[pygame.K_RIGHT] or active_key[pygame.K_d]:
        player_rect.x += SPEED
    if active_key[pygame.K_LEFT] or active_key[pygame.K_a]:
        player_rect.x -= SPEED
    if active_key[pygame.K_UP] or active_key[pygame.K_w]:
        player_rect.y -= SPEED
    if active_key[pygame.K_DOWN] or active_key[pygame.K_s]:
        player_rect.y += SPEED
    if active_key[pygame.K_SPACE]:
        bullet = Bullet(player_rect.x, player_rect.y, mouse_x, mouse_y)
        bullets.append(bullet)
        
def boundary_check(player_rect):
    if player_rect.x <= 0:
        player_rect.x = 1
    if player_rect.x >= X_BOUNDARY:
        player_rect.x = X_BOUNDARY - 1
    if player_rect.y <= 0:
        player_rect.y = 1
    if player_rect.y > Y_BOUNDARY:
        player_rect.y = Y_BOUNDARY - 1

def main():
    bullets = []
    screen = pygame.display.set_mode((800, 600))
    running = True
    player = Player()
    clock = pygame.time.Clock()
    while running:
        clock.tick(69)
        screen.fill((60,200,255))
        mouseX, mouseY = pygame.mouse.get_pos()
        for event in pygame.event.get():
            #Quit game
            if event.type == pygame.QUIT:
                running = False

        #MOVEMENT
        move_and_shoot(player.rect, bullets, mouseX, mouseY)

        #Boundaries
        boundary_check(player.rect)


        player.rotate(mouseX, mouseY)
        screen.blit(player.image, player.rect)
        for bullet in bullets:
            bullet.update()
            if bullet.rect.x >= X_BOUNDARY or bullet.rect.y >= Y_BOUNDARY or bullet.rect.x < 0 or bullet.rect.y < 0:
                del bullet
            else:
                #print(bullets)
                screen.blit(bullet.image, bullet.rect)
        pygame.display.update()

if __name__ == '__main__':
    main()

    