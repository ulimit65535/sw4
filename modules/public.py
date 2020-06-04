import cv2
import random
import time
import os
import sys
import subprocess
import multiprocessing

from datetime import datetime

from lib.functions import window_click, window_capture, get_match_points, window_mouse_move, window_mouse_down
from lib.wechat import senddata
from etc import settings


icon_shimen_img = cv2.cvtColor(cv2.imread("src/icon_shimen.png"), cv2.COLOR_BGR2GRAY)
icon_richeng_img = cv2.cvtColor(cv2.imread("src/icon_richeng.png"), cv2.COLOR_BGR2GRAY)
zidong_img = cv2.cvtColor(cv2.imread("src/zidong.png"), cv2.COLOR_BGR2GRAY)
quxiaozidong_img = cv2.cvtColor(cv2.imread("src/quxiaozidong.png"), cv2.COLOR_BGR2GRAY)
yanzheng_img = cv2.cvtColor(cv2.imread("src/yanzheng.png"), cv2.COLOR_BGR2GRAY)
goumai_zhuangbei_img = cv2.cvtColor(cv2.imread("src/goumai_zhuangbei.png"), cv2.COLOR_BGR2GRAY)
goumai_guangtan_img = cv2.cvtColor(cv2.imread("src/goumai_guangtan.png"), cv2.COLOR_BGR2GRAY)
icon_tongbi_img = cv2.cvtColor(cv2.imread("src/icon_tongbi.png"), cv2.COLOR_BGR2GRAY)
icon_tongbi_big_img = cv2.cvtColor(cv2.imread("src/icon_tongbi_big.png"), cv2.COLOR_BGR2GRAY)
goumai_yaodian_img = cv2.cvtColor(cv2.imread("src/goumai_yaodian.png"), cv2.COLOR_BGR2GRAY)
jiyu_img = cv2.cvtColor(cv2.imread("src/jiyu.png"), cv2.COLOR_BGR2GRAY)
daguai_img = cv2.cvtColor(cv2.imread("src/daguai.png"), cv2.COLOR_BGR2GRAY)
lingqu_huoyue_img = cv2.cvtColor(cv2.imread("src/lingqu_huoyue.png"), cv2.COLOR_BGR2GRAY)
lingqu_shuangbei_img = cv2.cvtColor(cv2.imread("src/lingqu_shuangbei.png"), cv2.COLOR_BGR2GRAY)
buchongbaoshi_img = cv2.cvtColor(cv2.imread("src/buchongbaoshi.png"), cv2.COLOR_BGR2GRAY)
huobanbuzhen_img = cv2.cvtColor(cv2.imread("src/huobanbuzhen.png"), cv2.COLOR_BGR2GRAY)
suoping_img = cv2.cvtColor(cv2.imread("src/suoping.png"), cv2.COLOR_BGR2GRAY)
fanhui_img = cv2.cvtColor(cv2.imread("src/fanhui.png"), cv2.COLOR_BGR2GRAY)
pingbi_img = cv2.cvtColor(cv2.imread("src/pingbi.png"), cv2.COLOR_BGR2GRAY)
button_xuqiu_img = cv2.cvtColor(cv2.imread("src/button_xuqiu.png"), cv2.COLOR_BGR2GRAY)
button_xuqiu_checked_img = cv2.cvtColor(cv2.imread("src/button_xuqiu_checked.png"), cv2.COLOR_BGR2GRAY)
target_xuqiu_img_color = cv2.cvtColor(cv2.imread("src/target_xuqiu.png"), cv2.IMREAD_COLOR)
tishengzaizhan_img = cv2.cvtColor(cv2.imread("src/tishengzaizhan.png"), cv2.COLOR_BGR2GRAY)
button_tixian_img = cv2.cvtColor(cv2.imread("src/button_tixian.png"), cv2.COLOR_BGR2GRAY)
qiangda_img = cv2.cvtColor(cv2.imread("src/qiangda.png"), cv2.COLOR_BGR2GRAY)
qitian_close_img = cv2.cvtColor(cv2.imread("src/qitian_close.png"), cv2.COLOR_BGR2GRAY)
button_renwu_img_color = cv2.cvtColor(cv2.imread("src/button_renwu.png"), cv2.IMREAD_COLOR)
button_duiwu_img_color = cv2.cvtColor(cv2.imread("src/button_duiwu.png"), cv2.IMREAD_COLOR)
duiwu_zhankai_img_color = cv2.cvtColor(cv2.imread("src/duiwu_zhankai.png"), cv2.IMREAD_COLOR)
button_dianqumoxiang_img = cv2.cvtColor(cv2.imread("src/button_dianqumoxiang.png"), cv2.COLOR_BGR2GRAY)
tuijian_img = cv2.cvtColor(cv2.imread("src/tuijian.png"), cv2.COLOR_BGR2GRAY)
window_zhuanzhuanle_img = cv2.cvtColor(cv2.imread("src/window_zhuanzhuanle.png"), cv2.COLOR_BGR2GRAY)
icon_wupin_img_color = cv2.cvtColor(cv2.imread("src/icon_wupin.png"), cv2.IMREAD_COLOR)
button_jiejuekaji_img = cv2.cvtColor(cv2.imread("src/button_jiejuekaji.png"), cv2.COLOR_BGR2GRAY)
app_shenwu_img = cv2.cvtColor(cv2.imread("src/app_shenwu.png"), cv2.COLOR_BGR2GRAY)
gonggao_img = cv2.cvtColor(cv2.imread("src/gonggao.png"), cv2.COLOR_BGR2GRAY)
icon_wupin_img = cv2.cvtColor(cv2.imread("src/icon_wupin.png"), cv2.COLOR_BGR2GRAY)
fenxiang_close_img = cv2.cvtColor(cv2.imread("src/fenxiang_close.png"), cv2.COLOR_BGR2GRAY)
button_close_img_color = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.IMREAD_COLOR)
button_close_img = cv2.cvtColor(cv2.imread("src/button_close.png"), cv2.COLOR_BGR2GRAY)
window_renwu_img = cv2.cvtColor(cv2.imread("src/window_renwu.png"), cv2.COLOR_BGR2GRAY)
button_bangpai_img = cv2.cvtColor(cv2.imread("src/button_bangpai.png"), cv2.COLOR_BGR2GRAY)
button_huidaobangpai_img = cv2.cvtColor(cv2.imread("src/button_huidaobangpai.png"), cv2.COLOR_BGR2GRAY)
button_huidaobangpai_2_img = cv2.cvtColor(cv2.imread("src/button_huidaobangpai_2.png"), cv2.COLOR_BGR2GRAY)
button_zanyige_img = cv2.cvtColor(cv2.imread("src/button_zanyige.png"), cv2.COLOR_BGR2GRAY)
icon_zhaohuan_img = cv2.cvtColor(cv2.imread("src/icon_zhaohuan.png"), cv2.COLOR_BGR2GRAY)
button_zhaohuan_img = cv2.cvtColor(cv2.imread("src/button_zhaohuan.png"), cv2.COLOR_BGR2GRAY)
button_zhaohuan_img_color = cv2.cvtColor(cv2.imread("src/button_zhaohuan.png"), cv2.IMREAD_COLOR)
xuemai_longqi_img_color = cv2.cvtColor(cv2.imread("src/xuemai_longqi.png"), cv2.IMREAD_COLOR)
xuemai_guiche_img_color = cv2.cvtColor(cv2.imread("src/xuemai_guiche.png"), cv2.IMREAD_COLOR)
xuemai_moyuan_img_color = cv2.cvtColor(cv2.imread("src/xuemai_moyuan.png"), cv2.IMREAD_COLOR)
yanzheng_error_img =  cv2.cvtColor(cv2.imread("src/yanzheng_error.png"), cv2.COLOR_BGR2GRAY)
skill_fangyu_img = cv2.cvtColor(cv2.imread("src/skill_fangyu.png"), cv2.COLOR_BGR2GRAY)
yanzheng_error_shimen_img =  cv2.cvtColor(cv2.imread("src/yanzheng_error_shimen.png"), cv2.COLOR_BGR2GRAY)
xinxi_close_img = cv2.cvtColor(cv2.imread("src/xinxi_close.png"), cv2.COLOR_BGR2GRAY)
shiyong_img = cv2.cvtColor(cv2.imread("src/shiyong.png"), cv2.COLOR_BGR2GRAY)
hebao_img = cv2.cvtColor(cv2.imread("src/hebao.png"), cv2.COLOR_BGR2GRAY)
mapodoutang_img = cv2.cvtColor(cv2.imread("src/mapodoutang.png"), cv2.COLOR_BGR2GRAY)
xiaguangbaota_img = cv2.cvtColor(cv2.imread("src/xiaguangbaota.png"), cv2.COLOR_BGR2GRAY)
fotiaoqiang_img = cv2.cvtColor(cv2.imread("src/fotiaoqiang.png"), cv2.COLOR_BGR2GRAY)
longjinguopan_img = cv2.cvtColor(cv2.imread("src/longjinguopan.png"), cv2.COLOR_BGR2GRAY)
haiwaixianshan_img = cv2.cvtColor(cv2.imread("src/haiwaixianshan.png"), cv2.COLOR_BGR2GRAY)
baxianguohai_img = cv2.cvtColor(cv2.imread("src/baxianguohai.png"), cv2.COLOR_BGR2GRAY)
button_shiyong_img = cv2.cvtColor(cv2.imread("src/button_shiyong.png"), cv2.COLOR_BGR2GRAY)

