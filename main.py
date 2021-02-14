import pygame
from classes import Player, Bullet

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images/ufo.png')
pygame.display.set_icon(icon)

def main():
    bullets = []
    screen = pygame.display.set_mode((800, 600))
    running = True
    player = Player()
    clock = pygame.time.Clock()
    speed = 10
    while running:
        clock.tick(69)
        screen.fill((255,255,255))
        mouseX, mouseY = pygame.mouse.get_pos()
        for event in pygame.event.get():
            #Quit game
            if event.type == pygame.QUIT:
                running = False

        #MOVEMENT
        active_key = pygame.key.get_pressed()
        if active_key[pygame.K_RIGHT] or active_key[pygame.K_d]:
            player.rect.x += speed
        if active_key[pygame.K_LEFT] or active_key[pygame.K_a]:
            player.rect.x -= speed
        if active_key[pygame.K_UP] or active_key[pygame.K_w]:
            player.rect.y -= speed
        if active_key[pygame.K_DOWN] or active_key[pygame.K_s]:
            player.rect.y += speed
        if active_key[pygame.K_SPACE]:
            bullet = Bullet(player.rect.x, player.rect.y, mouseX, mouseY)
            bullets.append(bullet)

        #Boundaries
        x_boundary = 769
        y_boundary = 550
        if player.rect.x <= 0:
            player.rect.x = 1
        if player.rect.x >= x_boundary:
            player.rect.x = x_boundary - 1
        if player.rect.y <= 0:
            player.rect.y = 1
        if player.rect.y > y_boundary:
            player.rect.y = y_boundary - 1

        player.rotate(mouseX, mouseY)
        screen.blit(player.image, player.rect)
        for bullet in bullets:
            bullet.update()
            if bullet.rect.x >= x_boundary or bullet.rect.y >= y_boundary or bullet.rect.x < 0 or bullet.rect.y < 0:
                del bullet
            else:
                screen.blit(bullet.image, bullet.rect)
                
        pygame.display.update()

if __name__ == '__main__':
    main()

    