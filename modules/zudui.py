import random
import time
import cv2

from . import public

import sys
sys.path.append('../')
from etc import settings
from lib.functions import window_click, window_capture, get_match_points

# 邀请界面等待刷新时间
waiting_for_refresh = 1.2


def zudui(hwnd, x, y, is_leader, member_waiting=50):
    if is_leader:
        #duiwu_zhankai_img = cv2.cvtColor(cv2.imread("src/duiwu_zhankai.png"), cv2.COLOR_BGR2GRAY)
        button_renwu_img = cv2.cvtColor(cv2.imread("src/button_renwu.png"), cv2.COLOR_BGR2GRAY)
        chuangjianduiwu_img = cv2.cvtColor(cv2.imread("src/chuangjianduiwu.png"), cv2.COLOR_BGR2GRAY)
        likaiduiwu_img = cv2.cvtColor(cv2.imread("src/likaiduiwu.png"), cv2.COLOR_BGR2GRAY)
        button_yaoqing_img = cv2.cvtColor(cv2.imread("src/button_yaoqing.png"), cv2.COLOR_BGR2GRAY)
        button_close_img = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.COLOR_BGR2GRAY)
        member1_img = cv2.cvtColor(cv2.imread("src/replace/member1.png"), cv2.COLOR_BGR2GRAY)
        member2_img = cv2.cvtColor(cv2.imread("src/replace/member2.png"), cv2.COLOR_BGR2GRAY)
        member3_img = cv2.cvtColor(cv2.imread("src/replace/member3.png"), cv2.COLOR_BGR2GRAY)
        member4_img = cv2.cvtColor(cv2.imread("src/replace/member4.png"), cv2.COLOR_BGR2GRAY)
        xinxi_close_img = cv2.cvtColor(cv2.imread("src/xinxi_close.png"), cv2.COLOR_BGR2GRAY)

        # 若锁屏，则解锁
        public.jiesuo(hwnd, x, y)

        src_img = window_capture(hwnd, x, y)

        points = get_match_points(src_img, button_close_img)
        if points:
            # 误点到战备，或者NPC对话，关闭
            pos = points[0]
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.5, 0.6))
            src_img = window_capture(hwnd, x, y)

        points = get_match_points(src_img, button_renwu_img, threshold=0.8)
        if not points:
            # 展开任务列表
            pos = (2863 - 1927, 303 - 193)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.6, 0.8))

        # 打开队伍界面
        pos = (2800 - 1927, 265 - 156)
        randint_x = random.randint(0, 20)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.0))

        src_img = window_capture(hwnd, x, y)

        # 如果已在队伍中，离开队伍
        points = get_match_points(src_img, likaiduiwu_img)
        if points:
            # 让队友先离队
            time.sleep(random.uniform(2.8, 3.2))
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, likaiduiwu_img)
            if points:
                # 如果未能离开，则离开队伍
                pos = points[0]
                randint_x = random.randint(25, 60)
                randint_y = random.randint(-10, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.8, 1.0))
            # 关闭队伍窗口
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, xinxi_close_img, threshold=0.8)
            if points:
                pos = points[0]
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.5, 0.6))
                pos = (2725 - 1927, 270 - 156)
                randint_x = random.randint(0, 10)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
            return

        points = get_match_points(src_img, chuangjianduiwu_img)
        if points:
            pos = points[0]
            randint_x = random.randint(25, 60)
            randint_y = random.randint(-10, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.8, 1.2))
            has_invite = False
            # 邀请队员
            pos = (2137 - 1927, 392 - 193)
            randint_x = random.randint(0, 50)
            randint_y = random.randint(0, 20)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(1.4, 1.6))
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, button_yaoqing_img)
            if points:
                has_invite = True
                # # 合区后卡，多等待一断时间
                time.sleep(waiting_for_refresh)
                src_img = window_capture(hwnd, x, y)
                points1 = get_match_points(src_img, member1_img, threshold=0.85)
                points2 = get_match_points(src_img, member2_img, threshold=0.85)
                points3 = get_match_points(src_img, member3_img, threshold=0.85)
                points4 = get_match_points(src_img, member4_img, threshold=0.85)
                if points1:
                    px, py = points1[0]
                    pos = (px + 95, py + 13)
                    randint_x = random.randint(0, 40)
                    randint_y = random.randint(0, 20)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(0.1, 0.15))
                if points3:
                    px, py = points3[0]
                    pos = (px + 95, py + 13)
                    randint_x = random.randint(0, 40)
                    randint_y = random.randint(0, 20)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(0.1, 0.15))
                if points4:
                    points_before = []
                    for px, py in points4:
                        is_exist = False
                        for point_before in points_before:
                            px_before, py_before = point_before
                            if abs(px - px_before) <= 10 and abs(py - py_before) <= 10:
                                is_exist = True
                                break
                        if not is_exist:
                            points_before.append((px, py))
                            pos = (px + 95, py + 13)
                            randint_x = random.randint(0, 40)
                            randint_y = random.randint(0, 20)
                            window_click(hwnd, pos, randint_x, randint_y)
                            time.sleep(random.uniform(0.1, 0.15))
                if points2:
                    if points3 or points4:
                        # 保证第三个大号，最后一个进队.龙阵五号位
                        time.sleep(random.uniform(1.8, 2.2))
                    px, py = points2[0]
                    pos = (px + 95, py + 13)
                    randint_x = random.randint(0, 40)
                    randint_y = random.randint(0, 20)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(0.1, 0.15))

                time.sleep(random.uniform(0.2, 0.3))
                # 关闭邀请窗口
                pos = (2639 - 1927, 294 - 193)
                randint_x = random.randint(0, 15)
                randint_y = random.randint(0, 15)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.5, 0.6))

                if settings.zudui_zhenfa_num > 0:
                    # 切换到阵法选择
                    pos = (2668 - 1927, 225 - 156)
                    randint_x = random.randint(0, 50)
                    randint_y = random.randint(0, 15)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(0.5, 0.6))
                    # 切换到对应阵法
                    pos = (2687 - 1927, 297 - 156 + 34 * settings.zudui_zhenfa_num)
                    randint_x = random.randint(0, 50)
                    randint_y = random.randint(0, 15)
                    window_click(hwnd, pos, randint_x, randint_y)
                    """
                    time.sleep(random.uniform(1.8, 2.2))
                    # 龙飞阵调位置
                    pos = (2550 - 1927, 480 - 156)
                    randint_x = random.randint(0, 5)
                    randint_y = random.randint(0, 5)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(0.4, 0.5))
                    pos = (2605 - 1927, 401 - 156)
                    randint_x = random.randint(0, 5)
                    randint_y = random.randint(0, 5)
                    window_click(hwnd, pos, randint_x, randint_y)
                    """
                    time.sleep(random.uniform(0.8, 0.9))
            else:
                # 关闭邀请窗口
                pos = (2639 - 1927, 294 - 193)
                randint_x = random.randint(0, 15)
                randint_y = random.randint(0, 15)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.5, 0.6))

            if not has_invite:
                # 未邀请到任何队员，退出队伍
                pos = (2091 - 1927, 217 - 156)
                randint_x = random.randint(25, 60)
                randint_y = random.randint(5, 15)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.8, 1.0))

            # 关闭队伍窗口
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, xinxi_close_img, threshold=0.8)
            if points:
                pos = points[0]
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.5, 0.6))
                pos = (2725 - 1927, 270 - 156)
                randint_x = random.randint(0, 10)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
            return

        # 既不是离开，也不是创建.等待优化
        print("大喇叭干扰，无法创建队伍")
        return
    else:
        #duiwu_zhankai_img = cv2.cvtColor(cv2.imread("src/duiwu_zhankai.png"), cv2.COLOR_BGR2GRAY)
        button_renwu_img = cv2.cvtColor(cv2.imread("src/button_renwu.png"), cv2.COLOR_BGR2GRAY)
        likaiduiwu_img = cv2.cvtColor(cv2.imread("src/likaiduiwu.png"), cv2.COLOR_BGR2GRAY)
        guidui_img = cv2.cvtColor(cv2.imread("src/guidui.png"), cv2.COLOR_BGR2GRAY)
        leader_img = cv2.cvtColor(cv2.imread("src/replace/leader.png"), cv2.COLOR_BGR2GRAY)
        button_close_img = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.COLOR_BGR2GRAY)
        xinxi_close_img = cv2.cvtColor(cv2.imread("src/xinxi_close.png"), cv2.COLOR_BGR2GRAY)

        # 若锁屏，则解锁
        public.jiesuo(hwnd, x, y)

        src_img = window_capture(hwnd, x, y)

        points = get_match_points(src_img, button_close_img)
        if points:
            # 误点到战备，或者NPC对话，关闭
            pos = points[0]
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.5, 0.6))
            src_img = window_capture(hwnd, x, y)

        points = get_match_points(src_img, button_renwu_img, threshold=0.8)
        if not points:
            # 展开任务列表
            pos = (2863 - 1927, 303 - 193)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.6, 0.8))

        # 打开队伍界面
        pos = (2800 - 1927, 265 - 156)
        randint_x = random.randint(0, 20)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.0))

        src_img = window_capture(hwnd, x, y)

        # 如果已在队伍中，离开队伍
        points = get_match_points(src_img, likaiduiwu_img)
        if points:
            pos = points[0]
            randint_x = random.randint(25, 60)
            randint_y = random.randint(-10, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.8, 1.0))
            # 关闭队伍窗口
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, xinxi_close_img, threshold=0.8)
            if points:
                pos = points[0]
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.5, 0.6))
                pos = (2725 - 1927, 270 - 156)
                randint_x = random.randint(0, 10)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
            return

        # 点队伍信息
        pos = (2566 - 1927, 259 - 193)
        randint_x = random.randint(0, 50)
        randint_y = random.randint(0, 20)
        window_click(hwnd, pos, randint_x, randint_y)

        for i in range(member_waiting):
            time.sleep(0.2)
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, leader_img)
            if points:
                px, py = points[0]
                pos = (px + 95, py + 11)
                randint_x = random.randint(5, 50)
                randint_y = random.randint(5, 20)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(1.0, 1.2))
                # 如需归队，归队
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, guidui_img)
                if points:
                    pos = points[0]
                    randint_x = random.randint(5, 70)
                    randint_y = random.randint(5, 20)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(0.8, 1.0))
                break

        # 关闭队伍窗口
        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, xinxi_close_img, threshold=0.8)
        if points:
            pos = points[0]
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.5, 0.6))
            pos = (2725 - 1927, 270 - 156)
            randint_x = random.randint(0, 10)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
        return


