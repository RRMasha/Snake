import pygame
from random import randrange

RES = 800 #размер рабочего окна
SIZE = 50 #размер секций змейки

x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE) #началоное положение змейки
apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE) #положение яблока
leng = 1 #длинна змейки
snake = [(x, y)] #сама змея
dx, dy = 0, 0 #направление движения
fps = 3 # скорость

pygame.init()
win = pygame.display.set_mode([RES, RES]) #окно игры
clock = pygame.time.Clock() #время игры, для регулироваие скорости змейки, без этой фигни вообще не работает!!!

while True:
    win.fill(pygame.Color('white'))
    # отображение змейки и яблока pygame.draw.rect(окно, цвет, координаты)
    [(pygame.draw.rect(win, pygame.Color('green'), (i, j, SIZE, SIZE))) for i, j in snake] #рисуем квадрат зеленого цвета на каждой координате змейки
    ([pygame.draw.rect(win, pygame.Color('red'), (*apple, SIZE, SIZE))]) # рисуем яблоки, *appen распоковка координат
    #шаг змейки, шаг = размер головы
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y)) #рост змейки для ее перемещения
    snake = snake[-leng:] #обрезаем по размеру
    #поедание яблок
    if snake[-1] == apple: #голова на уровне с яблоком
        apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)  # положение яблока
        leng += 1
        fps += 1

    #проход сквозь стены
    if x < 0:
        x = RES - SIZE
    if x > RES - SIZE:
        x = 0
    if y < 0:
        y = RES - SIZE
    if y > RES - SIZE:
        y = 0

    #проигрыщ
    if len(snake) != len(set(snake)): #если есть совпадащие координаты, то змейка наткнулась на себя
        f_end = pygame.font.SysFont('Arial', 66, bold=True) #для конца игры
        while True:
            r_end = f_end.render('ПОТРАЧЕНО', 1, pygame.Color('red'))
            win.blit(r_end, (250, 250))
            pygame.display.flip()
            for event in pygame.event.get():  # проверка события на закрытие приложения
                if event.type == pygame.QUIT:
                    exit()


    pygame.display.flip() #обновляем поверхность
    clock.tick(fps) #задержка для fps, обнавление экрана каждые 5 милисекунд

    for event in pygame.event.get(): #проверка события на закрытие приложения
        if event.type == pygame.QUIT:
            exit()

    #управление
    key = pygame.key.get_pressed() # состояние всех кнопок на клаве
    if key[pygame.K_UP] or key[pygame.K_w]:
        dx = 0
        dy = -1
    if key[pygame.K_DOWN] or key[pygame.K_s]:
        dx = 0
        dy = 1
    if key[pygame.K_LEFT] or key[pygame.K_a]:
        dx = -1
        dy = 0
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        dx = 1
        dy = 0