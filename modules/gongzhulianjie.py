import random
import time
import cv2
import numpy as np

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points


def main(hwnd, x, y, task):
    if task == "进入游戏":
        enter_game(hwnd, x, y)
    elif task == "无限战斗":
        battle_loop(hwnd, x, y)
    elif task == "地下城助战":
        zhuzhan(hwnd, x, y)
    elif task == "捐赠点赞":
        juanzeng(hwnd, x, y)
    elif task == "其它日常":
        niudan(hwnd, x, y)
        time.sleep(random.uniform(1.8, 2.2))
        gonghui(hwnd, x, y)
        time.sleep(random.uniform(1.8, 2.2))
        tansuo(hwnd, x, y)
        time.sleep(random.uniform(1.8, 2.2))
        jiaorenwu(hwnd, x, y)
        time.sleep(random.uniform(1.8, 2.2))
        lingliwu(hwnd, x, y)


def lingliwu(hwnd, x, y):
    button_liwu_img = cv2.cvtColor(cv2.imread("src/gzlj/button_liwu.png"), cv2.COLOR_BGR2GRAY)
    button_quanbushouqu_img = cv2.cvtColor(cv2.imread("src/gzlj/button_quanbushouqu.png"), cv2.COLOR_BGR2GRAY)
    shouquliwu_img = cv2.cvtColor(cv2.imread("src/gzlj/shouquliwu.png"), cv2.COLOR_BGR2GRAY)

    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, button_liwu_img)
    if points:
        pos = (2822 - 1927, 579 - 156)
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
    else:
        # 点主页
        pos = (2006 - 1927, 661 - 156)
        randint_x = random.randint(0, 50)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(4.8, 5.2))
        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, button_liwu_img)
        if points:
            pos = (2822 - 1927, 579 - 156)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
        else:
            print("未找到礼物按钮，退出。")
            return

    time.sleep(random.uniform(2.8, 3.2))

    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, button_quanbushouqu_img)
    if points:
        pos = (2695 - 1927, 622 - 156)
        randint_x = random.randint(0, 30)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(2.8, 3.2))

        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, shouquliwu_img)
        if points:
            pos = (2483 - 1927, 625 - 156)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(2.4, 2.6))
            # 点Ok
            pos = (2378 - 1927, 630 - 156)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(2.4, 2.6))

    # 点取消
    pos = (2484 - 1927, 625 - 156)
    randint_x = random.randint(0, 30)
    randint_y = random.randint(0, 10)
    window_click(hwnd, pos, randint_x, randint_y)


def jiaorenwu(hwnd, x, y):
    button_renwu_img = cv2.cvtColor(cv2.imread("src/gzlj/button_renwu.png"), cv2.COLOR_BGR2GRAY)
    button_quanbushouqu_img = cv2.cvtColor(cv2.imread("src/gzlj/button_quanbushouqu.png"), cv2.COLOR_BGR2GRAY)
    shouqubaochou_img = cv2.cvtColor(cv2.imread("src/gzlj/shouqubaochou.png"), cv2.COLOR_BGR2GRAY)
    level_up_img = cv2.cvtColor(cv2.imread("src/gzlj/level_up.png"), cv2.COLOR_BGR2GRAY)

    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, button_renwu_img)
    if points:
        pos = (2754 - 1927, 579 - 156)
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
    else:
        # 点主页
        pos = (2006 - 1927, 661 - 156)
        randint_x = random.randint(0, 50)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(4.8, 5.2))
        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, button_renwu_img)
        if points:
            pos = (2754 - 1927, 579 - 156)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
        else:
            print("未找到任务按钮，退出。")
            return

    time.sleep(random.uniform(4.8, 5.2))

    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, button_quanbushouqu_img)
    if points:
        pos = (2736 - 1927, 585 - 156)
        randint_x = random.randint(0, 30)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(2.8, 3.2))

        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, shouqubaochou_img)
        if points:
            pos = (2378 - 1927, 630 - 156)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(2.8, 3.2))

        src_img = window_capture(hwnd, x, y)
        # 升级了，点ok
        points = get_match_points(src_img, level_up_img, threshold=0.95)
        if points:
            # 这里用窗口4抓的坐标
            pos = (3330 - 2881, 1066 - 705)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)


