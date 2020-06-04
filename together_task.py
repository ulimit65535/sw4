import sys
import multiprocessing
import random
import time
import os
import subprocess

from etc import settings
from modules import zudui, zhuogui, fengyao, shimen, putian, task
from lib.loggingpool import LoggingPool
from lib.wechat import senddata


if __name__ == '__main__':
    hwnd1 = 0
    hwnd2 = 0
    hwnd3 = 9
    hwnd4 = 0
    hwnd5 = 0
    hwnd6 = 0
    try:
        hwnd1 = int(sys.argv[1])
    except:
        hwnd1 = 0
    try:
        hwnd2 = int(sys.argv[2])
    except:
        hwnd2 = 0
    try:
        hwnd3 = int(sys.argv[3])
    except:
        hwnd3 = 0
    try:
        hwnd4 = int(sys.argv[4])
    except:
        hwnd4 = 0
    # 五开，则窗口4不生效
    if len(sys.argv) == 6:
        hwnd5 = hwnd4
        hwnd4 = 0
        try:
            hwnd6 = int(sys.argv[5])
        except:
            hwnd6 = 0

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
        senddata("开始捉鬼，队伍人数:{}".format(team_num), "")
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