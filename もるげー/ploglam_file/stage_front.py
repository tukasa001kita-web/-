import pygame
import global_value as g
hanntoumei = pygame.Surface((1000,800), pygame.SRCALPHA)
# RGBA (黒, 透明度128)
hanntoumei.fill((0, 0, 0, 190))
g.menu_Flag = False
def menu():#---------------------メニューの表示-----------------
    g.screen.blit(hanntoumei, (0, 0))
    
    if g.key[pygame.K_b]:
            g.menu_Flag = False









    
    