icon_shimen_img_color = cv2.cvtColor(cv2.imread("src/icon_shimen.png"), cv2.IMREAD_COLOR)
icon_baotu_img_color = cv2.cvtColor(cv2.imread("src/icon_baotu.png"), cv2.IMREAD_COLOR)
icon_sichou_img_color = cv2.cvtColor(cv2.imread("src/icon_sichou.png"), cv2.IMREAD_COLOR)
icon_jingjichang_img_color = cv2.cvtColor(cv2.imread("src/icon_jingjichang.png"), cv2.IMREAD_COLOR)
icon_shilian_img_color = cv2.cvtColor(cv2.imread("src/icon_shilian.png"), cv2.IMREAD_COLOR)
huobanrenwu_img_color = cv2.cvtColor(cv2.imread("src/huobanrenwu.png"), cv2.IMREAD_COLOR)

global qiangda_warning

qiangda_warning = False


def is_richeng(hwnd, x, y, src_img=None):
    if src_img is None:
        src_img = window_capture(hwnd, x, y)

    points = get_match_points(src_img, icon_shimen_img)
    if points:
        return True
    else:
        return False


def is_pet_alive(hwnd, x, y, src_img=None):
    if src_img is None:
        src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)

    left = 707
    top = 20
    w = 1
    h = 1
    opponent_img = src_img[top:top + h, left:left + w]
    #cv2.namedWindow("Image")
    #cv2.imshow("Image", opponent_img)
    #cv2.waitKey(0)
    #sys.exit(1)
    r = opponent_img[0, 0, 0]
    g = opponent_img[0, 0, 1]
    b = opponent_img[0, 0, 2]

    if r == g == b:
        return False
    else:
        return True