def tansuo(hwnd, x, y):
    button_tansuo_img = cv2.cvtColor(cv2.imread("src/gzlj/button_tansuo.png"), cv2.COLOR_BGR2GRAY)
    three_stars_img = cv2.cvtColor(cv2.imread("src/gzlj/three_stars.png"), cv2.COLOR_BGR2GRAY)
    button_shiyongliangzhang_img = cv2.cvtColor(cv2.imread("src/gzlj/button_shiyongliangzhang.png"), cv2.COLOR_BGR2GRAY)
    saodangquanqueren_img = cv2.cvtColor(cv2.imread("src/gzlj/saodangquanqueren.png"), cv2.COLOR_BGR2GRAY)
    button_jinrutansuoshouye_img_color = cv2.cvtColor(cv2.imread("src/gzlj/button_jinrutansuoshouye.png"), cv2.IMREAD_COLOR)

    # 点冒险
    pos = (2376 - 1927, 661 - 156)
    randint_x = random.randint(0, 50)
    randint_y = random.randint(0, 10)
    window_click(hwnd, pos, randint_x, randint_y)
    time.sleep(random.uniform(4.8, 5.2))

    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, button_tansuo_img)
    if points:
        pos = (2644 - 1927, 264 - 156)
        randint_x = random.randint(0, 50)
        randint_y = random.randint(0, 50)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(4.8, 5.2))
    else:
        print("未能找到探索按钮.")
        return

    for i in range(2):
        # 进入关卡
        pos = (2476 - 1927 + i * 220, 337 - 156)
        randint_x = random.randint(0, 80)
        randint_y = random.randint(0, 80)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(2.8, 3.2))

        # 找最上面的3星通关的关卡
        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, three_stars_img)
        if points:
            target_x, target_y = points.pop(0)
            for x, y in points:
                if y < target_y:
                    target_x = x
                    target_y = y
            target_pos = (target_x, target_y)
            randint_x = random.randint(0, 150)
            randint_y = random.randint(-30, 0)
            # 点击最上方三星
            window_click(hwnd, target_pos, randint_x, randint_y)
            time.sleep(random.uniform(2.4, 2.6))

            # 点+号
            pos = (2798 - 1927, 479 - 156)
            randint_x = random.randint(0, 15)
            randint_y = random.randint(0, 15)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(1.8, 2.2))

            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, button_shiyongliangzhang_img)
            if points:
                # 点使用2张
                pos = (2660 - 1927, 479 - 156)
                randint_x = random.randint(0, 30)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(2.4, 2.6))

                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, saodangquanqueren_img)
                if points:
                    # 点ok
                    pos = (2490 - 1927, 515 - 156)
                    randint_x = random.randint(0, 30)
                    randint_y = random.randint(0, 10)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(2.4, 2.6))

                    for i in range(10):
                        time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

                        src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
                        points = get_match_points(src_img, button_jinrutansuoshouye_img_color, threshold=0.9)
                        if points:
                            pos = (2381 - 1927, 623 - 156)
                            randint_x = random.randint(0, 30)
                            randint_y = random.randint(0, 10)
                            window_click(hwnd, pos, randint_x, randint_y)
                            time.sleep(random.uniform(2.8, 3.2))
                            break
            else:
                # 扫荡券不够，或已完成
                # 点取消
                pos = (2565 - 1927, 602 - 156)
                randint_x = random.randint(0, 30)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(2.4, 2.6))
                # 点返回
                pos = (1950 - 1927, 177 - 156)
                randint_x = random.randint(0, 10)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(2.8, 3.2))


