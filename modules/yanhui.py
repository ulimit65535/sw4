import random
import time
import cv2
import numpy as np

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points


def yanhui(hwnd, x, y, jianlihua=False):
    # 初始化变量，分中午跟晚上
    button_close_img = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.COLOR_BGR2GRAY)
    button_wanchengliaoli_img = cv2.cvtColor(cv2.imread("src/button_wanchengliaoli.png"), cv2.COLOR_BGR2GRAY)
    button_pinchang_img_color = cv2.cvtColor(cv2.imread("src/button_pinchang.png"), cv2.IMREAD_COLOR)
    button_pinchang_gray_img_color = cv2.cvtColor(cv2.imread("src/button_pinchang_gray.png"), cv2.IMREAD_COLOR)
    biaoqing_chaoren_img_color = cv2.cvtColor(cv2.imread("src/biaoqing_chaoren.png"), cv2.IMREAD_COLOR)
    lihua_rest_img = cv2.cvtColor(cv2.imread("src/lihua_rest.png"), cv2.COLOR_BGR2GRAY)
    lihua_end_img = cv2.cvtColor(cv2.imread("src/lihua_end.png"), cv2.COLOR_BGR2GRAY)
    duiwu_yincang_img = cv2.cvtColor(cv2.imread("src/duiwu_yincang.png"), cv2.COLOR_BGR2GRAY)
    zhuozi_choice_img = cv2.cvtColor(cv2.imread("src/zhuozi_choice.png"), cv2.COLOR_BGR2GRAY)
    xinxi_close_img = cv2.cvtColor(cv2.imread("src/xinxi_close.png"), cv2.COLOR_BGR2GRAY)
    yanhui_clock_img = cv2.cvtColor(cv2.imread("src/yanhui_clock.png"), cv2.COLOR_BGR2GRAY)

    if jianlihua:
        lihua_img_color = cv2.cvtColor(cv2.imread("src/lihua.png"), cv2.IMREAD_COLOR)
        lower = np.array([24, 160, 180], dtype="uint8")
        upper = np.array([67, 230, 255], dtype="uint8")
        mask = cv2.inRange(lihua_img_color, lower, upper)
        lihua_img_color = cv2.bitwise_and(lihua_img_color, lihua_img_color, mask=mask)
        lihua_img = cv2.cvtColor(lihua_img_color, cv2.COLOR_BGR2GRAY)

        lihua_choice_img = cv2.cvtColor(cv2.imread("src/lihua_choice.png"), cv2.COLOR_BGR2GRAY)

    while True:
        hour = time.localtime().tm_hour
        minute = time.localtime().tm_min
        if hour == 12:
            if minute <= 20:
                print("还未到20分，等待2-3分钟。")
                time.sleep(random.uniform(120.0, 180.0))
                continue
            yanhuirenwu_img_color = cv2.cvtColor(cv2.imread("src/yanhuirenwu_zhongwu.png"), cv2.IMREAD_COLOR)
            duihua_woyaoquyanhui_img = cv2.cvtColor(cv2.imread("src/duihua_woyaoquyanhui.png"), cv2.COLOR_BGR2GRAY)
            duihua_kaishizhunbeishicai_img = cv2.cvtColor(cv2.imread("src/duihua_kaishizhunbeishicai.png"),
                                                          cv2.COLOR_BGR2GRAY)
            ditu_yanhui_img = cv2.cvtColor(cv2.imread("src/ditu_yanhui_zhongwu.png"), cv2.COLOR_BGR2GRAY)
            # 分别为待机的位置和要点的桌子的坐标
            pos_list = [
                ((2427 - 1927, 435 - 156), (2174 - 1927, 443 - 156)),
                ((2409 - 1927, 416 - 156), (2210 - 1927, 491 - 156)),
                ((2339 - 1927, 388 - 156), (2403 - 1927, 567 - 156)),
                ((2309 - 1927, 396 - 156), (2474 - 1927, 551 - 156)),
                ((2282 - 1927, 436 - 156), (2539 - 1927, 446 - 156)),
            ]
            break
        elif hour == 19:
            if minute <= 20:
                print("还未到20分，等待2-3分钟。")
                time.sleep(random.uniform(120.0, 180.0))
                continue
            yanhuirenwu_img_color = cv2.cvtColor(cv2.imread("src/yanhuirenwu.png"), cv2.IMREAD_COLOR)
            #yanhuirenwu_img_color = cv2.cvtColor(cv2.imread("src/yanhuirenwu_chunjie.png"), cv2.IMREAD_COLOR)
            duihua_woyaoquyanhui_img = cv2.cvtColor(cv2.imread("src/duihua_woyaoquyanhui.png"), cv2.COLOR_BGR2GRAY)
            #duihua_woyaoquyanhui_img = cv2.cvtColor(cv2.imread("src/duihua_woyaoquyanhui_chunjie.png"), cv2.COLOR_BGR2GRAY)
            duihua_kaishizhunbeishicai_img = cv2.cvtColor(cv2.imread("src/duihua_kaishizhunbeishicai.png"), cv2.COLOR_BGR2GRAY)
            ditu_yanhui_img = cv2.cvtColor(cv2.imread("src/ditu_yanhui.png"), cv2.COLOR_BGR2GRAY)
            # 分别为待机的位置和要点的桌子的坐标
            pos_list = [
                ((2491 - 1927, 472 - 156), (2147 - 1927, 395 - 156)),
                ((2465 - 1927, 442 - 156), (2252 - 1927, 504 - 156)),
                ((2424 - 1927, 425 - 156), (2417 - 1927, 577 - 156)),
                ((2384 - 1927, 436 - 156), (2574 - 1927, 540 - 156)),
                ((2374 - 1927, 463 - 156), (2617 - 1927, 427 - 156)),
            ]
            break
        else:
            # 等待30分钟
            print("还未到12点或19点，等待5分钟。")
            time.sleep(300)
            continue

    # 若锁屏，则解锁
    public.jiesuo(hwnd, x, y)

    num_error = 0
    while True:
        if num_error >= 5:
            print("错误次数过多，退出")
            return

        time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

        result = public.open_window_richeng(hwnd, x, y)
        if not result:
            print("未能打开日程窗口")
            num_error += 1
            continue
        else:
            num_error = 0

        src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
        points = get_match_points(src_img, yanhuirenwu_img_color, threshold=0.9)
        if not points:
            # 等待字幕消失
            time.sleep(random.uniform(2.8, 3.2))
            src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
            points = get_match_points(src_img, yanhuirenwu_img_color, threshold=0.9)
            if not points:
                print("错误，宴会未开始，退出。")
                public.close_window_richeng(hwnd, x, y)
                return

        # 点前往参加
        pos = points[0]
        randint_x = random.randint(15, 30)
        randint_y = random.randint(68, 78)
        window_click(hwnd, pos, randint_x, randint_y)

        for i in range(5):
            time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, duihua_woyaoquyanhui_img)
            if points:
                time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
                px, py = points[0]
                pos = (px + 50, py + 20)
                randint_x = random.randint(0, 80)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                for i in range(2):
                    time.sleep(random.uniform(settings.inverval_min * 2, settings.inverval_max * 2))
                    src_img = window_capture(hwnd, x, y)
                    points = get_match_points(src_img, duihua_woyaoquyanhui_img)
                    if points:
                        px, py = points[0]
                        pos = (px + 50, py + 20)
                        randint_x = random.randint(0, 80)
                        randint_y = random.randint(0, 5)
                        window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(2.8, 3.2))
                break
        break

    time.sleep(random.uniform(1.8, 2.2))
    # 关闭未知对话
    points = get_match_points(src_img, button_close_img)
    if points:
        pos = (2856 - 1927, 233 - 193)
        randint_x = random.randint(0, 10)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)

    time.sleep(random.uniform(1.8, 2.2))
    
    # 隐藏任务列表
    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, duiwu_yincang_img)
    if points:
        pos = points[0]
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.6, 0.8))

    # 打开地图
    pos = (1997 - 1927, 178 - 156)
    randint_x = random.randint(0, 5)
    randint_y = random.randint(0, 10)
    window_click(hwnd, pos, randint_x, randint_y)
    time.sleep(random.uniform(1.4, 1.6))
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
        time.sleep(random.uniform(1.4, 1.6))
        src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, ditu_yanhui_img)
    if not points:
        print("进入宴会失败，退出")
        return
    else:
        # 随机取一对坐标
        r = random.randint(0, len(pos_list) - 1)
        pos_wait, pos_target = pos_list[r]
        print("#######################")
        print(hwnd)
        print(pos_wait, pos_target)
        print("#######################")
        # 去待机位置
        randint_x = random.randint(0, 1)
        randint_y = random.randint(0, 1)
        window_click(hwnd, pos_wait, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.0))

        # 关闭地图
        pos = (1997 - 1927, 178 - 156)
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(1.0, 1.2))
        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, button_close_img)
        if points:
            # 地图未能关闭?重新关闭。
            print("场景切换？未能关闭地图，重新关闭。")
            time.sleep(random.uniform(4.8, 5.2))
            pos = (1997 - 1927, 178 - 156)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)

        time.sleep(random.uniform(9.8, 10.2))

        # 点桌子，做菜
        randint_x = random.randint(0, 1)
        randint_y = random.randint(0, 1)
        window_click(hwnd, pos_target, randint_x, randint_y)
        time.sleep(random.uniform(1.0, 1.2))
        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, zhuozi_choice_img, threshold=0.98)
        if points:
            # 在一起了，需要选择
            pos = points[0]
            randint_x = random.randint(5, 90)
            randint_y = random.randint(5, 20)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(1.0, 1.2))

        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, duihua_kaishizhunbeishicai_img)
        if points:
            px, py = points[0]
            pos = (px + 50, py + 20)
            randint_x = random.randint(0, 80)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            for i in range(2):
                time.sleep(random.uniform(settings.inverval_min * 2, settings.inverval_max * 2))
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, duihua_kaishizhunbeishicai_img)
                if points:
                    px, py = points[0]
                    pos = (px + 50, py + 20)
                    randint_x = random.randint(0, 80)
                    randint_y = random.randint(0, 5)
                    window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(2.8, 3.2))

            # 等待完成料理
            while True:
                time.sleep(random.uniform(settings.inverval_min * 3, settings.inverval_max * 3))
                print("等待完成料理...")
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, button_wanchengliaoli_img)
                if points:
                    pos = points[0]
                    randint_x = random.randint(25, 65)
                    randint_y = random.randint(5, 15)
                    window_click(hwnd, pos, randint_x, randint_y)
                    for i in range(2):
                        time.sleep(random.uniform(settings.inverval_min * 2, settings.inverval_max * 2))
                        src_img = window_capture(hwnd, x, y)
                        points = get_match_points(src_img, button_wanchengliaoli_img)
                        if points:
                            pos = points[0]
                            randint_x = random.randint(25, 65)
                            randint_y = random.randint(5, 15)
                            window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(1.6, 1.8))
                    break
            # 退出做菜循环,避免未知移动，回到原位置
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

            # 去待机位置
            randint_x = random.randint(0, 1)
            randint_y = random.randint(0, 1)
            window_click(hwnd, pos_wait, randint_x, randint_y)
            time.sleep(random.uniform(0.5, 0.6))

            # 关闭地图
            pos = (1997 - 1927, 178 - 156)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(1.0, 1.2))
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, button_close_img)
            if points:
                # 地图未能关闭?重新关闭。
                print("场景切换？未能关闭地图，重新关闭。")
                time.sleep(random.uniform(4.8, 5.2))
                pos = (1997 - 1927, 178 - 156)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(1.0, 1.2))

            time.sleep(random.uniform(1.8, 2.2))

            print("完成料理.")
        else:
            # 未知对话，关闭对话
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, button_close_img)
            if points:
                pos = points[0]
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.4, 0.6))
            print("未知，做菜失败.")



    waiting_num = 0
    already_huanqing = False
    index = 0
    is_lihua_end = False
    while True:
        # 循环次数
        index += 1
        # 吃菜循环
        time.sleep(random.uniform(settings.inverval_min * 2, settings.inverval_max * 2))
        if waiting_num >= 30:
            # 5分钟点桌子都没反映，点开地图看下
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
                src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, ditu_yanhui_img)
            if not points:
                pos = (1997 - 1927, 178 - 156)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                print("帮派宴会已结束，退出")
                return
            else:
                pos = (1997 - 1927, 178 - 156)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                waiting_num = 0
                continue

        src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
        # 欢庆神武4
        left = 0
        top = 0
        w = 970
        h = 400
        opponent_img = src_img[top:top + h, left:left + w]
        points = get_match_points(opponent_img, biaoqing_chaoren_img_color, threshold=0.8)
        if points:
            if not already_huanqing:
                px, py = points[0]
                pos = (px + 87, py)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                already_huanqing = True
                continue
        else:
            already_huanqing = False

        if jianlihua and not is_lihua_end:
            is_move = False
            while True:
                time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

                if is_lihua_end:
                    break

                src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
                left = 151
                top = 115
                w = 740
                h = 280
                opponent_img = src_img[top:top + h, left:left + w]

                lower = np.array([24, 160, 180], dtype="uint8")
                upper = np.array([67, 230, 255], dtype="uint8")
                mask = cv2.inRange(opponent_img, lower, upper)
                opponent_img = cv2.bitwise_and(opponent_img, opponent_img, mask=mask)
                opponent_img = cv2.cvtColor(opponent_img, cv2.COLOR_BGR2GRAY)

                points = get_match_points(opponent_img, lihua_img, threshold=0.6)
                if points:
                    is_move = True
                    px, py = points[0]
                    # px, py是相对于opponent_img的坐标，所以还要加上left和top
                    pos = (px + 151 + 10, py + 115 - 25)
                    randint_x = random.randint(0, 5)
                    randint_y = random.randint(0, 5)
                    window_click(hwnd, pos, randint_x, randint_y)

                    # 最多等待5秒
                    for i in range(20):
                        time.sleep(random.uniform(0.2, 0.3))
                        src_img = window_capture(hwnd, x, y)
                        points = get_match_points(src_img, lihua_choice_img, threshold=0.98)
                        if points:
                            # 在一起了，需要选择
                            pos = points[0]
                            randint_x = random.randint(5, 90)
                            randint_y = random.randint(5, 20)
                            window_click(hwnd, pos, randint_x, randint_y)
                            continue
                        points = get_match_points(src_img, lihua_end_img, threshold=0.8)
                        if points:
                            is_lihua_end = True
                            print("礼花拾取完毕。")
                            break
                        points = get_match_points(src_img, lihua_rest_img, threshold=0.8)
                        if points:
                            print("CD中，继续点礼花。")
                            break

                    # 五秒未能拾取，卡住了,直接去吃饭
                    index = 5
                    break
                else:
                    break

            if is_move:
                # 回到餐桌旁边
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

                # 去待机位置
                randint_x = random.randint(0, 1)
                randint_y = random.randint(0, 1)
                window_click(hwnd, pos_wait, randint_x, randint_y)
                time.sleep(random.uniform(0.5, 0.6))

                # 关闭地图
                pos = (1997 - 1927, 178 - 156)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(1.0, 1.2))
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, button_close_img)
                if points:
                    # 地图未能关闭?重新关闭。
                    print("场景切换？未能关闭地图，重新关闭。")
                    time.sleep(random.uniform(4.8, 5.2))
                    pos = (1997 - 1927, 178 - 156)
                    randint_x = random.randint(0, 5)
                    randint_y = random.randint(0, 10)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(1.0, 1.2))

                time.sleep(random.uniform(4.8, 5.2))

        if index >= 5:
            # 每五次循环，点一下桌子
            index = 0
            # 关闭其它窗口
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, xinxi_close_img, threshold=0.8)
            if points:
                pos = points[0]
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.8, 1.0))
            # 点桌子前，先关闭对话
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, button_close_img)
            if points:
                pos = points[0]
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.8, 1.0))
            """
            # 点桌子
            randint_x = random.randint(0, 1)
            randint_y = random.randint(0, 1)
            window_click(hwnd, pos_target, randint_x, randint_y)
            time.sleep(random.uniform(1.0, 1.2))
            """
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, yanhui_clock_img, threshold=0.8)
            if points:
                px, py = points[0]
                pos = (px + 33, py + 100)
                randint_x = random.randint(0, 2)
                randint_y = random.randint(0, 2)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(1.0, 1.2))
            else:
                print("未能发现倒计时。")
                # 不用处理，继续往下判断
                #waiting_num += 1
                #continue

            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, zhuozi_choice_img, threshold=0.98)
            if points:
                # 在一起了，需要选择
                pos = points[0]
                randint_x = random.randint(5, 90)
                randint_y = random.randint(5, 20)
                window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(1.0, 1.2))

            src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
            points1 = get_match_points(src_img, button_pinchang_gray_img_color)
            points2 = get_match_points(src_img, button_pinchang_img_color)
            if points1:
                # 点下任务栏，取消吃菜窗口
                waiting_num = 0
                pos = (2863 - 1927, 303 - 193)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.8, 1.2))
                pos = (2863 - 1927, 303 - 193)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                continue
            elif points2:
                # 点吃菜
                waiting_num = 0
                pos = points2[0]
                randint_x = random.randint(10, 80)
                randint_y = random.randint(5, 15)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(5.0, 6.0))
                continue
            else:
                # 未知对话，关闭对话
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, button_close_img)
                if points:
                    pos = points[0]
                    randint_x = random.randint(0, 5)
                    randint_y = random.randint(0, 5)
                    window_click(hwnd, pos, randint_x, randint_y)
                waiting_num += 1
                continue