def jiesuo(hwnd, x, y, src_img=None):
    if src_img is None:
        src_img = window_capture(hwnd, x, y)

    points = get_match_points(src_img, suoping_img)
    if points:
        start = (2277 - 1927, 445 - 193)
        end = (2666 - 1927, 445 - 193)
        randint_x = random.randint(0, 25)
        randint_y = random.randint(0, 25)
        window_mouse_move(hwnd, start, end, randint_x, randint_y)
        time.sleep(random.uniform(0.6, 0.8))


def get_status(hwnd, x, y, src_img1=None, with_standing=True, auto_buy=True, npc_jiaohu=True, call_pet=False):
    global qiangda_warning

    if src_img1 is None:
        src_img1 = window_capture(hwnd, x, y)

    points = get_match_points(src_img1, shiyong_img)
    if points:
        # 直接领取活跃
        pos = points[0]
        randint_x = random.randint(5, 50)
        randint_y = random.randint(5, 15)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.6, 0.8))
        return "wupin_shiyong"

    points = get_match_points(src_img1, button_zanyige_img)
    if points:
        pos = points[0]
        randint_x = random.randint(5, 50)
        randint_y = random.randint(5, 15)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.6, 0.8))
        return "zanyige_finished"

    points = get_match_points(src_img1, fenxiang_close_img)
    if points:
        # 弹出的分享窗口，关闭
        pos = points[0]
        randint_x = random.randint(5, 10)
        randint_y = random.randint(5, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.6, 0.8))
        return "fenxiang_close"

    points = get_match_points(src_img1, qitian_close_img)
    if points:
        pos = points[0]
        randint_x = random.randint(2, 7)
        randint_y = random.randint(5, 15)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.6, 0.8))
        return "jiangli_close"

    points = get_match_points(src_img1, suoping_img)
    if points:
        start = (2277 - 1927, 445 - 193)
        end = (2666 - 1927, 445 - 193)
        randint_x = random.randint(0, 25)
        randint_y = random.randint(0, 25)
        window_mouse_move(hwnd, start, end, randint_x, randint_y)
        time.sleep(random.uniform(0.6, 0.8))
        return "suoping_finished"

    points = get_match_points(src_img1, yanzheng_img)
    if points:
        try:
            darknet_dir = settings.darknet_dir
        except:
            darknet_dir = None

        if not darknet_dir:
            # 不能自动过验证，发通知
            senddata("窗口:{}出现验证码!!!".format(hwnd), "")
        # 等待字幕消失
        time.sleep(random.uniform(3.8, 4.2))
        src_img1 = window_capture(hwnd, x, y)
        left = 230
        top = 170
        w = 464
        h = 218
        opponent_img = src_img1[top:top + h, left:left + w]
        #cv2.namedWindow("Image")
        #cv2.imshow("Image", opponent_img)
        #cv2.waitKey(0)
        #sys.exit(1)
        filename = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3] + ".png"
        file_abs = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "runtime/img", filename)
        cv2.imwrite(file_abs, opponent_img)

        if darknet_dir:
            cmd = "pythonw " + os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "yanzheng.py") \
                  + " {} {}".format(hwnd, file_abs)
            sp = subprocess.Popen(cmd, shell=True)
            while True:
                if sp.poll() is None:
                    time.sleep(1)
                    continue
                else:
                    break
            time.sleep(random.uniform(0.6, 0.8))
            return "darknet_finished"
            """
            subp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in iter(subp.stdout.readline, 'b'):
                print(line)
                time.sleep(0.5)
                if not subprocess.Popen.poll(subp) is None:
                    if line == "":
                        break
            subp.stdout.close()
            """
        else:
            while True:
                time.sleep(1)
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, yanzheng_img)
                if points:
                    senddata("窗口:{}出现验证码!!!".format(hwnd), "")
                    time.sleep(5)
                    continue
                else:
                    time.sleep(10)
                    return "yanzheng_finished"

    points1 = get_match_points(src_img1, yanzheng_error_img)
    points2 = get_match_points(src_img1, yanzheng_error_shimen_img)
    if points1 or points2:
        pos = (2856 - 1927, 233 - 193)
        randint_x = random.randint(0, 10)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.6, 0.8))
        return "yanzheng_failed"

    """
    points = get_match_points(src_img1,  qiangda_img)
    if points:
        if not qiangda_warning:
            senddata("窗口:{}出现世界答题!!!".format(hwnd), "")
            qiangda_warning = True
    else:
        qiangda_warning = False
    """

    points = get_match_points(src_img1, lingqu_huoyue_img)
    if points:
        # 直接领取活跃
        pos = points[0]
        randint_x = random.randint(5, 50)
        randint_y = random.randint(5, 15)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(3.8, 4.2))

        # 转转乐
        src_img1 = window_capture(hwnd, x, y)
        points = get_match_points(src_img1, window_zhuanzhuanle_img, threshold=0.85)
        if points:
            pos = (2272 - 1927, 420 - 156)
            randint_x = random.randint(0, 20)
            randint_y = random.randint(0, 20)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(4.8, 5.2))
            for i in range(10):
                time.sleep(random.uniform(2.8, 3.2))
                src_img1 = window_capture(hwnd, x, y)
                points = get_match_points(src_img1, window_zhuanzhuanle_img, threshold=0.85)
                if points:
                    # 直接关闭
                    pos = (2735 - 1927, 192 - 156)
                    randint_x = random.randint(0, 10)
                    randint_y = random.randint(0, 10)
                    window_click(hwnd, pos, randint_x, randint_y)
                    continue
                else:
                    break
        return "lingqu_huoyue"

    points = get_match_points(src_img1, lingqu_shuangbei_img)
    if points:
        """
        pos = points[0]
        randint_x = random.randint(5, 45)
        randint_y = random.randint(5, 15)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.6, 0.8))
        return "lingqu_shuangbei"
        """
        x, y = points[0]
        pos = (x + 284, y - 104)
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.6, 0.8))
        return "close_shuangbei"

    points = get_match_points(src_img1, buchongbaoshi_img, threshold=0.95)
    if points:
        pos = points[0]
        randint_x = random.randint(-80, -50)
        randint_y = random.randint(5, 15)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.6, 0.8))
        return "buchongbaoshi"

    if npc_jiaohu:
        points = get_match_points(src_img1, icon_tongbi_img)
        if points:
            is_tongbi = True
        else:
            points = get_match_points(src_img1, icon_tongbi_big_img)
            if points:
                is_tongbi = True
            else:
                is_tongbi = False

        if is_tongbi:
            points = get_match_points(src_img1, goumai_zhuangbei_img)
            if points:
                pos = points[0]
                randint_x = random.randint(10, 80)
                randint_y = random.randint(10, 30)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.6, 0.8))
                return "goumai_zhuangbei"

            points = get_match_points(src_img1, goumai_yaodian_img)
            if points:
                pos = points[0]
                randint_x = random.randint(10, 80)
                randint_y = random.randint(10, 30)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.6, 0.8))
                return "goumai_yaodian"

        points = get_match_points(src_img1, jiyu_img)
        if points:
            pos = (2440 - 1927, 309 - 193)
            randint_x = random.randint(0, 10)
            randint_y = random.randint(0, 30)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.6, 0.8))
            pos = (2504 - 1927, 309 - 193)
            randint_x = random.randint(0, 10)
            randint_y = random.randint(0, 30)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.6, 0.8))
            pos = (2568 - 1927, 309 - 193)
            randint_x = random.randint(0, 10)
            randint_y = random.randint(0, 30)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.6, 0.8))
            pos = points[0]
            randint_x = random.randint(10, 180)
            randint_y = random.randint(10, 30)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.6, 0.8))
            return "jiyu"

        points = get_match_points(src_img1, button_tixian_img)
        if points:
            # 点摊位列表
            pos = (2111 - 1927, 261 - 193)
            randint_x = random.randint(0, 50)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.6, 0.8))
            return "guantan_baitan"

        points = get_match_points(src_img1, goumai_guangtan_img)
        if points:
            if auto_buy:
                while True:
                    time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
                    src_img = window_capture(hwnd, x, y)
                    points = get_match_points(src_img1, goumai_guangtan_img)
                    if not points:
                        return "guangtan_closed"
                    points = get_match_points(src_img, button_xuqiu_checked_img)
                    if points:
                        # 翻页次数
                        num_next = 0
                        while True:
                            time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
                            if num_next >= 20:
                                # 翻了30页，都未买到相应物品，关闭窗口
                                pos = (2764 - 1927, 218 - 193)
                                randint_x = random.randint(0, 15)
                                randint_y = random.randint(0, 15)
                                window_click(hwnd, pos, randint_x, randint_y)
                                time.sleep(random.uniform(30.0, 60.0))
                                return "guangtan_close"
                            src_img = window_capture(hwnd, x, y)
                            points = get_match_points(src_img, button_xuqiu_checked_img)
                            if not points:
                                # 选中的摊位已购买完毕
                                break
                            src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
                            points = get_match_points(src_img, target_xuqiu_img_color)
                            if points:
                                # 购买物品
                                pos = points[0]
                                randint_x = random.randint(60, 160)
                                randint_y = random.randint(-5, 25)
                                window_click(hwnd, pos, randint_x, randint_y)
                                time.sleep(random.uniform(0.6, 0.8))
                                # 点购买
                                pos = (2489 - 1927, 661 - 193)
                                randint_x = random.randint(0, 25)
                                randint_y = random.randint(0, 20)
                                window_click(hwnd, pos, randint_x, randint_y)
                                # 等待字幕消失
                                time.sleep(random.uniform(2.4, 2.6))
                                continue
                            else:
                                # 点下一页
                                pos = (2642 - 1927, 661 - 193)
                                randint_x = random.randint(0, 50)
                                randint_y = random.randint(0, 20)
                                window_click(hwnd, pos, randint_x, randint_y)
                                num_next += 1
                                continue
                    else:
                        # 未发现选中的需求摊位
                        points = get_match_points(src_img, button_xuqiu_img)
                        if points:
                            # 点第一个需求的摊位
                            pos = points[0]
                            randint_x = random.randint(-80, 0)
                            randint_y = random.randint(10, 25)
                            window_click(hwnd, pos, randint_x, randint_y)
                            continue
                        else:
                            # 购买完毕
                            return "guangtan_finished"
            else:
                time.sleep(random.uniform(4.8, 5.2))
                return "guangtan_waiting"

    # 点到人物信息查看了，关闭
    points = get_match_points(src_img1, pingbi_img)
    if points:
        # 点下任务栏，关闭该窗口
        pos = (2863 - 1927, 303 - 193)
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.6, 0.8))
        pos = (2863 - 1927, 303 - 193)
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.6, 0.8))
        return "close_renwuxinxi"

    # 竞技场战斗失败
    points = get_match_points(src_img1, tishengzaizhan_img)
    if points:
        # 关闭提升再战窗口
        pos = (2649 - 1927, 263 - 193)
        randint_x = random.randint(0, 10)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.6, 0.8))
        return "battle_fail"

    points = get_match_points(src_img1, huobanbuzhen_img)
    if points:
        time.sleep(random.uniform(0.8, 0.8))
        src_img1 = window_capture(hwnd, x, y)
        points = get_match_points(src_img1, huobanbuzhen_img)
        if points:
            return "window_jingjichang"

    """
    # 关闭未知对话窗口
    points = get_match_points(src_img1, button_close_img)
    if points:
        pos = points[0]
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.6, 0.8))
        return "close_duihua_unknown"
    """

    # 关闭其它窗口
    points = get_match_points(src_img1, xinxi_close_img, threshold=0.8)
    if points:
        pos = points[0]
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.6, 0.8))
        return "close_window_other"

    points = get_match_points(src_img1, zidong_img)
    if points:
        pos_zidong = points[0]
        randint_x_zidong = random.randint(0, 10)
        randint_y_zidong = random.randint(0, 10)
        if call_pet:
            is_alive = is_pet_alive(hwnd, x, y)
            if not is_alive:
                src_img1 = window_capture(hwnd, x, y)
                points = get_match_points(src_img1, icon_zhaohuan_img)
                if points:
                    # 点开召唤
                    pos = points[0]
                    randint_x = random.randint(5, 10)
                    randint_y = random.randint(10, 15)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(1.6, 1.8))
                    src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
                    points = get_match_points(src_img, button_zhaohuan_img_color)
                    if points:
                        pos_zhaohuan = points[0]
                        randint_x_zhaohuan = random.randint(5, 50)
                        randint_y_zhaohuan = random.randint(5, 15)
                        # 选择有输出血脉的宝宝
                        points = get_match_points(src_img, xuemai_guiche_img_color)
                        if points:
                            pos = points[0]
                            randint_x = random.randint(-50, -10)
                            randint_y = random.randint(-10, 0)
                            window_click(hwnd, pos, randint_x, randint_y)
                            time.sleep(random.uniform(1.6, 1.8))
                        else:
                            points = get_match_points(src_img, xuemai_longqi_img_color)
                            if points:
                                pos = points[0]
                                randint_x = random.randint(-50, -10)
                                randint_y = random.randint(-10, 0)
                                window_click(hwnd, pos, randint_x, randint_y)
                                time.sleep(random.uniform(1.6, 1.8))
                            else:
                                points = get_match_points(src_img, xuemai_moyuan_img_color)
                                if points:
                                    pos = points[0]
                                    randint_x = random.randint(-50, -10)
                                    randint_y = random.randint(-10, 0)
                                    window_click(hwnd, pos, randint_x, randint_y)
                                    time.sleep(random.uniform(1.6, 1.8))
                        # 点召唤
                        window_click(hwnd, pos_zhaohuan, randint_x_zhaohuan, randint_y_zhaohuan)
                        time.sleep(random.uniform(2.8, 3.2))
                        src_img1 = window_capture(hwnd, x, y)
                        points = get_match_points(src_img1, button_zhaohuan_img)
                        if points:
                            print("召唤宠物失败，无宠物可召唤.")
                            window_click(hwnd, pos_zidong, randint_x_zidong, randint_y_zidong)
                            time.sleep(random.uniform(1.6, 1.8))
                            window_click(hwnd, pos_zidong, randint_x_zidong, randint_y_zidong)
                        else:
                            print("召唤宠物成功.")
                        return "in_battle"
                    else:
                        print("打开召唤窗口失败.")
                        return "in_battle"
                else:
                    print("等待新回合开始.")
                    return "in_battle"
            else:
                window_click(hwnd, pos_zidong, randint_x_zidong, randint_y_zidong)
                return "in_battle"
        else:
            window_click(hwnd, pos_zidong, randint_x_zidong, randint_y_zidong)
            return "in_battle"

    points = get_match_points(src_img1, quxiaozidong_img)
    if points:
        if call_pet:
            is_alive = is_pet_alive(hwnd, x, y)
            if not is_alive:
                # 取消自动
                pos = points[0]
                randint_x = random.randint(0, 10)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(1.4, 1.6))
        return "in_battle"

    if with_standing:
        time.sleep(1)
        src_img2 = window_capture(hwnd, x, y)
        points = get_match_points(src_img2, zidong_img)
        if not points:
            points = get_match_points(src_img2, quxiaozidong_img)
            if points:
                return "in_battle"
        else:
            pos = points[0]
            randint_x = random.randint(0, 10)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            return "in_battle"

        points = get_match_points(src_img1, src_img2, threshold=0.8)
        if points:
            time.sleep(1)
            src_img3 = window_capture(hwnd, x, y)
            points = get_match_points(src_img3, zidong_img)
            if not points:
                points = get_match_points(src_img3, quxiaozidong_img)
                if points:
                    return "in_battle"
            else:
                pos = points[0]
                randint_x = random.randint(0, 10)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                return "in_battle"
            points = get_match_points(src_img2, src_img3, threshold=0.8)
            if points:
                return "standing"
            else:
                return "moving"
        else:
            return "moving"
    else:
        return "unknown"

