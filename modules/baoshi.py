import random
import time
import cv2

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points


def baoshi(hwnd, x, y):
    icon_baoshidu_img = cv2.cvtColor(cv2.imread("src/icon_baoshidu.png"), cv2.COLOR_BGR2GRAY)
    icon_baoshidu_big_img = cv2.cvtColor(cv2.imread("src/icon_baoshidu_big.png"), cv2.COLOR_BGR2GRAY)
    icon_xiuli_img = cv2.cvtColor(cv2.imread("src/icon_xiuli.png"), cv2.COLOR_BGR2GRAY)
    icon_xiuli_big_img = cv2.cvtColor(cv2.imread("src/icon_xiuli_big.png"), cv2.COLOR_BGR2GRAY)
    close_baoshidu_img = cv2.cvtColor(cv2.imread("src/close_baoshidu.png"), cv2.COLOR_BGR2GRAY)
    buchongbaoshi_img = cv2.cvtColor(cv2.imread("src/buchongbaoshi.png"), cv2.COLOR_BGR2GRAY)
    xiulizhuangbei_img = cv2.cvtColor(cv2.imread("src/xiulizhuangbei.png"), cv2.COLOR_BGR2GRAY)
    button_close_img = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.COLOR_BGR2GRAY)

    # 若锁屏，则解锁
    public.jiesuo(hwnd, x, y)

    src_img = window_capture(hwnd, x, y)

    points = get_match_points(src_img, button_close_img)
    if points:
        # 误点到战备，或者NPC对话，关闭
        pos = points[0]
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.4, 0.6))
        src_img = window_capture(hwnd, x, y)

    # 修理装备耐久度
    points = get_match_points(src_img, icon_xiuli_img, threshold=0.8)
    if points:
        pos = points[0]
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.6, 0.8))

        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, icon_xiuli_big_img, threshold=0.85)
        if points:
            px, py = points[0]
            pos = (px + 339, py)
            randint_x = random.randint(5, 10)
            randint_y = random.randint(5, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.8, 1.2))

            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, xiulizhuangbei_img)
            if points:
                pos = points[0]
                randint_x = random.randint(-30, 0)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)

        time.sleep(random.uniform(0.6, 0.8))
        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, close_baoshidu_img)
        if points:
            # 关闭饱食度窗口
            pos = points[0]
            randint_x = random.randint(0, 10)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)

        time.sleep(random.uniform(0.4, 0.6))
        src_img = window_capture(hwnd, x, y)

    points = get_match_points(src_img, icon_baoshidu_img)
    if points:
        pos = points[0]
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.6, 0.8))

        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, icon_baoshidu_big_img)
        if points:
            px, py = points[0]
            pos = (px + 339, py)
            randint_x = random.randint(5, 10)
            randint_y = random.randint(5, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.8, 1.2))

            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, buchongbaoshi_img, threshold=0.95)
            #print(points)
            if points:
                pos = points[0]
                randint_x = random.randint(-80, -50)
                randint_y = random.randint(5, 15)
                window_click(hwnd, pos, randint_x, randint_y)

        time.sleep(random.uniform(0.6, 0.8))
        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, close_baoshidu_img)
        if points:
            # 关闭饱食度窗口
            pos = points[0]
            randint_x = random.randint(0, 10)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
