import random
import time
import cv2
import numpy as np

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points


def mingrifangzhou(hwnd, x, y):
    begin_blue_img = cv2.cvtColor(cv2.imread("src/mrfz/begin_blue.png"), cv2.COLOR_BGR2GRAY)
    begin_confirm_img = cv2.cvtColor(cv2.imread("src/mrfz/begin_confirm.png"), cv2.COLOR_BGR2GRAY)
    battle_end_img = cv2.cvtColor(cv2.imread("src/mrfz/battle_end.png"), cv2.COLOR_BGR2GRAY)
    levelup_img = cv2.cvtColor(cv2.imread("src/mrfz/levelup.png"), cv2.COLOR_BGR2GRAY)
    buy_lizhi_img = cv2.cvtColor(cv2.imread("src/mrfz/buy_lizhi.png"), cv2.COLOR_BGR2GRAY)
    use_lizhi_img = cv2.cvtColor(cv2.imread("src/mrfz/use_lizhi.png"), cv2.COLOR_BGR2GRAY)

    while True:
        time.sleep(random.uniform(settings.inverval_min * 3, settings.inverval_max * 3))

        src_img = window_capture(hwnd, x, y)

        # 开始行动
        points = get_match_points(src_img, begin_blue_img, threshold=0.8)
        if points:
            pos = (1797 - 960, 519 - 36)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 确认行动
        points = get_match_points(src_img, begin_confirm_img)
        if points:
            pos = (1778 - 960, 394 - 36)
            randint_x = random.randint(0, 100)
            randint_y = random.randint(0, 50)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 战斗结束
        points = get_match_points(src_img, battle_end_img)
        if points:
            pos = (1387 - 960, 215 - 36)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 等级提升
        points = get_match_points(src_img, levelup_img)
        if points:
            pos = (1387 - 960, 215 - 36)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 理智不够，使用理智药
        points = get_match_points(src_img, use_lizhi_img)
        if points:
            pos = (1771 - 960, 463 - 36)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 理智不够，无理智药
        points = get_match_points(src_img, buy_lizhi_img)
        if points:
            print("理智药使用完毕，退出.")
            return