"""
def hide_menu(hwnd, x, y, src_img):
    if src_img is None:
        src_img = window_capture(hwnd, x, y)

    points = get_match_points(src_img, fanhui_img)
    if not points:
        win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F4, 0)
        win32gui.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_F4, 0)
        time.sleep(random.uniform(0.08, 0.12))
        win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F4, 0)
        win32gui.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_F4, 0)
        time.sleep(random.uniform(0.08, 0.12))
        win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F4, 0)
        win32gui.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_F4, 0)


def show_menu(hwnd, x, y, src_img=None):
    if src_img is None:
        src_img = window_capture(hwnd, x, y)

    points = get_match_points(src_img, fanhui_img)
    print(points)
    if points:
        pos = points[0]
        randint_x = random.randint(0, 10)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.2))
"""


def show_menu_renwu(hwnd, x, y):
    src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
    points = get_match_points(src_img, button_close_img_color)
    if points:
        # 误点到战备，或者NPC对话，关闭
        pos = points[0]
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.0))
        src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
    points = get_match_points(src_img, button_duiwu_img_color, threshold=0.8)
    if not points:
        # 展开任务列表
        pos = (2863 - 1927, 303 - 193)
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(1.8, 2.2))
        src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
    points = get_match_points(src_img, button_duiwu_img_color, threshold=0.95)
    if points:
        # 切换到任务显示
        pos = (2707 - 1927, 263 - 156)
        randint_x = random.randint(5, 50)
        randint_y = random.randint(5, 20)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.0))
        src_img = window_capture(hwnd, x, y)
        # 如果误点开任务，关闭
        points = get_match_points(src_img, window_renwu_img)
        if points:
            pos = (2867 - 1927, 268 - 156)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.6, 0.8))


