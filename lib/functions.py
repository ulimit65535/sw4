import ctypes
import psutil
import cv2
import win32gui, win32con, win32ui, win32api
import numpy as np
import time
import random
import sys
import os

from etc import settings

button_quxiao_img = cv2.cvtColor(cv2.imread("src/button_quxiao.png"), cv2.COLOR_BGR2GRAY)
button_quxiao_img_color = cv2.cvtColor(cv2.imread("src/button_quxiao.png"), cv2.IMREAD_COLOR)


def kill_proc_tree(pid, including_parent=True):
    parent = psutil.Process(pid)
    children = parent.children(recursive=True)
    for child in children:
        child.kill()
    gone, still_alive = psutil.wait_procs(children, timeout=5)
    if including_parent:
        parent.kill()
        parent.wait(5)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def window_capture(hwnd, x, y, color=cv2.COLOR_BGR2GRAY):
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bot - top
    hwndDC = win32gui.GetWindowDC(hwnd)
    srcDC = win32ui.CreateDCFromHandle(hwndDC)
    memDC = srcDC.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcDC, w, h)
    memDC.SelectObject(bmp)
    memDC.BitBlt((0, 0), (w, h), srcDC, (0, 0), win32con.SRCCOPY)

    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (h, w, 4)

    srcDC.DeleteDC()
    memDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    win32gui.DeleteObject(bmp.GetHandle())

    src_img = cv2.cvtColor(img, color)

    if color == cv2.COLOR_BGR2GRAY:
        points = get_match_points(src_img, button_quxiao_img)
    else:
        points = get_match_points(src_img, button_quxiao_img_color)
    if points:
        # 弹窗统一点取消
        pos = points[0]
        randint_x = random.randint(10, 60)
        randint_y = random.randint(10, 25)
        window_click(hwnd, pos, randint_x, randint_y)
        time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

        left, top, right, bot = win32gui.GetWindowRect(hwnd)
        w = right - left
        h = bot - top
        hwndDC = win32gui.GetWindowDC(hwnd)
        srcDC = win32ui.CreateDCFromHandle(hwndDC)
        memDC = srcDC.CreateCompatibleDC()
        bmp = win32ui.CreateBitmap()
        bmp.CreateCompatibleBitmap(srcDC, w, h)
        memDC.SelectObject(bmp)
        memDC.BitBlt((0, 0), (w, h), srcDC, (0, 0), win32con.SRCCOPY)

        signedIntsArray = bmp.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (h, w, 4)

        srcDC.DeleteDC()
        memDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, hwndDC)
        win32gui.DeleteObject(bmp.GetHandle())
        src_img = cv2.cvtColor(img, color)
    return src_img


def get_match_points(src_img, template_img, threshold=0.9):
    res = cv2.matchTemplate(src_img, template_img, cv2.TM_CCOEFF_NORMED)
    points = []
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        points.append(pt)
    return points


# 提供相对坐标
def window_click(hwnd, client_pos, randint_x, randint_y):
    tmp = win32api.MAKELONG(client_pos[0] + randint_x, client_pos[1] + randint_y)
    win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
    time.sleep(random.uniform(0.07, 0.08))
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)


# 鼠标拖动
def window_mouse_move(hwnd, start_pos, end_pos, randint_x, randint_y):
    start_x = start_pos[0] + randint_x
    start_y = start_pos[1] + randint_y
    end_x = end_pos[0] + randint_x
    end_y = end_pos[1] + randint_y

    start = win32api.MAKELONG(start_x, start_y)
    end = win32api.MAKELONG(end_x, end_y)
    win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, start)
    time.sleep(random.uniform(0.40, 0.60))

    temp_x = start_x
    temp_y = start_y
    while True:
        time.sleep(random.uniform(0.01, 0.02))
        if temp_y < end_y:
            temp_y += random.randint(0, 10)
        elif temp_y > end_y:
            temp_y += random.randint(-10, 0)
        else:
            temp_y += random.randint(-10, 10)

        if temp_x < end_x:
            temp_x += 10
        elif temp_x > end_x:
            temp_x -= 10

        if abs(temp_x - end_x) <= 10:
            temp_x = end_x

        temp = win32api.MAKELONG(temp_x, temp_y)
        win32gui.SendMessage(hwnd, win32con.WM_MOUSEMOVE, 0, temp)

        if temp_x == end_x:
            break

    time.sleep(random.uniform(0.40, 0.60))
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, end)


# 鼠标按住不动
def window_mouse_down(hwnd, client_pos, randint_x, randint_y, randsec_start, randsec_end):
    tmp = win32api.MAKELONG(client_pos[0] + randint_x, client_pos[1] + randint_y)
    win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
    time.sleep(random.uniform(randsec_start, randsec_end))
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)