def gonghui(hwnd, x, y):
    button_shouqu_img = cv2.cvtColor(cv2.imread("src/gzlj/button_shouqu.png"), cv2.COLOR_BGR2GRAY)
    quanbushouqu_img = cv2.cvtColor(cv2.imread("src/gzlj/quanbushouqu.png"), cv2.COLOR_BGR2GRAY)

    # 点公会之家
    pos = (2525 - 1927, 661 - 156)
    randint_x = random.randint(0, 50)
    randint_y = random.randint(0, 10)
    window_click(hwnd, pos, randint_x, randint_y)
    time.sleep(random.uniform(4.8, 5.2))

    # 点全部收取
    pos = (2808 - 1927, 563 - 156)
    randint_x = random.randint(0, 25)
    randint_y = random.randint(0, 25)
    window_click(hwnd, pos, randint_x, randint_y)
    time.sleep(random.uniform(2.4, 2.6))

    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, quanbushouqu_img)
    if points:
        # 点OK
        pos = (2367 - 1927, 625 - 156)
        randint_x = random.randint(0, 30)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)


def niudan(hwnd, x, y):
    button_mianfei_img = cv2.cvtColor(cv2.imread("src/gzlj/button_mianfei.png"), cv2.COLOR_BGR2GRAY)
    putongniudan_img = cv2.cvtColor(cv2.imread("src/gzlj/putongniudan.png"), cv2.COLOR_BGR2GRAY)

    # 点扭蛋
    pos = (2655 - 1927, 661 - 156)
    randint_x = random.randint(0, 50)
    randint_y = random.randint(0, 10)
    window_click(hwnd, pos, randint_x, randint_y)
    time.sleep(random.uniform(4.8, 5.2))

    # 点普通
    pos = (2779 - 1927, 222 - 156)
    randint_x = random.randint(0, 30)
    randint_y = random.randint(0, 10)
    window_click(hwnd, pos, randint_x, randint_y)
    time.sleep(random.uniform(2.4, 2.6))

    # 点免费
    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, button_mianfei_img)
    if points:
        pos = (2607 - 1927, 492 - 156)
        randint_x = random.randint(0, 50)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(2.4, 2.6))

        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, putongniudan_img)
        if points:
            # 点ok
            pos = (2485 - 1927, 515 - 156)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(4.8, 5.2))
            # 点ok
            pos = (2373 - 1927, 588 - 156)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)