def show_menu_duiwu(hwnd, x, y):
    src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
    points = get_match_points(src_img, button_close_img_color)
    if points:
        # 误点到战备，或者NPC对话，关闭
        pos = points[0]
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.0))
        src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
    points = get_match_points(src_img, button_duiwu_img_color, threshold=0.8)
    if not points:
        # 展开任务列表
        pos = (2863 - 1927, 303 - 193)
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(1.8, 2.2))
        src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
    points = get_match_points(src_img, button_duiwu_img_color, threshold=0.95)
    if not points:
        # 切换到队伍显示
        pos = (2785 - 1927, 263 - 156)
        randint_x = random.randint(5, 50)
        randint_y = random.randint(5, 20)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.0))
        # 关闭队伍弹窗
        pos = (2852 - 1927, 339 - 156)
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)


def open_window_richeng(hwnd, x, y, src_img=None):

    if src_img is None:
        src_img = window_capture(hwnd, x, y)

    if is_richeng(hwnd, x , y, src_img):
        return True
    else:
        # 关闭其它窗口
        points = get_match_points(src_img, xinxi_close_img, threshold=0.8)
        if points:
            pos = points[0]
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.8, 1.0))

        pos = (2234 - 1927, 182 - 156)
        randint_x = random.randint(0, 15)
        randint_y = random.randint(0, 15)
        window_click(hwnd, pos, randint_x, randint_y)

        time.sleep(random.uniform(1.2, 1.4))

        if is_richeng(hwnd, x, y):
            return True
        else:
            return False


