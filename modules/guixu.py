import random
import time
import cv2
import numpy as np

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points


def guixu(hwnd, x, y, is_leader):
    lower = np.array([29, 29, 141], dtype="uint8")
    upper = np.array([90, 98, 240], dtype="uint8")

    duiwu_yincang_img = cv2.cvtColor(cv2.imread("src/duiwu_yincang.png"), cv2.COLOR_BGR2GRAY)
    duihua_any_img = cv2.cvtColor(cv2.imread("src/duihua_any.png"), cv2.COLOR_BGR2GRAY)
    button_close_img = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.COLOR_BGR2GRAY)
    duidie_close_img = cv2.cvtColor(cv2.imread("src/duidie_close.png"), cv2.COLOR_BGR2GRAY)

    #guixu_pipeiting_img = cv2.cvtColor(cv2.imread("src/guixu_pipeiting.png"), cv2.COLOR_BGR2GRAY)
    icon_wenda_img = cv2.cvtColor(cv2.imread("src/guixu_pipeiting.png"), cv2.COLOR_BGR2GRAY)
    duiwu_zhankai_img = cv2.cvtColor(cv2.imread("src/duiwu_zhankai.png"), cv2.COLOR_BGR2GRAY)
    guidui_img = cv2.cvtColor(cv2.imread("src/guidui.png"), cv2.COLOR_BGR2GRAY)
    button_queren_img = cv2.cvtColor(cv2.imread("src/button_queren.png"), cv2.COLOR_BGR2GRAY)
    guixu_close_img = cv2.cvtColor(cv2.imread("src/guixu_close.png"), cv2.COLOR_BGR2GRAY)
    button_querenxuanze_img = cv2.cvtColor(cv2.imread("src/button_querenxuanze.png"), cv2.COLOR_BGR2GRAY)

    guixu_jineng_img_color = cv2.cvtColor(cv2.imread("src/guixu_jineng.png"), cv2.IMREAD_COLOR)
    lower = np.array([24, 160, 180], dtype="uint8")
    upper = np.array([67, 230, 255], dtype="uint8")
    mask = cv2.inRange(guixu_jineng_img_color, lower, upper)
    guixu_jineng_img_color = cv2.bitwise_and(guixu_jineng_img_color, guixu_jineng_img_color, mask=mask)
    guixu_jineng_img = cv2.cvtColor(guixu_jineng_img_color, cv2.COLOR_BGR2GRAY)

    guixu_zhuangbei_img_color = cv2.cvtColor(cv2.imread("src/guixu_zhuangbei.png"), cv2.IMREAD_COLOR)
    lower = np.array([24, 160, 180], dtype="uint8")
    upper = np.array([67, 230, 255], dtype="uint8")
    mask = cv2.inRange(guixu_zhuangbei_img_color, lower, upper)
    guixu_zhuangbei_img_color = cv2.bitwise_and(guixu_zhuangbei_img_color, guixu_zhuangbei_img_color, mask=mask)
    guixu_zhuangbei_img = cv2.cvtColor(guixu_zhuangbei_img_color, cv2.COLOR_BGR2GRAY)

    guixu_chongwu_img_color = cv2.cvtColor(cv2.imread("src/guixu_chongwu.png"), cv2.IMREAD_COLOR)
    lower = np.array([24, 160, 180], dtype="uint8")
    upper = np.array([67, 230, 255], dtype="uint8")
    mask = cv2.inRange(guixu_chongwu_img_color, lower, upper)
    guixu_chongwu_img_color = cv2.bitwise_and(guixu_chongwu_img_color, guixu_chongwu_img_color, mask=mask)
    guixu_chongwu_img = cv2.cvtColor(guixu_chongwu_img_color, cv2.COLOR_BGR2GRAY)

    # 若锁屏，则解锁
    public.jiesuo(hwnd, x, y)

    while True:
        time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

        src_img = window_capture(hwnd, x, y)

        status = public.get_status(hwnd, x, y, src_img, with_standing=False, npc_jiaohu=False)
        if status == "in_battle":
            continue

        points = get_match_points(src_img, icon_wenda_img, threshold=0.92)
        if points:
            if is_leader:
                # 打开地图
                pos = (1997 - 1927, 178 - 156)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(1.0, 1.2))
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, button_close_img)
                if not points:
                    # 未点开地图?,重新点开，重新截图
                    print("场景切换？未能点开地图，重新点开")
                    time.sleep(random.uniform(4.8, 5.2))
                    pos = (1997 - 1927, 178 - 156)
                    randint_x = random.randint(0, 5)
                    randint_y = random.randint(0, 10)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(1.0, 1.2))
                # 点乱斗之王
                pos = (2399 - 1927, 435 - 156)
                randint_x = random.randint(0, 2)
                randint_y = random.randint(0, 2)
                window_click(hwnd, pos, randint_x, randint_y)
                # 等队员归队
                time.sleep(random.uniform(4.8, 5.2))

                while True:
                    time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
                    src_img = window_capture(hwnd, x, y)
                    # 点确认
                    points = get_match_points(src_img, button_queren_img)
                    if points:
                        pos = points[0]
                        randint_x = random.randint(10, 80)
                        randint_y = random.randint(5, 20)
                        window_click(hwnd, pos, randint_x, randint_y)
                        break

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

                    points = get_match_points(src_img, button_close_img)
                    if points:
                        # 误点到战备，或者NPC对话，关闭
                        pos = points[0]
                        randint_x = random.randint(0, 5)
                        randint_y = random.randint(0, 5)
                        window_click(hwnd, pos, randint_x, randint_y)
                        time.sleep(random.uniform(1.0, 1.2))
                        # 点乱斗之王
                        pos = (2399 - 1927, 435 - 156)
                        randint_x = random.randint(0, 2)
                        randint_y = random.randint(0, 2)
                        window_click(hwnd, pos, randint_x, randint_y)
                        time.sleep(random.uniform(1.0, 1.2))
                        continue
            else:
                while True:
                    time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
                    src_img = window_capture(hwnd, x, y)

                    # 点确认
                    points = get_match_points(src_img, button_queren_img)
                    if points:
                        pos = points[0]
                        randint_x = random.randint(10, 80)
                        randint_y = random.randint(5, 20)
                        window_click(hwnd, pos, randint_x, randint_y)
                        break

                    # 展开队伍列表
                    points = get_match_points(src_img, duiwu_zhankai_img)
                    if points:
                        pos = points[0]
                        randint_x = random.randint(0, 5)
                        randint_y = random.randint(0, 5)
                        window_click(hwnd, pos, randint_x, randint_y)
                        time.sleep(random.uniform(0.6, 0.8))

                    # 开关队伍界面
                    pos = (2792 - 1927, 302 - 193)
                    randint_x = random.randint(0, 50)
                    randint_y = random.randint(0, 20)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(0.8, 1.0))

                    src_img = window_capture(hwnd, x, y)
                    points = get_match_points(src_img, guidui_img)
                    if points:
                        pos = points[0]
                        randint_x = random.randint(5, 70)
                        randint_y = random.randint(5, 20)
                        window_click(hwnd, pos, randint_x, randint_y)
                        time.sleep(random.uniform(0.6, 0.8))

        points = get_match_points(src_img, button_querenxuanze_img)
        if points:
            time.sleep(15)
            # 进入战斗循环
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

                # 点确认
                points = get_match_points(src_img, button_queren_img)
                if points:
                    pos = points[0]
                    randint_x = random.randint(10, 80)
                    randint_y = random.randint(5, 20)
                    window_click(hwnd, pos, randint_x, randint_y)
                    continue

                points = get_match_points(src_img, guixu_close_img)
                if points:
                    # 退出归墟乱斗
                    pos = points[0]
                    randint_x = random.randint(5, 10)
                    randint_y = random.randint(5, 10)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(4.8, 5.2))
                    break

                src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
                # 注意点怪的时候，Y最多向上移25-30个像素，不然会点开人物界面

                left = 151
                top = 115
                w = 740
                h = 280
                opponent_img = src_img[top:top + h, left:left + w]

                # cv2.namedWindow("Image")
                # cv2.imshow("Image", opponent_img)
                # cv2.waitKey(0)
                # sys.exit(1)

                lower = np.array([24, 160, 180], dtype="uint8")
                upper = np.array([67, 230, 255], dtype="uint8")
                mask = cv2.inRange(opponent_img, lower, upper)
                opponent_img = cv2.bitwise_and(opponent_img, opponent_img, mask=mask)
                opponent_img = cv2.cvtColor(opponent_img, cv2.COLOR_BGR2GRAY)

                points = get_match_points(opponent_img, guixu_jineng_img, threshold=0.6)
                if not points:
                    points = get_match_points(opponent_img, guixu_zhuangbei_img, threshold=0.6)
                    if not points:
                        points = get_match_points(opponent_img, guixu_chongwu_img, threshold=0.6)

                if points:
                    px, py = points[0]
                    # px, py是相对于opponent_img的坐标，所以还要加上left和top
                    pos = (px + 151 + 10, py + 115 - 25)
                    randint_x = random.randint(0, 5)
                    randint_y = random.randint(0, 5)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(0.5, 0.6))
                    src_img = window_capture(hwnd, x, y)
                    # 目标堆叠，选中第一个目标
                    points = get_match_points(src_img, duidie_close_img)
                    if points:
                        pos = points[0]
                        randint_x = random.randint(-100, -80)
                        randint_y = random.randint(0, 15)
                        window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(3.8, 4.2))
                    # 选第一个物品
                    pos = (2269 - 1927, 511 - 156)
                    randint_x = random.randint(0, 5)
                    randint_y = random.randint(0, 5)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(0.5, 0.6))
                    # 点确定
                    pos = (2218 - 1927, 516 - 156)
                    randint_x = random.randint(0, 5)
                    randint_y = random.randint(0, 5)
                    window_click(hwnd, pos, randint_x, randint_y)
                else:
                    status = public.get_status(hwnd, x, y, with_standing=True, npc_jiaohu=False)
                    if status == "standing":
                        status = public.get_status(hwnd, x, y, with_standing=True, npc_jiaohu=False)
                        if status == "standing":
                            pos_list = [
                                (2142 - 1927, 305 - 156),
                                (2685 - 1927, 591 - 156),
                                (2682 - 1927, 283 - 156),
                                (2099 - 1927, 601 - 156),
                            ]
                            r = random.randint(0, len(pos_list) - 1)
                            pos_target = pos_list[r]
                            # 点开大地图
                            pos = (1949 - 1927, 232 - 156)
                            randint_x = random.randint(0, 5)
                            randint_y = random.randint(0, 5)
                            window_click(hwnd, pos, randint_x, randint_y)
                            time.sleep(random.uniform(0.5, 0.6))
                            randint_x = random.randint(0, 1)
                            randint_y = random.randint(0, 1)
                            window_click(hwnd, pos_target, randint_x, randint_y)
                            time.sleep(random.uniform(0.5, 0.6))
                            # 关闭大地图
                            pos = (1949 - 1927, 232 - 156)
                            randint_x = random.randint(0, 5)
                            randint_y = random.randint(0, 5)
                            window_click(hwnd, pos, randint_x, randint_y)
