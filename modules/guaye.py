import random
import time
import cv2
import numpy as np

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points
from . import baoshi


def guaye(hwnd, x, y, is_leader, skill_order=None):
    if is_leader:
        duiwu_yincang_img = cv2.cvtColor(cv2.imread("src/duiwu_yincang.png"), cv2.COLOR_BGR2GRAY)

        src_img = window_capture(hwnd, x, y)

        # 若锁屏，则解锁
        public.jiesuo(hwnd, x, y, src_img)

        # 切换挂机技能
        if skill_order is not None:
            public.change_skill(hwnd, x, y, skill_order)
        else:
            time.sleep(2.0)

        # 隐藏任务列表
        points = get_match_points(src_img, duiwu_yincang_img)
        if points:
            pos = points[0]
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.6, 0.8))

        # 开始巡逻
        result = public.goto_yewai(hwnd, x, y, qumo=False)
        if not result:
            print("前往野外失败,退出")
            return

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

            if wait_num >= 2:
                # 开始巡逻
                result = public.xunluo(hwnd, x, y)
                if not result:
                    print("巡逻失败,退出")
                    return

            if num >= 120:
                baoshi.baoshi(hwnd, x, y)
                num = 0
    else:
        # 若锁屏，则解锁
        public.jiesuo(hwnd, x, y)

        # 切换挂机技能
        if skill_order is not None:
            public.change_skill(hwnd, x, y, skill_order)

        wait_num = 0
        num = 0
        while True:
            time.sleep(random.uniform(settings.inverval_min * 10, settings.inverval_max * 10))
            num += 1

            src_img = window_capture(hwnd, x, y)

            public.jiesuo(hwnd, x, y, src_img)

            # 是否在移动中?
            status = public.get_status(hwnd, x, y, src_img, npc_jiaohu=False)
            if status == "standing":
                wait_num += 1
            else:
                wait_num = 0

            if wait_num >= 3:
                print("挂机时间过长，退出")
                return

            if num >= 60:
                baoshi.baoshi(hwnd, x, y)
                num = 0





