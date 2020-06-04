import random
import time
import cv2
import numpy as np

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points
from lib.wechat import senddata
from . import public


def taolaile(hwnd, x, y):
    duihua_taomeilai_img = cv2.cvtColor(cv2.imread("src/duihua_taomeilai.png"), cv2.COLOR_BGR2GRAY)
    duihua_any_img = cv2.cvtColor(cv2.imread("src/duihua_any.png"), cv2.COLOR_BGR2GRAY)
    duihua_img = cv2.cvtColor(cv2.imread("src/duihua.png"), cv2.COLOR_BGR2GRAY)
    wolaibangni_img = cv2.cvtColor(cv2.imread("src/wolaibangni.png"), cv2.COLOR_BGR2GRAY)
    icon_wupin_img_color = cv2.cvtColor(cv2.imread("src/icon_wupin.png"), cv2.IMREAD_COLOR)
    icon_tao_img = cv2.cvtColor(cv2.imread("src/icon_tao.png"), cv2.COLOR_BGR2GRAY)
    button_shiyong_img = cv2.cvtColor(cv2.imread("src/button_shiyong.png"), cv2.COLOR_BGR2GRAY)
    icon_taozihuizhang_img = cv2.cvtColor(cv2.imread("src/icon_taozihuizhang.png"), cv2.COLOR_BGR2GRAY)
    button_linshi_img = cv2.cvtColor(cv2.imread("src/button_linshi.png"), cv2.COLOR_BGR2GRAY)
    duihua_taolaile_img = cv2.cvtColor(cv2.imread("src/duihua_taolaile.png"), cv2.COLOR_BGR2GRAY)

    lower = np.array([20, 150, 140], dtype="uint8")
    upper = np.array([80, 240, 255], dtype="uint8")

    renwu_taolaile_img_color = cv2.cvtColor(cv2.imread("src/renwu_taolaile.png"), cv2.IMREAD_COLOR)
    mask = cv2.inRange(renwu_taolaile_img_color, lower, upper)
    renwu_taolaile_img_color = cv2.bitwise_and(renwu_taolaile_img_color, renwu_taolaile_img_color, mask=mask)
    renwu_taolaile_img = cv2.cvtColor(renwu_taolaile_img_color, cv2.COLOR_BGR2GRAY)

    # 若锁屏，则解锁
    public.jiesuo(hwnd, x, y)

    has_renwu = False
    while True:
        time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

        src_img = window_capture(hwnd, x, y)

        # 点击对话
        points = get_match_points(src_img, duihua_img, threshold=0.95)
        if points:
            pos = (812, 154)
            randint_x = random.randint(0, 100)
            randint_y = random.randint(0, 30)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 对话，接任务
        points = get_match_points(src_img, duihua_taolaile_img)
        if points:
            px, py = points[0]
            pos = (px + 50, py + 20)
            randint_x = random.randint(0, 80)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 我来帮你
        points = get_match_points(src_img, wolaibangni_img)
        if points:
            pos = points[0]
            randint_x = random.randint(5, 105)
            randint_y = random.randint(5, 15)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 与黄子韬对话
        points = get_match_points(src_img, duihua_any_img)
        if points:
            points = get_match_points(src_img, duihua_taomeilai_img)
            if points:
                # 关闭NPC对话框
                pos = (2856 - 1927, 233 - 193)
                randint_x = random.randint(0, 10)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                print("未能接到桃来了任务")
                return
            else:
                # 接任务
                pos = (2773 - 1927, 219 - 156)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)

                has_renwu = True
                continue

        # 是否在移动中?
        status = public.get_status(hwnd, x, y, src_img, npc_jiaohu=False)

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

        #cv2.namedWindow("Image")
        #cv2.imshow("Image", opponent_img)
        #cv2.waitKey(0)
        #sys.exit(1)

        points = get_match_points(opponent_img, renwu_taolaile_img, threshold=0.7)
        if points:
            has_renwu = True
            # 点击任务栏任务
            px, py = points[0]
            # px, py是相对于opponent_img的坐标，所以还要加上left和top
            pos = (px + 770 + 70, py + 140 + 15)
            randint_x = random.randint(0, 20)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            continue
        else:
            if has_renwu:
                time.sleep(random.uniform(0.8, 1.2))
                src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
                opponent_img = src_img[top:top + h, left:left + w]
                mask = cv2.inRange(opponent_img, lower, upper)
                opponent_img = cv2.bitwise_and(opponent_img, opponent_img, mask=mask)
                opponent_img = cv2.cvtColor(opponent_img, cv2.COLOR_BGR2GRAY)
                points = get_match_points(opponent_img, renwu_taolaile_img, threshold=0.7)
                if points:
                    px, py = points[0]
                    # px, py是相对于opponent_img的坐标，所以还要加上left和top
                    pos = (px + 770 + 70, py + 140 + 15)
                    randint_x = random.randint(0, 20)
                    randint_y = random.randint(0, 10)
                    window_click(hwnd, pos, randint_x, randint_y)
                    continue
                else:
                    # 交桃子，打开背包
                    src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
                    points = get_match_points(src_img, icon_wupin_img_color)
                    if points:
                        pos = points[0]
                        randint_x = random.randint(0, 10)
                        randint_y = random.randint(0, 10)
                        window_click(hwnd, pos, randint_x, randint_y)
                        time.sleep(random.uniform(0.6, 0.8))
                        src_img = window_capture(hwnd, x, y)
                        points = get_match_points(src_img, icon_tao_img)
                        if points:
                            pos = points[0]
                            randint_x = random.randint(10, 20)
                            randint_y = random.randint(10, 20)
                            window_click(hwnd, pos, randint_x, randint_y)
                            time.sleep(random.uniform(0.8, 1.2))
                            src_img = window_capture(hwnd, x, y)
                            points = get_match_points(src_img, button_shiyong_img)
                            if points:
                                pos = points[0]
                                randint_x = random.randint(5, 80)
                                randint_y = random.randint(5, 20)
                                window_click(hwnd, pos, randint_x, randint_y)
                                time.sleep(random.uniform(0.8, 1.2))
                                # 赠送蟠桃,等待字幕消失
                                pos = (2640 - 1927, 484 - 156)
                                randint_x = random.randint(0, 80)
                                randint_y = random.randint(0, 15)
                                window_click(hwnd, pos, randint_x, randint_y)
                                time.sleep(random.uniform(4.4, 4.6))
                                # 选中临时背包
                                src_img = window_capture(hwnd, x, y)
                                points = get_match_points(src_img, button_linshi_img)
                                if points:
                                    pos = points[0]
                                    randint_x = random.randint(10, 30)
                                    randint_y = random.randint(5, 15)
                                    window_click(hwnd, pos, randint_x, randint_y)
                                    time.sleep(random.uniform(0.8, 1.2))
                                src_img = window_capture(hwnd, x, y)
                                points = get_match_points(src_img, icon_taozihuizhang_img, threshold=0.8)
                                if points:
                                    pos = points[0]
                                    randint_x = random.randint(10, 20)
                                    randint_y = random.randint(0, 10)
                                    window_click(hwnd, pos, randint_x, randint_y)
                                    time.sleep(random.uniform(0.8, 1.2))
                                    src_img = window_capture(hwnd, x, y)
                                    points = get_match_points(src_img, button_shiyong_img)
                                    if points:
                                        pos = points[0]
                                        randint_x = random.randint(5, 80)
                                        randint_y = random.randint(5, 20)
                                        window_click(hwnd, pos, randint_x, randint_y)
                                        time.sleep(random.uniform(0.8, 1.2))
                                        # 点抽奖，点关闭
                                        pos = (2482 - 1927, 365 - 156)
                                        randint_x = random.randint(0, 25)
                                        randint_y = random.randint(0, 25)
                                        window_click(hwnd, pos, randint_x, randint_y)
                                        time.sleep(random.uniform(0.8, 1.2))
                                        pos = (2654 - 1927, 232 - 156)
                                        randint_x = random.randint(0, 15)
                                        randint_y = random.randint(0, 15)
                                        window_click(hwnd, pos, randint_x, randint_y)

                    print("桃来了任务结束")
                    return

        # 任务栏没桃来了，去接桃来了
        result = public.open_window_richeng(hwnd, x, y)
        if not result:
            print("未能打开日程窗口")
            return
        pos = (2432 - 1927, 295 - 193)
        randint_x = random.randint(0, 40)
        randint_y = random.randint(0, 40)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(1.4, 1.6))
        # 点开大地图
        pos = (1997 - 1927, 178 - 156)
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.2))
        # 移动到黄子韬的位置
        pos = (2223 - 1927, 307 - 156)
        randint_x = random.randint(0, 10)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.2))
        # 关闭地图
        pos = (2766 - 1927, 169 - 156)
        randint_x = random.randint(0, 10)
        randint_y = random.randint(0, 2)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(2.0, 2.2))