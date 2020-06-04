import time
import os
import subprocess
import win32gui
import sys
import multiprocessing
import ctypes
import random

from etc import settings
from modules import public
from modules import zudui, zhuogui, fengyao, shimen, putian, task, baoshi
from lib.loggingpool import LoggingPool
from lib.wechat import senddata


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def open_leidian():
    file_abs = os.path.join(settings.leidian_dir, "dnconsole.exe")

    if settings.leidian_num == 1:
        hwnd = win32gui.FindWindow(settings.hwnd1_windowclass, settings.hwnd1_title)
        if hwnd <= 0:
            cmd = file_abs + " launch --name " + settings.hwnd1_title
            subprocess.Popen(cmd, shell=True)
    elif settings.leidian_num == 2:
        hwnd = win32gui.FindWindow(settings.hwnd1_windowclass, settings.hwnd1_title)
        if hwnd <= 0:
            cmd = file_abs + " launch --name " + settings.hwnd1_title
            subprocess.Popen(cmd, shell=True)
            time.sleep(1)
        hwnd = win32gui.FindWindow(settings.hwnd2_windowclass, settings.hwnd2_title)
        if hwnd <= 0:
            cmd = file_abs + " launch --name " + settings.hwnd2_title
            subprocess.Popen(cmd, shell=True)
    elif settings.leidian_num == 3:
        hwnd = win32gui.FindWindow(settings.hwnd1_windowclass, settings.hwnd1_title)
        if hwnd <= 0:
            cmd = file_abs + " launch --name " + settings.hwnd1_title
            subprocess.Popen(cmd, shell=True)
            time.sleep(1)
        hwnd = win32gui.FindWindow(settings.hwnd2_windowclass, settings.hwnd2_title)
        if hwnd <= 0:
            cmd = file_abs + " launch --name " + settings.hwnd2_title
            subprocess.Popen(cmd, shell=True)
            time.sleep(1)
        hwnd = win32gui.FindWindow(settings.hwnd3_windowclass, settings.hwnd3_title)
        if hwnd <= 0:
            cmd = file_abs + " launch --name " + settings.hwnd3_title
            subprocess.Popen(cmd, shell=True)
    elif settings.leidian_num == 4:
        hwnd = win32gui.FindWindow(settings.hwnd1_windowclass, settings.hwnd1_title)
        if hwnd <= 0:
            cmd = file_abs + " launch --name " + settings.hwnd1_title
            subprocess.Popen(cmd, shell=True)
            time.sleep(1)
        hwnd = win32gui.FindWindow(settings.hwnd2_windowclass, settings.hwnd2_title)
        if hwnd <= 0:
            cmd = file_abs + " launch --name " + settings.hwnd2_title
            subprocess.Popen(cmd, shell=True)
            time.sleep(1)
        hwnd = win32gui.FindWindow(settings.hwnd3_windowclass, settings.hwnd3_title)
        if hwnd <= 0:
            cmd = file_abs + " launch --name " + settings.hwnd3_title
            subprocess.Popen(cmd, shell=True)
            time.sleep(1)
        hwnd = win32gui.FindWindow(settings.hwnd4_windowclass, settings.hwnd4_title)
        if hwnd <= 0:
            cmd = file_abs + " launch --name " + settings.hwnd4_title
            subprocess.Popen(cmd, shell=True)


