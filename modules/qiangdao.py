import random
import time
import cv2
import numpy as np

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points


def bangpaixunluo(hwnd, x, y, target_pos_num):
    if target_pos_num == 0:
        target_pos = (2283 - 1927, 321 - 156)
    elif target_pos_num == 1:
        target_pos = (2171 - 1927, 443 - 156)
    elif target_pos_num == 2:
        target_pos = (2264 - 1927, 591 - 156)
    elif target_pos_num == 3:
        target_pos = (2486 - 1927, 561 - 156)
    elif target_pos_num == 4:
        target_pos = (2601 - 1927, 599 - 156)
    elif target_pos_num == 5:
        target_pos = (2645 - 1927, 461 - 156)
    elif target_pos_num == 6:
        target_pos = (2484 - 1927, 275 - 156)

    # 点开大地图
    pos = (1997 - 1927, 178 - 156)
    randint_x = random.randint(0, 5)
    randint_y = random.randint(0, 10)
    window_click(hwnd, pos, randint_x, randint_y)
    time.sleep(random.uniform(0.2, 0.3))

    # 点目的地
    randint_x = random.randint(0, 5)
    randint_y = random.randint(0, 5)
    window_click(hwnd, target_pos, randint_x, randint_y)
    time.sleep(random.uniform(0.2, 0.3))

    # 关闭大地图
    pos = (1997 - 1927, 178 - 156)
    randint_x = random.randint(0, 5)
    randint_y = random.randint(0, 10)
    window_click(hwnd, pos, randint_x, randint_y)


