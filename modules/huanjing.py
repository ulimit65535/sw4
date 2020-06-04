import random
import time
import cv2
import numpy as np

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points


def huanjing(hwnd, x, y, get_shenmi=False):
    hanweizhe_img_color = cv2.cvtColor(cv2.imread("src/hanweizhe.png"), cv2.IMREAD_COLOR)
    lower = np.array([24, 160, 180], dtype="uint8")
    upper = np.array([67, 230, 255], dtype="uint8")
    mask = cv2.inRange(hanweizhe_img_color, lower, upper)
    hanweizhe_img_color = cv2.bitwise_and(hanweizhe_img_color, hanweizhe_img_color, mask=mask)
    hanweizhe_img = cv2.cvtColor(hanweizhe_img_color, cv2.COLOR_BGR2GRAY)

    shouhuzhe_img_color = cv2.cvtColor(cv2.imread("src/shouhuzhe.png"), cv2.IMREAD_COLOR)
    lower = np.array([24, 160, 180], dtype="uint8")
    upper = np.array([67, 230, 255], dtype="uint8")
    mask = cv2.inRange(shouhuzhe_img_color, lower, upper)
    shouhuzhe_img_color = cv2.bitwise_and(shouhuzhe_img_color, shouhuzhe_img_color, mask=mask)
    shouhuzhe_img = cv2.cvtColor(shouhuzhe_img_color, cv2.COLOR_BGR2GRAY)

    shenmibaoxiang_img_color = cv2.cvtColor(cv2.imread("src/shenmibaoxiang.png"), cv2.IMREAD_COLOR)
    lower = np.array([24, 160, 180], dtype="uint8")
    upper = np.array([67, 230, 255], dtype="uint8")
    mask = cv2.inRange(shenmibaoxiang_img_color, lower, upper)
    shenmibaoxiang_img_color = cv2.bitwise_and(shenmibaoxiang_img_color, shenmibaoxiang_img_color, mask=mask)
    shenmibaoxiang_img = cv2.cvtColor(shenmibaoxiang_img_color, cv2.COLOR_BGR2GRAY)

    hanweizhe_choice_img = cv2.cvtColor(cv2.imread("src/hanweizhe_choice.png"), cv2.COLOR_BGR2GRAY)
    shouhuzhe_choice_img = cv2.cvtColor(cv2.imread("src/shouhuzhe_choice.png"), cv2.COLOR_BGR2GRAY)

    duiwu_yincang_img = cv2.cvtColor(cv2.imread("src/duiwu_yincang.png"), cv2.COLOR_BGR2GRAY)
    duidie_close_img = cv2.cvtColor(cv2.imread("src/duidie_close.png"), cv2.COLOR_BGR2GRAY)
    button_close_img = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.COLOR_BGR2GRAY)
    button_queding_huanjing_img = cv2.cvtColor(cv2.imread("src/button_queding_huanjing.png"), cv2.COLOR_BGR2GRAY)
    zidong_img = cv2.cvtColor(cv2.imread("src/zidong.png"), cv2.COLOR_BGR2GRAY)
    quxiaozidong_img = cv2.cvtColor(cv2.imread("src/quxiaozidong.png"), cv2.COLOR_BGR2GRAY)

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
    has_gold_key = True
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

        if get_shenmi and has_gold_key:
            points1 = get_match_points(opponent_img, shenmibaoxiang_img, threshold=0.6)
            if points1:
                # 点神秘宝箱
                px, py = points1[0]
                # px, py是相对于opponent_img的坐标，所以还要加上left和top
                pos = (px + 151 + 30, py + 115 - 25)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)

                # 最多等待2.5秒
                for i in range(10):
                    time.sleep(random.uniform(0.2, 0.3))
                    src_img = window_capture(hwnd, x, y)
                    # 需要选择，没有截图，默认选第一个
                    points = get_match_points(src_img, duidie_close_img)
                    if points:
                        pos = points[0]
                        randint_x = random.randint(-100, -80)
                        randint_y = random.randint(0, 15)
                        window_click(hwnd, pos, randint_x, randint_y)
                        continue
                    points = get_match_points(src_img, button_queding_huanjing_img)
                    if points:
                        pos = points[0]
                        randint_x = random.randint(10, 80)
                        randint_y = random.randint(5, 20)
                        window_click(hwnd, pos, randint_x, randint_y)
                        time.sleep(random.uniform(1.8, 2.2))
                        src_img = window_capture(hwnd, x, y)
                        points = get_match_points(src_img, button_close_img)
                        if points:
                            pos = points[0]
                            randint_x = random.randint(0, 5)
                            randint_y = random.randint(0, 5)
                            window_click(hwnd, pos, randint_x, randint_y)
                        break
                    points = get_match_points(src_img, button_close_img)
                    if points:
                        # 没金钥匙
                        pos = points[0]
                        randint_x = random.randint(0, 5)
                        randint_y = random.randint(0, 5)
                        window_click(hwnd, pos, randint_x, randint_y)
                        has_gold_key = False

                # 摇色子
                for i in range(20):
                    time.sleep(random.uniform(0.2, 0.3))
                    src_img = window_capture(hwnd, x, y)
                    points = get_match_points(src_img, button_queding_huanjing_img)
                    if points:
                        pos = points[0]
                        randint_x = random.randint(10, 80)
                        randint_y = random.randint(5, 20)
                        window_click(hwnd, pos, randint_x, randint_y)
                        time.sleep(random.uniform(1.8, 2.2))
                        src_img = window_capture(hwnd, x, y)
                        points = get_match_points(src_img, button_close_img)
                        if points:
                            pos = points[0]
                            randint_x = random.randint(0, 5)
                            randint_y = random.randint(0, 5)
                            window_click(hwnd, pos, randint_x, randint_y)
                        break

        points2 = get_match_points(opponent_img, hanweizhe_img, threshold=0.6)
        if points2:
            # 点捍卫者
            px, py = points2[0]
            # px, py是相对于opponent_img的坐标，所以还要加上left和top
            pos = (px + 151 + 40, py + 115 - 25)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)

            # 最多等待2.5秒
            for i in range(10):
                time.sleep(random.uniform(0.2, 0.3))
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, hanweizhe_choice_img, threshold=0.98)
                if points:
                    # 怪站一起了，需要选择
                    pos = points[0]
                    randint_x = random.randint(5, 90)
                    randint_y = random.randint(5, 20)
                    window_click(hwnd, pos, randint_x, randint_y)
                    continue
                points = get_match_points(src_img, zidong_img)
                if not points:
                    points = get_match_points(src_img, quxiaozidong_img)
                    if points:
                        # 已进入战斗
                        has_gold_key = True
                        break
                else:
                    # 已进入战斗，自动准备
                    pos = points[0]
                    randint_x = random.randint(0, 10)
                    randint_y = random.randint(0, 10)
                    window_click(hwnd, pos, randint_x, randint_y)
                    has_gold_key = True
                    break

        """
        if not get_shenmi:
            # 不拾取神秘的话，宝箱怪也杀
            points3 = get_match_points(opponent_img, shouhuzhe_img, threshold=0.6)
            if points3:
                # 点宝箱守护者
                px, py = points3[0]
                # px, py是相对于opponent_img的坐标，所以还要加上left和top
                pos = (px + 151 + 45, py + 115 - 25)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)

                # 最多等待2.5秒
                for i in range(10):
                    time.sleep(random.uniform(0.2, 0.3))
                    src_img = window_capture(hwnd, x, y)
                    points = get_match_points(src_img, shouhuzhe_choice_img, threshold=0.98)
                    if points:
                        # 怪站一起了，需要选择
                        pos = points[0]
                        randint_x = random.randint(5, 90)
                        randint_y = random.randint(5, 20)
                        window_click(hwnd, pos, randint_x, randint_y)
                        continue
                    points = get_match_points(src_img, zidong_img)
                    if not points:
                        points = get_match_points(src_img, quxiaozidong_img)
                        if points:
                            # 已进入战斗
                            has_gold_key = True
                            break
                    else:
                        # 已进入战斗，自动准备
                        pos = points[0]
                        randint_x = random.randint(0, 10)
                        randint_y = random.randint(0, 10)
                        window_click(hwnd, pos, randint_x, randint_y)
                        has_gold_key = True
                        break
        """
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
