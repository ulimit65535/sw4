import random
import time
import cv2
import numpy as np

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points
from lib.wechat import senddata


def fengyao(hwnd, x, y, is_leader, skill_order=None, eat_food=False):
    if is_leader:
        yuangu_img_color = cv2.cvtColor(cv2.imread("src/yuangu.png"), cv2.IMREAD_COLOR)
        lower = np.array([24, 160, 180], dtype="uint8")
        upper = np.array([67, 230, 255], dtype="uint8")
        mask = cv2.inRange(yuangu_img_color, lower, upper)
        yuangu_img_color = cv2.bitwise_and(yuangu_img_color, yuangu_img_color, mask=mask)
        yuangu_img = cv2.cvtColor(yuangu_img_color, cv2.COLOR_BGR2GRAY)

        duihua_fengyao_img = cv2.cvtColor(cv2.imread("src/duihua_fengyao.png"), cv2.COLOR_BGR2GRAY)
        duiwu_yincang_img = cv2.cvtColor(cv2.imread("src/duiwu_yincang.png"), cv2.COLOR_BGR2GRAY)
        fengyao_end_img = cv2.cvtColor(cv2.imread("src/fengyao_end.png"), cv2.COLOR_BGR2GRAY)
        yuangu_choice_img = cv2.cvtColor(cv2.imread("src/yuangu_choice.png"), cv2.COLOR_BGR2GRAY)
        button_close_img = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.COLOR_BGR2GRAY)
        fengyao_bielaidarao_img = cv2.cvtColor(cv2.imread("src/fengyao_bielaidarao.png"), cv2.COLOR_BGR2GRAY)

        # 若锁屏，则解锁
        public.jiesuo(hwnd, x, y)

        if eat_food:
            public.eat_food(hwnd, x, y, "fengyao")

        # 切换挂机技能
        if skill_order is not None:
            public.change_skill(hwnd, x, y, skill_order)
        else:
            time.sleep(2.0)

        src_img = window_capture(hwnd, x, y)

        # 隐藏任务列表
        points = get_match_points(src_img, duiwu_yincang_img)
        if points:
            pos = points[0]
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.6, 0.8))

        # 去倒数第二个地图
        result = public.goto_yewai(hwnd, x, y, qumo=True)
        if not result:
            print("前往野外失败,退出")
            return

        has_battle = False
        num_standing = 0
        while True:
            time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

            src_img = window_capture(hwnd, x, y)

            status = public.get_status(hwnd, x, y, src_img, with_standing=False, npc_jiaohu=False)

            if status == "yanzheng_failed":
                senddata("窗口:{}验证失败，退出。".format(hwnd), "")
                return

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

            if has_battle:
                points = get_match_points(src_img, fengyao_end_img, threshold=0.8)
                if points:
                    # 你今天已经很累了
                    print("封妖任务结束，退出")
                    return

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

            points = get_match_points(opponent_img, yuangu_img, threshold=0.5)
            if points:
                # 计数重置
                num = 0
                px, py = points[0]
                # px, py是相对于opponent_img的坐标，所以还要加上left和top
                pos = (px + 151 + 35, py + 115 - 25)
                randint_x = random.randint(0, 2)
                randint_y = random.randint(0, 2)
                window_click(hwnd, pos, randint_x, randint_y)

                has_battle = True

                # 最多等待2.5秒
                for i in range(10):
                    time.sleep(random.uniform(0.2, 0.3))
                    src_img = window_capture(hwnd, x, y)
                    points = get_match_points(src_img, yuangu_choice_img, threshold=0.98)
                    if points:
                        # 怪站一起了，需要选择
                        pos = points[0]
                        randint_x = random.randint(5, 90)
                        randint_y = random.randint(5, 20)
                        window_click(hwnd, pos, randint_x, randint_y)
                        continue
                    points = get_match_points(src_img, duihua_fengyao_img)
                    if points:
                        # 开打
                        pos = (2604 - 1927, 522 - 193)
                        randint_x = random.randint(0, 80)
                        randint_y = random.randint(0, 20)
                        window_click(hwnd, pos, randint_x, randint_y)
                        break

                for i in range(4):
                    time.sleep(random.uniform(0.2, 0.3))
                    src_img = window_capture(hwnd, x, y)
                    points = get_match_points(src_img, fengyao_bielaidarao_img)
                    if points:
                        pos = (2856 - 1927, 233 - 193)
                        randint_x = random.randint(0, 10)
                        randint_y = random.randint(0, 10)
                        window_click(hwnd, pos, randint_x, randint_y)
                        print("进入战斗失败")
                        has_battle = False
                        break
            else:
                has_battle = False
                # 是否在移动中?
                src_img = window_capture(hwnd, x, y)
                status = public.get_status(hwnd, x, y, src_img, npc_jiaohu=False)

                if status == "yanzheng_failed":
                    senddata("窗口:{}验证失败，退出。".format(hwnd), "")
                    return

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
    else:
        # 若锁屏，则解锁
        public.jiesuo(hwnd, x, y)

        if eat_food:
            public.eat_food(hwnd, x, y, "fengyao")

        # 切换挂机技能
        if skill_order is not None:
            public.change_skill(hwnd, x, y, skill_order)

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