def qiangdao(hwnd, x, y, is_leader, skill_order=None):
    # 若锁屏，则解锁
    public.jiesuo(hwnd, x, y)

    # 切换挂机技能
    if skill_order is not None:
        public.change_skill(hwnd, x, y, skill_order)
    else:
        if is_leader:
            time.sleep(2.0)

    while True:
        minute = time.localtime().tm_min
        if minute >= 20:
            print("还未开始，等待10秒。")
            time.sleep(10)
            continue
        else:
            break

    if is_leader:
        qiangdao_img_color = cv2.cvtColor(cv2.imread("src/qiangdao.png"), cv2.IMREAD_COLOR)
        lower = np.array([24, 160, 180], dtype="uint8")
        upper = np.array([67, 230, 255], dtype="uint8")
        mask = cv2.inRange(qiangdao_img_color, lower, upper)
        qiangdao_img_color = cv2.bitwise_and(qiangdao_img_color, qiangdao_img_color, mask=mask)
        qiangdao_img = cv2.cvtColor(qiangdao_img_color, cv2.COLOR_BGR2GRAY)
        #duidie_close_img = cv2.cvtColor(cv2.imread("src/duidie_close.png"), cv2.COLOR_BGR2GRAY)

        #duihua_qiangdao_img = cv2.cvtColor(cv2.imread("src/duihua_qiangdao.png"), cv2.COLOR_BGR2GRAY)
        qiangdao_choice_img = cv2.cvtColor(cv2.imread("src/qiangdao_choice.png"), cv2.COLOR_BGR2GRAY)
        duihua_any_img = cv2.cvtColor(cv2.imread("src/duihua_any.png"), cv2.COLOR_BGR2GRAY)
        duiwu_yincang_img = cv2.cvtColor(cv2.imread("src/duiwu_yincang.png"), cv2.COLOR_BGR2GRAY)
        button_close_img = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.COLOR_BGR2GRAY)

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

        # 回到帮派
        result = public.return_bangpai(hwnd, x, y)
        if not result:
            print("回到帮派失败，退出。")
            return

        target_pos_num = 0
        move_num = 0
        waiting_num = 0
        while True:
            time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

            src_img = window_capture(hwnd, x, y)

            status = public.get_status(hwnd, x, y, src_img, with_standing=False, npc_jiaohu=False)
            if status == "in_battle":
                continue

            # 隐藏任务列表
            points = get_match_points(src_img, duiwu_yincang_img)
            if points:
                pos = points[0]
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                continue

            # 说好不打脸的，关闭对话
            points = get_match_points(src_img, button_close_img)
            if points:
                pos = (2856 - 1927, 233 - 193)
                randint_x = random.randint(0, 10)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                continue

            src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
            # 注意点怪的时候，Y最多向上移25-30个像素，不然会点开人物界面
            left = 151
            top = 115
            w = 740
            h = 280
            opponent_img = src_img[top:top + h, left:left + w]

            #cv2.namedWindow("Image")
            #cv2.imshow("Image", opponent_img)
            #cv2.waitKey(0)
            #sys.exit(1)

            lower = np.array([24, 160, 180], dtype="uint8")
            upper = np.array([67, 230, 255], dtype="uint8")
            mask = cv2.inRange(opponent_img, lower, upper)
            opponent_img = cv2.bitwise_and(opponent_img, opponent_img, mask=mask)
            opponent_img = cv2.cvtColor(opponent_img,cv2.COLOR_BGR2GRAY)

            points = get_match_points(opponent_img, qiangdao_img, threshold=0.6)
            if points:
                # 重置计数
                move_num = 0
                waiting_num = 0
                px, py = points[0]
                # px, py是相对于opponent_img的坐标，所以还要加上left和top
                pos = (px + 151 - 15, py + 115 - 25)
                randint_x = random.randint(0, 2)
                randint_y = random.randint(0, 2)
                window_click(hwnd, pos, randint_x, randint_y)

                # 最多等待2.5秒
                for i in range(10):
                    time.sleep(random.uniform(0.2, 0.3))
                    src_img = window_capture(hwnd, x, y)
                    points = get_match_points(src_img, qiangdao_choice_img, threshold=0.95)
                    if points:
                        # 怪站一起了，需要选择
                        pos = points[0]
                        randint_x = random.randint(5, 90)
                        randint_y = random.randint(5, 20)
                        window_click(hwnd, pos, randint_x, randint_y)
                        continue
                    # 未知对话，选第一个
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
                        continue

                for i in range(4):
                    time.sleep(random.uniform(0.2, 0.3))
                    src_img = window_capture(hwnd, x, y)
                    points = get_match_points(src_img, button_close_img)
                    if points:
                        pos = (2856 - 1927, 233 - 193)
                        randint_x = random.randint(0, 10)
                        randint_y = random.randint(0, 10)
                        window_click(hwnd, pos, randint_x, randint_y)
                        print("进入战斗失败")
                        break
            else:
                waiting_num += 1
                if target_pos_num == 4:
                    mask = 2
                else:
                    mask = 3
                if waiting_num >= mask:
                    move_num += 1
                    if move_num >= 10:
                        print("移动一圈后，仍未发现强盗，回长安，退出")
                        # 打开世界地图
                        pos = (1965 - 1927, 195 - 156)
                        randint_x = random.randint(0, 5)
                        randint_y = random.randint(0, 5)
                        window_click(hwnd, pos, randint_x, randint_y)
                        time.sleep(random.uniform(0.8, 1.2))
                        # 去长安
                        pos = (2439 - 1927, 527 - 156)
                        randint_x = random.randint(0, 10)
                        randint_y = random.randint(0, 10)
                        window_click(hwnd, pos, randint_x, randint_y)
                        return
                    bangpaixunluo(hwnd, x, y, target_pos_num)
                    waiting_num = 0
                    target_pos_num += 1
                    if target_pos_num > 6:
                        target_pos_num = 0
    else:
        # 若锁屏，则解锁
        public.jiesuo(hwnd, x, y)

        waiting_num = 0
        while True:
            if waiting_num >= 40:
                print("开启后120秒未进战斗，退出")
                return

            time.sleep(random.uniform(settings.inverval_min * 3, settings.inverval_max * 3))
            src_img = window_capture(hwnd, x, y)
            status = public.get_status(hwnd, x, y, src_img, with_standing=False, npc_jiaohu=False)
            if status == "in_battle":
                # 开启自动后，退出
                return
            else:
                waiting_num += 1

