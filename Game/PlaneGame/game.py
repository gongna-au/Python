#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame, random

from sys import exit

from pygame.locals import *

from model import *


# 设置屏幕的宽度
SCREEN_WIDTH = 700
# 设置屏幕的高度
SCREEN_HEIGHT = 900

pygame.init()

pygame.display.set_caption("Aircraft war")


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

pygame.mouse.set_visible(False)

bg = pygame.image.load("img_resouce/bg.jpg")


bg_game_over = pygame.image.load("img_resouce/game_over.jpeg")

img_plane = pygame.image.load("img_resouce/shoot.png")

img_start = pygame.image.load("img_resouce/start.png")

img_pause = pygame.image.load("img_resouce/pause.png")

img_icon = pygame.image.load("img_resouce/plane.png").convert_alpha()

pygame.display.set_icon(img_icon)

player_rect = []

player_rect.append(pygame.Rect(0, 99, 102, 126))

player_rect.append(pygame.Rect(165, 360, 102, 126))


player_rect.append(pygame.Rect(165, 234, 102, 126))

player_rect.append(pygame.Rect(330, 624, 102, 126))

player_rect.append(pygame.Rect(330, 498, 102, 126))

player_rect.append(pygame.Rect(432, 624, 102, 126))

player_pos = [200, 450]


player = Player(img_plane, player_rect, player_pos)

bullet_rect = pygame.Rect(1004, 987, 9, 21)

bullet_img = img_plane.subsurface(bullet_rect)


enemy_rect = pygame.Rect(534, 612, 57, 43)

enemy_img = img_plane.subsurface(enemy_rect)

enemy_explosion_imgs = []

enemy_explosion_imgs.append(img_plane.subsurface(pygame.Rect(267, 347, 57, 43)))

enemy_explosion_imgs.append(img_plane.subsurface(pygame.Rect(873, 697, 57, 43)))

enemy_explosion_imgs.append(img_plane.subsurface(pygame.Rect(267, 296, 57, 43)))

enemy_explosion_imgs.append(img_plane.subsurface(pygame.Rect(930, 697, 57, 43)))

enemies = pygame.sprite.Group()

enemies_explosion = pygame.sprite.Group()

shoot_frequency = 0

enemy_frequency = 0

player_explosion_index = 16

score = 0

running = True

is_pause = False

is_game_over = False

clock = pygame.time.Clock()

while running:

    clock.tick(60)

    if not is_pause and not is_game_over:
        if not player.is_hit:
            if shoot_frequency % 15 == 0:
                player.shoot(bullet_img)
                shoot_frequency += 1
                if shoot_frequency >= 15:
                    shoot_frequency = 0

    if enemy_frequency % 50 == 0:
        enemy_pos = [random.randint(0, SCREEN_WIDTH - enemy_rect.width), 0]
        enemy = Enemy(enemy_img, enemy_explosion_imgs, enemy_pos)
        enemies.add(enemy)
        enemy_frequency += 1
        if enemy_frequency >= 100:
            enemy_frequency = 0

for bullet in player.bullets:
    bullet.move()
    if bullet.rect.bottom < 0:
        player.bullets.remove(bullet)


for enemy in enemies:
    enemy.move()
    if pygame.sprite.collide_circle(enemy, player):
        enemies_explosion.add(enemy)
        enemies.remove(enemy)
        player.is_hit = True
        is_game_over = True
        if enemy.rect.top < 0:
            enemies.remove(enemy)

            enemy_explosion = pygame.sprite.groupcollide(enemies, player.bullets, 1, 1)
            for enemy in enemy_explosion:
                enemies_explosion.add(enemy)

            screen.fill(0)

            screen.blit(bg, (0, 0))

            if not player.is_hit:
                screen.blit(player.image[int(player.img_index)], player.rect)
                player.img_index = shoot_frequency / 8
            else:

                if player_explosion_index > 47:
                    is_game_over = True
                else:
                    player_img_index = player_explosion_index / 8
                    screen.bilt(player.image[int(player.img_index)], player_rect)
                    player_explosion_index += 1

        for enemy in enemies_explosion:
            if enemy_explosion_index == 0:
                pass
            if enemy_explosion_index > 7:
                enemies_explosion.remove(enemy)
                score += 100
                continue

screen.blit(enemy.explosion_img[int(enemy.explosion_index / 2)], enemy_rect)
enemy.explosion_index += 1


player.bullets.draw(screen)


score_font = pygame.font.Font(None, 36)
score_text = score_font.render(str(score), True, (0, 0, 255))

text_rect = score_text.get_rect()

text_rect.topleft = [20, 10]

screen.blit(score_text, text_rect)

left, middle, right = pygame.mouse.get_pressed()

if right == True and not is_game_over:

    is_pause = True

if left == True:
    if is_game_over:
        is_game_over = False
    player_rect = []
    player_rect.append(pygame.Rect(0, 99, 102, 126))
    player_rect.append(pygame.Rect(165, 360, 102, 126))
    player_rect.append(pygame.Rect(165, 234, 102, 126))
    player_rect.append(pygame.Rect(330, 624, 102, 126))
    player_rect.append(pygame.Rect(330, 498, 102, 126))
    player_rect.append(pygame.Rect(432, 624, 102, 126))
    player = Player(img_plane, player_rect, player_pos)
    bullet_rect = pygame.Rect(1004, 987, 9, 21)
    bullet_img = img_plane.subsurface(bullet_rect)
    enemy_rect = pygame.Rect(534, 612, 57, 43)
    enemy_img = img_plane.subsurface(enemy_rect)
    enemy_explosion_imgs = []

    enemy_explosion_imgs.append(img_plane.subsurface(pygame.Rect(267, 347, 57, 43)))
    enemy_explosion_imgs.append(img_plane.subsurface(pygame.Rect(873, 697, 57, 43)))
    enemy_explosion_imgs.append(img_plane.subsurface(pygame.Rect(267, 296, 57, 43)))
    enemy_explosion_imgs.append(img_plane.subsurface(pygame.Rect(930, 697, 57, 43)))

    enemies = pygame.sprite.Group()
    enemies_explosion = pygame.sprite.Group()
    score = 0
    shoot_frequency = 0
    enemy_frequency = 0
    player_explosion_index = 16


if is_pause:
    is_pause = False


if is_game_over:
    font = pygame.font.SysFont("楷体", 48)
    text = font.render("Score:" + str(score), True, (255, 0, 0))
    text_rect = text.get_rect()
    centerx = screen.get_rect().centerx
    text_rect.centery = screen.get_rect().centery + 70


screen.blit(bg_game_over, (0, 0))


font = pygame.font.SysFont("楷体", 48)
text = font.render("Please Left Mouse to Restart", True, (255, 0, 0))
text_rect = text.get_rect()
text_rect.centerx = screen.get_rect().centerx
rext_rect.centery = screen.get_rect().centery + 150
screen.blit(text, text_rect)

pygame.display.update()


for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()
if not is_pause and not is_game_over:
    key = pygame.key.get_pressed()
    if key[K_w] or key[K_UP]:
        player.moveUp()
        if key[K_s] or key[K_DOWN]:
            player.moveDown()
        if key[K_a] or key[K_LEFT]:
            player.moveLeft()
        if key[K_d] or key[K_RIGHT]:
            player.moveRight()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
pygame.display.update()