def fengyao_unlimited(hwnd, x, y):
    yuangu_img_color = cv2.cvtColor(cv2.imread("src/yuangu.png"), cv2.IMREAD_COLOR)
    lower = np.array([24, 160, 180], dtype="uint8")
    upper = np.array([67, 230, 255], dtype="uint8")
    mask = cv2.inRange(yuangu_img_color, lower, upper)
    yuangu_img_color = cv2.bitwise_and(yuangu_img_color, yuangu_img_color, mask=mask)
    yuangu_img = cv2.cvtColor(yuangu_img_color, cv2.COLOR_BGR2GRAY)

    duihua_fengyao_img = cv2.cvtColor(cv2.imread("src/duihua_fengyao.png"), cv2.COLOR_BGR2GRAY)
    duiwu_yincang_img = cv2.cvtColor(cv2.imread("src/duiwu_yincang.png"), cv2.COLOR_BGR2GRAY)
    #fengyao_end_img = cv2.cvtColor(cv2.imread("src/fengyao_end.png"), cv2.COLOR_BGR2GRAY)
    yuangu_choice_img = cv2.cvtColor(cv2.imread("src/yuangu_choice.png"), cv2.COLOR_BGR2GRAY)
    #button_close_img = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.COLOR_BGR2GRAY)
    fengyao_bielaidarao_img = cv2.cvtColor(cv2.imread("src/fengyao_bielaidarao.png"), cv2.COLOR_BGR2GRAY)

    button_queding_img = cv2.cvtColor(cv2.imread("src/button_queding.png"), cv2.COLOR_BGR2GRAY)

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

        # 继续点香
        points = get_match_points(src_img, button_queding_img)
        if points:
            pos = points[0]
            randint_x = random.randint(10, 80)
            randint_y = random.randint(5, 20)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(1.8, 2.2))
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

        points = get_match_points(opponent_img, yuangu_img, threshold=0.4)
        if points:
            # 计数重置
            num = 0
            px, py = points[0]
            # px, py是相对于opponent_img的坐标，所以还要加上left和top
            pos = (px + 151 + 35, py + 115 - 25)
            randint_x = random.randint(0, 2)
            randint_y = random.randint(0, 2)
            window_click(hwnd, pos, randint_x, randint_y)

            # 最多等待2.5秒
            for i in range(10):
                time.sleep(random.uniform(0.2, 0.3))
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, yuangu_choice_img, threshold=0.98)
                if points:
                    # 怪站一起了，需要选择
                    pos = points[0]
                    randint_x = random.randint(5, 90)
                    randint_y = random.randint(5, 20)
                    window_click(hwnd, pos, randint_x, randint_y)
                    continue
                points = get_match_points(src_img, duihua_fengyao_img)
                if points:
                    # 开打
                    pos = (2604 - 1927, 522 - 193)
                    randint_x = random.randint(0, 80)
                    randint_y = random.randint(0, 20)
                    window_click(hwnd, pos, randint_x, randint_y)
                    break

            for i in range(4):
                time.sleep(random.uniform(0.2, 0.3))
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, fengyao_bielaidarao_img)
                if points:
                    pos = (2856 - 1927, 233 - 193)
                    randint_x = random.randint(0, 10)
                    randint_y = random.randint(0, 10)
                    window_click(hwnd, pos, randint_x, randint_y)
                    print("进入战斗失败")
                    break
        else:
            # 是否在移动中?
            src_img = window_capture(hwnd, x, y)
            status = public.get_status(hwnd, x, y, src_img, npc_jiaohu=False)
            
            if status == "yanzheng_failed":
                senddata("窗口:{}验证失败，退出。".format(hwnd), "")
                return

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