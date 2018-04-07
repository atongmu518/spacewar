# -*- coding: utf-8 -*-

import sys
import pygame

import game_functions as gf

from settings import Settings
from ship import Ship

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen)

    pygame.display.set_caption("外星人入侵")

    # 开始游戏的主循环
    while True:
        gf.check_event()
        gf.update_screen()

run_game()
