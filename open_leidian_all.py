import time
import os
import subprocess
import win32gui

from etc import settings


if __name__ == '__main__':
    file_abs = os.path.join(settings.leidian_dir, "dnconsole.exe")

    hwnd1 = win32gui.FindWindow(settings.hwnd1_windowclass, settings.hwnd1_title)
    if hwnd1 <= 0:
        cmd = file_abs + " launch --name " + settings.hwnd1_title
        subprocess.Popen(cmd, shell=True)
        time.sleep(1)
    hwnd2 = win32gui.FindWindow(settings.hwnd2_windowclass, settings.hwnd2_title)
    if hwnd2 <= 0:
        cmd = file_abs + " launch --name " + settings.hwnd2_title
        subprocess.Popen(cmd, shell=True)
        time.sleep(1)
    hwnd3 = win32gui.FindWindow(settings.hwnd3_windowclass, settings.hwnd3_title)
    if hwnd3 <= 0:
        cmd = file_abs + " launch --name " + settings.hwnd3_title
        subprocess.Popen(cmd, shell=True)
        time.sleep(1)
    if hwnd1 > 0 or hwnd2 > 0 or hwnd3 > 0:
        # 三个大号开启后，再按，则开启两个小号
        hwnd5 = win32gui.FindWindow(settings.hwnd5_windowclass, settings.hwnd5_title)
        hwnd6 = win32gui.FindWindow(settings.hwnd6_windowclass, settings.hwnd6_title)
        if hwnd5 > 0 and hwnd6 > 0:
            cmd = file_abs + " quit --name " + settings.hwnd5_title
            subprocess.Popen(cmd, shell=True)
            time.sleep(1)
            cmd = file_abs + " quit --name " + settings.hwnd6_title
            subprocess.Popen(cmd, shell=True)
        else:
            if hwnd5 <= 0:
                cmd = file_abs + " launch --name " + settings.hwnd5_title
                subprocess.Popen(cmd, shell=True)
                time.sleep(1)
            if hwnd6 <= 0:
                cmd = file_abs + " launch --name " + settings.hwnd6_title
                subprocess.Popen(cmd, shell=True)
