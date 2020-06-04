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


def renwulian(hwnd, x, y):
    renwulian_duihua_img = cv2.cvtColor(cv2.imread("src/renwulian_duihua.png"), cv2.COLOR_BGR2GRAY)
    renwulian_zhandou_duihua_img = cv2.cvtColor(cv2.imread("src/renwulian_zhandou_duihua.png"), cv2.COLOR_BGR2GRAY)
    guyongbangshou_img = cv2.cvtColor(cv2.imread("src/guyongbangshou.png"), cv2.COLOR_BGR2GRAY)

    lower = np.array([20, 150, 140], dtype="uint8")
    upper = np.array([80, 240, 255], dtype="uint8")

    renwu_renwulian_img_color = cv2.cvtColor(cv2.imread("src/renwu_renwulian.png"), cv2.IMREAD_COLOR)
    mask = cv2.inRange(renwu_renwulian_img_color, lower, upper)
    renwu_renwulian_img_color = cv2.bitwise_and(renwu_renwulian_img_color, renwu_renwulian_img_color, mask=mask)
    renwu_renwulian_img = cv2.cvtColor(renwu_renwulian_img_color, cv2.COLOR_BGR2GRAY)

    # 若锁屏，则解锁
    public.jiesuo(hwnd, x, y)

    is_start = True
    while True:
        time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

        src_img = window_capture(hwnd, x, y)

        """
        # 战斗，需要组人
        points = get_match_points(src_img, renwulian_zhandou_duihua_img, threshold=0.97)
        if points:
            pos = (2856 - 1927, 233 - 193)
            randint_x = random.randint(0, 10)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(9.8, 10.2))
            continue
        """
        # 提升再战
        points = get_match_points(src_img, guyongbangshou_img)
        if points:
            senddata("窗口:{}战斗失败，退出。".format(hwnd), "")
            # 关闭对话
            pos = (2856 - 1927, 234 - 193)
            randint_x = random.randint(0, 15)
            randint_y = random.randint(0, 15)
            window_click(hwnd, pos, randint_x, randint_y)
            return
        
        # 对话，接任务
        points = get_match_points(src_img, renwulian_duihua_img)
        if points:
            px, py = points[0]
            pos = (px + 50, py + 20)
            randint_x = random.randint(0, 80)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 是否在移动中?
        status = public.get_status(hwnd, x, y, src_img, auto_buy=False)

        if status == "in_battle":
            public.show_menu_renwu(hwnd, x, y)
        if status != "standing":
            continue

        public.show_menu_renwu(hwnd, x, y)

        # 优先查找任务栏显示
        src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
        # 注意点怪的时候，Y最多向上移25-30个像素，不然会点开人物界面
        left = 770
        top = 140
        w = 100
        h = 250
        opponent_img = src_img[top:top + h, left:left + w]
        mask = cv2.inRange(opponent_img, lower, upper)
        opponent_img = cv2.bitwise_and(opponent_img, opponent_img, mask=mask)
        opponent_img = cv2.cvtColor(opponent_img, cv2.COLOR_BGR2GRAY)

        points = get_match_points(opponent_img, renwu_renwulian_img, threshold=0.7)
        if points:
            is_start = False
            # 点击任务栏任务
            px, py = points[0]
            # px, py是相对于opponent_img的坐标，所以还要加上left和top
            pos = (px + 770 + 70, py + 140 + 15)
            randint_x = random.randint(0, 20)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
        else:
            if is_start:
                print("任务栏不存在任务链任务，退出")
                return