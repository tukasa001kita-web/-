import pygame
import global_value as g
g.pygame_font = pygame.font.Font(None,30)
def command():
    if g.key[pygame.K_x]:
        stage_txt = g.pygame_font.render("stage="+str(g.stage),True,pygame.Color("BLACK"))
        g.screen.blit(stage_txt,(0,0))
        
        PRPT_txt = g.pygame_font.render("PRPT="+str(g.PRPT),True,pygame.Color("BLACK"))
        g.screen.blit(PRPT_txt,(0,22))
        
        morucommandxyz = g.pygame_font.render("dokokanomachi_back"+str(g.moruxyz),True,pygame.Color("BLACK"))
        g.screen.blit(morucommandxyz,(0,44))
        
        mouseXY = (g.mx,g.my)
        mousecommand = g.pygame_font.render("mouse"+str(mouseXY),True,pygame.Color("BLACK"))
        g.screen.blit(mousecommand,(0,66))
        
        inventorycommand = g.pygame_font.render("inventory"+str(g.inventory),True,pygame.Color("BLACK"))
        g.screen.blit(inventorycommand,(0,88))