def close_window_richeng(hwnd, x, y):
    if is_richeng(hwnd, x , y):
        pos = (2763 - 1927, 183 - 156)
        randint_x = random.randint(0, 10)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.4, 0.6))


def xunluo(hwnd, x, y, src_img=None):

    if src_img is None:
        src_img = window_capture(hwnd, x, y)

    points = get_match_points(src_img, button_close_img)
    if points:
        # NPC对话，关闭
        pos = points[0]
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.0))
        src_img = window_capture(hwnd, x, y)

    for i in range(5):
        result = open_window_richeng(hwnd, x, y)
        if not result:
            time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
        else:
            break

    src_img = window_capture(hwnd, x, y)

    points = get_match_points(src_img, daguai_img)
    if points:
        pos = points[0]
        randint_x = random.randint(0, 40)
        randint_y = random.randint(0, 40)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.2))
        # 点自动巡逻
        pos = (2110 - 1927, 608 - 156)
        randint_x = random.randint(0, 80)
        randint_y = random.randint(0, 20)
        window_click(hwnd, pos, randint_x, randint_y)
        return True
    else:
        print("未能打开打怪双倍窗口")
        return False


def goto_yewai(hwnd, x, y, src_img=None, qumo=False):

    if src_img is None:
        src_img = window_capture(hwnd, x, y)

    for i in range(5):
        result = open_window_richeng(hwnd, x, y)
        if not result:
            time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
        else:
            break

    src_img = window_capture(hwnd, x, y)

    points = get_match_points(src_img, daguai_img)
    if points:
        pos = points[0]
        randint_x = random.randint(0, 40)
        randint_y = random.randint(0, 40)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.2))
    else:
        print("未能打开打怪双倍窗口")
        return False

    if qumo:
        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, button_dianqumoxiang_img)
        if points:
            pos = points[0]
            randint_x = random.randint(0, 80)
            randint_y = random.randint(0, 20)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.6, 0.8))
            # 点确定
            pos = (2179 - 1927, 510 - 156)
            randint_x = random.randint(0, 80)
            randint_y = random.randint(0, 20)
            window_click(hwnd, pos, randint_x, randint_y)
            # 不用等待字幕消失
            time.sleep(random.uniform(0.8, 1.2))
        """
        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, tuijian_img)
        if points:
            px, py = points[0]
            pos = (px + 61, py + 65)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
        else:
            print("未能找到推荐地图")
            return False
        """
        interval = settings.fengyao_position - 1
        pos = (2119 - 1927 + 173 * interval, 339 - 156)
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(0.1)
        # 点确定
        pos = (2179 - 1927, 510 - 156)
        randint_x = random.randint(0, 80)
        randint_y = random.randint(0, 20)
        window_click(hwnd, pos, randint_x, randint_y)
        return True
    else:
        """
        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, tuijian_img)
        if points:
            px, py = points[0]
            pos = (px + 61, py + 65)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(0.1)
            # 点确定
            pos = (2179 - 1927, 510 - 156)
            randint_x = random.randint(0, 80)
            randint_y = random.randint(0, 20)
            window_click(hwnd, pos, randint_x, randint_y)
            return True
        else:
            print("未能找到推荐地图")
            return False
        """
        interval = settings.fengyao_position - 1
        pos = (2119 - 1927 + 173 * interval, 339 - 156)
        randint_x = random.randint(0, 5)
        randint_y = random.randint(0, 5)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(0.1)
        # 点确定
        pos = (2179 - 1927, 510 - 156)
        randint_x = random.randint(0, 80)
        randint_y = random.randint(0, 20)
        window_click(hwnd, pos, randint_x, randint_y)
        return True


