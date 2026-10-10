import pygame
import global_value as g
pygame.init()
g.N_Flag = False
g.smx = 100
g.sbtn = pygame.image.load("../SS/start_text.png")
g.morurun = pygame.mixer.Sound("../SS/start.mp3")
def stage_start():
    g.screen.fill(pygame.Color("WHITE"))
    g.screen.blit(g.back1,(0,0))
    g.screen.blit(g.tital,(100,50))
    g.screen.blit(g.moruR,(g.smx,400))
    if g.N_Flag == False:
        g.screen.blit(g.sbtn,(300,200))
    
    if g.push[0]:
        if (569,300) > (g.mx,g.my) >(300,200) and g.N_Flag == False:
            g.N_Flag = True
            g.morurun.play()
    elif g.N_Flag == True:
        g.smx += 100
        if g.smx > 1000:
            g.stage = "2"