def juanzeng(hwnd, x, y):
    dianzanqueren_img = cv2.cvtColor(cv2.imread("src/gzlj/dianzanqueren.png"), cv2.COLOR_BGR2GRAY)
    button_hanghui_img = cv2.cvtColor(cv2.imread("src/gzlj/button_hanghui.png"), cv2.COLOR_BGR2GRAY)
    button_juanzeng_img = cv2.cvtColor(cv2.imread("src/gzlj/button_juanzeng.png"), cv2.COLOR_BGR2GRAY)
    querenjuanzeng_img = cv2.cvtColor(cv2.imread("src/gzlj/querenjuanzeng.png"), cv2.COLOR_BGR2GRAY)
    button_ok_img_color = cv2.cvtColor(cv2.imread("src/gzlj/button_ok.png"), cv2.IMREAD_COLOR)
    button_chengyuan_img = cv2.cvtColor(cv2.imread("src/gzlj/button_chengyuan.png"), cv2.COLOR_BGR2GRAY)
    juanzengwanbi_img = cv2.cvtColor(cv2.imread("src/gzlj/juanzengwanbi.png"), cv2.COLOR_BGR2GRAY)
    dianzanwancheng_img = cv2.cvtColor(cv2.imread("src/gzlj/dianzanwancheng.png"), cv2.COLOR_BGR2GRAY)

    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, button_hanghui_img)
    if points:
        pos = (2610 - 1927, 579 - 156)
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
    else:
        # 点主页
        pos = (2006 - 1927, 661 - 156)
        randint_x = random.randint(0, 50)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(3.8, 4.2))
        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, button_hanghui_img)
        if points:
            pos = (2610 - 1927, 579 - 156)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
        else:
            print("未找到行会按钮，退出。")
            return

    time.sleep(random.uniform(2.8, 3.2))

    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, dianzanqueren_img)
    if points:
        pos = (2370 - 1927, 517 - 156)
        randint_x = random.randint(0, 30)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(1.4, 1.6))

    # 定位捐赠按钮
    pos = (2286 - 1927, 191 - 156)
    randint_x = random.randint(0, 5)
    randint_y = random.randint(0, 5)
    window_click(hwnd, pos, randint_x, randint_y)
    time.sleep(random.uniform(1.0, 1.2))

    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, button_juanzeng_img)
    if points:
        target_x, target_y = points.pop(0)
        for x, y in points:
            if y > target_y:
                target_x = x
                target_y = y
        target_pos = (target_x, target_y)
        randint_x = random.randint(40, 60)
        randint_y = random.randint(0, 10)
        # 点击最下方的捐赠
        window_click(hwnd, target_pos, randint_x, randint_y)
        time.sleep(random.uniform(1.4, 1.6))

        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, querenjuanzeng_img)
        if points:
            # 点max
            pos = (2553 - 1927, 534 - 156)
            randint_x = random.randint(0, 15)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(1.4, 1.6))
            src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
            points = get_match_points(src_img, button_ok_img_color, threshold=0.98)
            if points:
                # 点OK
                pos = (2485 - 1927, 624 - 156)
                randint_x = random.randint(0, 30)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
            else:
                # 未持有物品?点取消
                pos = (2262 - 1927, 624 - 156)
                randint_x = random.randint(0, 30)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(1.4, 1.6))

    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, juanzengwanbi_img)
    if points:
        # 点OK
        pos = (2371 - 1927, 515 - 156)
        randint_x = random.randint(0, 30)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(1.4, 1.6))

    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, button_chengyuan_img)
    if points:
        pos = (2144 - 1927, 489 - 156)
        randint_x = random.randint(0, 30)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.2))
        pos = (2144 - 1927, 489 - 156)
        randint_x = random.randint(0, 30)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.2))
        pos = (2144 - 1927, 489 - 156)
        randint_x = random.randint(0, 30)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.2))
        # 点第二个人，点赞
        pos = (2749 - 1927, 460 - 156)
        randint_x = random.randint(0, 25)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(1.4, 1.6))

    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, dianzanwancheng_img)
    if points:
        # 点OK
        pos = (2371 - 1927, 515 - 156)
        randint_x = random.randint(0, 30)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)


