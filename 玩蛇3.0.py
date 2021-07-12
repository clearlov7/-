import pygame
import sys
import random
from pygame.locals import *
import time

windowWidth=600
windowHeight=600
cellSize=20
head = 0

def main():
    #初始化
    pygame.init()
    global screen
    screen=pygame.display.set_mode((windowWidth,windowHeight))
    pygame.display.set_caption("Greedy Snake")
    gameStart()
    FPS=pygame.time.Clock()
    startX=cellSize*random.randint(8,windowWidth/cellSize-8)
    startY=cellSize*random.randint(8,windowHeight/cellSize-8)

    snake=[{'x': startX , 'y': startY},
           {'x': startX - 1 * cellSize, 'y': startY},
            {'x': startX - 2 * cellSize, 'y': startY},
           {'x': startX - 3 * cellSize, 'y': startY}]
    appleX = cellSize * random.randint(0, windowWidth / cellSize)
    appleY = cellSize * random.randint(0, windowHeight / cellSize)

    while True:
        FPS.tick(15)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                turn(snake,event)
        move(snake)
        if snake[head]['x']==appleX and snake[head]['y']==appleY:
            appleX = cellSize * random.randint(0, windowWidth / cellSize)
            appleY = cellSize * random.randint(0, windowHeight / cellSize)
            eat(snake)

        if snake[head]['x']<0 or snake[head]['x']>windowWidth or snake[head]['y']<0 or snake[head]['y']>windowHeight:
            gameOver(snake)
        for body in snake[1:]:
            if body==snake[head]:
                gameOver(snake)

        screen.fill((0, 150, 0))

        drawSnake(snake)
        pygame.draw.rect(screen, (255, 0, 0), (appleX, appleY, cellSize, cellSize))

        pygame.display.update()



#绘制蛇
def drawSnake(snake):
    for cood in snake:
        pygame.draw.rect(screen,(150,150,0),(cood['x'],cood['y'],cellSize,cellSize))
    pygame.draw.rect(screen, (250, 250, 0), (snake[head]['x'], snake[head]['y'], cellSize, cellSize))

def turn(snake,event):
    # 上下转向
    if snake[head]['y'] == snake[1]['y']:
        if event.key == K_UP:
            del snake[-1]
            newHead = {'x': snake[head]['x'], 'y': snake[head]['y'] - cellSize}
            snake.insert(0, newHead)

        elif event.key == K_DOWN:
            del snake[-1]
            newHead = {'x': snake[head]['x'], 'y': snake[head]['y'] + cellSize}
            snake.insert(0, newHead)

    # 左右转向
    if snake[head]['x'] == snake[1]['x']:
        if event.key == K_LEFT:
            del snake[-1]
            newHead = {'x': snake[head]['x'] - cellSize, 'y': snake[head]['y']}
            snake.insert(0, newHead)

        if event.key == K_RIGHT:
            del snake[-1]
            newHead = {'x': snake[head]['x'] + cellSize, 'y': snake[head]['y']}
            snake.insert(0, newHead)


def move(snake):
    # 向左运动
    if snake[head]['x'] < snake[1]['x']:
        del snake[-1]
        newHead = {'x': snake[head]['x'] - cellSize, 'y': snake[head]['y']}
        snake.insert(0, newHead)
    # 向右运动
    elif snake[head]['x'] > snake[1]['x']:
        del snake[-1]
        newHead = {'x': snake[head]['x'] + cellSize, 'y': snake[head]['y']}
        snake.insert(0, newHead)
    # 向上运动
    elif snake[head]['y'] < snake[1]['y']:
        del snake[-1]
        newHead = {'x': snake[head]['x'], 'y': snake[head]['y'] - cellSize}
        snake.insert(0, newHead)
    # 向下运动
    elif snake[head]['y'] > snake[1]['y']:
        del snake[-1]
        newHead = {'x': snake[head]['x'], 'y': snake[head]['y'] + cellSize}
        snake.insert(0, newHead)

def eat(snake):
    # 向左运动
    if snake[head]['x'] < snake[1]['x']:
        newHead = {'x': snake[head]['x'] - cellSize, 'y': snake[head]['y']}
        snake.insert(0, newHead)
    # 向右运动
    elif snake[head]['x'] > snake[1]['x']:
        newHead = {'x': snake[head]['x'] + cellSize, 'y': snake[head]['y']}
        snake.insert(0, newHead)
    # 向上运动
    elif snake[head]['y'] < snake[1]['y']:
        newHead = {'x': snake[head]['x'], 'y': snake[head]['y'] - cellSize}
        snake.insert(0, newHead)
    # 向下运动
    elif snake[head]['y'] > snake[1]['y']:
        newHead = {'x': snake[head]['x'], 'y': snake[head]['y'] + cellSize}
        snake.insert(0, newHead)

def gameStart():
    screen.fill((0, 150, 0))

    fontObj1 = pygame.font.Font('freesansbold.ttf', 60)
    textSurfaceObj1 = fontObj1.render('Greedy Snake', True, (255,255,255))
    textRectObj1 = textSurfaceObj1.get_rect()
    textRectObj1.center = (windowWidth/2, windowHeight/3)
    screen.blit(textSurfaceObj1,textRectObj1)

    fontObj2 =pygame.font.Font('freesansbold.ttf', 30)
    textSurfaceObj2 = fontObj2.render('Devloper: XIE YI PING ', True,(0, 0, 0))
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj2.center = (windowWidth/2, windowHeight*2/3)
    screen.blit(textSurfaceObj2,textRectObj2)

    pygame.display.update()
    flag=True
    while(flag):
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_SPACE:
                    flag=False


def gameOver(snake) :
    screen.fill((0, 150, 0))
    drawgrid()
    fontObj = pygame.font.Font('freesansbold.ttf', 60)
    textSurfaceObj1 = fontObj.render('Game over!', True, (255,0,0))
    textRectObj1 = textSurfaceObj1.get_rect()
    textRectObj1.center = (windowWidth/3, windowHeight/3)
    screen.blit(textSurfaceObj1,textRectObj1)

    textSurfaceObj2 = fontObj.render('Score: %s' % (len(snake)-4), True, (255, 0, 0))
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj2.center = (windowWidth*2/3, windowHeight*2/3)
    screen.blit(textSurfaceObj2,textRectObj2)

    pygame.display.update()
    while(True):

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    main()