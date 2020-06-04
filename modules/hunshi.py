import random
import time
import cv2
import numpy as np

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points


def hunshi(hwnd, x, y):
    lower = np.array([29, 29, 141], dtype="uint8")
    upper = np.array([90, 98, 240], dtype="uint8")

    xianfeng_img_color = cv2.cvtColor(cv2.imread("src/xianfeng.png"), cv2.IMREAD_COLOR)
    mask = cv2.inRange(xianfeng_img_color, lower, upper)
    xianfeng_img_color = cv2.bitwise_and(xianfeng_img_color, xianfeng_img_color, mask=mask)
    xianfeng_img = cv2.cvtColor(xianfeng_img_color, cv2.COLOR_BGR2GRAY)

    zhanjiang_img_color = cv2.cvtColor(cv2.imread("src/zhanjiang.png"), cv2.IMREAD_COLOR)
    mask = cv2.inRange(zhanjiang_img_color, lower, upper)
    zhanjiang_img_color = cv2.bitwise_and(zhanjiang_img_color, zhanjiang_img_color, mask=mask)
    zhanjiang_img = cv2.cvtColor(zhanjiang_img_color, cv2.COLOR_BGR2GRAY)

    duiwu_yincang_img = cv2.cvtColor(cv2.imread("src/duiwu_yincang.png"), cv2.COLOR_BGR2GRAY)
    duihua_any_img = cv2.cvtColor(cv2.imread("src/duihua_any.png"), cv2.COLOR_BGR2GRAY)
    button_close_img = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.COLOR_BGR2GRAY)
    duidie_close_img = cv2.cvtColor(cv2.imread("src/duidie_close.png"), cv2.COLOR_BGR2GRAY)

    # 若锁屏，则解锁
    public.jiesuo(hwnd, x, y)

    src_img = window_capture(hwnd, x, y)

    # 隐藏任务列表
    points = get_match_points(src_img, duiwu_yincang_img)
    if points:
        pos = points[0]
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.6, 0.8))

    num_standing = 0
    while True:
        time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

        src_img = window_capture(hwnd, x, y)

        status = public.get_status(hwnd, x, y, src_img, with_standing=False, npc_jiaohu=False)
        if status == "in_battle":
            continue

        src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
        # 注意点怪的时候，Y最多向上移25-30个像素，不然会点开人物界面

        left = 151
        top = 115
        w = 740
        h = 280
        opponent_img = src_img[top:top + h, left:left + w]

        mask = cv2.inRange(opponent_img, lower, upper)
        opponent_img = cv2.bitwise_and(opponent_img, opponent_img, mask=mask)
        opponent_img = cv2.cvtColor(opponent_img,cv2.COLOR_BGR2GRAY)

        points = get_match_points(opponent_img, zhanjiang_img, threshold=0.6)
        if not points:
            points = get_match_points(opponent_img, xianfeng_img, threshold=0.6)
        if points:
            # 计数重置
            num = 0
            px, py = points[0]
            # px, py是相对于opponent_img的坐标，所以还要加上left和top
            pos = (px + 151 + 30, py + 115 - 25)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)

            has_battle = True

            # 最多等待5秒
            for i in range(20):
                time.sleep(random.uniform(0.2, 0.3))
                src_img = window_capture(hwnd, x, y)
                # 目标堆叠，选中第一个目标
                points = get_match_points(src_img, duidie_close_img)
                if points:
                    pos = points[0]
                    randint_x = random.randint(-100, -80)
                    randint_y = random.randint(0, 15)
                    window_click(hwnd, pos, randint_x, randint_y)
                    continue
                # 未知对话，选第一个,开打
                points = get_match_points(src_img, duihua_any_img)
                if points:
                    min_y = 1000
                    for point in points:
                        x, y = point
                        if y < min_y:
                            pos_duihua = point
                            min_y = y

                    px, py = pos_duihua
                    pos = (px - 80, py + 20)
                    randint_x = random.randint(0, 80)
                    randint_y = random.randint(0, 5)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(0.8, 1.2))
                    break

            for i in range(10):
                time.sleep(random.uniform(0.4, 0.6))
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, button_close_img)
                if points:
                    # 关闭对话
                    pos = (2856 - 1927, 233 - 193)
                    randint_x = random.randint(0, 10)
                    randint_y = random.randint(0, 10)
                    window_click(hwnd, pos, randint_x, randint_y)
                    print("进入战斗失败")
                    break
        else:
            # 是否在移动中?
            src_img = window_capture(hwnd, x, y)
            status = public.get_status(hwnd, x, y, src_img, npc_jiaohu=False)
            if status != "standing":
                num_standing = 0
                continue
            else:
                num_standing += 1
                if num_standing <= 1:
                    continue

            # 开始巡逻
            result = public.xunluo(hwnd, x, y)
            if not result:
                print("巡逻失败,退出")
                return
