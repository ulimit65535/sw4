import time
import os
import subprocess
import win32gui

from etc import settings


if __name__ == '__main__':
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