def zhuzhan(hwnd, x, y):
    button_dixiacheng_img = cv2.cvtColor(cv2.imread("src/gzlj/button_dixiacheng.png"), cv2.COLOR_BGR2GRAY)
    mubaoxiang_img = cv2.cvtColor(cv2.imread("src/gzlj/mubaoxiang.png"), cv2.COLOR_BGR2GRAY)
    jinbaoxiang_img = cv2.cvtColor(cv2.imread("src/gzlj/jinbaoxiang.png"), cv2.COLOR_BGR2GRAY)
    xianzaidecengsu_img = cv2.cvtColor(cv2.imread("src/gzlj/xianzaidecengsu.png"), cv2.COLOR_BGR2GRAY)
    button_caidan_img = cv2.cvtColor(cv2.imread("src/gzlj/button_caidan.png"), cv2.COLOR_BGR2GRAY)
    duiwubianzu_img = cv2.cvtColor(cv2.imread("src/gzlj/duiwubianzu.png"), cv2.COLOR_BGR2GRAY)
    zhuzhan_choice_img = cv2.cvtColor(cv2.imread("src/gzlj/replace/zhuzhan_choice.png"), cv2.COLOR_BGR2GRAY)
    button_tiaozhan_img = cv2.cvtColor(cv2.imread("src/gzlj/button_tiaozhan.png"), cv2.COLOR_BGR2GRAY)
    button_zhandoukaishi_img_color = cv2.cvtColor(cv2.imread("src/gzlj/button_zhandoukaishi.png"), cv2.IMREAD_COLOR)
    button_xiayibu_img = cv2.cvtColor(cv2.imread("src/gzlj/button_xiayibu.png"), cv2.COLOR_BGR2GRAY)
    shouqubaochou_img = cv2.cvtColor(cv2.imread("src/gzlj/shouqubaochou.png"), cv2.COLOR_BGR2GRAY)
    button_qianwangdixiacheng_img = cv2.cvtColor(cv2.imread("src/gzlj/button_qianwangdixiacheng.png"), cv2.COLOR_BGR2GRAY)
    chetuiqueren_img = cv2.cvtColor(cv2.imread("src/gzlj/chetuiqueren.png"), cv2.COLOR_BGR2GRAY)

    # 点冒险
    pos = (2376 - 1927, 661 - 156)
    randint_x = random.randint(0, 50)
    randint_y = random.randint(0, 10)
    window_click(hwnd, pos, randint_x, randint_y)
    time.sleep(random.uniform(2.8, 3.2))

    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, button_dixiacheng_img)
    if points:
        pos = (2781 - 1927, 264 - 156)
        randint_x = random.randint(0, 50)
        randint_y = random.randint(0, 50)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(3.8, 4.2))
    else:
        print("未能找到地下城按钮.")
        return

    # 未选择地下城
    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, xianzaidecengsu_img)
    if not points:
        # 选择地下城，第一个是0
        i = 0
        pos = (2131 - 1927 + i * 2, 337 - 156)
        randint_x = random.randint(0, 50)
        randint_y = random.randint(0, 50)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(1.4, 1.6))
        # 点OK
        pos = (2483 - 1927, 514 - 156)
        randint_x = random.randint(0, 30)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(1.4, 1.6))

    waiting_num = 0
    while True:
        waiting_num += 1
        time.sleep(random.uniform(settings.inverval_min * 2, settings.inverval_max * 2))

        src_img = window_capture(hwnd, x, y)

        points = get_match_points(src_img, button_caidan_img)
        if points:
            # 战斗中
            print("战斗中...")
            waiting_num = 0
            continue

        if waiting_num >= 15:
            print("等待时间过长，退出。")
            return

        # 战斗失败
        points = get_match_points(src_img, button_qianwangdixiacheng_img)
        if points:
            pos = (2695 - 1927, 638 - 156)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(2.8, 3.2))
            # 点撤退
            pos = (2700 - 1927, 581 - 156)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(1.4, 1.6))
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, chetuiqueren_img)
            if points:
                # 点OK
                pos = (2490 - 1927, 518 - 156)
                randint_x = random.randint(0, 30)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
            return

        # 挑战
        points = get_match_points(src_img, button_tiaozhan_img)
        if points:
            pos = (2729 - 1927, 602 - 156)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(1.0, 1.2))
            continue

        # 下一步
        points = get_match_points(src_img, button_xiayibu_img)
        if points:
            pos = (2731 - 1927, 641 - 156)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 收取报酬
        points = get_match_points(src_img, shouqubaochou_img)
        if points:
            pos = (2378 - 1927, 630 - 156)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 队伍编组
        points = get_match_points(src_img, duiwubianzu_img)
        if points:
            src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
            # 战斗开始
            points = get_match_points(src_img, button_zhandoukaishi_img_color, threshold=0.98)
            if points:
                pos = (2736 - 1927, 602 - 156)
                randint_x = random.randint(0, 30)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                continue
            else:
                for i in range(4):
                    pos = (2021 - 1927 + i * 106, 312 - 156)
                    randint_x = random.randint(0, 10)
                    randint_y = random.randint(0, 10)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(1.0, 1.2))

                # 点协助
                pos = (2383 - 1927, 236 - 156)
                randint_x = random.randint(0, 30)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(1.0, 1.2))

                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, zhuzhan_choice_img)
                if points:
                    pos = points[0]
                    randint_x = random.randint(10, 30)
                    randint_y = random.randint(0, 20)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(1.0, 1.2))
                    # 点战斗开始
                    pos = (2736 - 1927, 602 - 156)
                    randint_x = random.randint(0, 30)
                    randint_y = random.randint(0, 10)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(1.8, 2.2))
                    # 点OK
                    pos = (2479 - 1927, 623 - 156)
                    randint_x = random.randint(0, 30)
                    randint_y = random.randint(0, 10)
                    window_click(hwnd, pos, randint_x, randint_y)
                    continue
                else:
                    print("未能找到助战对象")
                    return

        # 在地下城中,选择挑战对象
        points = get_match_points(src_img, xianzaidecengsu_img)
        if points:
            pos_list = []

            points = get_match_points(src_img, mubaoxiang_img, threshold=0.8)
            if points:
                pos_list += points
            points = get_match_points(src_img, jinbaoxiang_img, threshold=0.8)
            if points:
                pos_list += points

            if pos_list:
                target_x, target_y = pos_list.pop(0)
                for x, y in pos_list:
                    if y > target_y:
                        target_x = x
                        target_y = y
                target_pos = (target_x, target_y)
                randint_x = random.randint(32, 35)
                randint_y = random.randint(10, 15)
                # 点击战斗目标，等待弹窗
                window_click(hwnd, target_pos, randint_x, randint_y)
                continue
            else:
                print("未发现宝箱")
                continue


