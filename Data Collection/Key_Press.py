import pygame
def init():
    pygame.init()
    win = pygame.display.set_mode((250,250))

def getKey(keyName):
    Flag = False
    for eveent in pygame.event.get():pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput[myKey]:
        Flag = True
    pygame.display.update()
    return Flag

