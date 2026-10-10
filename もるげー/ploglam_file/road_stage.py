import pygame
import global_value as g
import save_and_load
hazimekaraxyz = pygame.Rect(200,20,500,150)
tsudukikaraxyz = pygame.Rect(200,400,500,150)
hazimekara = pygame.image.load("../SS/初めから.png")
hazimekara = pygame.transform.scale(hazimekara,(500,150))
tsudukikara = pygame.image.load("../SS/続きから.png")
tsudukikara = pygame.transform.scale(tsudukikara,(600,200))
def stage_load():
    g.screen.fill(pygame.Color("WHITE"))
    g.screen.blit(g.back1,(0,0))
    g.screen.blit(hazimekara,hazimekaraxyz)
    g.screen.blit(tsudukikara,tsudukikaraxyz)
    if hazimekaraxyz.collidepoint(g.mx,g.my) and g.push[0]:
        save_and_load.save()
        g.stage = "3"
    elif tsudukikaraxyz.collidepoint(g.mx,g.my) and g.push[0] or g.key[pygame.K_a]:
        save_one = open('../save_data/save1.txt','r')
        save_datalist = save_one.read().split("\n")
        if "1" != save_datalist[1] and  "2" != save_datalist[1] and "" != save_datalist[0]:
            save_and_load.save_load()
        else:
            font = pygame.font.SysFont("yumincho",50)#！！！！！！！！！！！！！
            no_data = font.render("セーブデータがありません",True,pygame.Color("RED"))
            g.screen.blit(no_data,(200,300))
            
