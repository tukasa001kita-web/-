import pygame
import global_value as g

g.tsue = pygame.image.load("../SS/杖.png")
g.tsue = pygame.transform.scale(g.tsue,(150,150))
g.douguya = pygame.image.load("../SS/ぽるすけの道具屋店内.png")
g.tsueXYZ = pygame.Rect(175,50,200,200)
g.pipo = pygame.mixer.Sound("../SS/piro.mp3")
g.py = pygame.mixer.Sound("../SS/購入.mp3")
g.morubaku = pygame.image.load("../SS/モル爆.png")
g.morubaku = pygame.transform.scale(g.morubaku,(100,150))
g.morubakuXYZ = pygame.Rect(350,50,100,150)
g.dennsetsunokenn = pygame.image.load("../SS/伝説の剣.png")
g.dennsetsunokenn = pygame.transform.scale(g.dennsetsunokenn,(150,150))
g.dennsetsunokennXYZ = pygame.Rect(0,165,150,150)
def douguya():
    g.screen.fill(pygame.Color("WHITE"))
    g.screen.blit(g.douguya,(0,0))
    pygame_font = pygame.font.Font(None,50)
    PRPT_X = pygame_font.render("PRPT:"+str(g.PRPT),True,pygame.Color("gold"))
    g.screen.blit(PRPT_X,(80,715))
    if not "杖" in g.inventory:
        g.screen.blit(g.tsue,(g.tsueXYZ))
        if g.mouserect.colliderect(g.tsueXYZ) and g.push[0]:
            if g.PRPT >= 1000 :
                g.inventory.append("杖")
                g.py.play()
                g.PRPT -= 1000
            else:
                g.pipo.play()
    if not "モル爆" in g.inventory:
        g.screen.blit(g.morubaku,(g.morubakuXYZ))
        if g.mouserect.colliderect(g.morubakuXYZ) and g.push[0]:
            if g.PRPT >= 200 :
                g.inventory.append("モル爆")
                g.py.play()
                g.PRPT -= 200
            else:
                g.pipo.play()
    if not "伝説の剣" in g.inventory:
        g.screen.blit(g.dennsetsunokenn,(g.dennsetsunokennXYZ))
        if g.mouserect.colliderect(g.dennsetsunokennXYZ) and g.push[0]:
            if g.PRPT >= 5600000 :
                g.inventory.append("伝説の剣")
                g.py.play()
                PRPT -= 5600000
            else:
                g.pipo.play()
    if g.key[pygame.K_b]:
        g.doawoakeru.play()
        g.stage = "3"
