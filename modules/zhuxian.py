import random
import time
import cv2
import numpy as np

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points


def zhuxian(hwnd, x, y):
    duihua_img = cv2.cvtColor(cv2.imread("src/duihua.png"), cv2.COLOR_BGR2GRAY)
    duihua_any_img = cv2.cvtColor(cv2.imread("src/duihua_any.png"), cv2.COLOR_BGR2GRAY)
    choice_any_img = cv2.cvtColor(cv2.imread("src/choice_any.png"), cv2.COLOR_BGR2GRAY)
    tiaoguo_img = cv2.cvtColor(cv2.imread("src/tiaoguo.png"), cv2.COLOR_BGR2GRAY)
    button_yijianxuexi_img = cv2.cvtColor(cv2.imread("src/button_yijianxuexi.png"), cv2.COLOR_BGR2GRAY)
    close_shouchong_img = cv2.cvtColor(cv2.imread("src/close_shouchong.png"), cv2.COLOR_BGR2GRAY)
    qitian_close_img = cv2.cvtColor(cv2.imread("src/qitian_close.png"), cv2.COLOR_BGR2GRAY)
    button_qianwang_img = cv2.cvtColor(cv2.imread("src/button_qianwang.png"), cv2.COLOR_BGR2GRAY)

    lower = np.array([20, 150, 140], dtype="uint8")
    upper = np.array([80, 240, 255], dtype="uint8")

    renwu_zhuxian_img_color = cv2.cvtColor(cv2.imread("src/renwu_zhuxian.png"), cv2.IMREAD_COLOR)
    mask = cv2.inRange(renwu_zhuxian_img_color, lower, upper)
    renwu_zhuxian_img_color = cv2.bitwise_and(renwu_zhuxian_img_color, renwu_zhuxian_img_color, mask=mask)
    renwu_zhuxian_img = cv2.cvtColor(renwu_zhuxian_img_color, cv2.COLOR_BGR2GRAY)

    renwu_yindao_img_color = cv2.cvtColor(cv2.imread("src/renwu_yindao.png"), cv2.IMREAD_COLOR)
    mask = cv2.inRange(renwu_yindao_img_color, lower, upper)
    renwu_yindao_img_color = cv2.bitwise_and(renwu_yindao_img_color, renwu_yindao_img_color, mask=mask)
    renwu_yindao_img = cv2.cvtColor(renwu_yindao_img_color, cv2.COLOR_BGR2GRAY)

    renwu_shimen_img_color = cv2.cvtColor(cv2.imread("src/renwu_shimen.png"), cv2.IMREAD_COLOR)
    mask = cv2.inRange(renwu_shimen_img_color, lower, upper)
    renwu_shimen_img_color = cv2.bitwise_and(renwu_shimen_img_color, renwu_shimen_img_color, mask=mask)
    renwu_shimen_img = cv2.cvtColor(renwu_shimen_img_color, cv2.COLOR_BGR2GRAY)

    #cv2.namedWindow("Image")
    #cv2.imshow("Image", renwu_huoban_img)
    #cv2.waitKey(0)
    #sys.exit(1)

    # 若锁屏，则解锁
    public.jiesuo(hwnd, x, y)

    while True:

        time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

        src_img = window_capture(hwnd, x, y)

        # 未知选项，选第一个
        points = get_match_points(src_img, choice_any_img)
        if points:
            min_y = 1000
            for point in points:
                x, y = point
                if y < min_y:
                    pos_choice = point
                    min_y = y

            randint_x = random.randint(5, 25)
            randint_y = random.randint(5, 15)
            window_click(hwnd, pos_choice, randint_x, randint_y)
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

        # 点一键学习
        points = get_match_points(src_img, button_yijianxuexi_img)
        if points:
            pos = points[0]
            randint_x = random.randint(20, 50)
            randint_y = random.randint(5, 15)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 点前往
        points = get_match_points(src_img, button_qianwang_img)
        if points:
            pos = points[0]
            randint_x = random.randint(20, 50)
            randint_y = random.randint(5, 15)
            window_click(hwnd, pos, randint_x, randint_y)
            print("20级，结束主线。")
            return

        # 关闭首充
        points = get_match_points(src_img, close_shouchong_img)
        if points:
            pos = points[0]
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 7天奖励，关闭
        points = get_match_points(src_img, qitian_close_img)
        if points:
            pos = points[0]
            randint_x = random.randint(2, 7)
            randint_y = random.randint(5, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 点跳过
        points = get_match_points(src_img, tiaoguo_img, threshold=0.8)
        if points:
            pos = points[0]
            randint_x = random.randint(20, 50)
            randint_y = random.randint(10, 20)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 点击对话
        points = get_match_points(src_img, duihua_img, threshold=0.95)
        if points:
            pos = (812, 154)
            randint_x = random.randint(0, 100)
            randint_y = random.randint(0, 30)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 是否在移动中?
        status = public.get_status(hwnd, x, y, src_img)

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

        points = get_match_points(opponent_img, renwu_shimen_img, threshold=0.7)
        if points:
            # 点击任务栏任务
            px, py = points[0]
            # px, py是相对于opponent_img的坐标，所以还要加上left和top
            pos = (px + 770 + 70, py + 140 + 15)
            randint_x = random.randint(0, 20)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        points = get_match_points(opponent_img, renwu_yindao_img, threshold=0.7)
        if points:
            # 点击任务栏任务
            px, py = points[0]
            # px, py是相对于opponent_img的坐标，所以还要加上left和top
            pos = (px + 770 + 70, py + 140 + 15)
            randint_x = random.randint(0, 20)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        points = get_match_points(opponent_img, renwu_zhuxian_img, threshold=0.7)
        if points:
            # 点击任务栏任务
            px, py = points[0]
            # px, py是相对于opponent_img的坐标，所以还要加上left和top
            pos = (px + 770 + 70, py + 140 + 15)
            randint_x = random.randint(0, 20)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            continue
