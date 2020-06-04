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


def zhuogui(hwnd, x, y, is_leader, skill_order=None, eat_food=False):
    #huangzitao_choice_img = cv2.cvtColor(cv2.imread("src/huangzitao_choice.png"), cv2.COLOR_BGR2GRAY)
    if is_leader:
        zhuogui_duihua_img = cv2.cvtColor(cv2.imread("src/zhuogui_duihua.png"), cv2.COLOR_BGR2GRAY)
        wobangniquzhuo_img = cv2.cvtColor(cv2.imread("src/wobangniquzhuo.png"), cv2.COLOR_BGR2GRAY)
        zhuogui_finished_img = cv2.cvtColor(cv2.imread("src/zhuogui_finished.png"), cv2.COLOR_BGR2GRAY)
        #duihua_lingquputian_img = cv2.cvtColor(cv2.imread("src/duihua_lingquputian.png"), cv2.COLOR_BGR2GRAY)
        #button_close_img = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.COLOR_BGR2GRAY)

        # 若锁屏，则解锁
        public.jiesuo(hwnd, x, y)

        if eat_food:
            public.eat_food(hwnd, x, y, "zhuogui")

        # 切换挂机技能
        if skill_order is not None:
            public.change_skill(hwnd, x, y, skill_order)
        else:
            time.sleep(4.0)

        result = public.open_window_richeng(hwnd, x, y)
        if not result:
            print("未能打开日程窗口")
            return

        pos = (2432 - 1927, 295 - 193)
        randint_x = random.randint(0, 40)
        randint_y = random.randint(0, 40)
        window_click(hwnd, pos, randint_x, randint_y)

        # 等待传送
        time.sleep(random.uniform(2.8, 3.2))

        num_error = 0
        while True:
            if num_error >= 5:
                print("错误次数过多，退出")
                return

            time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

            src_img = window_capture(hwnd, x, y)

            # 钟馗对话，接任务
            points = get_match_points(src_img, wobangniquzhuo_img)
            if points:
                px, py = points[0]
                pos = (px + 50, py + 20)
                randint_x = random.randint(0, 80)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                continue

            # 捉鬼，交任务
            points = get_match_points(src_img, zhuogui_duihua_img)
            if points:
                px, py = points[0]
                pos = (px + 50, py + 20)
                randint_x = random.randint(0, 80)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                continue

            # 钟馗对话，已完成任务
            points = get_match_points(src_img, zhuogui_finished_img)
            if points:
                # 关闭NPC对话框
                pos = (2856 - 1927, 233 - 193)
                randint_x = random.randint(0, 10)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                print("捉鬼任务已完成")
                return

            # 是否在移动中?
            status = public.get_status(hwnd, x, y, src_img)

            if status == "yanzheng_failed":
                senddata("窗口:{}验证失败，退出。".format(hwnd), "")
                return

            if status != "standing":
                continue

            result = public.open_window_richeng(hwnd, x, y)
            if not result:
                print("未能打开日程窗口")
                num_error += 1
                continue
            else:
                num_error = 0

            pos = (2432 - 1927, 295 - 193)
            randint_x = random.randint(0, 40)
            randint_y = random.randint(0, 40)
            window_click(hwnd, pos, randint_x, randint_y)
            continue
    else:
        # 若锁屏，则解锁
        public.jiesuo(hwnd, x, y)

        if eat_food:
            public.eat_food(hwnd, x, y, "zhuogui")

        # 切换挂机技能
        if skill_order is not None:
            public.change_skill(hwnd, x, y, skill_order)
        else:
            time.sleep(4.0)

        wait_num = 0
        num = 0
        while True:
            time.sleep(random.uniform(settings.inverval_min * 5, settings.inverval_max * 5))
            num += 1
            # 是否在移动中?
            status = public.get_status(hwnd, x, y, npc_jiaohu=False)
            if status == "standing":
                wait_num += 1
            else:
                wait_num = 0

            if wait_num >= 15:
                print("挂机时间过长，退出")
                return

            if num >= 60:
                # 点下任务栏，避免锁屏
                pos = (2863 - 1927, 303 - 193)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                num = 0