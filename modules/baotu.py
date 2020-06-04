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


def baotu(hwnd, x, y, skill_order=None, eat_food=False):
    icon_baotu_img_color = cv2.cvtColor(cv2.imread("src/icon_baotu.png"), cv2.IMREAD_COLOR)
    duihua_datingcangbaotu_img = cv2.cvtColor(cv2.imread("src/duihua_datingcangbaotu.png"), cv2.COLOR_BGR2GRAY)
    baotu_duihua_img = cv2.cvtColor(cv2.imread("src/baotu_duihua.png"), cv2.COLOR_BGR2GRAY)
    baotu_finished_img = cv2.cvtColor(cv2.imread("src/baotu_finished.png"), cv2.COLOR_BGR2GRAY)

    lower = np.array([20, 150, 140], dtype="uint8")
    upper = np.array([80, 240, 255], dtype="uint8")

    renwu_baotu_img_color = cv2.cvtColor(cv2.imread("src/renwu_baotu.png"), cv2.IMREAD_COLOR)
    mask = cv2.inRange(renwu_baotu_img_color, lower, upper)
    renwu_baotu_img_color = cv2.bitwise_and(renwu_baotu_img_color, renwu_baotu_img_color, mask=mask)
    renwu_baotu_img = cv2.cvtColor(renwu_baotu_img_color, cv2.COLOR_BGR2GRAY)

    # 若锁屏，则解锁
    public.jiesuo(hwnd, x, y)

    if eat_food:
        public.eat_food(hwnd, x, y, "baotu")

    # 切换挂机技能
    if skill_order is not None:
        public.change_skill(hwnd, x, y, skill_order)

    num_error = 0
    num_get = 0
    while True:
        if num_error >= 5:
            print("错误次数过多，退出")
            return


        time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

        src_img = window_capture(hwnd, x, y)

        # 对话，选“打听藏宝图”
        points = get_match_points(src_img, duihua_datingcangbaotu_img)
        if points:
            if num_get >= 1:
                # 关闭NPC对话框
                pos = (2856 - 1927, 233 - 193)
                randint_x = random.randint(0, 10)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                print("无法领取宝图任务，退出")
                return
            else:
                num_get += 1
                px, py = points[0]
                pos = (px + 50, py + 20)
                randint_x = random.randint(0, 80)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(3.8, 4.2))
                continue
        # 宝图对话，交任务
        points = get_match_points(src_img, baotu_duihua_img)
        if points:
            px, py = points[0]
            pos = (px + 50, py + 20)
            randint_x = random.randint(0, 80)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 对话，已完成任务
        points = get_match_points(src_img, baotu_finished_img)
        if points:
            # 关闭NPC对话框
            pos = (2856 - 1927, 233 - 193)
            randint_x = random.randint(0, 10)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            print("宝图任务已完成")
            return

        # 是否在移动中?
        status = public.get_status(hwnd, x, y, src_img)

        if status != "standing":
            continue

        public.show_menu_renwu(hwnd, x, y)

        # 优先查找任务栏显示
        src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
        left = 770
        top = 140
        w = 100
        h = 250
        opponent_img = src_img[top:top + h, left:left + w]
        mask = cv2.inRange(opponent_img, lower, upper)
        opponent_img = cv2.bitwise_and(opponent_img, opponent_img, mask=mask)
        opponent_img = cv2.cvtColor(opponent_img, cv2.COLOR_BGR2GRAY)

        #cv2.namedWindow("Image")
        #cv2.imshow("Image", opponent_img)
        #cv2.waitKey(0)
        #sys.exit(1)

        points = get_match_points(opponent_img, renwu_baotu_img, threshold=0.7)
        if points:
            # 点击任务栏任务
            px, py = points[0]
            # px, py是相对于opponent_img的坐标，所以还要加上left和top
            pos = (px + 770 + 70, py + 140 + 15)
            randint_x = random.randint(0, 20)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        result = public.open_window_richeng(hwnd, x, y)
        if not result:
            print("未能打开日程窗口")
            num_error += 1
            continue
        else:
            num_error = 0

        src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
        points = get_match_points(src_img, icon_baotu_img_color, threshold=0.95)
        if not points:
            # 等待字幕消失
            time.sleep(random.uniform(2.8, 3.2))
            src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
            points = get_match_points(src_img, icon_baotu_img_color, threshold=0.95)
            if not points:
                print("宝图任务已完成")
                public.close_window_richeng(hwnd, x, y)
                return

        pos = (2224 - 1927, 294 - 193)
        randint_x = random.randint(0, 40)
        randint_y = random.randint(0, 40)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(3.8, 4.2))
        continue