def enter_game(hwnd, x, y):
    app_pcr_img = cv2.cvtColor(cv2.imread("src/gzlj/app_pcr.png"), cv2.COLOR_BGR2GRAY)
    button_zhucaidan_img = cv2.cvtColor(cv2.imread("src/gzlj/button_zhucaidan.png"), cv2.COLOR_BGR2GRAY)
    tongzhi_img = cv2.cvtColor(cv2.imread("src/gzlj/tongzhi.png"), cv2.COLOR_BGR2GRAY)
    button_skip_img = cv2.cvtColor(cv2.imread("src/gzlj/button_skip.png"), cv2.COLOR_BGR2GRAY)
    denglujiangli_img = cv2.cvtColor(cv2.imread("src/gzlj/denglujiangli.png"), cv2.COLOR_BGR2GRAY)

    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, app_pcr_img)
    if points:
        pos = points[0]
        randint_x = random.randint(10, 15)
        randint_y = random.randint(10, 15)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(7.8, 8.2))

        is_in = False
        for i in range(30):
            time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, button_zhucaidan_img)
            if points:
                is_in = True
                pos = (2263 - 1927, 338 - 156)
                randint_x = random.randint(0, 100)
                randint_y = random.randint(0, 100)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(1.8, 2.2))
                continue
            else:
                if is_in:
                    break

        if is_in:
            for i in range(30):
                time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, button_skip_img)
                if points:
                    pos = points[0]
                    randint_x = random.randint(5, 15)
                    randint_y = random.randint(5, 10)
                    window_click(hwnd, pos, randint_x, randint_y)
                    continue
                points = get_match_points(src_img, denglujiangli_img, threshold=0.8)
                if points:
                    pos = points[0]
                    randint_x = random.randint(20, 50)
                    randint_y = random.randint(20, 50)
                    window_click(hwnd, pos, randint_x, randint_y)
                    continue
                points = get_match_points(src_img, tongzhi_img)
                if points:
                    pos = (2366 - 1927, 625 - 156)
                    randint_x = random.randint(0, 30)
                    randint_y = random.randint(0, 10)
                    window_click(hwnd, pos, randint_x, randint_y)
                    return