def leave(hwnd, x, y, is_leader):
    #duiwu_zhankai_img = cv2.cvtColor(cv2.imread("src/duiwu_zhankai.png"), cv2.COLOR_BGR2GRAY)
    button_renwu_img = cv2.cvtColor(cv2.imread("src/button_renwu.png"), cv2.COLOR_BGR2GRAY)
    chuangjianduiwu_img = cv2.cvtColor(cv2.imread("src/chuangjianduiwu.png"), cv2.COLOR_BGR2GRAY)
    button_close_img = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.COLOR_BGR2GRAY)
    xinxi_close_img = cv2.cvtColor(cv2.imread("src/xinxi_close.png"), cv2.COLOR_BGR2GRAY)

    # 若锁屏，则解锁
    public.jiesuo(hwnd, x, y)

    src_img = window_capture(hwnd, x, y)

    points = get_match_points(src_img, button_close_img)
    if points:
        # 误点到战备，或者NPC对话，关闭
        pos = points[0]
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.5, 0.6))
        src_img = window_capture(hwnd, x, y)

    points = get_match_points(src_img, button_renwu_img, threshold=0.8)
    if not points:
        # 展开任务列表
        pos = (2863 - 1927, 303 - 193)
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.6, 0.8))

    # 打开队伍界面
    pos = (2800 - 1927, 265 - 156)
    randint_x = random.randint(0, 20)
    randint_y = random.randint(0, 10)
    window_click(hwnd, pos, randint_x, randint_y)
    time.sleep(random.uniform(0.8, 1.0))

    src_img = window_capture(hwnd, x, y)

    if is_leader:
        # 如果已在队伍中，离开队伍
        points = get_match_points(src_img, chuangjianduiwu_img)
        if not points:
            # 让队友先离队
            time.sleep(random.uniform(2.8, 3.2))
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, chuangjianduiwu_img)
            if not points:
                # 如果未能离开，则离开队伍
                pos = (2091 - 1927, 217 - 156)
                randint_x = random.randint(25, 60)
                randint_y = random.randint(5, 15)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.8, 1.0))
            # 关闭队伍窗口
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, xinxi_close_img, threshold=0.8)
            if points:
                pos = points[0]
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.5, 0.6))
                pos = (2725 - 1927, 270 - 156)
                randint_x = random.randint(0, 10)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
        return
    else:
        # 找不到创建队伍按键，直接点离开队伍，避免喇叭干扰
        points = get_match_points(src_img, chuangjianduiwu_img)
        if not points:
            pos = (2091 - 1927, 217 - 156)
            randint_x = random.randint(25, 60)
            randint_y = random.randint(5, 15)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.8, 1.0))
            # 关闭队伍窗口
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, xinxi_close_img, threshold=0.8)
            if points:
                pos = points[0]
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.5, 0.6))
                pos = (2725 - 1927, 270 - 156)
                randint_x = random.randint(0, 10)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
        return


