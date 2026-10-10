import pygame
import global_value as g
import stage_front
g.mox , g.moy = 0 , 0
g.sunaba_Flag = False
g.menu_Flag = False
g.moruxyz = pygame.Rect(0,-650,10000,10000)
g.sunabaxyz = pygame.Rect(g.moruxyz.x + 1100,g.moruxyz.y + 800,400,250)
g.douguyaXYZ = pygame.Rect(g.moruxyz.x+1800,g.moruxyz.y+2000,652,403)
g.kannbann = pygame.image.load("../SS/看板.png")
g.kannbann = pygame.transform.scale(g.kannbann,(200,150))
g.sunaba = pygame.image.load("../SS/すなば.png")
g.sunaba = pygame.transform.scale(g.sunaba,(400,250))
g.sunabahairenai = pygame.image.load("../SS/吹き出し砂場入れない.png")
g.sunabahairenai = pygame.transform.scale(g.sunabahairenai,(150,100))
g.porusukenodouguya = pygame.image.load("../SS/ぽるすけの道具屋.png")
g.douguyaxyz = pygame.Rect(450,600,700,400)
g.porusukenodouguya = pygame.transform.scale(g.porusukenodouguya,(700,400))
g.doawoakeru = pygame.mixer.Sound("../SS/ドア開け.mp3")
g.honnmonomoru = pygame.Rect(450,400,100,100)
g.sidemenu = pygame.image.load("../ss/サイドメニュー.png")
#maping
dokokanomachimapbase = pygame.Surface((3000,3000))
walls = []

g.pygame_font = pygame.font.Font(None,30)
#mapcip 100*100
mapchip = [pygame.image.load("../SS/壁.png"),
           pygame.image.load("../SS/草原.png"),
           pygame.image.load("../SS/壁.png"),
           pygame.image.load("../SS/道.png"),
           g.kannbann
           ]
#data mapcip = 100×100　なので1行当たり30回 縦30回

dokokanomachimap = [[2,2,2,2,2,2,2,2,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                    [2,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [2,1,1,1,1,4,0,1,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [2,1,1,1,1,0,0,1,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [3,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
                    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
                    ]
for doy in range(30):
    for dox in range(30):
        man = dokokanomachimap[doy][dox]
        b = (dox*100,doy*100)
        if man != 0:
            dokokanomachimapbase.blit(mapchip[man],b)
def maprectupdata():
    global walls
    walls = []
    for doy in range(30):
        for dox in range(30):
            n = dokokanomachimap[doy][dox]
            if n == 2 or n == 0 or n == 4:
                walls.append(pygame.Rect(dox*100+g.moruxyz.x,doy*100+g.moruxyz.y,100,100))
maprectupdata()
#----------どこかのまち--どこかの町は後ろに作る-----------------
def stage_dokokanomachi():
    #---------キーボード操作--------------------
    if g.menu_Flag != True:
        if g.key[pygame.K_a] or g.key[pygame.K_LEFT]:
            g.mox += 10
            g.right_Flag = False
        if g.key[pygame.K_d] or g.key[pygame.K_RIGHT]:
            g.mox -= 10
            g.right_Flag = True
        if g.key[pygame.K_w] or g.key[pygame.K_UP]:
            g.moy += 10
        if g.key[pygame.K_s] or g.key[pygame.K_DOWN]:
            g.moy -= 10
    #
    g.moruxyz.x += g.mox
    g.moruxyz.y += g.moy
    #----------------各種当たり判定-----------
    #どこかの町の周りの壁たち　と　看板などの壁が必要になるもの
    maprectupdata()
    if  g.honnmonomoru.collidelist(walls) != -1:
        g.moruxyz.x -= g.mox
        g.moruxyz.y -= g.moy
    
    #砂場などの当たり判定
    g.sunabaxyz = pygame.Rect(g.moruxyz.x + 1100,g.moruxyz.y + 800,400,250)
    g.sunaba_Flag = False
    if  g.honnmonomoru.colliderect(g.sunabaxyz):
        g.moruxyz.x -= g.mox
        g.moruxyz.y -= g.moy
        g.sunabaxyz.x = g.moruxyz.x+1100
        g.sunabaxyz.y = g.moruxyz.y+800
        g.sunaba_Flag = True
    #道具屋との当たり判定
    g.douguyaXYZ.y = g.moruxyz.y+2000#道具屋の位置y
    g.douguyaXYZ.x = g.moruxyz.x+1800#道具屋の位置x
    if g.honnmonomoru.colliderect(g.douguyaXYZ):
        if g.key[pygame.K_n]:
            g.doawoakeru.play()
            g.stage = "3-1"

    
    g.mox , g.moy = 0 , 0
    #---------------------------表示-------------------
    #スクリーンをリセットする
    g.screen.fill(pygame.Color("white"))
    #どこかの町の表示
    g.screen.blit(dokokanomachimapbase,(g.moruxyz))
    #砂場の表示
    g.sunabaxyz = pygame.Rect(g.moruxyz.x + 1100,g.moruxyz.y + 800,400,230)
    g.screen.blit(g.sunaba,(g.sunabaxyz))
    #ぽるすけの道具屋
    g.screen.blit(g.porusukenodouguya,(g.douguyaXYZ))
    #砂場に入れない
    if g.sunaba_Flag == True:
        g.screen.blit(g.sunabahairenai,(500,300))
    
    #モルスケの絵画
    if g.right_Flag == True:
        g.screen.blit(g.moruR,(g.honnmonomoru))
    else:
        g.screen.blit(g.moruL,(g.honnmonomoru))

    g.screen.blit(g.sidemenu,(0,0))
    
    stage_txt = g.pygame_font.render("stage "+str(g.stage),True,pygame.Color("BLACK"))
    g.screen.blit(stage_txt,(0,0))
    
    PRPT_txt = g.pygame_font.render("PRPT:"+str(g.PRPT),True,pygame.Color("BLACK"))
    g.screen.blit(PRPT_txt,(0,22))

    level_txt = g.pygame_font.render("level:"+str(g.level),True,pygame.Color("BLACK"))
    g.screen.blit(level_txt,(0,45))
    if g.key[pygame.K_m]:
        g.menu_Flag = True
        
    if g.menu_Flag == True:
        stage_front.menu()
        
