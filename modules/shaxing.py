import random
import time
import cv2
import numpy as np

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points


def shaxing(hwnd, x, y, target):

    lower = np.array([29, 29, 141], dtype="uint8")
    upper = np.array([90, 98, 240], dtype="uint8")

    target28_img_color = cv2.cvtColor(cv2.imread("src/target28.png"), cv2.IMREAD_COLOR)
    mask = cv2.inRange(target28_img_color, lower, upper)
    target28_img_color = cv2.bitwise_and(target28_img_color, target28_img_color, mask=mask)
    target28_img = cv2.cvtColor(target28_img_color, cv2.COLOR_BGR2GRAY)

    duihua_tiaozhan_img = cv2.cvtColor(cv2.imread("src/duihua_tiaozhan.png"), cv2.COLOR_BGR2GRAY)
    duihua_xianlaihoudao_img = cv2.cvtColor(cv2.imread("src/duihua_xianlaihoudao.png"), cv2.COLOR_BGR2GRAY)
    zidong_img = cv2.cvtColor(cv2.imread("src/zidong.png"), cv2.COLOR_BGR2GRAY)

    targetyaowang_img_color = cv2.cvtColor(cv2.imread("src/targetyaowang.png"), cv2.IMREAD_COLOR)
    mask = cv2.inRange(targetyaowang_img_color, lower, upper)
    targetyaowang_img_color = cv2.bitwise_and(targetyaowang_img_color, targetyaowang_img_color, mask=mask)
    targetyaowang_img = cv2.cvtColor(targetyaowang_img_color, cv2.COLOR_BGR2GRAY)

    targetshenqi_img_color = cv2.cvtColor(cv2.imread("src/targetshenqi.png"), cv2.IMREAD_COLOR)
    mask = cv2.inRange(targetshenqi_img_color, lower, upper)
    targetshenqi_img_color = cv2.bitwise_and(targetshenqi_img_color, targetshenqi_img_color, mask=mask)
    targetshenqi_img = cv2.cvtColor(targetshenqi_img_color, cv2.COLOR_BGR2GRAY)

    duihua_jinruzhandou_img = cv2.cvtColor(cv2.imread("src/duihua_jinruzhandou.png"), cv2.COLOR_BGR2GRAY)
    duihua_qingwudarao_img = cv2.cvtColor(cv2.imread("src/duihua_qingwudarao.png"), cv2.COLOR_BGR2GRAY)

    target36_img_color = cv2.cvtColor(cv2.imread("src/target36.png"), cv2.IMREAD_COLOR)
    mask = cv2.inRange(target36_img_color, lower, upper)
    target36_img_color = cv2.bitwise_and(target36_img_color, target36_img_color, mask=mask)
    target36_img = cv2.cvtColor(target36_img_color, cv2.COLOR_BGR2GRAY)

    duihua_buhuidecheng_img = cv2.cvtColor(cv2.imread("src/duihua_buhuidecheng.png"), cv2.COLOR_BGR2GRAY)
    duihua_xianlaihoudao_36_img = cv2.cvtColor(cv2.imread("src/duihua_xianlaihoudao_36.png"), cv2.COLOR_BGR2GRAY)

    duihua_guanzhan_img = cv2.cvtColor(cv2.imread("src/duihua_guanzhan.png"), cv2.COLOR_BGR2GRAY)
    duihua_woyaoguanzhan_img = cv2.cvtColor(cv2.imread("src/duihua_woyaoguanzhan.png"), cv2.COLOR_BGR2GRAY)
    duidie_close_img = cv2.cvtColor(cv2.imread("src/duidie_close.png"), cv2.COLOR_BGR2GRAY)

    if target == "":
        print("开始抢灭，请注意人物不要移动")
        # 不点选目标，抢灭
        target_pos = None
        target = ""
        for i in range(1, 10):
            src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
            mask = cv2.inRange(src_img, lower, upper)
            src_img = cv2.bitwise_and(src_img, src_img, mask=mask)
            src_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)

            left = 480 - 48 * i
            top = 270 - 27 * i
            w = 48 * 2 * i
            h = 27 * 2 * i
            opponent_img = src_img[top:top + h, left:left + w]

            points = get_match_points(opponent_img, targetyaowang_img, threshold=0.5)
            if not points:
                points = get_match_points(opponent_img, targetshenqi_img, threshold=0.5)
            if points:
                px, py = points[0]
                target_pos = (px + 35 + left, py - 30 + top)
                target = "妖王神器"
                break
            points = get_match_points(opponent_img, target36_img, threshold=0.5)
            if points:
                px, py = points[0]
                target_pos = (px + 40 + left, py - 30 + top)
                target = "36天罡"
                break
            points = get_match_points(opponent_img, target28_img, threshold=0.5)
            if points:
                px, py = points[0]
                target_pos = (px + 40 + left, py - 30 + top)
                target = "28星宿"
                break
        print(target_pos)
        print(target)
        if target_pos:
            window_click(hwnd, target_pos, 0, 0)
            time.sleep(random.uniform(1.0, 1.2))

            if target == "28星宿":
                duihua_start_img = duihua_tiaozhan_img
                duihua_wait_img = duihua_woyaoguanzhan_img
            elif target == "妖王神器":
                duihua_start_img = duihua_jinruzhandou_img
                duihua_wait_img = duihua_guanzhan_img
            elif target == "36天罡":
                duihua_start_img = duihua_buhuidecheng_img
                duihua_wait_img = duihua_woyaoguanzhan_img
            while True:
                time.sleep(0.2)
                src_img = window_capture(hwnd, x, y)
                left = 595
                top = 270
                w = 345
                h = 250
                opponent_img = src_img[top:top + h, left:left + w]
                points = get_match_points(opponent_img, duihua_start_img)
                if points:
                    px, py = points[0]
                    pos = (px + 50 + left, py + 20 + top)
                    randint_x = random.randint(0, 80)
                    randint_y = random.randint(0, 5)

                    points = get_match_points(opponent_img, duihua_wait_img)
                    if points:
                        # 还能观点，无法进入战斗,继续点怪刷新
                        window_click(hwnd, target_pos, 0, 0)
                        continue
                    else:
                        # 不存在观战按钮，进入战斗
                        window_click(hwnd, pos, randint_x, randint_y)
                        return
    else:
        while True:
            time.sleep(0.2)

            src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
            mask = cv2.inRange(src_img, lower, upper)
            src_img = cv2.bitwise_and(src_img, src_img, mask=mask)
            src_img = cv2.cvtColor(src_img,cv2.COLOR_BGR2GRAY)

            #cv2.namedWindow("Image")
            #cv2.imshow("Image", targetyaowang_img)
            #cv2.waitKey(0)
            #sys.exit(1)

            if target == "28星宿":
                points = get_match_points(src_img, target28_img, threshold=0.6)
                if points:
                    px, py = points[0]
                    pos = (px + 35, py - 35)
                    randint_x = random.randint(0, 5)
                    randint_y = random.randint(0, 5)
                    window_click(hwnd, pos, randint_x, randint_y)

                    # 这里死循环，除非手动关闭进程,或进入战斗
                    is_first = True
                    while True:
                        time.sleep(0.1)
                        src_img = window_capture(hwnd, x, y)
                        points = get_match_points(src_img, duihua_tiaozhan_img)
                        if points:
                            # 开打
                            px, py = points[0]
                            pos = (px + 50, py + 20)
                            randint_x = random.randint(0, 80)
                            randint_y = random.randint(0, 5)
                            window_click(hwnd, pos, randint_x, randint_y)
                            continue
                        if is_first:
                            # 目标堆叠，选中第一个目标
                            points = get_match_points(src_img, duidie_close_img)
                            if points:
                                pos = points[0]
                                randint_x = random.randint(-100, -80)
                                randint_y = random.randint(0, 15)
                                window_click(hwnd, pos, randint_x, randint_y)
                                continue
                        points = get_match_points(src_img, duihua_xianlaihoudao_img)
                        if points:
                            is_first = False
                            # 未抢到，关闭NPC对话
                            pos = (2856 - 1927, 233 - 193)
                            randint_x = random.randint(0, 10)
                            randint_y = random.randint(0, 10)
                            window_click(hwnd, pos, randint_x, randint_y)
                            print("未能成功进入战斗")
                            continue
                        points = get_match_points(src_img, zidong_img)
                        if points:
                            print("已成功进入战斗，退出.")
                            return
            elif target == "妖王神器":
                points = get_match_points(src_img, targetyaowang_img, threshold=0.6)
                if not points:
                    points = get_match_points(src_img, targetshenqi_img, threshold=0.6)
                if points:
                    px, py = points[0]
                    pos = (px + 30, py - 35)
                    randint_x = random.randint(0, 5)
                    randint_y = random.randint(0, 5)
                    window_click(hwnd, pos, randint_x, randint_y)

                    # 这里死循环，除非手动关闭进程,或进入战斗
                    is_first = True
                    while True:
                        time.sleep(0.1)
                        src_img = window_capture(hwnd, x, y)
                        points = get_match_points(src_img, duihua_jinruzhandou_img)
                        if points:
                            # 开打
                            px, py = points[0]
                            pos = (px + 50, py + 20)
                            randint_x = random.randint(0, 80)
                            randint_y = random.randint(0, 5)
                            window_click(hwnd, pos, randint_x, randint_y)
                            continue
                        if is_first:
                            # 目标堆叠，选中第一个目标
                            points = get_match_points(src_img, duidie_close_img)
                            if points:
                                pos = points[0]
                                randint_x = random.randint(-100, -80)
                                randint_y = random.randint(0, 15)
                                window_click(hwnd, pos, randint_x, randint_y)
                                continue
                        points = get_match_points(src_img, duihua_qingwudarao_img)
                        if points:
                            is_first = False
                            # 未抢到，关闭NPC对话
                            pos = (2856 - 1927, 233 - 193)
                            randint_x = random.randint(0, 10)
                            randint_y = random.randint(0, 10)
                            window_click(hwnd, pos, randint_x, randint_y)
                            print("未能成功进入战斗")
                            continue
                        points = get_match_points(src_img, zidong_img)
                        if points:
                            print("已成功进入战斗，退出.")
                            return
            elif target == "36天罡":
                points = get_match_points(src_img, target36_img, threshold=0.6)
                if points:
                    px, py = points[0]
                    pos = (px + 35, py - 35)
                    randint_x = random.randint(0, 5)
                    randint_y = random.randint(0, 5)
                    window_click(hwnd, pos, randint_x, randint_y)

                    # 这里死循环，除非手动关闭进程,或进入战斗
                    is_first = True
                    while True:
                        time.sleep(0.1)
                        src_img = window_capture(hwnd, x, y)
                        points = get_match_points(src_img, duihua_buhuidecheng_img)
                        if points:
                            # 开打
                            px, py = points[0]
                            pos = (px + 50, py + 20)
                            randint_x = random.randint(0, 80)
                            randint_y = random.randint(0, 5)
                            window_click(hwnd, pos, randint_x, randint_y)
                            continue
                        if is_first:
                            # 目标堆叠，选中第一个目标
                            points = get_match_points(src_img, duidie_close_img)
                            if points:
                                pos = points[0]
                                randint_x = random.randint(-100, -80)
                                randint_y = random.randint(0, 15)
                                window_click(hwnd, pos, randint_x, randint_y)
                                continue
                        points = get_match_points(src_img, duihua_xianlaihoudao_36_img)
                        if points:
                            is_first = False
                            # 未抢到，关闭NPC对话
                            pos = (2856 - 1927, 233 - 193)
                            randint_x = random.randint(0, 10)
                            randint_y = random.randint(0, 10)
                            window_click(hwnd, pos, randint_x, randint_y)
                            print("未能成功进入战斗")
                            continue
                        points = get_match_points(src_img, zidong_img)
                        if points:
                            print("已成功进入战斗，退出.")
                            return