def join(hwnd, x, y, is_leader, member_waiting=80):
    if is_leader:
        # duiwu_zhankai_img = cv2.cvtColor(cv2.imread("src/duiwu_zhankai.png"), cv2.COLOR_BGR2GRAY)
        button_renwu_img = cv2.cvtColor(cv2.imread("src/button_renwu.png"), cv2.COLOR_BGR2GRAY)
        chuangjianduiwu_img = cv2.cvtColor(cv2.imread("src/chuangjianduiwu.png"), cv2.COLOR_BGR2GRAY)
        button_yaoqing_img = cv2.cvtColor(cv2.imread("src/button_yaoqing.png"), cv2.COLOR_BGR2GRAY)
        member1_img = cv2.cvtColor(cv2.imread("src/replace/member1.png"), cv2.COLOR_BGR2GRAY)
        member2_img = cv2.cvtColor(cv2.imread("src/replace/member2.png"), cv2.COLOR_BGR2GRAY)
        member3_img = cv2.cvtColor(cv2.imread("src/replace/member3.png"), cv2.COLOR_BGR2GRAY)
        member4_img = cv2.cvtColor(cv2.imread("src/replace/member4.png"), cv2.COLOR_BGR2GRAY)
        button_close_img = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.COLOR_BGR2GRAY)
        xinxi_close_img = cv2.cvtColor(cv2.imread("src/xinxi_close.png"), cv2.COLOR_BGR2GRAY)
        icon_member_invite_img = cv2.cvtColor(cv2.imread("src/icon_member_invite.png"), cv2.COLOR_BGR2GRAY)

        # 若锁屏，则解锁
        public.jiesuo(hwnd, x, y)

        src_img = window_capture(hwnd, x, y)

        points = get_match_points(src_img, button_close_img)
        if points:
            # 误点到战备，或者NPC对话，关闭
            pos = points[0]
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.5, 0.6))
            src_img = window_capture(hwnd, x, y)

        points = get_match_points(src_img, button_renwu_img, threshold=0.8)
        if not points:
            # 展开任务列表
            pos = (2863 - 1927, 303 - 193)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.6, 0.8))

        # 打开队伍界面
        pos = (2800 - 1927, 265 - 156)
        randint_x = random.randint(0, 20)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.0))

        src_img = window_capture(hwnd, x, y)

        points = get_match_points(src_img, chuangjianduiwu_img)
        if points:
            pos = points[0]
            randint_x = random.randint(25, 60)
            randint_y = random.randint(-10, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.8, 1.2))
            has_invite = False
            # 邀请队员
            pos = (2137 - 1927, 392 - 193)
            randint_x = random.randint(0, 50)
            randint_y = random.randint(0, 20)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(1.4, 1.6))
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, button_yaoqing_img)
            if points:
                has_invite = True
                # # 合区后卡，多等待一断时间
                time.sleep(waiting_for_refresh * 2)
                src_img = window_capture(hwnd, x, y)
                points1 = get_match_points(src_img, member1_img, threshold=0.85)
                points2 = get_match_points(src_img, member2_img, threshold=0.85)
                points3 = get_match_points(src_img, member3_img, threshold=0.85)
                points4 = get_match_points(src_img, member4_img, threshold=0.85)
                if points1:
                    px, py = points1[0]
                    pos = (px + 95, py + 13)
                    randint_x = random.randint(0, 40)
                    randint_y = random.randint(0, 20)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(0.1, 0.15))
                if points3:
                    px, py = points3[0]
                    pos = (px + 95, py + 13)
                    randint_x = random.randint(0, 40)
                    randint_y = random.randint(0, 20)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(0.1, 0.15))
                if points4:
                    points_before = []
                    for px, py in points4:
                        is_exist = False
                        for point_before in points_before:
                            px_before, py_before = point_before
                            if abs(px - px_before) <= 10 and abs(py - py_before) <= 10:
                                is_exist = True
                                break
                        if not is_exist:
                            points_before.append((px, py))
                            pos = (px + 95, py + 13)
                            randint_x = random.randint(0, 40)
                            randint_y = random.randint(0, 20)
                            window_click(hwnd, pos, randint_x, randint_y)
                            time.sleep(random.uniform(0.1, 0.15))
                if points2:
                    if points3 or points4:
                        # 保证第三个大号，最后一个进队.龙阵五号位
                        time.sleep(random.uniform(2.8, 3.2))
                    px, py = points2[0]
                    pos = (px + 95, py + 13)
                    randint_x = random.randint(0, 40)
                    randint_y = random.randint(0, 20)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(0.1, 0.15))
                time.sleep(random.uniform(0.2, 0.3))
                # 关闭邀请窗口
                pos = (2639 - 1927, 294 - 193)
                randint_x = random.randint(0, 15)
                randint_y = random.randint(0, 15)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.5, 0.6))

                if settings.zudui_zhenfa_num > 0:
                    # 切换到阵法选择
                    pos = (2668 - 1927, 225 - 156)
                    randint_x = random.randint(0, 50)
                    randint_y = random.randint(0, 15)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(0.5, 0.6))
                    # 切换到对应阵法
                    pos = (2687 - 1927, 297 - 156 + 34 * settings.zudui_zhenfa_num)
                    randint_x = random.randint(0, 50)
                    randint_y = random.randint(0, 15)
                    window_click(hwnd, pos, randint_x, randint_y)
                    """
                    # 跨服等待时间
                    time.sleep(random.uniform(2.8, 3.2))
                    # 龙飞阵调位置
                    pos = (2550 - 1927, 480 - 156)
                    randint_x = random.randint(0, 5)
                    randint_y = random.randint(0, 5)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(0.4, 0.5))
                    pos = (2605 - 1927, 401 - 156)
                    randint_x = random.randint(0, 5)
                    randint_y = random.randint(0, 5)
                    window_click(hwnd, pos, randint_x, randint_y)
                    """
                    time.sleep(random.uniform(1.4, 1.6))
            else:
                # 关闭邀请窗口
                pos = (2639 - 1927, 294 - 193)
                randint_x = random.randint(0, 15)
                randint_y = random.randint(0, 15)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.5, 0.6))

            if not has_invite:
                # 未邀请到任何队员，退出队伍
                pos = (2091 - 1927, 217 - 156)
                randint_x = random.randint(25, 60)
                randint_y = random.randint(5, 15)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.8, 1.0))
        else:
            print("已在队伍中，无需创建队伍.")
            time.sleep(random.uniform(0.5, 0.6))

        # 关闭队伍窗口
        src_img = window_capture(hwnd, x, y)

        # 查看队伍中的人数
        points = get_match_points(src_img, icon_member_invite_img)
        team_num = 0
        if points:
            x, y = points[0]
            if y < 374 - 156:
                team_num = 1
            elif y < 453 - 156:
                team_num = 2
            elif y < 532 - 156:
                team_num = 3
            else:
                team_num = 4
        else:
            team_num = 5

        points = get_match_points(src_img, xinxi_close_img, threshold=0.8)
        if points:
            pos = points[0]
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.5, 0.6))
            pos = (2725 - 1927, 270 - 156)
            randint_x = random.randint(0, 10)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
        return team_num
    else:
        #duiwu_zhankai_img = cv2.cvtColor(cv2.imread("src/duiwu_zhankai.png"), cv2.COLOR_BGR2GRAY)
        guidui_img = cv2.cvtColor(cv2.imread("src/guidui.png"), cv2.COLOR_BGR2GRAY)
        likaiduiwu_img = cv2.cvtColor(cv2.imread("src/likaiduiwu.png"), cv2.COLOR_BGR2GRAY)
        leader_img = cv2.cvtColor(cv2.imread("src/replace/leader.png"), cv2.COLOR_BGR2GRAY)
        button_close_img = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.COLOR_BGR2GRAY)
        xinxi_close_img = cv2.cvtColor(cv2.imread("src/xinxi_close.png"), cv2.COLOR_BGR2GRAY)
        button_renwu_img = cv2.cvtColor(cv2.imread("src/button_renwu.png"), cv2.COLOR_BGR2GRAY)

        # 若锁屏，则解锁
        public.jiesuo(hwnd, x, y)

        src_img = window_capture(hwnd, x, y)

        points = get_match_points(src_img, button_close_img)
        if points:
            # 误点到战备，或者NPC对话，关闭
            pos = points[0]
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.5, 0.6))
            src_img = window_capture(hwnd, x, y)

        points = get_match_points(src_img, button_renwu_img, threshold=0.8)
        if not points:
            # 展开任务列表
            pos = (2863 - 1927, 303 - 193)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.6, 0.8))

        # 打开队伍界面
        pos = (2800 - 1927, 265 - 156)
        randint_x = random.randint(0, 20)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.0))

        src_img = window_capture(hwnd, x, y)

        # 如果已在队伍中，离开队伍
        points = get_match_points(src_img, likaiduiwu_img)
        if not points:
            # 点队伍信息
            pos = (2566 - 1927, 259 - 193)
            randint_x = random.randint(0, 50)
            randint_y = random.randint(0, 20)
            window_click(hwnd, pos, randint_x, randint_y)

            for i in range(member_waiting):
                time.sleep(0.2)
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, leader_img)
                if points:
                    px, py = points[0]
                    pos = (px + 95, py + 11)
                    randint_x = random.randint(5, 50)
                    randint_y = random.randint(5, 20)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(1.0, 1.2))
                    # 如需归队，归队
                    src_img = window_capture(hwnd, x, y)
                    points = get_match_points(src_img, guidui_img)
                    if points:
                        pos = points[0]
                        randint_x = random.randint(5, 70)
                        randint_y = random.randint(5, 20)
                        window_click(hwnd, pos, randint_x, randint_y)
                        time.sleep(random.uniform(0.8, 1.0))
                    break

        # 关闭队伍窗口
        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, xinxi_close_img, threshold=0.8)
        if points:
            pos = points[0]
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.5, 0.6))
            pos = (2725 - 1927, 270 - 156)
            randint_x = random.randint(0, 10)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
        return