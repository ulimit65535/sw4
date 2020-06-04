import random
import time
import cv2
import numpy as np

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points


def fuben(hwnd, x, y, is_leader, skill_order=None):
    if is_leader:
        fuben_jianglibaoxiang_img = cv2.cvtColor(cv2.imread("src/fuben_jianglibaoxiang.png"), cv2.COLOR_BGR2GRAY)
        duihua_any_img = cv2.cvtColor(cv2.imread("src/duihua_any.png"), cv2.COLOR_BGR2GRAY)
        window_kaiqibaoxiang_img = cv2.cvtColor(cv2.imread("src/window_kaiqibaoxiang.png"), cv2.COLOR_BGR2GRAY)
        button_close_img = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.COLOR_BGR2GRAY)
        xuanwumen_zhuzhan_img = cv2.cvtColor(cv2.imread("src/xuanwumen_zhuzhan.png"), cv2.COLOR_BGR2GRAY)
        #duiwu_yincang_img = cv2.cvtColor(cv2.imread("src/duiwu_yincang.png"), cv2.COLOR_BGR2GRAY)
        button_queding_huanjing_img = cv2.cvtColor(cv2.imread("src/button_queding_huanjing.png"), cv2.COLOR_BGR2GRAY)
        xuanwumen_end_img = cv2.cvtColor(cv2.imread("src/xuanwumen_end.png"), cv2.COLOR_BGR2GRAY)
        duihua_zaitingyibian_img = cv2.cvtColor(cv2.imread("src/duihua_zaitingyibian.png"), cv2.COLOR_BGR2GRAY)
        icon_fuben_img_color = cv2.cvtColor(cv2.imread("src/icon_fuben.png"), cv2.IMREAD_COLOR)
        duiwu_zhankai_top_img = cv2.cvtColor(cv2.imread("src/duiwu_zhankai_top.png"), cv2.COLOR_BGR2GRAY)

        lower = np.array([20, 150, 140], dtype="uint8")
        upper = np.array([80, 240, 255], dtype="uint8")

        renwu_fuben_img_color = cv2.cvtColor(cv2.imread("src/renwu_fuben.png"), cv2.IMREAD_COLOR)
        mask = cv2.inRange(renwu_fuben_img_color, lower, upper)
        renwu_fuben_img_color = cv2.bitwise_and(renwu_fuben_img_color, renwu_fuben_img_color, mask=mask)
        renwu_fuben_img = cv2.cvtColor(renwu_fuben_img_color, cv2.COLOR_BGR2GRAY)

        renwu_xuanwumen_img_color = cv2.cvtColor(cv2.imread("src/renwu_xuanwumen.png"), cv2.IMREAD_COLOR)
        mask = cv2.inRange(renwu_xuanwumen_img_color, lower, upper)
        renwu_xuanwumen_img_color = cv2.bitwise_and(renwu_xuanwumen_img_color, renwu_xuanwumen_img_color, mask=mask)
        renwu_xuanwumen_img = cv2.cvtColor(renwu_xuanwumen_img_color, cv2.COLOR_BGR2GRAY)

        taiziyishi_img_color = cv2.cvtColor(cv2.imread("src/taiziyishi.png"), cv2.IMREAD_COLOR)
        mask = cv2.inRange(taiziyishi_img_color, lower, upper)
        taiziyishi_img_color = cv2.bitwise_and(taiziyishi_img_color, taiziyishi_img_color, mask=mask)
        taiziyishi_img = cv2.cvtColor(taiziyishi_img_color, cv2.COLOR_BGR2GRAY)

        #cv2.namedWindow("Image")
        #cv2.imshow("Image", renwu_huoban_img)
        #cv2.waitKey(0)
        #sys.exit(1)

        # 若锁屏，则解锁
        public.jiesuo(hwnd, x, y)

        # 切换挂机技能
        if skill_order is not None:
            public.change_skill(hwnd, x, y, skill_order)
        else:
            time.sleep(2.0)

        num_error = 0
        num_waiting = 0
        while True:
            if num_error >= 5:
                print("错误次数过多，退出")
                return
            if num_waiting >= 5:
                print("副本已完成，退出")
                return

            time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

            src_img = window_capture(hwnd, x, y)

            points = get_match_points(src_img, xuanwumen_end_img, threshold=0.8)
            if points:
                print("副本奖励次数不足，退出。")
                return

            points = get_match_points(src_img, duihua_zaitingyibian_img)
            if points:
                # 展开左端列表
                points = get_match_points(src_img, duiwu_zhankai_top_img)
                if points:
                    pos = points[0]
                    randint_x = random.randint(2, 7)
                    randint_y = random.randint(0, 5)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(1.8, 2.2))
                # 打开日程
                pos = (1947 - 1927, 337 - 156)
                randint_x = random.randint(0, 15)
                randint_y = random.randint(0, 15)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(1.8, 2.2))
                src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
                points = get_match_points(src_img, icon_fuben_img_color, threshold=0.95)
                print(points)
                if not points:
                    # 等待字幕消失
                    time.sleep(random.uniform(2.8, 3.2))
                    src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
                    points = get_match_points(src_img, icon_fuben_img_color, threshold=0.95)
                    print(points)
                    if not points:
                        print("副本已完成")
                        # 关闭日程
                        pos = (2763 - 1927, 183 - 156)
                        randint_x = random.randint(0, 10)
                        randint_y = random.randint(0, 10)
                        window_click(hwnd, pos, randint_x, randint_y)
                        return
                # 关闭日程
                pos = (2763 - 1927, 183 - 156)
                randint_x = random.randint(0, 10)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                # 继续向下匹配，开始副本
                time.sleep(random.uniform(1.8, 2.2))
                src_img = window_capture(hwnd, x, y)

            points = get_match_points(src_img, xuanwumen_zhuzhan_img, threshold=0.8)
            if points:
                time.sleep(random.uniform(1.8, 2.2))
                # 点开地图
                pos = (1997 - 1927, 178 - 156)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.4, 0.6))
                # 点目的地
                pos = (2602 - 1927, 525 - 156)
                randint_x = random.randint(0, 1)
                randint_y = random.randint(0, 1)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.4, 0.6))
                # 关闭地图
                pos = (1997 - 1927, 178 - 156)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(4.8, 5.2))

                src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
                mask = cv2.inRange(src_img, lower, upper)
                src_img = cv2.bitwise_and(src_img, src_img, mask=mask)
                src_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)

                points = get_match_points(src_img, taiziyishi_img, threshold=0.5)
                if points:
                    px, py = points[0]
                    pos = (px + 30, py - 25)
                    randint_x = random.randint(0, 5)
                    randint_y = random.randint(0, 5)
                    window_click(hwnd, pos, randint_x, randint_y)
                    continue
                else:
                    print("未找到太子医师，退出")
                    return

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

            # 点奖励
            points = get_match_points(src_img, fuben_jianglibaoxiang_img)
            if points:
                px, py = points[0]
                pos = (px + 10, py + 10)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                continue
            points = get_match_points(src_img, window_kaiqibaoxiang_img)
            if points:
                px, py = points[0]
                pos = (px + 25, py + 10)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                continue

            points = get_match_points(src_img, button_queding_huanjing_img)
            if points:
                time.sleep(random.uniform(0.8, 1.2))
                pos = points[0]
                randint_x = random.randint(10, 80)
                randint_y = random.randint(5, 20)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(1.8, 2.2))
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, button_queding_huanjing_img)
                if points:
                    time.sleep(random.uniform(0.8, 1.2))
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
                continue

            # 关闭失败对话
            points = get_match_points(src_img, button_close_img)
            if points:
                pos = points[0]
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                continue

            # 是否在移动中?
            src_img = window_capture(hwnd, x, y)
            status = public.get_status(hwnd, x, y, src_img, npc_jiaohu=False, call_pet=True)

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

            points = get_match_points(opponent_img, renwu_fuben_img, threshold=0.7)
            if not points:
                points = get_match_points(opponent_img, renwu_xuanwumen_img, threshold=0.7)
            if points:
                # 点击任务栏任务
                num_waiting = 0
                px, py = points[0]
                # px, py是相对于opponent_img的坐标，所以还要加上left和top
                pos = (px + 770 + 70, py + 140 + 15)
                randint_x = random.randint(0, 20)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                continue
            else:
                num_waiting += 1
    else:
        fuben_jianglibaoxiang_img = cv2.cvtColor(cv2.imread("src/fuben_jianglibaoxiang.png"), cv2.COLOR_BGR2GRAY)
        button_close_img = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.COLOR_BGR2GRAY)
        window_kaiqibaoxiang_img = cv2.cvtColor(cv2.imread("src/window_kaiqibaoxiang.png"), cv2.COLOR_BGR2GRAY)
        button_queding_huanjing_img = cv2.cvtColor(cv2.imread("src/button_queding_huanjing.png"), cv2.COLOR_BGR2GRAY)

        # 若锁屏，则解锁
        public.jiesuo(hwnd, x, y)

        # 切换挂机技能
        if skill_order is not None:
            public.change_skill(hwnd, x, y, skill_order)

        wait_num = 0
        num = 0
        while True:
            time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
            num += 1

            src_img = window_capture(hwnd, x, y)

            # 点奖励
            points = get_match_points(src_img, fuben_jianglibaoxiang_img)
            if points:
                px, py = points[0]
                pos = (px + 10, py + 10)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                continue
            points = get_match_points(src_img, window_kaiqibaoxiang_img)
            if points:
                px, py = points[0]
                pos = (px + 25, py + 10)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                continue

            points = get_match_points(src_img, button_queding_huanjing_img)
            if points:
                time.sleep(random.uniform(0.8, 1.2))
                pos = points[0]
                randint_x = random.randint(10, 80)
                randint_y = random.randint(5, 20)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(1.8, 2.2))
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, button_queding_huanjing_img)
                if points:
                    time.sleep(random.uniform(0.8, 1.2))
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
                continue

            # 关闭失败对话
            points = get_match_points(src_img, button_close_img)
            if points:
                pos = points[0]
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                continue

            # 是否在移动中?
            status = public.get_status(hwnd, x, y, src_img, npc_jiaohu=False, call_pet=True)
            if status == "standing":
                wait_num += 1
            else:
                wait_num = 0

            if wait_num >= 10:
                print("挂机时间过长，退出")
                return

            if num >= 300:
                # 点下任务栏，避免锁屏
                pos = (2863 - 1927, 303 - 193)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                num = 0