def change_skill(hwnd, x, y, order):
    time.sleep(random.uniform(0.6, 0.8))
    src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
    points = get_match_points(src_img, icon_wupin_img_color)
    if points:
        if order > 0:
            param = order - 1
            row = param // 3
            col = param % 3
            skill_pos = (2373 - 1927 + 64 * col, 401 - 156 + 64 * row)

        # 长按右下角
        pos = (2853 - 1927, 641 - 156)
        randint_x = random.randint(0, 10)
        randint_y = random.randint(0, 10)
        window_mouse_down(hwnd, pos, randint_x, randint_y, 1.2, 1.4)
        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, button_jiejuekaji_img)
        if points:
            # 点人物技能
            pos = (2375 - 1927, 303 - 156)
            randint_x = random.randint(0, 5)
            randint_y = random.randint(0, 5)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.6, 0.8))
            if order == 0:
                # 切换防御
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, skill_fangyu_img, threshold=0.96)
                if points:
                    pos = points[0]
                    randint_x = random.randint(10, 20)
                    randint_y = random.randint(10, 20)
                    window_click(hwnd, pos, randint_x, randint_y)
                else:
                    print("未找到防御技能.")
            else:
                # 选中挂机技能
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, skill_pos, randint_x, randint_y)
            time.sleep(random.uniform(0.5, 0.6))
            # 关闭挂机技能窗口
            pos = (2534 - 1927, 210 - 156)
            randint_x = random.randint(0, 10)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.5, 0.6))


def enter_game(hwnd, x, y, q=multiprocessing.Queue()):
    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, app_shenwu_img)
    if points:
        pos = points[0]
        randint_x = random.randint(10, 15)
        randint_y = random.randint(10, 15)
        window_click(hwnd, pos, randint_x, randint_y)
        for i in range(30):
            time.sleep(random.uniform(1.8, 2.2))
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, qitian_close_img)
            if points:
                pos = points[0]
                randint_x = random.randint(2, 7)
                randint_y = random.randint(5, 15)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(0.6, 0.8))
                continue
            points = get_match_points(src_img, gonggao_img)
            if points:
                pos = (2729 - 1927, 183 - 156)
                randint_x = random.randint(0, 10)
                randint_y = random.randint(0, 10)
                window_click(hwnd, pos, randint_x, randint_y)
                continue
            points = get_match_points(src_img, icon_wupin_img)
            if points:
                time.sleep(random.uniform(1.4, 1.6))
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, gonggao_img)
                if points:
                    pos = (2729 - 1927, 183 - 156)
                    randint_x = random.randint(0, 10)
                    randint_y = random.randint(0, 10)
                    window_click(hwnd, pos, randint_x, randint_y)
                print("已进入游戏")
                q.put(True)
                return True
    points = get_match_points(src_img, icon_wupin_img)
    if points:
        time.sleep(random.uniform(1.4, 1.6))
        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, gonggao_img)
        if points:
            pos = (2729 - 1927, 183 - 156)
            randint_x = random.randint(0, 10)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
        print("已进入游戏")
        q.put(True)
        return True
    else:
        q.put(False)
        return False


