import random
import time
import cv2
import numpy as np

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points


def huoban(hwnd, x, y, skill_order=None):
    huobanrenwu_img_color = cv2.cvtColor(cv2.imread("src/huobanrenwu.png"), cv2.IMREAD_COLOR)
    duihua_lingquhuobanrenwu_img = cv2.cvtColor(cv2.imread("src/duihua_lingquhuobanrenwu.png"), cv2.COLOR_BGR2GRAY)
    lingqurenwu_gold_img_color = cv2.cvtColor(cv2.imread("src/lingqurenwu_gold.png"), cv2.IMREAD_COLOR)
    lingqurenwu_blue_img_color = cv2.cvtColor(cv2.imread("src/lingqurenwu_blue.png"), cv2.IMREAD_COLOR)
    duihua_jinxingrenwu_img = cv2.cvtColor(cv2.imread("src/duihua_jinxingrenwu.png"), cv2.COLOR_BGR2GRAY)
    duihua_jiyuchongwu_img = cv2.cvtColor(cv2.imread("src/duihua_jiyuchongwu.png"), cv2.COLOR_BGR2GRAY)
    duihua_jinruzhandou_img = cv2.cvtColor(cv2.imread("src/duihua_jinruzhandou.png"), cv2.COLOR_BGR2GRAY)
    jinruzhandou_img = cv2.cvtColor(cv2.imread("src/jinruzhandou.png"), cv2.COLOR_BGR2GRAY)
    duihua_img = cv2.cvtColor(cv2.imread("src/duihua.png"), cv2.COLOR_BGR2GRAY)
    duihua_huoban_img = cv2.cvtColor(cv2.imread("src/duihua_huoban.png"), cv2.COLOR_BGR2GRAY)
    duihua_any_img = cv2.cvtColor(cv2.imread("src/duihua_any.png"), cv2.COLOR_BGR2GRAY)

    lower = np.array([20, 150, 140], dtype="uint8")
    upper = np.array([80, 240, 255], dtype="uint8")

    renwu_huoban_img_color = cv2.cvtColor(cv2.imread("src/renwu_huoban.png"), cv2.IMREAD_COLOR)
    mask = cv2.inRange(renwu_huoban_img_color, lower, upper)
    renwu_huoban_img_color = cv2.bitwise_and(renwu_huoban_img_color, renwu_huoban_img_color, mask=mask)
    renwu_huoban_img = cv2.cvtColor(renwu_huoban_img_color, cv2.COLOR_BGR2GRAY)

    #cv2.namedWindow("Image")
    #cv2.imshow("Image", renwu_huoban_img)
    #cv2.waitKey(0)
    #sys.exit(1)

    # 若锁屏，则解锁
    public.jiesuo(hwnd, x, y)

    # 切换挂机技能
    if skill_order is not None:
        public.change_skill(hwnd, x, y, skill_order)

    num_error = 0
    duihua_any_num = 0
    while True:
        if num_error >= 5:
            print("错误次数过多，退出")
            return
        if duihua_any_num >= 10:
            print("未知对话过多，退出")
            return

        time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

        src_img = window_capture(hwnd, x, y)

        # 对话，选“领取伙伴任务”
        points = get_match_points(src_img, duihua_lingquhuobanrenwu_img)
        if points:
            px, py = points[0]
            pos = (px + 50, py + 20)
            randint_x = random.randint(0, 80)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 对话，选进行任务
        points = get_match_points(src_img, duihua_jinxingrenwu_img)
        if points:
            px, py = points[0]
            pos = (px + 50, py + 20)
            randint_x = random.randint(0, 80)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 对话,给予宠物
        points = get_match_points(src_img, duihua_jiyuchongwu_img)
        if points:
            px, py = points[0]
            pos = (px + 50, py + 20)
            randint_x = random.randint(0, 80)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 对话，进入战斗
        points = get_match_points(src_img, duihua_jinruzhandou_img)
        if points:
            px, py = points[0]
            pos = (px + 50, py + 20)
            randint_x = random.randint(0, 80)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 对话，伙伴-
        points = get_match_points(src_img, duihua_huoban_img)
        if points:
            px, py = points[0]
            pos = (px + 50, py + 20)
            randint_x = random.randint(0, 80)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 未知对话，选第一个
        points = get_match_points(src_img, duihua_any_img)
        if points:
            duihua_any_num += 1
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

        # 点击对话
        points = get_match_points(src_img, duihua_img, threshold=0.95)
        if points:
            pos = (812, 154)
            randint_x = random.randint(0, 100)
            randint_y = random.randint(0, 30)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 小BOSS。进入战斗
        points = get_match_points(src_img, jinruzhandou_img,threshold=0.8)
        if points:
            pos = points[0]
            randint_x = random.randint(5, 105)
            randint_y = random.randint(5, 15)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
        # 优先领取金色任务
        points = get_match_points(src_img, lingqurenwu_gold_img_color, threshold=0.95)
        if points:
            duihua_any_num = 0
            pos = points[0]
            randint_x = random.randint(10, 80)
            randint_y = random.randint(5, 20)
            window_click(hwnd, pos, randint_x, randint_y)
            continue
        # 其次领取蓝色任务
        points = get_match_points(src_img, lingqurenwu_blue_img_color, threshold=0.95)
        if points:
            duihua_any_num = 0
            pos = points[0]
            randint_x = random.randint(10, 80)
            randint_y = random.randint(5, 20)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 是否在移动中?
        status = public.get_status(hwnd, x, y)

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

        points = get_match_points(opponent_img, renwu_huoban_img, threshold=0.7)
        if points:
            # 点击任务栏任务
            px, py = points[0]
            # px, py是相对于opponent_img的坐标，所以还要加上left和top
            pos = (px + 770 + 70, py + 140 + 15)
            randint_x = random.randint(0, 20)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        result = public.open_window_richeng(hwnd, x, y)
        if not result:
            print("未能打开日程窗口")
            num_error += 1
            continue
        else:
            num_error = 0

        src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
        points = get_match_points(src_img, huobanrenwu_img_color, threshold=0.95)
        if not points:
            # 等待字幕消失
            time.sleep(random.uniform(2.8, 3.2))
            src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
            points = get_match_points(src_img, huobanrenwu_img_color, threshold=0.95)
            if not points:
                print("伙伴任务已完成")
                public.close_window_richeng(hwnd, x, y)
                return

        # 点前往参加
        pos = points[0]
        randint_x = random.randint(15, 30)
        randint_y = random.randint(68, 78)
        window_click(hwnd, pos, randint_x, randint_y)
        continue
