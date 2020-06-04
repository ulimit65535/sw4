import random
import time
import cv2
import numpy as np

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points


def jianxueren(hwnd, x, y):
    xiaoxueren_img = cv2.cvtColor(cv2.imread("src/xiaoxueren.png"), cv2.COLOR_BGR2GRAY)
    xiaoxueren2_img = cv2.cvtColor(cv2.imread("src/xiaoxueren2.png"), cv2.COLOR_BGR2GRAY)
    duidie_close_img = cv2.cvtColor(cv2.imread("src/duidie_close.png"), cv2.COLOR_BGR2GRAY)

    src_img = window_capture(hwnd, x, y)

    # 若锁屏，则解锁
    public.jiesuo(hwnd, x, y, src_img)

    num = 0
    while True:
        time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

        num += 1
        if num >= 600:
            # 点下任务栏，避免锁屏
            pos = (2863 - 1927, 303 - 193)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.8, 1.2))
            pos = (2863 - 1927, 303 - 193)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            num = 0

        src_img = window_capture(hwnd, x, y)

        # 目标堆叠，选中第一个目标
        points = get_match_points(src_img, duidie_close_img)
        if points:
            pos = points[0]
            randint_x = random.randint(-100, -80)
            randint_y = random.randint(0, 15)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        points = get_match_points(src_img, xiaoxueren_img, threshold=0.85)
        if not points:
            points = get_match_points(src_img, xiaoxueren2_img, threshold=0.85)
        if points:
            pos = points[0]
            randint_x = random.randint(5, 10)
            randint_y = random.randint(5, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            continue
