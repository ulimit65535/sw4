import random
import time
import cv2

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points


def jingji(hwnd, x, y, skill_order=None, eat_food=False):
    icon_jingjichang_img_color = cv2.cvtColor(cv2.imread("src/icon_jingjichang.png"), cv2.IMREAD_COLOR)
    button_tiaozhan_img = cv2.cvtColor(cv2.imread("src/button_tiaozhan.png"), cv2.COLOR_BGR2GRAY)

    # 若锁屏，则解锁
    public.jiesuo(hwnd, x, y)

    if eat_food:
        public.eat_food(hwnd, x, y, "jingji")

    # 切换挂机技能
    if skill_order is not None:
        public.change_skill(hwnd, x, y, skill_order)

    for i in range(10):
        result = public.open_window_richeng(hwnd, x, y)
        if not result:
            time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
        else:
            break
    if not result:
        print("未能打开日程窗口")
        return

    src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
    points = get_match_points(src_img, icon_jingjichang_img_color, threshold=0.95)
    if not points:
        # 等待字幕消失
        time.sleep(random.uniform(1.8, 2.2))
        src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
        points = get_match_points(src_img, icon_jingjichang_img_color, threshold=0.95)
        if not points:
            print("竞技场任务已完成")
            public.close_window_richeng(hwnd, x, y)
            return

    px, py = points[0]
    pos = (px, py - 36)
    randint_x = random.randint(0, 40)
    randint_y = random.randint(0, 40)
    window_click(hwnd, pos, randint_x, randint_y)
    time.sleep(random.uniform(1.4, 1.6))

    num_standing = 0
    while True:
        time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

        src_img = window_capture(hwnd, x, y)

        status = public.get_status(hwnd, x, y, src_img, npc_jiaohu=False, call_pet=False)
        if status == "window_jingjichang":
            num_standing = 0
            # 先点刷新对手
            pos = (2652 - 1927, 660 - 193)
            randint_x = random.randint(0, 80)
            randint_y = random.randint(0, 25)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(1.2, 1.4))

            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, button_tiaozhan_img)
            if points:
                print("开始挑战")
                pos = points[0]
                randint_x = random.randint(0, 40)
                randint_y = random.randint(0, 20)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(1.4, 1.6))
        elif status == "standing":
            num_standing += 1
            if num_standing <2:
                continue
            else:
                for i in range(10):
                    result = public.open_window_richeng(hwnd, x, y)
                    if not result:
                        time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
                    else:
                        break
                if not result:
                    print("未能打开日程窗口")
                    return

                src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
                points = get_match_points(src_img, icon_jingjichang_img_color, threshold=0.95)
                if not points:
                    # 等待字幕消失
                    time.sleep(random.uniform(1.8, 2.2))
                    src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
                    points = get_match_points(src_img, icon_jingjichang_img_color, threshold=0.95)
                    if not points:
                        print("竞技场任务已完成")
                        public.close_window_richeng(hwnd, x, y)
                        return
                px, py = points[0]
                pos = (px, py - 36)
                randint_x = random.randint(0, 40)
                randint_y = random.randint(0, 40)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(1.4, 1.6))
                num_standing = 0
                continue
