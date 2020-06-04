import random
import time
import cv2
import numpy as np

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points


def shimen(hwnd, x, y, skill_order=None):
    icon_shimen_img_color = cv2.cvtColor(cv2.imread("src/icon_shimen.png"), cv2.IMREAD_COLOR)
    duihua_woyaozuorenwu_img = cv2.cvtColor(cv2.imread("src/duihua_woyaozuorenwu.png"), cv2.COLOR_BGR2GRAY)
    jinruzhandou_img = cv2.cvtColor(cv2.imread("src/jinruzhandou.png"), cv2.COLOR_BGR2GRAY)
    fanhuishimen_img = cv2.cvtColor(cv2.imread("src/fanhuishimen.png"), cv2.COLOR_BGR2GRAY)
    duihua_img = cv2.cvtColor(cv2.imread("src/duihua.png"), cv2.COLOR_BGR2GRAY)
    shimen_duihua_img = cv2.cvtColor(cv2.imread("src/shimen_duihua.png"), cv2.COLOR_BGR2GRAY)

    lower = np.array([20, 150, 140], dtype="uint8")
    upper = np.array([80, 240, 255], dtype="uint8")

    renwu_shimen_img_color = cv2.cvtColor(cv2.imread("src/renwu_shimen.png"), cv2.IMREAD_COLOR)
    mask = cv2.inRange(renwu_shimen_img_color, lower, upper)
    renwu_shimen_img_color = cv2.bitwise_and(renwu_shimen_img_color, renwu_shimen_img_color, mask=mask)
    renwu_shimen_img = cv2.cvtColor(renwu_shimen_img_color, cv2.COLOR_BGR2GRAY)

    # 若锁屏，则解锁
    public.jiesuo(hwnd, x, y)

    # 切换挂机技能
    if skill_order is not None:
        public.change_skill(hwnd, x, y, skill_order)

    num_error = 0
    while True:
        if num_error >= 5:
            print("错误次数过多，退出")
            return

        time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

        src_img = window_capture(hwnd, x, y)

        # 对话，选“我要做任务”
        points = get_match_points(src_img, duihua_woyaozuorenwu_img)
        if points:
            pos = (2649 - 1927, 520 - 193)
            randint_x = random.randint(0, 100)
            randint_y = random.randint(0, 20)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 师门对话，接任务
        points = get_match_points(src_img, shimen_duihua_img)
        if points:
            px, py = points[0]
            pos = (px + 50, py + 20)
            randint_x = random.randint(0, 80)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 点击对话
        points = get_match_points(src_img, duihua_img, threshold=0.95)
        if points:
            pos = (812, 154)
            randint_x = random.randint(0, 100)
            randint_y = random.randint(0, 30)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 小BOSS。进入战斗
        points = get_match_points(src_img, jinruzhandou_img,threshold=0.8)
        if points:
            pos = points[0]
            randint_x = random.randint(5, 105)
            randint_y = random.randint(5, 15)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 点返回师门
        points = get_match_points(src_img, fanhuishimen_img)
        if points:
            pos = points[0]
            randint_x = random.randint(5, 105)
            randint_y = random.randint(5, 15)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 是否在移动中?
        status = public.get_status(hwnd, x, y, src_img)

        if status == "close_window_other":
            print("师门任务已达上限，退出。")
            return
        if status == "yanzheng_failed":
            print("验证失败，退出.")
            return

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

        points = get_match_points(opponent_img, renwu_shimen_img, threshold=0.7)
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
        points = get_match_points(src_img, icon_shimen_img_color, threshold=0.95)
        if not points:
            # 等待字幕消失
            time.sleep(random.uniform(2.8, 3.2))
            src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
            points = get_match_points(src_img, icon_shimen_img_color, threshold=0.95)
            if not points:
                print("师门任务已完成")
                public.close_window_richeng(hwnd, x, y)
                return

        # 点师门任务
        pos = (200, 104)
        randint_x = random.randint(0, 40)
        randint_y = random.randint(0, 40)
        window_click(hwnd, pos, randint_x, randint_y)
        continue
