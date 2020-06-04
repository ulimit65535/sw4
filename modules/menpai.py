import random
import time
import cv2
import numpy as np

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points


def menpai(hwnd, x, y, is_leader, skill_order=None):
    while True:
        hour = time.localtime().tm_hour
        if hour != 21 and hour != 22:
            # 等待10分钟
            print("还未到21点或22点，等待10分钟。")
            time.sleep(600)
            continue
        else:
            break
    if hour == 21:
        while True:
            minute = time.localtime().tm_min
            if minute <= 40:
                print("还未开始，等待10秒。")
                time.sleep(10)
                continue
            else:
                break

    if is_leader:
        menpaichuangguan_img_color = cv2.cvtColor(cv2.imread("src/menpaichuangguan.png"), cv2.IMREAD_COLOR)
        duihua_canjiachuangguan_img = cv2.cvtColor(cv2.imread("src/duihua_canjiachuangguan.png"), cv2.COLOR_BGR2GRAY)
        duihua_songwoguoqu_img = cv2.cvtColor(cv2.imread("src/duihua_songwoguoqu.png"), cv2.COLOR_BGR2GRAY)
        duihua_tiaozhanyixing_img = cv2.cvtColor(cv2.imread("src/duihua_tiaozhanyixing.png"), cv2.COLOR_BGR2GRAY)

        lower = np.array([20, 150, 140], dtype="uint8")
        upper = np.array([80, 240, 255], dtype="uint8")

        renwu_menpaichuangguan_img_color = cv2.cvtColor(cv2.imread("src/renwu_menpaichuangguan.png"), cv2.IMREAD_COLOR)
        mask = cv2.inRange(renwu_menpaichuangguan_img_color, lower, upper)
        renwu_menpaichuangguan_img_color = cv2.bitwise_and(renwu_menpaichuangguan_img_color, renwu_menpaichuangguan_img_color, mask=mask)
        renwu_menpaichuangguan_img = cv2.cvtColor(renwu_menpaichuangguan_img_color, cv2.COLOR_BGR2GRAY)

        #cv2.namedWindow("Image")
        #cv2.imshow("Image", renwu_huoban_img)
        #cv2.waitKey(0)
        #sys.exit(1)

        # 若锁屏，则解锁
        public.jiesuo(hwnd, x, y)

        # 切换挂机技能
        if skill_order is not None:
            public.change_skill(hwnd, x, y, skill_order)
        else:
            time.sleep(2.0)

        num_error = 0
        while True:
            if num_error >= 5:
                print("错误次数过多，退出")
                return

            time.sleep(random.uniform(settings.inverval_min * 3, settings.inverval_max * 3))

            src_img = window_capture(hwnd, x, y)

            # 对话，参加闯关
            points = get_match_points(src_img, duihua_canjiachuangguan_img)
            if points:
                px, py = points[0]
                pos = (px + 50, py + 20)
                randint_x = random.randint(0, 80)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                continue

            # 对话，送我过去
            points = get_match_points(src_img, duihua_songwoguoqu_img)
            if points:
                px, py = points[0]
                pos = (px + 50, py + 20)
                randint_x = random.randint(0, 80)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                continue

            # 对话，挑战一星
            points = get_match_points(src_img, duihua_tiaozhanyixing_img)
            if points:
                px, py = points[0]
                pos = (px + 50, py + 20)
                randint_x = random.randint(0, 80)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                continue

            # 是否在移动中?
            src_img = window_capture(hwnd, x, y)
            status = public.get_status(hwnd, x, y, src_img, npc_jiaohu=False, call_pet=True)

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

            points = get_match_points(opponent_img, renwu_menpaichuangguan_img, threshold=0.7)
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
            points = get_match_points(src_img, menpaichuangguan_img_color, threshold=0.9)
            if not points:
                # 等待字幕消失
                time.sleep(random.uniform(2.8, 3.2))
                src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
                points = get_match_points(src_img, menpaichuangguan_img_color, threshold=0.9)
                if not points:
                    print("门派闯关已完成")
                    public.close_window_richeng(hwnd, x, y)
                    return

            # 点前往参加
            pos = points[0]
            randint_x = random.randint(15, 30)
            randint_y = random.randint(68, 78)
            window_click(hwnd, pos, randint_x, randint_y)
            continue
    else:
        button_close_img = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.COLOR_BGR2GRAY)
        
        # 若锁屏，则解锁
        public.jiesuo(hwnd, x, y)

        # 切换挂机技能
        if skill_order is not None:
            public.change_skill(hwnd, x, y, skill_order)

        wait_num = 0
        num = 0
        while True:
            time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
            num += 1

            src_img = window_capture(hwnd, x, y)

            points = get_match_points(src_img, button_close_img)
            if points:
                # 误点到战备，或者NPC对话，关闭
                pos = points[0]
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                continue

            # 是否在移动中?
            status = public.get_status(hwnd, x, y, npc_jiaohu=False, call_pet=True)
            if status == "standing":
                wait_num += 1
            else:
                wait_num = 0

            if wait_num >= 10:
                print("挂机时间过长，退出")
                return

            if num >= 300:
                # 点下任务栏，避免锁屏
                pos = (2863 - 1927, 303 - 193)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                num = 0
