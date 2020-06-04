import random
import time
import cv2
import numpy as np

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points


def keju(hwnd, x, y):
    kejudati_img_color = cv2.cvtColor(cv2.imread("src/kejudati.png"), cv2.IMREAD_COLOR)
    window_keju_img = cv2.cvtColor(cv2.imread("src/window_keju.png"), cv2.COLOR_BGR2GRAY)
    fuben_jianglibaoxiang_img = cv2.cvtColor(cv2.imread("src/fuben_jianglibaoxiang.png"), cv2.COLOR_BGR2GRAY)
    window_kaiqibaoxiang_img = cv2.cvtColor(cv2.imread("src/window_kaiqibaoxiang.png"), cv2.COLOR_BGR2GRAY)

    # 若锁屏，则解锁
    public.jiesuo(hwnd, x, y)

    num_error = 0
    num_keju = 0
    while True:
        if num_error >= 5:
            print("错误次数过多，退出")
            return
        if num_keju >= 2:
            print("无法参与科举，退出")
            return

        time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

        src_img = window_capture(hwnd, x, y)

        # 点奖励
        points = get_match_points(src_img, fuben_jianglibaoxiang_img)
        if points:
            px, py = points[0]
            pos = (px + 10, py + 10)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            continue
        else:
            points = get_match_points(src_img, window_kaiqibaoxiang_img)
            if points:
                px, py = points[0]
                pos = (px + 25, py + 10)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                continue

        points = get_match_points(src_img, window_keju_img, threshold=0.8)
        if points:
            num_keju = 0
            # 点第三个答案
            px, py = points[0]
            pos = (px + 50, py + 20)
            randint_x = random.randint(0, 80)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(2.4, 2.6))
            continue

        result = public.open_window_richeng(hwnd, x, y)
        if not result:
            print("未能打开日程窗口")
            num_error += 1
            continue
        else:
            num_error = 0

        src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
        points = get_match_points(src_img, kejudati_img_color, threshold=0.98)
        if not points:
            # 等待字幕消失
            time.sleep(random.uniform(2.8, 3.2))
            src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
            points = get_match_points(src_img, kejudati_img_color, threshold=0.98)
            if not points:
                print("科举答题已完成")
                public.close_window_richeng(hwnd, x, y)
                return

        # 点前往参加
        num_keju += 1
        pos = points[0]
        randint_x = random.randint(15, 30)
        randint_y = random.randint(68, 78)
        window_click(hwnd, pos, randint_x, randint_y)
        continue
