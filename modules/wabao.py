import random
import time
import cv2
import numpy as np

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points


def wabao(hwnd, x, y):
    icon_wupin_img = cv2.cvtColor(cv2.imread("src/icon_wupin.png"), cv2.COLOR_BGR2GRAY)
    baotu_img = cv2.cvtColor(cv2.imread("src/baotu.png"), cv2.COLOR_BGR2GRAY)
    #button_shiyong_img = cv2.cvtColor(cv2.imread("src/button_shiyong.png"), cv2.COLOR_BGR2GRAY)
    button_luopan_img = cv2.cvtColor(cv2.imread("src/button_luopan.png"), cv2.COLOR_BGR2GRAY)
    baotu_shiyong_img = cv2.cvtColor(cv2.imread("src/baotu_shiyong.png"), cv2.COLOR_BGR2GRAY)
    #wuping_close_img = cv2.cvtColor(cv2.imread("src/wuping_close.png"), cv2.COLOR_BGR2GRAY)

    # 若锁屏，则解锁
    public.jiesuo(hwnd, x, y)

    src_img = window_capture(hwnd, x, y)

    points = get_match_points(src_img, icon_wupin_img)
    if points:
        pos = points[0]
        randint_x = random.randint(5, 15)
        randint_y = random.randint(5, 15)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.2))
    else:
        print("未能打开背包，退出.")
        return

    has_baotu = False
    for i in range(3):
        # 切换物品栏
        pos = (2445 - 1927 + i * 65, 217 - 156)
        randint_x = random.randint(0, 30)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(1.4, 1.6))
        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, baotu_img)
        if points:
            has_baotu = True
            pos = points[0]
            randint_x = random.randint(10, 15)
            randint_y = random.randint(20, 25)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.8, 1.2))

            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, button_luopan_img)
            if points:
                pos = points[0]
                randint_x = random.randint(5 + 143, 80 + 143)
                randint_y = random.randint(5, 20)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.8, 1.2))

                # 关闭背包
                #src_img = window_capture(hwnd, x, y)
                #points = get_match_points(src_img, wuping_close_img)
                #if points:
                pos = (2766 - 1927, 180 - 156)
                randint_x = random.randint(5, 15)
                randint_y = random.randint(5, 15)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.6, 0.8))

                break
            else:
                print("使用宝图失败，退出")
                return

    if not has_baotu:
        pos = (2766 - 1927, 180 - 156)
        randint_x = random.randint(5, 15)
        randint_y = random.randint(5, 15)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.6, 0.8))
        print("背包中未发现宝图，退出")
        return

    wait_num = 0
    while True:
        if wait_num >= 60:
            # 再次查看背包
            wait_num = 0

            src_img = window_capture(hwnd, x, y)

            points = get_match_points(src_img, icon_wupin_img)
            if points:
                pos = points[0]
                randint_x = random.randint(5, 15)
                randint_y = random.randint(5, 15)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.8, 1.2))
            else:
                print("未能打开背包，退出.")
                return

            has_baotu = False
            for i in range(3):
                # 切换物品栏
                pos = (2445 - 1927 + i * 65, 217 - 156)
                randint_x = random.randint(0, 30)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(1.4, 1.6))
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, baotu_img)
                if points:
                    has_baotu = True
                    pos = points[0]
                    randint_x = random.randint(10, 15)
                    randint_y = random.randint(20, 25)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(0.8, 1.2))

                    src_img = window_capture(hwnd, x, y)
                    points = get_match_points(src_img, button_luopan_img)
                    if points:
                        pos = points[0]
                        randint_x = random.randint(5 + 143, 80 + 143)
                        randint_y = random.randint(5, 20)
                        window_click(hwnd, pos, randint_x, randint_y)
                        time.sleep(random.uniform(0.8, 1.2))

                        # 关闭背包
                        pos = (2766 - 1927, 180 - 156)
                        randint_x = random.randint(5, 15)
                        randint_y = random.randint(5, 15)
                        window_click(hwnd, pos, randint_x, randint_y)
                        time.sleep(random.uniform(0.6, 0.8))

                        break
                    else:
                        print("使用宝图失败，退出")
                        return

            if not has_baotu:
                pos = (2766 - 1927, 180 - 156)
                randint_x = random.randint(5, 15)
                randint_y = random.randint(5, 15)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.6, 0.8))
                print("背包中未发现宝图，挖宝结束")
                return

        time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

        src_img = window_capture(hwnd, x, y)

        # 点使用
        points = get_match_points(src_img, baotu_shiyong_img)
        if points:
            wait_num = 0
            pos = points[0]
            randint_x = random.randint(10, 50)
            randint_y = random.randint(5, 15)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(1.4, 1.6))
            continue
        else:
            wait_num += 1
            continue

