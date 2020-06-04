import random
import time
import cv2
import numpy as np

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points


def shilian(hwnd, x, y, skill_order=None, eat_food=False):
    icon_shilian_img_color = cv2.cvtColor(cv2.imread("src/icon_shilian.png"), cv2.IMREAD_COLOR)
    duihua_jieshoushilian_img = cv2.cvtColor(cv2.imread("src/duihua_jieshoushilian.png"), cv2.COLOR_BGR2GRAY)
    button_xuanze_img = cv2.cvtColor(cv2.imread("src/button_xuanze.png"), cv2.COLOR_BGR2GRAY)
    button_tiaozhan_shilian_img = cv2.cvtColor(cv2.imread("src/button_tiaozhan_shilian.png"), cv2.COLOR_BGR2GRAY)
    quxiaozidong_img = cv2.cvtColor(cv2.imread("src/quxiaozidong.png"), cv2.COLOR_BGR2GRAY)
    zidong_img = cv2.cvtColor(cv2.imread("src/zidong.png"), cv2.COLOR_BGR2GRAY)
    lingqu_huoyue_img = cv2.cvtColor(cv2.imread("src/lingqu_huoyue.png"), cv2.COLOR_BGR2GRAY)
    jineng_huoba_img = cv2.cvtColor(cv2.imread("src/jineng_huoba.png"), cv2.COLOR_BGR2GRAY)
    biaoqing_wenhao_img = cv2.cvtColor(cv2.imread("src/biaoqing_wenhao.png"), cv2.COLOR_BGR2GRAY)
    shilian_baoxiang_img = cv2.cvtColor(cv2.imread("src/shilian_baoxiang.png"), cv2.COLOR_BGR2GRAY)
    shilian_yiyu_img = cv2.cvtColor(cv2.imread("src/shilian_yiyu.png"), cv2.COLOR_BGR2GRAY)
    shilian_ruqinzhe_img = cv2.cvtColor(cv2.imread("src/shilian_ruqinzhe.png"), cv2.COLOR_BGR2GRAY)
    window_zhuanzhuanle_img = cv2.cvtColor(cv2.imread("src/window_zhuanzhuanle.png"), cv2.COLOR_BGR2GRAY)
    button_close_img = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.COLOR_BGR2GRAY)
    tiaoguo_img = cv2.cvtColor(cv2.imread("src/tiaoguo.png"), cv2.COLOR_BGR2GRAY)

    """
    shilian_judian1_img_color = cv2.cvtColor(cv2.imread("src/shilian_judian1.png"), cv2.IMREAD_COLOR)
    shilian_judian2_img_color = cv2.cvtColor(cv2.imread("src/shilian_judian2.png"), cv2.IMREAD_COLOR)
    shilian_judian3_img_color = cv2.cvtColor(cv2.imread("src/shilian_judian3.png"), cv2.IMREAD_COLOR)
    shilian_judian4_img_color = cv2.cvtColor(cv2.imread("src/shilian_judian4.png"), cv2.IMREAD_COLOR)
    shilian_judian5_img_color = cv2.cvtColor(cv2.imread("src/shilian_judian5.png"), cv2.IMREAD_COLOR)
    shilian_judian6_img_color = cv2.cvtColor(cv2.imread("src/shilian_judian6.png"), cv2.IMREAD_COLOR)
    shilian_judian7_img_color = cv2.cvtColor(cv2.imread("src/shilian_judian7.png"), cv2.IMREAD_COLOR)

    shilian_judian_img_list = []
    shilian_judian_img_list.append(shilian_judian1_img_color)
    shilian_judian_img_list.append(shilian_judian2_img_color)
    shilian_judian_img_list.append(shilian_judian3_img_color)
    shilian_judian_img_list.append(shilian_judian4_img_color)
    shilian_judian_img_list.append(shilian_judian5_img_color)
    shilian_judian_img_list.append(shilian_judian6_img_color)
    shilian_judian_img_list.append(shilian_judian7_img_color)
    """

    # 若锁屏，则解锁
    public.jiesuo(hwnd, x, y)

    if eat_food:
        public.eat_food(hwnd, x, y, "shilian")

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
    points = get_match_points(src_img, icon_shilian_img_color, threshold=0.95)
    if not points:
        # 等待字幕消失
        time.sleep(random.uniform(1.8, 2.2))
        src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
        points = get_match_points(src_img, icon_shilian_img_color, threshold=0.95)
        if not points:
            print("英雄试炼任务已完成")
            public.close_window_richeng(hwnd, x, y)
            return

    px, py = points[0]
    pos = (px, py - 36)
    randint_x = random.randint(0, 40)
    randint_y = random.randint(0, 40)
    window_click(hwnd, pos, randint_x, randint_y)
    time.sleep(random.uniform(1.2, 1.4))

    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, duihua_jieshoushilian_img)
    if points:
        px, py = points[0]
        pos = (px + 50, py + 20)
        randint_x = random.randint(0, 80)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(1.8, 2.2))
    else:
        print("进入试炼失败.")
        return

    # 点跳过
    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, tiaoguo_img, threshold=0.8)
    if points:
        pos = points[0]
        randint_x = random.randint(20, 50)
        randint_y = random.randint(10, 20)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(1.8, 2.2))

    # 进入据点
    src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
    pos = None
    judian_num = None
    for i in range(7):
        judian_num = i
        left = 1993 - 1927 + i * 62
        top = 191 - 156
        w = 1
        h = 1
        opponent_img = src_img[top:top + h, left:left + w]
        r = opponent_img[0, 0, 0]
        g = opponent_img[0, 0, 1]
        b = opponent_img[0, 0, 2]

        if r == g == b:
            # 未打过的据点
            pos = (1993 - 1927 + i * 62, 191 - 156)
            break

    if not pos:
        print("未找到未占领据点，退出。")
        return
    randint_x = random.randint(0, 1)
    randint_y = random.randint(0, 1)
    window_click(hwnd, pos, randint_x, randint_y)
    time.sleep(random.uniform(4.8, 5.2))

    # 点屏幕中间的据点
    pos = (2452 - 1927, 453 - 193)
    randint_x = random.randint(0, 5)
    randint_y = random.randint(0, 5)
    window_click(hwnd, pos, randint_x, randint_y)
    time.sleep(random.uniform(1.2, 1.4))

    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, button_xuanze_img)
    if points:
        pos = points[0]
        randint_x = random.randint(10, 80)
        randint_y = random.randint(5, 20)
        window_click(hwnd, pos, randint_x, randint_y)
    else:
        # 可能已经选择过了，点一下最左上角的太阳，取消窗口
        pos = (1948 - 1927, 221 - 193)
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)

    time.sleep(random.uniform(1.2, 1.4))

    if judian_num == 0:
        target_pos_list = [
            # y坐标上移了，所以抓取的时候留意减156而非193
            (2150 - 1927, 544 - 156),
            (2289 - 1927, 591 - 156),
            (2288 - 1927, 451 - 156),
            (2487 - 1927, 565 - 156),
            (2600 - 1927, 448 - 156)
        ]
    elif judian_num == 1:
        target_pos_list = [
            (2246 - 1927, 507 - 193),
            (2597 - 1927, 469 - 193),
            (2702 - 1927, 572 - 193),
            (2338 - 1927, 618 - 193),
            (2642 - 1927, 680 - 193)
        ]
    elif judian_num == 2:
        target_pos_list = [
            (2278 - 1927, 410 - 193),
            (2558 - 1927, 478 - 193),
            (2209 - 1927, 512 - 193),
            (2436 - 1927, 635 - 193),
            (2318 - 1927, 592 - 193)
        ]
    elif judian_num == 3:
        target_pos_list = [
            (2312 - 1927, 404 - 156),
            (2557 - 1927, 332 - 156),
            (2484 - 1927, 572 - 156),
            (2662 - 1927, 483 - 156),
            (2299 - 1927, 521 - 156)
        ]
    elif judian_num == 4:
        target_pos_list = [
            (2240 - 1927, 290 - 156),
            (2545 - 1927, 261 - 156),
            (2736 - 1927, 313 - 156),
            (2205 - 1927, 433 - 156),
            (2343 - 1927, 491 - 156)
        ]
    elif judian_num == 5:
        target_pos_list = [
            (2257 - 1927, 373 - 156),
            (2586 - 1927, 372 - 156),
            (2326 - 1927, 522 - 156),
            (2657 - 1927, 489 - 156),
            (2618 - 1927, 584 - 156)
        ]
    elif judian_num == 6:
        target_pos_list = [
            (2233 - 1927, 424 - 156),
            (2630 - 1927, 440 - 156),
            (2315 - 1927, 536 - 156),
            (2467 - 1927, 622 - 156),
            (2652 - 1927, 545 - 156)
        ]

    for target_pos in target_pos_list:
        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, lingqu_huoyue_img)
        if points:
            # 直接领取活跃
            pos = points[0]
            randint_x = random.randint(5, 50)
            randint_y = random.randint(5, 15)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(3.8, 4.2))

            # 转转乐
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, window_zhuanzhuanle_img, threshold=0.85)
            if points:
                pos = (2272 - 1927, 420 - 156)
                randint_x = random.randint(0, 20)
                randint_y = random.randint(0, 20)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(4.8, 5.2))
                for i in range(10):
                    time.sleep(random.uniform(2.8, 3.2))
                    src_img = window_capture(hwnd, x, y)
                    points = get_match_points(src_img, window_zhuanzhuanle_img, threshold=0.85)
                    if points:
                        # 直接关闭
                        pos = (2735 - 1927, 192 - 156)
                        randint_x = random.randint(0, 10)
                        randint_y = random.randint(0, 10)
                        window_click(hwnd, pos, randint_x, randint_y)
                        continue
                    else:
                        break

        points = get_match_points(src_img, button_close_img)
        if points:
            # 战斗失败，提升窗口，关闭
            pos = points[0]
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.4, 0.6))

        # 点选目标,因为对手可能刷新，故尝试多次
        for i in range(2):
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, zidong_img)
            if points:
                # 已进入战斗
                break
            # 点选目标
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, target_pos, randint_x, randint_y)
            time.sleep(random.uniform(1.6, 1.8))

            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, button_tiaozhan_shilian_img)
            if points:
                pos = points[0]
                randint_x = random.randint(10, 80)
                randint_y = random.randint(5, 20)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(2.2, 2.4))

        while True:
            time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, jineng_huoba_img)
            if points:
                pos_huoba = points[0]
                for i in range(60):
                    time.sleep(random.uniform(0.2, 0.3))
                    src_img = window_capture(hwnd, x, y)
                    left = 0
                    top = 0
                    w = 970
                    h = 400
                    opponent_img = src_img[top:top + h, left:left + w]
                    points = get_match_points(opponent_img, biaoqing_wenhao_img, threshold=0.8)
                    if points:
                        pos_biaoqing = points[0]
                        # 点火把技能
                        randint_x = random.randint(0, 5)
                        randint_y = random.randint(0, 5)
                        window_click(hwnd, pos_huoba, randint_x, randint_y)
                        time.sleep(random.uniform(1.2, 1.4))
                        # 点目标怪物
                        px, py = pos_biaoqing
                        pos = (px - 75, py + 80)
                        randint_x = random.randint(0, 1)
                        randint_y = random.randint(0, 1)
                        window_click(hwnd, pos, randint_x, randint_y)
                        time.sleep(random.uniform(1.2, 1.4))
                        # 点自动战斗
                        pos = (2846 - 1927, 682 - 193)
                        randint_x = random.randint(0, 10)
                        randint_y = random.randint(0, 10)
                        window_click(hwnd, pos, randint_x, randint_y)
                        break

            points = get_match_points(src_img, quxiaozidong_img)
            if points:
                continue
            points = get_match_points(src_img, zidong_img)
            if points:
                pos = points[0]
                randint_x = random.randint(0, 10)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                continue

            # 等待字幕消失，避免出现领取活跃窗口遮挡
            time.sleep(random.uniform(3.8, 4.2))
            break

    # 5次战斗结束
    for i in range(5):
        time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, shilian_baoxiang_img)
        if points:
            pos = points[0]
            randint_x = random.randint(5, 15)
            randint_y = random.randint(5, 15)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(4.8, 5.2))
            break

    if judian_num == 6:
        # 七次完成，领取宝箱
        pos = (1992 - 1927 + 7 * 61, 223 - 193)
        randint_x = random.randint(0, 10)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.2))

    # 是否还有入侵者？
    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, button_close_img)
    if points:
        # 战斗失败，提升窗口，关闭
        pos = points[0]
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.4, 0.6))
        src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, shilian_ruqinzhe_img)
    if points:
        pos = points[0]
        randint_x = random.randint(15, 25)
        randint_y = random.randint(15, 25)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(2.6, 2.8))

        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, button_tiaozhan_shilian_img)
        if points:
            pos = points[0]
            randint_x = random.randint(10, 80)
            randint_y = random.randint(5, 20)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(2.2, 2.4))

            while True:
                time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, jineng_huoba_img)
                if points:
                    pos_huoba = points[0]
                    for i in range(60):
                        time.sleep(random.uniform(0.2, 0.3))
                        src_img = window_capture(hwnd, x, y)
                        left = 0
                        top = 0
                        w = 970
                        h = 400
                        opponent_img = src_img[top:top + h, left:left + w]
                        points = get_match_points(opponent_img, biaoqing_wenhao_img, threshold=0.8)
                        if points:
                            pos_biaoqing = points[0]
                            # 点火把技能
                            randint_x = random.randint(0, 5)
                            randint_y = random.randint(0, 5)
                            window_click(hwnd, pos_huoba, randint_x, randint_y)
                            time.sleep(random.uniform(1.2, 1.4))
                            # 点目标怪物
                            px, py = pos_biaoqing
                            pos = (px - 75, py + 80)
                            randint_x = random.randint(0, 1)
                            randint_y = random.randint(0, 1)
                            window_click(hwnd, pos, randint_x, randint_y)
                            time.sleep(random.uniform(1.2, 1.4))
                            # 点自动战斗
                            pos = (2846 - 1927, 682 - 193)
                            randint_x = random.randint(0, 10)
                            randint_y = random.randint(0, 10)
                            window_click(hwnd, pos, randint_x, randint_y)
                            break

                points = get_match_points(src_img, quxiaozidong_img)
                if points:
                    continue
                points = get_match_points(src_img, zidong_img)
                if points:
                    pos = points[0]
                    randint_x = random.randint(0, 10)
                    randint_y = random.randint(0, 10)
                    window_click(hwnd, pos, randint_x, randint_y)
                    continue
                time.sleep(random.uniform(1.2, 1.4))
                break

    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, shilian_yiyu_img)
    if points:
        pos = points[0]
        randint_x = random.randint(0, 10)
        randint_y = random.randint(5, 15)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(2.6, 2.8))

        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, button_tiaozhan_shilian_img)
        if points:
            pos = points[0]
            randint_x = random.randint(10, 80)
            randint_y = random.randint(5, 20)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(2.2, 2.4))

            while True:
                time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, jineng_huoba_img)
                if points:
                    pos_huoba = points[0]
                    for i in range(60):
                        time.sleep(random.uniform(0.2, 0.3))
                        src_img = window_capture(hwnd, x, y)
                        left = 0
                        top = 0
                        w = 970
                        h = 400
                        opponent_img = src_img[top:top + h, left:left + w]
                        points = get_match_points(opponent_img, biaoqing_wenhao_img, threshold=0.8)
                        if points:
                            pos_biaoqing = points[0]
                            # 点火把技能
                            randint_x = random.randint(0, 5)
                            randint_y = random.randint(0, 5)
                            window_click(hwnd, pos_huoba, randint_x, randint_y)
                            time.sleep(random.uniform(1.2, 1.4))
                            # 点目标怪物
                            px, py = pos_biaoqing
                            pos = (px - 75, py + 80)
                            randint_x = random.randint(0, 1)
                            randint_y = random.randint(0, 1)
                            window_click(hwnd, pos, randint_x, randint_y)
                            time.sleep(random.uniform(1.2, 1.4))
                            # 点自动战斗
                            pos = (2846 - 1927, 682 - 193)
                            randint_x = random.randint(0, 10)
                            randint_y = random.randint(0, 10)
                            window_click(hwnd, pos, randint_x, randint_y)
                            break

                points = get_match_points(src_img, quxiaozidong_img)
                if points:
                    continue
                points = get_match_points(src_img, zidong_img)
                if points:
                    pos = points[0]
                    randint_x = random.randint(0, 10)
                    randint_y = random.randint(0, 10)
                    window_click(hwnd, pos, randint_x, randint_y)
                    continue
                time.sleep(random.uniform(1.2, 1.4))
                break

    # 退出
    time.sleep(random.uniform(4.8, 5.2))
    pos = (2836 - 1927, 649 - 156)
    randint_x = random.randint(0, 5)
    randint_y = random.randint(0, 5)
    window_click(hwnd, pos, randint_x, randint_y)