def battle_loop(hwnd, x, y):
    #button_normal_img = cv2.cvtColor(cv2.imread("src/gzlj/button_normal.png"), cv2.COLOR_BGR2GRAY)
    button_tiaozhan_img = cv2.cvtColor(cv2.imread("src/gzlj/button_tiaozhan.png"), cv2.COLOR_BGR2GRAY)
    button_zhandoukaishi_img = cv2.cvtColor(cv2.imread("src/gzlj/button_zhandoukaishi.png"), cv2.COLOR_BGR2GRAY)
    button_xiayibu_img = cv2.cvtColor(cv2.imread("src/gzlj/button_xiayibu.png"), cv2.COLOR_BGR2GRAY)
    #button_xiayibu_small_img = cv2.cvtColor(cv2.imread("src/gzlj/button_xiayibu_small.png"), cv2.COLOR_BGR2GRAY)
    #button_quxiao_img = cv2.cvtColor(cv2.imread("src/gzlj/button_quxiao.png"), cv2.COLOR_BGR2GRAY)
    button_skip_img = cv2.cvtColor(cv2.imread("src/gzlj/button_skip.png"), cv2.COLOR_BGR2GRAY)
    #user_img = cv2.cvtColor(cv2.imread("src/gzlj/user.png"), cv2.COLOR_BGR2GRAY)
    level_up_img = cv2.cvtColor(cv2.imread("src/gzlj/level_up.png"), cv2.COLOR_BGR2GRAY)
    no_tili_img = cv2.cvtColor(cv2.imread("src/gzlj/no_tili.png"), cv2.COLOR_BGR2GRAY)
    button_caidan_img = cv2.cvtColor(cv2.imread("src/gzlj/button_caidan.png"), cv2.COLOR_BGR2GRAY)
    button_zaicitiaozhan_img = cv2.cvtColor(cv2.imread("src/gzlj/button_zaicitiaozhan.png"), cv2.COLOR_BGR2GRAY)
    guanqiachongshi_img = cv2.cvtColor(cv2.imread("src/gzlj/guanqiachongshi.png"), cv2.COLOR_BGR2GRAY)
    xiandingchuxian_img = cv2.cvtColor(cv2.imread("src/gzlj/xiandingchuxian.png"), cv2.COLOR_BGR2GRAY)

    waiting_num = 0
    while True:
        time.sleep(random.uniform(settings.inverval_min * 2, settings.inverval_max * 2))

        src_img = window_capture(hwnd, x, y)

        points = get_match_points(src_img, button_caidan_img)
        if points:
            # 战斗中
            print("战斗中...")
            waiting_num = 0
            continue

        if waiting_num >= 10:
            print("等待时间过长，退出。")
            return

        # 结束
        points = get_match_points(src_img, no_tili_img, threshold=0.8)
        if points:
            print("体力不足，退出。")
            return

        # 升级了，点ok
        points = get_match_points(src_img, level_up_img,threshold=0.95)
        if points:
            # 这里用窗口4抓的坐标
            pos = (3330 - 2881, 1066 - 705)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 跳过
        points = get_match_points(src_img, button_skip_img)
        if points:
            pos = points[0]
            randint_x = random.randint(5, 15)
            randint_y = random.randint(5, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        """
        # 点关卡
        points = get_match_points(src_img, user_img, threshold=0.7)
        if points:
            pos = points[0]
            randint_x = random.randint(5, 10)
            randint_y = random.randint(55, 60)
            window_click(hwnd, pos, randint_x, randint_y)
            continue
        """

        # 挑战
        points = get_match_points(src_img, button_tiaozhan_img)
        if points:
            pos = (2729 - 1927, 602 - 156)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(2)
            continue

        # 战斗开始
        points = get_match_points(src_img, button_zhandoukaishi_img)
        if points:
            pos = (2736 - 1927, 602 - 156)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 下一步
        points = get_match_points(src_img, button_xiayibu_img)
        if points:
            pos = (2731 - 1927, 641 - 156)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 再次挑战
        points = get_match_points(src_img, button_zaicitiaozhan_img)
        if points:
            pos = (2551 - 1927, 639 - 156)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 关卡重试，点OK
        points = get_match_points(src_img, guanqiachongshi_img)
        if points:
            pos = (2476 - 1927, 516 - 156)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 限定出现，取消
        points = get_match_points(src_img, xiandingchuxian_img)
        if points:
            pos = (2264 - 1927, 518 - 156)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        """
        # 下一步
        points = get_match_points(src_img, button_xiayibu_small_img)
        if points:
            pos = (2731 - 1927, 641 - 156)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 取消
        points = get_match_points(src_img, button_quxiao_img)
        if points:
            pos = (2264 - 1927, 516 - 156)
            randint_x = random.randint(0, 50)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            continue
        """

        waiting_num += 1