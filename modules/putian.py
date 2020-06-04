import random
import time
import cv2
import numpy as np

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points
from lib.wechat import senddata
from . import public


def putian(hwnd, x, y):
    huangzitao_choice_img = cv2.cvtColor(cv2.imread("src/huangzitao_choice.png"), cv2.COLOR_BGR2GRAY)
    duihua_lingquputian_img = cv2.cvtColor(cv2.imread("src/duihua_lingquputian.png"), cv2.COLOR_BGR2GRAY)
    button_close_img = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.COLOR_BGR2GRAY)

    # 若锁屏，则解锁
    public.jiesuo(hwnd, x, y)

    result = public.open_window_richeng(hwnd, x, y)
    if not result:
        print("未能打开日程窗口")
        return

    pos = (2432 - 1927, 295 - 193)
    randint_x = random.randint(0, 40)
    randint_y = random.randint(0, 40)
    window_click(hwnd, pos, randint_x, randint_y)

    # 等待传送
    time.sleep(random.uniform(2.8, 3.2))

    # 领普天
    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, button_close_img)
    if points:
        # 点开大地图
        pos = (1997 - 1927, 178 - 156)
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.2))
        # 移动到能显示黄子韬的位置
        pos = (2211 - 1927, 336 - 156)
        randint_x = random.randint(0, 2)
        randint_y = random.randint(0, 2)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(2.8, 3.2))
        # 点黄子韬
        pos = (2223 - 1927, 307 - 156)
        randint_x = random.randint(0, 10)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.2))
        # 关闭地图
        pos = (1997 - 1927, 178 - 156)
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)

        for i in range(20):
            time.sleep(random.uniform(0.2, 0.3))
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, huangzitao_choice_img, threshold=0.98)
            if points:
                # 怪站一起了，需要选择
                pos = points[0]
                randint_x = random.randint(5, 90)
                randint_y = random.randint(5, 20)
                window_click(hwnd, pos, randint_x, randint_y)
                continue
            points = get_match_points(src_img, duihua_lingquputian_img)
            if points:
                px, py = points[0]
                pos = (px + 50, py + 20)
                randint_x = random.randint(0, 80)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                break