if __name__ == '__main__':
    try:
        startup = sys.argv[1]
    except:
        startup = ""

    # 需要管理员权限
    if not is_admin():
        if startup:
            params = __file__ + " " + startup
        else:
            params = __file__
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)

    # 随开机启动，判断是否运行.
    if startup:
        try:
            h, m = settings.start_time.split(":")
            start_hour = int(h)
            start_minute = int(m)
        except:
            print("未配置开启时间。")
            sys.exit(1)

        while True:
            hour = time.localtime().tm_hour
            minute = time.localtime().tm_min
            if hour > start_hour:
                print("已过{}点，直接退出。".format(start_hour))
                sys.exit(0)
            if hour >= start_hour and minute >= start_minute:
                print("已到时间，脚本启动。")
                break
            else:
                time.sleep(30)
                continue

    try:
        wait_leidian = settings.wait_leidian
    except:
        wait_leidian = 60

    for i in range(3):
        open_leidian()
        # 等待雷电模拟器启动
        time.sleep(wait_leidian)

        hwnd1 = 0
        hwnd2 = 0
        hwnd3 = 0
        hwnd4 = 0
        hwnd5 = 0
        hwnd6 = 0

        # 获取模拟器句柄
        hwnd1_main = win32gui.FindWindow(settings.hwnd1_windowclass, settings.hwnd1_title)
        hwnd2_main = win32gui.FindWindow(settings.hwnd2_windowclass, settings.hwnd2_title)
        hwnd3_main = win32gui.FindWindow(settings.hwnd3_windowclass, settings.hwnd3_title)
        hwnd4_main = win32gui.FindWindow(settings.hwnd4_windowclass, settings.hwnd4_title)
        hwnd5_main = win32gui.FindWindow(settings.hwnd5_windowclass, settings.hwnd5_title)
        hwnd6_main = win32gui.FindWindow(settings.hwnd6_windowclass, settings.hwnd6_title)

        if hwnd1_main > 0:
            win32gui.MoveWindow(hwnd1_main, settings.x1, settings.y1, settings.width, settings.height, True)
            hwndChildList = []
            win32gui.EnumChildWindows(hwnd1_main, lambda hwnd, param: param.append(hwnd), hwndChildList)
            hwnd1 = hwndChildList[0]
        if hwnd2_main > 0:
            win32gui.MoveWindow(hwnd2_main, settings.x2, settings.y2, settings.width, settings.height, True)
            hwndChildList = []
            win32gui.EnumChildWindows(hwnd2_main, lambda hwnd, param: param.append(hwnd), hwndChildList)
            # 第二个子窗口句柄
            hwnd2 = hwndChildList[0]
        if hwnd3_main > 0:
            win32gui.MoveWindow(hwnd3_main, settings.x3, settings.y3, settings.width, settings.height, True)
            hwndChildList = []
            win32gui.EnumChildWindows(hwnd3_main, lambda hwnd, param: param.append(hwnd), hwndChildList)
            # 第二个子窗口句柄
            hwnd3 = hwndChildList[0]
        if hwnd4_main > 0:
            win32gui.MoveWindow(hwnd4_main, settings.x4, settings.y4, settings.width, settings.height, True)
            hwndChildList = []
            win32gui.EnumChildWindows(hwnd4_main, lambda hwnd, param: param.append(hwnd), hwndChildList)
            # 第二个子窗口句柄
            hwnd4 = hwndChildList[0]
        if hwnd5_main > 0:
            win32gui.MoveWindow(hwnd5_main, settings.x5, settings.y5, settings.width, settings.height, True)
            hwndChildList = []
            win32gui.EnumChildWindows(hwnd5_main, lambda hwnd, param: param.append(hwnd), hwndChildList)
            # 第二个子窗口句柄
            hwnd5 = hwndChildList[0]
        if hwnd6_main > 0:
            win32gui.MoveWindow(hwnd6_main, settings.x6, settings.y6, settings.width, settings.height, True)
            hwndChildList = []
            win32gui.EnumChildWindows(hwnd6_main, lambda hwnd, param: param.append(hwnd), hwndChildList)
            # 第二个子窗口句柄
            hwnd6 = hwndChildList[0]

        q = multiprocessing.Queue()
        jobs = []
        if hwnd1 > 0:
            p = multiprocessing.Process(target=public.enter_game, args=(hwnd1, settings.x1, settings.y1, q))
            jobs.append(p)
            p.start()
        if hwnd2 > 0:
            p = multiprocessing.Process(target=public.enter_game, args=(hwnd2, settings.x2, settings.y2, q))
            jobs.append(p)
            p.start()
        if hwnd3 > 0:
            p = multiprocessing.Process(target=public.enter_game, args=(hwnd3, settings.x3, settings.y3, q))
            jobs.append(p)
            p.start()
        if hwnd4 > 0:
            p = multiprocessing.Process(target=public.enter_game, args=(hwnd4, settings.x4, settings.y4, q))
            jobs.append(p)
            p.start()
        if hwnd5 > 0:
            p = multiprocessing.Process(target=public.enter_game, args=(hwnd5, settings.x5, settings.y5, q))
            jobs.append(p)
            p.start()
        if hwnd6 > 0:
            p = multiprocessing.Process(target=public.enter_game, args=(hwnd6, settings.x6, settings.y6, q))
            jobs.append(p)
            p.start()

        for p in jobs:
            p.join()
        results = [q.get() for j in jobs]

        is_in_game = True
        for result in results:
            if not result:
                is_in_game = False
                break

        if is_in_game:
            break
        else:
            # 有窗口进入游戏失败,退出所有雷电窗口
            file_abs = os.path.join(settings.leidian_dir, "dnconsole.exe")
            cmd = file_abs + " " + "quitall"
            subprocess.Popen(cmd, shell=True)
            time.sleep(wait_leidian)
            continue

    if not is_in_game:
        print("3次进入游戏失败，退出.")
        sys.exit(1)

    time.sleep(5)

    multiprocessing.freeze_support()
    multiprocessing.log_to_stderr()
    pool = LoggingPool(processes=5)
    if hwnd1 > 0:
        pool.apply_async(shimen.shimen,
                         args=(hwnd1, settings.x1, settings.y1, settings.hwnd1_skill.get('shimen')))
    if hwnd2 > 0:
        pool.apply_async(shimen.shimen,
                         args=(hwnd2, settings.x2, settings.y2, settings.hwnd2_skill.get('shimen')))
    if hwnd3 > 0:
        pool.apply_async(shimen.shimen,
                         args=(hwnd3, settings.x3, settings.y3, settings.hwnd3_skill.get('shimen')))
    if hwnd4 > 0:
        pool.apply_async(shimen.shimen,
                         args=(hwnd4, settings.x4, settings.y4, settings.hwnd4_skill.get('shimen')))
    if hwnd5 > 0:
        pool.apply_async(shimen.shimen,
                         args=(hwnd5, settings.x5, settings.y5, settings.hwnd5_skill.get('shimen')))
    if hwnd6 > 0:
        pool.apply_async(shimen.shimen,
                         args=(hwnd6, settings.x6, settings.y6, settings.hwnd6_skill.get('shimen')))
    pool.close()
    pool.join()
    time.sleep(random.uniform(3.8, 4.2))

    multiprocessing.freeze_support()
    multiprocessing.log_to_stderr()
    pool = LoggingPool(processes=5)
    if hwnd1 > 0:
        pool.apply_async(putian.putian,
                         args=(hwnd1, settings.x1, settings.y1))
    if hwnd2 > 0:
        pool.apply_async(putian.putian,
                         args=(hwnd2, settings.x2, settings.y2))
    if hwnd3 > 0:
        pool.apply_async(putian.putian,
                         args=(hwnd3, settings.x3, settings.y3))
    if hwnd4 > 0:
        pool.apply_async(putian.putian,
                         args=(hwnd4, settings.x4, settings.y4))
    if hwnd5 > 0:
        pool.apply_async(putian.putian,
                         args=(hwnd5, settings.x5, settings.y5))
    if hwnd6 > 0:
        pool.apply_async(putian.putian,
                         args=(hwnd6, settings.x6, settings.y6))
    pool.close()
    pool.join()
    time.sleep(random.uniform(1.4, 1.6))

    multiprocessing.freeze_support()
    multiprocessing.log_to_stderr()
    pool = LoggingPool(processes=5)
    if hwnd1 > 0:
        result = pool.apply_async(zudui.join, args=(hwnd1, settings.x1, settings.y1, True))
    if hwnd2 > 0:
        pool.apply_async(zudui.join, args=(hwnd2, settings.x2, settings.y2, False))
    if hwnd3 > 0:
        pool.apply_async(zudui.join, args=(hwnd3, settings.x3, settings.y3, False))
    if hwnd4 > 0:
        pool.apply_async(zudui.join, args=(hwnd4, settings.x4, settings.y4, False))
    if hwnd5 > 0:
        pool.apply_async(zudui.join, args=(hwnd5, settings.x5, settings.y5, False))
    if hwnd6 > 0:
        pool.apply_async(zudui.join, args=(hwnd6, settings.x6, settings.y6, False))
    pool.close()
    pool.join()
    # 可能跨线，多等一会儿
    time.sleep(random.uniform(4.8, 5.2))

    team_num = result.get()
    if team_num >= 3:
        #senddata("开始捉鬼，队伍人数:{}".format(team_num), "")
        pass
    else:
        senddata("队伍人数不足3，为{}，停止运行.".format(team_num), "")
        sys.exit(1)

    multiprocessing.freeze_support()
    multiprocessing.log_to_stderr()
    pool = LoggingPool(processes=5)
    if hwnd1 > 0:
        pool.apply_async(zhuogui.zhuogui,
                         args=(hwnd1, settings.x1, settings.y1, True, settings.hwnd1_skill.get('zhuogui'), True))
    if hwnd2 > 0:
        pool.apply_async(zhuogui.zhuogui,
                         args=(hwnd2, settings.x2, settings.y2, False, settings.hwnd2_skill.get('zhuogui'), True))
    if hwnd3 > 0:
        pool.apply_async(zhuogui.zhuogui,
                         args=(hwnd3, settings.x3, settings.y3, False, settings.hwnd3_skill.get('zhuogui'), True))
    if hwnd4 > 0:
        pool.apply_async(zhuogui.zhuogui,
                         args=(hwnd4, settings.x4, settings.y4, False, settings.hwnd4_skill.get('zhuogui'), True))
    if hwnd5 > 0:
        pool.apply_async(zhuogui.zhuogui,
                         args=(hwnd5, settings.x5, settings.y5, False, settings.hwnd5_skill.get('zhuogui'), True))
    if hwnd6 > 0:
        pool.apply_async(zhuogui.zhuogui,
                         args=(hwnd6, settings.x6, settings.y6, False, settings.hwnd6_skill.get('zhuogui'), True))
    pool.close()
    pool.join()
    time.sleep(random.uniform(1.4, 1.6))

    multiprocessing.freeze_support()
    multiprocessing.log_to_stderr()
    pool = LoggingPool(processes=5)
    if hwnd1 > 0:
        pool.apply_async(fengyao.fengyao,
                         args=(hwnd1, settings.x1, settings.y1, True, settings.hwnd1_skill.get('fengyao'), True))
    if hwnd2 > 0:
        pool.apply_async(fengyao.fengyao,
                         args=(hwnd2, settings.x2, settings.y2, False, settings.hwnd2_skill.get('fengyao'), True))
    if hwnd3 > 0:
        pool.apply_async(fengyao.fengyao,
                         args=(hwnd3, settings.x3, settings.y3, False, settings.hwnd3_skill.get('fengyao'), True))
    if hwnd4 > 0:
        pool.apply_async(fengyao.fengyao,
                         args=(hwnd4, settings.x4, settings.y4, False, settings.hwnd4_skill.get('fengyao'), True))
    if hwnd5 > 0:
        pool.apply_async(fengyao.fengyao,
                         args=(hwnd5, settings.x5, settings.y5, False, settings.hwnd5_skill.get('fengyao'), True))
    if hwnd6 > 0:
        pool.apply_async(fengyao.fengyao,
                         args=(hwnd6, settings.x6, settings.y6, False, settings.hwnd6_skill.get('fengyao'), True))
    pool.close()
    pool.join()
    time.sleep(random.uniform(1.4, 1.6))

    multiprocessing.freeze_support()
    multiprocessing.log_to_stderr()
    pool = LoggingPool(processes=5)
    if hwnd1 > 0:
        pool.apply_async(zudui.leave, args=(hwnd1, settings.x1, settings.y1, True))
    if hwnd2 > 0:
        pool.apply_async(zudui.leave, args=(hwnd2, settings.x2, settings.y2, False))
    if hwnd3 > 0:
        pool.apply_async(zudui.leave, args=(hwnd3, settings.x3, settings.y3, False))
    if hwnd4 > 0:
        pool.apply_async(zudui.leave, args=(hwnd4, settings.x4, settings.y4, False))
    if hwnd5 > 0:
        pool.apply_async(zudui.leave, args=(hwnd5, settings.x5, settings.y5, False))
    if hwnd6 > 0:
        pool.apply_async(zudui.leave, args=(hwnd6, settings.x6, settings.y6, False))
    pool.close()
    pool.join()
    time.sleep(random.uniform(1.4, 1.6))

    multiprocessing.freeze_support()
    multiprocessing.log_to_stderr()
    pool = LoggingPool(processes=5)
    if hwnd1 > 0:
        pool.apply_async(baoshi.baoshi, args=(hwnd1, settings.x1, settings.y1))
    if hwnd2 > 0:
        pool.apply_async(baoshi.baoshi, args=(hwnd2, settings.x2, settings.y2))
    if hwnd3 > 0:
        pool.apply_async(baoshi.baoshi, args=(hwnd3, settings.x3, settings.y3))
    if hwnd4 > 0:
        pool.apply_async(baoshi.baoshi, args=(hwnd4, settings.x4, settings.y4))
    if hwnd5 > 0:
        pool.apply_async(baoshi.baoshi, args=(hwnd5, settings.x5, settings.y5))
    if hwnd6 > 0:
        pool.apply_async(baoshi.baoshi, args=(hwnd6, settings.x6, settings.y6))
    pool.close()
    pool.join()
    time.sleep(random.uniform(1.4, 1.6))

    multiprocessing.freeze_support()
    multiprocessing.log_to_stderr()
    pool = LoggingPool(processes=5)
    if hwnd1 > 0:
        pool.apply_async(task.task,
                         args=(hwnd1, settings.x1, settings.y1, "hwnd1", "baotu", "jingji", "shilian", "sichou", "huoban", "keju"))
    if hwnd2 > 0:
        pool.apply_async(task.task,
                         args=(hwnd2, settings.x2, settings.y2, "hwnd2", "baotu", "jingji", "shilian", "sichou", "huoban", "keju"))
    if hwnd3 > 0:
        pool.apply_async(task.task,
                         args=(hwnd3, settings.x3, settings.y3, "hwnd3", "baotu", "jingji", "shilian", "sichou", "huoban", "keju"))
    if hwnd4 > 0:
        pool.apply_async(task.task,
                         args=(hwnd4, settings.x4, settings.y4, "hwnd4", "baotu", "jingji", "shilian", "sichou", "huoban", "keju"))
    if hwnd5 > 0:
        pool.apply_async(task.task,
                         args=(hwnd5, settings.x5, settings.y5, "hwnd5", "baotu", "jingji", "shilian", "sichou"))
    if hwnd6 > 0:
        pool.apply_async(task.task,
                         args=(hwnd6, settings.x6, settings.y6, "hwnd6", "baotu", "jingji", "shilian", "sichou"))
    pool.close()
    pool.join()