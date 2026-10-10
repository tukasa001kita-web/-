import sys
import pygame
pygame.init()
#global_valueの中に変数のすべてを突っ込む
import global_value as g
#スクリーンの表示
g.screen = pygame. display.set_mode((1000,800))
g.moruR = pygame.image.load("../SS/モルスケ.png")
pygame.display.set_icon(g.moruR)
#---------NOW_LOADING---------------------------------------------------------
g.screen.fill(pygame.Color("WHITE"))
pygame_font = pygame.font.Font(None,1000)
roading = pygame_font.render("Now_loading",True,pygame.Color("blue"))
roading = pygame.transform.scale(roading,(500,100))
g.screen.blit(roading,(250,300))
pygame.display.update()
#road
import save_and_load
import stage_call
import command
#-------まずはobject and Sound--------------------
pygame.display.set_caption("モルスケノ冒険")
g.back1 = pygame.image.load("../SS/背景1.png")
g.back1 = pygame.transform.scale(g.back1,(1000,800))
g.tital = pygame.image.load("../SS/タイトル.png")
g.morurun = pygame.mixer.Sound("../SS/start.mp3")
#moruR
g.moruR = pygame.image.load("../SS/モルスケ.png")
g.moruR = pygame.transform.scale(g.moruR,(100,100))
#moruL
g.moruL = pygame.transform.flip(g.moruR,True,False)
g.right_Flag , g.morudeta= True , True

#---------値のリセット------------------------------------
g.PRPT = 1000
g.level , g.stage = 0 , "1"
#この下の中で短いやつ上に突っ込む
g.towback = pygame.Rect(0,0,0,0)
g.inventory = []
#ここから下をループ
while True:
    #-----------キーボードやマウスの操作-------------
    g.key = pygame.key.get_pressed()
    g.push = pygame.mouse.get_pressed()
    (g.mx,g.my) = pygame.mouse.get_pos()
    g.mouserect = pygame.Rect(g.mx,g.my,1,1)
    #--------------ステージを読み込む-------------------
    stage_call.stage_call()
    #コマンド
    command.command()
    #------------終了--------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if g.stage != "2" and g.stage != "1":
                save_and_load.save()
            pygame.quit()
            sys.exit()
    
    #-------------フレームレート-------------
    pygame.display.update()
    pygame.time.Clock().tick(60)
