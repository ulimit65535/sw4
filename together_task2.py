import sys
import multiprocessing
import random
import time
import os
import subprocess

from etc import settings
from modules import zudui, task, baoshi
from lib.loggingpool import LoggingPool


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
                         args=(hwnd1, settings.x1, settings.y1, "hwnd1", "baotu", "jingji", "shilian", "huoban"))
    if hwnd2 > 0:
        pool.apply_async(task.task,
                         args=(hwnd2, settings.x2, settings.y2, "hwnd2", "baotu", "jingji", "shilian", "huoban"))
    if hwnd3 > 0:
        pool.apply_async(task.task,
                         args=(hwnd3, settings.x3, settings.y3, "hwnd3", "baotu", "jingji", "shilian", "huoban"))
    if hwnd4 > 0:
        pool.apply_async(task.task,
                         args=(hwnd4, settings.x4, settings.y4, "hwnd4", "baotu", "jingji", "shilian", "huoban"))
    if hwnd5 > 0:
        pool.apply_async(task.task,
                         args=(hwnd5, settings.x5, settings.y5, "hwnd5", "baotu", "jingji", "shilian"))
    if hwnd6 > 0:
        pool.apply_async(task.task,
                         args=(hwnd6, settings.x6, settings.y6, "hwnd6", "baotu", "jingji", "shilian"))
    pool.close()
    pool.join()