def yanhui1(hwnd, x, y):
    yanhui_pighead_img_color = cv2.cvtColor(cv2.imread("src/yanhui_pighead.png"), cv2.IMREAD_COLOR)
    yanhui_tao_img_color = cv2.cvtColor(cv2.imread("src/yanhui_tao.png"), cv2.IMREAD_COLOR)
    button_pinchang_img_color = cv2.cvtColor(cv2.imread("src/button_pinchang.png"), cv2.IMREAD_COLOR)
    button_pinchang_gray_img_color = cv2.cvtColor(cv2.imread("src/button_pinchang_gray.png"), cv2.IMREAD_COLOR)
    button_close_img_color = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.IMREAD_COLOR)
    biaoqing_chaoren_img_color = cv2.cvtColor(cv2.imread("src/biaoqing_chaoren.png"), cv2.IMREAD_COLOR)
    #icon_huanqingshenwu_img_color = cv2.cvtColor(cv2.imread("src/icon_huanqingshenwu.png"), cv2.IMREAD_COLOR)

    already_eaten = False
    #already_huanqing = False
    while True:
        time.sleep(random.uniform(settings.inverval_min * 3, settings.inverval_max * 3))

        src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)

        """
        left = 0
        top = 0
        w = 970
        h = 400
        opponent_img = src_img[top:top + h, left:left + w]
        points = get_match_points(opponent_img, biaoqing_chaoren_img_color, threshold=0.8)
        if points:
            if not already_huanqing:
                px, py = points[0]
                pos = (px + 87, py)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                already_huanqing = True
                continue
        else:
            already_huanqing = False
        """

        points = get_match_points(src_img, button_close_img_color)
        if points:
            # 还未开始
            pos = points[0]
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(10.0, 12.0))
            continue

        points = get_match_points(src_img, button_pinchang_gray_img_color)
        if points:
            already_eaten = True
            # 点下任务栏，取消吃菜窗口
            pos = (2863 - 1927, 303 - 193)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.8, 1.2))
            pos = (2863 - 1927, 303 - 193)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        points = get_match_points(src_img, button_pinchang_img_color)
        if points:
            already_eaten = True
            # 点吃菜
            pos = points[0]
            randint_x = random.randint(10, 80)
            randint_y = random.randint(5, 15)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(5.0, 6.0))
            continue

        points = get_match_points(src_img, yanhui_pighead_img_color)
        if not points:
            points = get_match_points(src_img, yanhui_tao_img_color)
        if points:
            # 新菜上桌
            if already_eaten:
                continue
            else:
                # 没吃过这道菜，开吃
                pos = points[0]
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                continue
        else:
            already_eaten = False
            continue
