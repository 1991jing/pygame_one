import sys
from pygame.sprite import Group
import game_functions as gf
import pygame
from settings import Settings
from ship import Ship
from  alien import Alien
def run_game():
    #初始化游戏并开始创建一个屏幕对象
    #pygame.init()
    #screen=pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    ai_settings =Settings()
    screen =pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #创建一艘飞船
    ship= Ship(ai_settings,screen)
    #创建一个用于存储子子弹的编组
    bullets = Group()
    #创建一个外星人
    alien = Alien(ai_settings,screen)



    #bg_clolor = (230, 230, 230)
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()

        #删除消失的子弹
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship,alien, bullets)








run_game()