def return_bangpai(hwnd, x, y):
    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, button_bangpai_img)
    if points:
        pos = points[0]
        randint_x = random.randint(5, 15)
        randint_y = random.randint(5, 15)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(1.8, 2.2))
    else:
        # 切换下部菜单
        pos = (2853 - 1927, 641 - 156)
        randint_x = random.randint(0, 10)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(0.8, 1.0))
        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, button_bangpai_img)
        if points:
            pos = points[0]
            randint_x = random.randint(5, 15)
            randint_y = random.randint(5, 15)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(3.8, 4.2))
        else:
            print("打开帮派界面失败。")
            return False

    src_img = window_capture(hwnd, x, y)
    points = get_match_points(src_img, button_huidaobangpai_img)
    if points:
        pos = points[0]
        randint_x = random.randint(10, 80)
        randint_y = random.randint(5, 15)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(1.4, 1.6))
    else:
        points = get_match_points(src_img, button_huidaobangpai_2_img)
        if points:
            pos = points[0]
            randint_x = random.randint(5, 15)
            randint_y = random.randint(5, 15)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(1.4, 1.6))
        else:
            print("未找到回到帮派按钮。")
            return False

    return True


def get_undo_tasks(hwnd, x, y):
    undo_task_list = []
    result = open_window_richeng(hwnd, x, y)
    if not result:
        print("未能打开日程窗口。")
        return undo_task_list

    src_img = window_capture(hwnd, x, y, color=cv2.IMREAD_COLOR)
    points = get_match_points(src_img, icon_shimen_img_color, threshold=0.95)
    if points:
        undo_task_list.append("shimen")
    points = get_match_points(src_img, icon_baotu_img_color, threshold=0.95)
    if points:
        undo_task_list.append("baotu")
    points = get_match_points(src_img, icon_sichou_img_color, threshold=0.95)
    if points:
        undo_task_list.append("sichou")
    points = get_match_points(src_img, icon_jingjichang_img_color, threshold=0.95)
    if points:
        undo_task_list.append("jingji")
    points = get_match_points(src_img, icon_shilian_img_color, threshold=0.95)
    if points:
        undo_task_list.append("shilian")
    points = get_match_points(src_img, huobanrenwu_img_color, threshold=0.95)
    if points:
        undo_task_list.append("huoban")

    close_window_richeng(hwnd, x, y)

    return undo_task_list


def eat_food(hwnd, x, y, task=None):
    if task == "zhuogui":
        task_img = mapodoutang_img
    elif task == "baotu":
        task_img = xiaguangbaota_img
    elif task == "fengyao":
        task_img = fotiaoqiang_img
    elif task == "jingji":
        task_img = longjinguopan_img
    elif task == "sichou":
        task_img = haiwaixianshan_img
    elif task == "shilian":
        task_img = baxianguohai_img

    if task:
        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, icon_wupin_img)
        if points:
            pos = points[0]
            randint_x = random.randint(5, 15)
            randint_y = random.randint(5, 15)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(0.8, 1.2))
        else:
            print("未能打开背包，退出.")
            return False

        # 切换物品栏一
        pos = (2445 - 1927, 217 - 156)
        randint_x = random.randint(0, 30)
        randint_y = random.randint(0, 10)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(1.4, 1.6))
        src_img = window_capture(hwnd, x, y)
        points = get_match_points(src_img, hebao_img)
        if points:
            pos = points[0]
            randint_x = random.randint(10, 15)
            randint_y = random.randint(20, 25)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(1.4, 1.6))
            # 点食品
            pos = (2605 - 1927, 249 - 156)
            randint_x = random.randint(0, 30)
            randint_y = random.randint(0, 10)
            window_click(hwnd, pos, randint_x, randint_y)
            time.sleep(random.uniform(1.4, 1.6))
            # 点任务食品
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, task_img)
            if points:
                pos = points[0]
                randint_x = random.randint(10, 15)
                randint_y = random.randint(20, 25)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(1.4, 1.6))
                # 点使用
                src_img = window_capture(hwnd, x, y)
                points = get_match_points(src_img, button_shiyong_img)
                if points:
                    pos = points[0]
                    randint_x = random.randint(5, 80)
                    randint_y = random.randint(5, 20)
                    window_click(hwnd, pos, randint_x, randint_y)
                    time.sleep(random.uniform(1.4, 1.6))
                else:
                    print("未找到使用按钮，使用失败")
            # 关闭荷包
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, button_close_img)
            if points:
                pos = points[0]
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(1.4, 1.6))
            # 关闭物品窗口
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, xinxi_close_img, threshold=0.8)
            if points:
                pos = points[0]
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(1.4, 1.6))
            return True
        else:
            # 关闭物品窗口
            src_img = window_capture(hwnd, x, y)
            points = get_match_points(src_img, xinxi_close_img, threshold=0.8)
            if points:
                pos = points[0]
                randint_x = random.randint(0, 5)
                randint_y = random.randint(0, 5)
                window_click(hwnd, pos, randint_x, randint_y)
                time.sleep(random.uniform(1.4, 1.6))
            print("未找到金丝荷包")
            return False
    else:
        print("不存在的任务食品")
        return False
