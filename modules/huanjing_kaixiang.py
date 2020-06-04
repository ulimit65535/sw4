import random
import time
import cv2
import numpy as np

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points


def huanjing_kaixiang(hwnd, x, y, is_leader):
    button_queding_huanjing_img = cv2.cvtColor(cv2.imread("src/button_queding_huanjing.png"), cv2.COLOR_BGR2GRAY)
    button_zanli_img = cv2.cvtColor(cv2.imread("src/button_zanli.png"), cv2.COLOR_BGR2GRAY)
    button_guidui_img = cv2.cvtColor(cv2.imread("src/button_guidui.png"), cv2.COLOR_BGR2GRAY)
    button_close_img = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.COLOR_BGR2GRAY)

    # 若锁屏，则解锁
    public.jiesuo(hwnd, x, y)

    if is_leader:
        while True:
            time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, button_queding_huanjing_img)
            if points:
                time.sleep(random.uniform(3.8, 4.2))
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, button_close_img)
                if points:
                    pos = points[0]
                    randint_x = random.randint(0, 5)
                    randint_y = random.randint(0, 5)
                    window_click(hwnd, pos, randint_x, randint_y)
    else:
        # 切换到队伍显示
        public.show_menu_duiwu(hwnd, x, y)

        # 开箱时队员暂离，注意需要任务列表需要切换到队伍界面，方便离队归队
        while True:
            time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, button_queding_huanjing_img)
            if points:
                # 取消弹窗
                pos = (2852 - 1927, 339 - 156)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.8, 1.2))
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, button_zanli_img)
                if points:
                    pos = (2852 - 1927, 339 - 156)
                    randint_x = random.randint(0, 5)
                    randint_y = random.randint(0, 5)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(4.8, 5.2))
                else:
                    # 点下队伍
                    pos = (2852 - 1927, 339 - 156)
                    randint_x = random.randint(0, 5)
                    randint_y = random.randint(0, 5)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(0.8, 1.2))
                    src_img = window_capture(hwnd, x, y)
                    points = get_match_points(src_img, button_zanli_img)
                    if points:
                        pos = (2852 - 1927, 339 - 156)
                        randint_x = random.randint(0, 5)
                        randint_y = random.randint(0, 5)
                        window_click(hwnd, pos, randint_x, randint_y)
                        time.sleep(random.uniform(4.8, 5.2))
                    else:
                        print("暂离失败,退出")
                        return
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, button_guidui_img)
                if points:
                    pos = (2852 - 1927, 339 - 156)
                    randint_x = random.randint(0, 5)
                    randint_y = random.randint(0, 5)
                    window_click(hwnd, pos, randint_x, randint_y)
                else:
                    # 点下队伍
                    pos = (2852 - 1927, 339 - 156)
                    randint_x = random.randint(0, 5)
                    randint_y = random.randint(0, 5)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(0.8, 1.2))
                    src_img = window_capture(hwnd, x, y)
                    points = get_match_points(src_img, button_guidui_img)
                    if points:
                        pos = (2852 - 1927, 339 - 156)
                        randint_x = random.randint(0, 5)
                        randint_y = random.randint(0, 5)
                        window_click(hwnd, pos, randint_x, randint_y)
                    else:
                        print("归队失败,退出")
                        return
