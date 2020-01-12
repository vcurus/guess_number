import pygame
import random

num = random.randint(0, 100)
print(num)
numeral = ''
move = 1
block = 0
start = 1
W = 480
H = 360
SILVER = (192, 192, 192)
BLACK = (0, 0, 0)
OUTSIDE_BG = (-100, -100)

pygame.init()
pygame.display.set_caption('Угадай число')
screen = pygame.display.set_mode((W, H))

font = pygame.font.SysFont('Arial', 28, True, False)
font_box = pygame.Surface((W - font.get_height(), font.get_height()))
font_rect = font_box.get_rect(center=(W // 2, H - font.get_height()))
font2 = pygame.font.SysFont('Arial', 14, False, True)

bg = pygame.image.load('room.png')
bg_rect = bg.get_rect(topleft=(0, 0))
cat = pygame.image.load('cat.png')
cat_rect = cat.get_rect(center=(70, 220))
dog = pygame.image.load('dog.png')
dog_rect = dog.get_rect(center=(410, 220))
owl = pygame.image.load('owl.png')
owl_rect = owl.get_rect(center=(210, 120))
dialog = pygame.image.load('dialog.png')
dialog_rect = dialog.get_rect()
dialog_cat_pos = (cat_rect.x, cat_rect.y - dialog_rect.h)
dialog_dog_pos = (dog_rect.x - dialog_rect.w // 2, dog_rect.y - dialog_rect.h)


def dialogs(text, pos, owl_text):
    screen.blit(dialog, pos)
    screen.blit(
        font2.render(text, True, BLACK), (pos[0] + 5, pos[1] + 5))
    dialog_owl_pos = (owl_rect.x, owl_rect.y - dialog_rect.h)
    screen.blit(dialog, dialog_owl_pos)
    screen.blit(
        font2.render(owl_text, True, BLACK),
        (dialog_owl_pos[0] + 5, dialog_owl_pos[1] + 5))
    pygame.display.update()
    pygame.time.wait(2000)


run = True
while run:
    for e in pygame.event.get():
        # выход из программы при нажатии на крестик
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            # выход из программы при нажатии клавиши q или ESCAPE
            if e.key == pygame.K_q or e.key == pygame.K_ESCAPE:
                run = False
            # печатает только цифры
            elif e.unicode.isdecimal() and block == 0:
                numeral += e.unicode
            # при нажатии BACKSPACE убирает последний символ
            elif e.key == pygame.K_BACKSPACE:
                numeral = numeral[:-1]
            # при нажатии Enter сравнение зананного и введенного чисел
            elif e.key == pygame.K_RETURN and numeral:
                if int(numeral) > num and int(numeral) < 101:
                    dialogs('', OUTSIDE_BG, 'Число меньше')
                elif int(numeral) < num:
                    dialogs('', OUTSIDE_BG, 'Число больше')
                elif int(numeral) > 100:
                    dialogs('', OUTSIDE_BG, 'Вы ошиблись')
                if move == 1:
                    if int(numeral) == num:
                        dialogs(f'Это число {numeral}', dialog_cat_pos, 'Кот, ты выиграл!')
                        block = 1
                    else:
                        dialogs('Дог, твой ход', dialog_cat_pos, 'Продолжаем')
                elif move == 2:
                    if int(numeral) == num:
                        dialogs(f'Это число {numeral}', dialog_dog_pos, 'Дог, ты выиграл!')
                        block = 1
                    else:
                        dialogs('Кот, твой ход', dialog_dog_pos, 'Продолжаем')
                # при нажатии Enter очищаем переменную numeral и меняем ход
                numeral = ''
                move += 1
                if move > 2:
                    move = 1

    if block == 0:
        screen.blit(bg, bg_rect)
        screen.blit(cat, cat_rect)
        screen.blit(dog, dog_rect)
        screen.blit(owl, owl_rect)
        screen.blit(font_box, font_rect)
        font_box.fill(SILVER)
        font_box.blit(
            font.render(numeral, True, BLACK), (10, 0))
    pygame.display.update()

    if start == 1:
        dialogs('', OUTSIDE_BG, 'Я загадала число')
        dialogs('', OUTSIDE_BG, 'от 0 до 100')
        dialogs('Кот, твой ход', dialog_dog_pos, 'Отгадайте его')
        start = 0

pygame.quit()
