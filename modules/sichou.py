import random
import time
import cv2

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points
from lib.wechat import senddata
from . import public


def sichou(hwnd, x, y, eat_food=False):
    icon_sichou_img_color = cv2.cvtColor(cv2.imread("src/icon_sichou.png"), cv2.IMREAD_COLOR)

    kaishizhuanghuo_img = cv2.cvtColor(cv2.imread("src/kaishizhuanghuo.png"), cv2.COLOR_BGR2GRAY)
    button_kaishizhuanghuo_img = cv2.cvtColor(cv2.imread("src/button_kaishizhuanghuo.png"), cv2.COLOR_BGR2GRAY)
    shangchuanhaixudengdai_img = cv2.cvtColor(cv2.imread("src/shangchuanhaixudengdai.png"), cv2.COLOR_BGR2GRAY)
    button_zhuanghuo_img = cv2.cvtColor(cv2.imread("src/button_zhuanghuo.png"), cv2.COLOR_BGR2GRAY)
    sichou_goumai_img = cv2.cvtColor(cv2.imread("src/sichou_goumai.png"), cv2.COLOR_BGR2GRAY)
    button_chufa_img = cv2.cvtColor(cv2.imread("src/button_chufa.png"), cv2.COLOR_BGR2GRAY)
    jiyu_img = cv2.cvtColor(cv2.imread("src/jiyu.png"), cv2.COLOR_BGR2GRAY)
    duihua_jinruwupincangku_img = cv2.cvtColor(cv2.imread("src/duihua_jinruwupincangku.png"), cv2.COLOR_BGR2GRAY)
    window_cangku_img = cv2.cvtColor(cv2.imread("src/window_cangku.png"), cv2.COLOR_BGR2GRAY)
    target_xuqiu_img = cv2.cvtColor(cv2.imread("src/target_xuqiu.png"), cv2.COLOR_BGR2GRAY)

    # 若锁屏，则解锁
    public.jiesuo(hwnd, x, y)

    if eat_food:
        public.eat_food(hwnd, x, y, "sichou")

    num_error = 0
    num_zhuanghuo = 0
    while True:
        if num_error >= 5:
            print("错误次数过多，退出")
            return
        
        time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

        src_img = window_capture(hwnd, x, y)

        if num_zhuanghuo >= 10:
            pos = (2773 - 1927, 217 - 193)
            randint_x = random.randint(0, 15)
            randint_y = random.randint(0, 15)
            window_click(hwnd, pos, randint_x, randint_y)
            print("装货次数过多，退出")
            return

        # 已完成，关闭窗口
        points = get_match_points(src_img, shangchuanhaixudengdai_img)
        if points:
            pos = (2773 - 1927, 217 - 193)
            randint_x = random.randint(0, 15)
            randint_y = random.randint(0, 15)
            window_click(hwnd, pos, randint_x, randint_y)
            print("丝绸之路已完成")
            return

        # 开始装货
        points = get_match_points(src_img, kaishizhuanghuo_img)
        if points:
            num_zhuanghuo = 0
            points = get_match_points(src_img, button_kaishizhuanghuo_img)
            if points:
                pos = points[0]
                randint_x = random.randint(10, 80)
                randint_y = random.randint(5, 20)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(1.4, 1.6))
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, button_kaishizhuanghuo_img)
                if points:
                    # 关闭丝绸窗口
                    pos = (2773 - 1927, 217 - 193)
                    randint_x = random.randint(0, 15)
                    randint_y = random.randint(0, 15)
                    window_click(hwnd, pos, randint_x, randint_y)
                    print("无法领取丝绸任务，退出")
                    return
                # 关闭丝绸窗口
                pos = (2773 - 1927, 217 - 193)
                randint_x = random.randint(0, 15)
                randint_y = random.randint(0, 15)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.8, 1.2))
                # 打开世界地图
                pos = (1965 - 1927, 195 - 156)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.8, 1.2))
                # 去长安
                pos = (2439 - 1927, 527 - 156)
                randint_x = random.randint(0, 10)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(1.4, 1.6))
                # 点开大地图
                pos = (1997 - 1927, 178 - 156)
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.8, 1.2))
                # 移动到仓库的位置
                pos = (2609 - 1927, 472 - 156)
                randint_x = random.randint(0, 10)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(1.8, 2.2))
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, duihua_jinruwupincangku_img)
                if points:
                    px, py = points[0]
                    pos = (px + 50, py + 20)
                    randint_x = random.randint(0, 80)
                    randint_y = random.randint(0, 5)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(1.4, 1.6))
                else:
                    # 关闭地图
                    pos = (1997 - 1927, 178 - 156)
                    randint_x = random.randint(0, 5)
                    randint_y = random.randint(0, 10)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(1.8, 2.2))
                    for i in range(20):
                        time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
                        src_img = window_capture(hwnd, x, y)
                        points = get_match_points(src_img, duihua_jinruwupincangku_img)
                        if points:
                            px, py = points[0]
                            pos = (px + 50, py + 20)
                            randint_x = random.randint(0, 80)
                            randint_y = random.randint(0, 5)
                            window_click(hwnd, pos, randint_x, randint_y)
                            time.sleep(random.uniform(1.4, 1.6))
                            break
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, window_cangku_img)
                if points:
                    # 打开仓库1
                    pos = (2089 - 1927, 618 - 156)
                    randint_x = random.randint(0, 50)
                    randint_y = random.randint(0, 15)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(0.8, 1.2))
                    pos = (2089 - 1927, 388 - 156)
                    randint_x = random.randint(0, 50)
                    randint_y = random.randint(0, 15)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(0.8, 1.2))
                    while True:
                        time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
                        src_img = window_capture(hwnd, x, y)
                        points = get_match_points(src_img, target_xuqiu_img, threshold=0.85)
                        if points:
                            # 双击取出物品
                            pos = points[0]
                            randint_x = random.randint(15, 25)
                            randint_y = random.randint(0, 10)
                            window_click(hwnd, pos, randint_x, randint_y)
                            time.sleep(random.uniform(0.2, 0.3))
                            window_click(hwnd, pos, randint_x, randint_y)
                        else:
                            print("该仓库页无需求物品")
                            break
                    for i in range(3):
                        # 切换仓库
                        pos = (2154 - 1927 + i * 80, 225 - 156)
                        randint_x = random.randint(0, 30)
                        randint_y = random.randint(0, 10)
                        window_click(hwnd, pos, randint_x, randint_y)
                        time.sleep(random.uniform(1.4, 1.6))
                        while True:
                            time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
                            src_img = window_capture(hwnd, x, y)
                            points = get_match_points(src_img, target_xuqiu_img, threshold=0.8)
                            if points:
                                # 双击取出物品
                                pos = points[0]
                                randint_x = random.randint(15, 25)
                                randint_y = random.randint(0, 10)
                                window_click(hwnd, pos, randint_x, randint_y)
                                time.sleep(random.uniform(0.2, 0.3))
                                window_click(hwnd, pos, randint_x, randint_y)
                            else:
                                print("该仓库页无需求物品")
                                break
                    # 关闭仓库
                    pos = (2765 - 1927, 189 - 156)
                    randint_x = random.randint(0, 10)
                    randint_y = random.randint(0, 10)
                    window_click(hwnd, pos, randint_x, randint_y)
                    continue
                else:
                    print("未能打开仓库")
                    return

        # 点第一个去购买
        points = get_match_points(src_img, sichou_goumai_img)
        if points:
            num_zhuanghuo = 0
            pos = points[0]
            randint_x = random.randint(-100, 0)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            continue

        # 给予
        points = get_match_points(src_img, jiyu_img)
        if points:
            pos = (2440 - 1927, 309 - 193)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 30)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.6, 0.8))
            pos = (2504 - 1927, 309 - 193)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 30)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.6, 0.8))
            pos = (2568 - 1927, 309 - 193)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 30)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.6, 0.8))
            pos = points[0]
            randint_x = random.randint(10, 180)
            randint_y = random.randint(10, 30)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.6, 0.8))
            continue

        # 点装货
        points = get_match_points(src_img, button_zhuanghuo_img)
        if points:
            num_zhuanghuo += 1
            pos = points[0]
            randint_x = random.randint(10, 80)
            randint_y = random.randint(5, 20)
            window_click(hwnd, pos, randint_x, randint_y)
            continue
        else:
            points = get_match_points(src_img, button_chufa_img)
            if points:
                num_zhuanghuo = 0
                # 已装完货，点出发
                pos = points[0]
                randint_x = random.randint(10, 80)
                randint_y = random.randint(5, 20)
                window_click(hwnd, pos, randint_x, randint_y)
                continue

        # 是否在移动中?
        status = public.get_status(hwnd, x, y, src_img)

        if status != "standing":
            continue

        result = public.open_window_richeng(hwnd, x, y)
        if not result:
            print("未能打开日程窗口")
            num_error += 1
            continue
        else:
            num_error = 0

        src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
        points = get_match_points(src_img, icon_sichou_img_color, threshold=0.95)
        if not points:
            # 等待字幕消失
            time.sleep(random.uniform(2.8, 3.2))
            src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
            points = get_match_points(src_img, icon_sichou_img_color, threshold=0.95)
            if not points:
                print("丝绸之路已完成")
                public.close_window_richeng(hwnd, x, y)
                return

        num_zhuanghuo = 0
        pos = (2326 - 1927, 294 - 193)
        randint_x = random.randint(0, 40)
        randint_y = random.randint(0, 40)
        window_click(hwnd, pos, randint_x, randint_y)
        continue
