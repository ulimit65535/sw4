import threading
import time
import ctypes
import win32gui, win32con
import subprocess
import os
import cv2
import random

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from multiprocessing import Process


from lib.functions import kill_proc_tree, is_admin, window_click, window_capture, get_match_points
from etc import settings
from modules import public, renwulian, fengyao, baoshi, zudui, zhuogui, shaxing, guaye, qiangdao, task, yanhui, shilian, sichou, single_task, team_task, mingrifangzhou, gongzhulianjie
from lib.wechat import senddata

class AppUI():
    def __init__(self):
        self.hwnd1 = 0
        self.hwnd2 = 0
        self.hwnd3 = 0
        self.hwnd4 = 0
        self.hwnd5 = 0
        self.hwnd6 = 0

        self.hwnd1_main = 0
        self.hwnd2_main = 0
        self.hwnd3_main = 0
        self.hwnd4_main = 0
        self.hwnd5_main = 0
        self.hwnd6_main = 0

        self.process1 = None
        self.process2 = None
        self.process3 = None
        self.process4 = None
        self.process5 = None
        self.process6 = None
        self.subprocess = None

        self.running = None

        # 从小到大排窗口
        self.hwnd_order = 0

        root = Tk()

        lf1 = ttk.Frame(root)
        lf1.pack(side=LEFT, fill=X, anchor=NW, padx=5, pady=5)

        lf1_0 = ttk.Frame(lf1)
        lf1_0.pack(side=TOP, fill=Y)

        lf1_1 = ttk.LabelFrame(lf1_0, text="启动")
        lf1_1.pack(side=LEFT, anchor=NW, fill=Y, padx=5, pady=5)

        lf1_2 = ttk.LabelFrame(lf1_0, text="功能")
        lf1_2.pack(side=RIGHT, anchor=NW, fill=Y, padx=5, pady=5)

        lf1_3 = ttk.Frame(lf1)
        lf1_3.pack(side=TOP, fill=Y, padx=5, pady=5)

        self.msglist = Text(lf1_3, width=50, height=28)
        self.msglist.pack(side=LEFT, fill=Y)
        self.msglist.tag_config('important', foreground='blue')
        self.msglist.tag_config('warning', foreground='red')
        scroll = Scrollbar(lf1_3)
        self.msglist.configure(yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT, fill=Y)

        lf2 = ttk.Frame(root)
        lf2.pack(side=LEFT, fill=X, anchor=NE, padx=5, pady=5)

        lf2_0 = ttk.LabelFrame(lf2, text="杀星")
        lf2_0.pack(side=TOP, fill=Y, padx=5, pady=5)

        lf2_1 = ttk.LabelFrame(lf2, text="单人任务")
        lf2_1.pack(side=TOP, fill=Y, padx=5, pady=5)

        lf2_3 = ttk.LabelFrame(lf2, text="组队任务")
        lf2_3.pack(side=TOP, fill=Y, padx=5, pady=5)

        lf2_2 = ttk.LabelFrame(lf2, text="一条")
        lf2_2.pack(side=TOP, fill=Y, padx=5, pady=5)

        lf2_4 = ttk.LabelFrame(lf2, text="其它游戏")
        lf2_4.pack(side=TOP, fill=Y, padx=5, pady=5)

        self.shaxing_target = StringVar()
        self.cbx_shaxing_target = ttk.Combobox(lf2_0, textvariable=self.shaxing_target, width=6, state='readonly')
        self.cbx_shaxing_target["values"] = ("", "28星宿", "妖王神器", "36天罡")
        self.cbx_shaxing_target.current(0)
        self.cbx_shaxing_target.pack(side=TOP, padx=2, pady=2, fill=X)

        self.btn_shaxing = ttk.Button(lf2_0, text="杀星", state=DISABLED, command=self.run_shaxing)
        self.btn_shaxing.pack(side=TOP, padx=2, pady=2, fill=X)

        self.single_task = StringVar()
        self.cbx_single_task = ttk.Combobox(lf2_1, textvariable=self.single_task, width=6, state='readonly')
        self.cbx_single_task["values"] = ("丝绸之路", "帮派宴会", "自动挖宝", "科举答题", "桃来了", "主线任务", "任务链", "师门任务")
        self.cbx_single_task.current(0)
        self.cbx_single_task.pack(side=TOP, padx=2, pady=2, fill=X)

        self.btn_single_task = ttk.Button(lf2_1, text="开始任务", state=DISABLED, command=self.run_single_task)
        self.btn_single_task.pack(side=TOP, padx=2, pady=2, fill=X)

        self.team_task = StringVar()
        self.cbx_team_task = ttk.Combobox(lf2_3, textvariable=self.team_task, width=6, state='readonly')
        self.cbx_team_task["values"] = ("帮派强盗", "三界悬赏", "门派闯关", "幻境寻宝", "副本", "挂野", "无限封妖", "捉鬼", "封妖")
        self.cbx_team_task.current(0)
        self.cbx_team_task.pack(side=TOP, padx=2, pady=2, fill=X)

        self.btn_team_task = ttk.Button(lf2_3, text="开始任务", state=DISABLED, command=self.run_team_task)
        self.btn_team_task.pack(side=TOP, padx=2, pady=2, fill=X)

        """
        self.is_target_28 = IntVar()
        self.chx_is_target_28 = Checkbutton(lf2_0, text="28", variable=self.is_target_28)
        self.chx_is_target_28.pack(side=LEFT, padx=3, fill=X)

        self.is_target_yaowang = IntVar()
        self.chx_is_target_yaowang = Checkbutton(lf2_0, text="妖王", variable=self.is_target_yaowang)
        self.chx_is_target_yaowang.pack(side=LEFT, padx=3, fill=X)

        self.is_target_36 = IntVar()
        self.chx_is_target_36 = Checkbutton(lf2_0, text="36", variable=self.is_target_36)
        self.chx_is_target_36.pack(side=LEFT, padx=3, fill=X)
        """
        frame1 = Frame(lf1_1)
        frame1.pack(fill=X, side=TOP, padx=5, pady=5)

        self.btn_open = ttk.Button(frame1, text="多开", width=6, command=self.open)
        self.btn_open_all = ttk.Button(frame1, text="3/5", width=6, command=self.open_all)
        self.btn_start = ttk.Button(frame1, text="开始", width=6, command=self.start)
        self.btn_close = ttk.Button(frame1, text="强关", width=6, command=self.close)
        self.btn_open.pack(side=LEFT, padx=2, fill=X)
        self.btn_open_all.pack(side=LEFT, padx=2, fill=X)
        self.btn_start.pack(side=LEFT, padx=2, fill=X)
        self.btn_close.pack(side=LEFT, padx=2, fill=X)

        frame2 = Frame(lf1_2)
        frame2.pack(fill=X, side=TOP, padx=5, pady=5)

        self.btn_baoshi = ttk.Button(frame2, text="饱食", width=6, state=DISABLED, command=self.run_baoshi)
        self.btn_zudui = ttk.Button(frame2, text="组队", width=6, state=DISABLED, command=self.run_zudui)
        self.btn_baoshi.pack(side=LEFT, padx=2, fill=X)
        self.btn_zudui.pack(side=LEFT, padx=2, fill=X)

        #frame3 = Frame(lf2_2)
        #frame3.pack(fill=X, side=TOP, padx=5, pady=5)
        self.btn_task1 = ttk.Button(lf2_2, text="验证一条", state=DISABLED, command=self.run_task1)
        self.btn_task2 = ttk.Button(lf2_2, text="无验证一条", state=DISABLED, command=self.run_task2)
        self.btn_sichou = ttk.Button(lf2_2, text="暂无", state=DISABLED, command=self.run_test)
        self.btn_shilian = ttk.Button(lf2_2, text="暂无", state=DISABLED, command=self.run_test)
        self.btn_renwulian = ttk.Button(lf2_2, text="暂无", state=DISABLED, command=self.run_test)
        self.btn_task1.pack(side=TOP, padx=2, pady=2, fill=X)
        self.btn_task2.pack(side=TOP, padx=2, pady=2, fill=X)
        #self.btn_sichou.pack(side=TOP, padx=2, pady=2, fill=X)
        #self.btn_shilian.pack(side=TOP, padx=2, pady=2, fill=X)
        #self.btn_renwulian.pack(side=TOP, padx=2, pady=2, fill=X)

        #frame4 = Frame(lf2_4)
        #frame4.pack(fill=X, side=TOP, padx=5, pady=5)
        #self.btn_team_task = ttk.Button(frame4, text="组队捉鬼", state=DISABLED, command=self.run_zhuogui)
        self.other_task = StringVar()
        self.cbx_other_task = ttk.Combobox(lf2_4, textvariable=self.other_task, width=6, state='readonly')
        self.cbx_other_task["values"] = ("进入游戏", "捐赠点赞", "地下城助战", "其它日常", "无限战斗")
        self.cbx_other_task.current(0)
        self.cbx_other_task.pack(side=TOP, padx=2, pady=2, fill=X)
        self.btn_other = ttk.Button(lf2_4, text="开始任务", state=DISABLED, command=self.run_other)
        self.btn_guaye = ttk.Button(lf2_4, text="暂无", state=DISABLED, command=self.run_test)
        self.btn_qiangdao = ttk.Button(lf2_4, text="暂无", state=DISABLED, command=self.run_test)
        #self.btn_team_task.pack(side=TOP, padx=2, pady=2, fill=X)
        self.btn_other.pack(side=TOP, padx=2, pady=2, fill=X)
        #self.btn_guaye.pack(side=TOP, padx=2, pady=2, fill=X)
        #self.btn_qiangdao.pack(side=TOP, padx=2, pady=2, fill=X)

        root.title("工作报告.xlsx - Excel")
        root.update()
        root.resizable(False, False)

        width = root.winfo_width()
        height = root.winfo_height()
        # screenwidth = root.winfo_screenwidth()
        # screenheight = root.winfo_screenheight()
        # size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
        size = '%dx%d+%d+%d' % (width, height, 280, 550)
        root.geometry(size)

        monitor = threading.Thread(target=self.monitor_process)
        monitor.setDaemon(True)
        monitor.start()

        root.mainloop()

    def monitor_process(self):
        while True:
            if self.process1 or self.process2 or self.process3 or self.process4 or self.process5 or self.subprocess:
                # 任务正在进行
                while True:
                    time.sleep(1)
                    if self.process1:
                        if self.process1.is_alive():
                            continue
                    if self.process2:
                        if self.process2.is_alive():
                            continue
                    if self.process3:
                        if self.process3.is_alive():
                            continue
                    if self.process4:
                        if self.process4.is_alive():
                            continue
                    if self.process5:
                        if self.process5.is_alive():
                            continue
                    if self.process6:
                        if self.process6.is_alive():
                            continue
                    if self.subprocess:
                        if self.subprocess.poll() is None:
                            continue

                    self.btn_task2.state(['!pressed', '!disabled'])
                    self.btn_task1.state(['!pressed', '!disabled'])
                    self.btn_single_task.state(['!pressed', '!disabled'])
                    self.btn_sichou.state(['!pressed', '!disabled'])
                    self.btn_shilian.state(['!pressed', '!disabled'])
                    self.btn_renwulian.state(['!pressed', '!disabled'])
                    self.btn_shaxing.state(['!pressed', '!disabled'])
                    self.btn_guaye.state(['!pressed', '!disabled'])
                    self.btn_team_task.state(['!pressed', '!disabled'])
                    self.btn_other.state(['!pressed', '!disabled'])
                    self.btn_zudui.state(['!pressed', '!disabled'])
                    self.btn_baoshi.state(['!pressed', '!disabled'])
                    self.btn_qiangdao.state(['!pressed', '!disabled'])

                    if self.process1:
                        self.process1.terminate()
                        self.process1 = None
                    if self.process2:
                        self.process2.terminate()
                        self.process2 = None
                    if self.process3:
                        self.process3.terminate()
                        self.process3 = None
                    if self.process4:
                        self.process4.terminate()
                        self.process4 = None
                    if self.process5:
                        self.process5.terminate()
                        self.process5 = None
                    if self.process6:
                        self.process6.terminate()
                        self.process6 = None
                    if self.subprocess:
                        try:
                            kill_proc_tree(self.subprocess.pid)
                        except:
                            pass
                        self.subprocess = None

                    if self.running:
                        self.msglist.insert(END, "{}已结束。\n结束时间:{}\n".format(self.running, str(datetime.now())),
                                            'warning')
                        self.msglist.see("end")
                        if self.running not in ["饱食补充", "组队离队", "杀星", "其它任务"]:
                            senddata("{}已结束。结束时间:{}".format(self.running, str(datetime.now())), "")
                    else:
                        # 自己手动关闭的
                        self.msglist.insert(END, "任务已被强制结束。\n结束时间:{}\n".format(str(datetime.now())), 'warning')
                        self.msglist.see("end")

                    break
            else:
                # 任务未开启
                time.sleep(1)
                continue

    def run_test(self):
        pass

    def start(self):
        if self.running:
            if self.process1:
                self.process1.terminate()
            if self.process2:
                self.process2.terminate()
            if self.process3:
                self.process3.terminate()
            if self.process4:
                self.process4.terminate()
            if self.process5:
                self.process5.terminate()
            if self.process6:
                self.process6.terminate()
            if self.subprocess:
                try:
                    kill_proc_tree(self.subprocess.pid)
                except:
                    pass
                self.subprocess = None

        self.process1 = None
        self.process2 = None
        self.process3 = None
        self.process4 = None
        self.process5 = None
        self.process6 = None

        self.hwnd1 = 0
        self.hwnd2 = 0
        self.hwnd3 = 0
        self.hwnd4 = 0
        self.hwnd5 = 0
        self.hwnd6 = 0

        self.running = None
        # 获取模拟器句柄
        self.hwnd1_main = win32gui.FindWindow(settings.hwnd1_windowclass, settings.hwnd1_title)
        self.hwnd2_main = win32gui.FindWindow(settings.hwnd2_windowclass, settings.hwnd2_title)
        self.hwnd3_main = win32gui.FindWindow(settings.hwnd3_windowclass, settings.hwnd3_title)
        self.hwnd4_main = win32gui.FindWindow(settings.hwnd4_windowclass, settings.hwnd4_title)
        self.hwnd5_main = win32gui.FindWindow(settings.hwnd5_windowclass, settings.hwnd5_title)
        self.hwnd6_main = win32gui.FindWindow(settings.hwnd6_windowclass, settings.hwnd6_title)

        if self.hwnd1_main > 0:
            win32gui.MoveWindow(self.hwnd1_main, settings.x1, settings.y1, settings.width, settings.height, True)
            hwndChildList = []
            win32gui.EnumChildWindows(self.hwnd1_main, lambda hwnd, param: param.append(hwnd), hwndChildList)
            self.hwnd1 = hwndChildList[0]
            self.msglist.insert(END, "窗口1句柄:{}\n".format(self.hwnd1))
        if self.hwnd2_main > 0:
            win32gui.MoveWindow(self.hwnd2_main, settings.x2, settings.y2, settings.width, settings.height, True)
            hwndChildList = []
            win32gui.EnumChildWindows(self.hwnd2_main, lambda hwnd, param: param.append(hwnd), hwndChildList)
            # 第二个子窗口句柄
            self.hwnd2 = hwndChildList[0]
            self.msglist.insert(END, "窗口2句柄:{}\n".format(self.hwnd2))
        if self.hwnd3_main > 0:
            win32gui.MoveWindow(self.hwnd3_main, settings.x3, settings.y3, settings.width, settings.height, True)
            hwndChildList = []
            win32gui.EnumChildWindows(self.hwnd3_main, lambda hwnd, param: param.append(hwnd), hwndChildList)
            # 第二个子窗口句柄
            self.hwnd3 = hwndChildList[0]
            self.msglist.insert(END, "窗口3句柄:{}\n".format(self.hwnd3))
        if self.hwnd4_main > 0:
            win32gui.MoveWindow(self.hwnd4_main, settings.x4, settings.y4, settings.width, settings.height, True)
            hwndChildList = []
            win32gui.EnumChildWindows(self.hwnd4_main, lambda hwnd, param: param.append(hwnd), hwndChildList)
            # 第二个子窗口句柄
            self.hwnd4 = hwndChildList[0]
            self.msglist.insert(END, "窗口4句柄:{}\n".format(self.hwnd4))
        if self.hwnd5_main > 0:
            win32gui.MoveWindow(self.hwnd5_main, settings.x5, settings.y5, settings.width, settings.height, True)
            hwndChildList = []
            win32gui.EnumChildWindows(self.hwnd5_main, lambda hwnd, param: param.append(hwnd), hwndChildList)
            # 第二个子窗口句柄
            self.hwnd5 = hwndChildList[0]
            self.msglist.insert(END, "窗口5句柄:{}\n".format(self.hwnd5))
        if self.hwnd6_main > 0:
            win32gui.MoveWindow(self.hwnd6_main, settings.x6, settings.y6, settings.width, settings.height, True)
            hwndChildList = []
            win32gui.EnumChildWindows(self.hwnd6_main, lambda hwnd, param: param.append(hwnd), hwndChildList)
            # 第二个子窗口句柄
            self.hwnd6 = hwndChildList[0]
            self.msglist.insert(END, "窗口6句柄:{}\n".format(self.hwnd6))
        self.msglist.see("end")

        if self.btn_start['text'] == "重置":
            # 再次点击，才会进入游戏
            if self.hwnd1 > 0:
                p = Process(target=public.enter_game, args=(self.hwnd1, settings.x1, settings.y1))
                p.daemon = True
                p.start()
            if self.hwnd2 > 0:
                p = Process(target=public.enter_game, args=(self.hwnd2, settings.x2, settings.y2))
                p.daemon = True
                p.start()
            if self.hwnd3 > 0:
                p = Process(target=public.enter_game, args=(self.hwnd3, settings.x3, settings.y3))
                p.daemon = True
                p.start()
            if self.hwnd4 > 0:
                p = Process(target=public.enter_game, args=(self.hwnd4, settings.x4, settings.y4))
                p.daemon = True
                p.start()
            if self.hwnd5 > 0:
                p = Process(target=public.enter_game, args=(self.hwnd5, settings.x5, settings.y5))
                p.daemon = True
                p.start()
            if self.hwnd6 > 0:
                p = Process(target=public.enter_game, args=(self.hwnd6, settings.x6, settings.y6))
                p.daemon = True
                p.start()

        self.btn_start.config(text="重置")
        self.btn_open.state(['!pressed', '!disabled'])
        self.btn_baoshi.state(['!pressed', '!disabled'])
        self.btn_zudui.state(['!pressed', '!disabled'])
        self.btn_close.state(['!pressed', '!disabled'])
        self.btn_task2.state(['!pressed', '!disabled'])
        self.btn_task1.state(['!pressed', '!disabled'])
        self.btn_single_task.state(['!pressed', '!disabled'])
        self.btn_sichou.state(['!pressed', '!disabled'])
        self.btn_shilian.state(['!pressed', '!disabled'])
        self.btn_renwulian.state(['!pressed', '!disabled'])
        self.btn_shaxing.state(['!pressed', '!disabled'])
        self.btn_guaye.state(['!pressed', '!disabled'])
        self.btn_team_task.state(['!pressed', '!disabled'])
        self.btn_other.state(['!pressed', '!disabled'])
        self.btn_zudui.state(['!pressed', '!disabled'])
        self.btn_baoshi.state(['!pressed', '!disabled'])
        self.btn_qiangdao.state(['!pressed', '!disabled'])

    def open(self):
        file_abs = os.path.join(os.path.dirname(os.path.abspath(__file__)), "open_leidian.py")
        cmd = "pythonw " + file_abs
        subprocess.Popen(cmd, shell=True)

    def open_all(self):
        file_abs = os.path.join(os.path.dirname(os.path.abspath(__file__)), "open_leidian_all.py")
        cmd = "pythonw " + file_abs
        subprocess.Popen(cmd, shell=True)

    def close(self):
        if messagebox.askyesno('提示', "是否强制关闭所有游戏程序?"):
            file_abs = os.path.join(settings.leidian_dir, "dnconsole.exe")
            cmd = file_abs + " " + "quitall"
            subprocess.Popen(cmd, shell=True)
            self.msglist.insert(END, "雷电模拟器已关闭。\n关闭时间:{}\n".format(str(datetime.now())),
                                'warning')
            self.msglist.see("end")

    def run_task1(self):
        self.running = "验证一条"
        self.btn_task2.state(['!pressed', 'disabled'])
        self.btn_task1.state(['pressed', 'disabled'])
        self.btn_single_task.state(['!pressed', 'disabled'])
        self.btn_sichou.state(['!pressed', 'disabled'])
        self.btn_shilian.state(['!pressed', 'disabled'])
        self.btn_renwulian.state(['!pressed', 'disabled'])
        self.btn_shaxing.state(['!pressed', 'disabled'])
        self.btn_guaye.state(['!pressed', 'disabled'])
        self.btn_team_task.state(['!pressed', 'disabled'])
        self.btn_other.state(['!pressed', 'disabled'])
        self.btn_zudui.state(['!pressed', 'disabled'])
        self.btn_baoshi.state(['!pressed', 'disabled'])
        self.btn_qiangdao.state(['!pressed', 'disabled'])

        self.msglist.insert(END, "{}已开始。\n开始时间:{}\n".format(self.running, str(datetime.now())),
                            'important')
        self.msglist.see("end")

        file_abs = os.path.join(os.path.dirname(os.path.abspath(__file__)), "together_task.py")
        # 至少三开
        if self.hwnd1 > 0 and self.hwnd2 > 0 and self.hwnd3:
            cmd = "pythonw " + file_abs + " {} {} {}".format(self.hwnd1, self.hwnd2, self.hwnd3)
            if self.hwnd4 > 0:
                cmd = cmd + " {}".format(self.hwnd4)
            else:
                # 窗口四开启时，5、6不工作
                if self.hwnd5 > 0:
                    cmd = cmd + " {}".format(self.hwnd5)
                    if self.hwnd6 > 0:
                        cmd = cmd + " {}".format(self.hwnd6)
        self.subprocess = subprocess.Popen(cmd, shell=True)
        """
        self.subprocess = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in iter(self.subprocess.stdout.readline, 'b'):
            print(line)
            time.sleep(0.5)
            if not subprocess.Popen.poll(self.subprocess) is None:
                if line == "":
                    break
        self.subprocess.stdout.close()
        """

    def run_task2(self):
        self.running = "无验证一条"
        self.btn_task2.state(['pressed', 'disabled'])
        self.btn_task1.state(['!pressed', 'disabled'])
        self.btn_single_task.state(['!pressed', 'disabled'])
        self.btn_sichou.state(['!pressed', 'disabled'])
        self.btn_shilian.state(['!pressed', 'disabled'])
        self.btn_renwulian.state(['!pressed', 'disabled'])
        self.btn_shaxing.state(['!pressed', 'disabled'])
        self.btn_guaye.state(['!pressed', 'disabled'])
        self.btn_team_task.state(['!pressed', 'disabled'])
        self.btn_other.state(['!pressed', 'disabled'])
        self.btn_zudui.state(['!pressed', 'disabled'])
        self.btn_baoshi.state(['!pressed', 'disabled'])
        self.btn_qiangdao.state(['!pressed', 'disabled'])

        self.msglist.insert(END, "{}已开始。\n开始时间:{}\n".format(self.running, str(datetime.now())),
                            'important')
        self.msglist.see("end")

        file_abs = os.path.join(os.path.dirname(os.path.abspath(__file__)), "together_task2.py")
        cmd = "pythonw " + file_abs

        if self.hwnd1 > 0:
            cmd = cmd + " {}".format(self.hwnd1)
        if self.hwnd2 > 0:
            cmd = cmd + " {}".format(self.hwnd2)
        if self.hwnd3 > 0:
            cmd = cmd + " {}".format(self.hwnd3)
        if self.hwnd4 > 0:
            cmd = cmd + " {}".format(self.hwnd4)
        else:
            # 窗口4开启时，5、6不工作
            if self.hwnd5 > 0:
                cmd = cmd + " {}".format(self.hwnd5)
                if self.hwnd6 > 0:
                    cmd = cmd + " {}".format(self.hwnd6)
        self.subprocess = subprocess.Popen(cmd, shell=True)

    def run_single_task(self):
        self.running = self.single_task.get()
        self.btn_task2.state(['!pressed', 'disabled'])
        self.btn_task1.state(['!pressed', 'disabled'])
        self.btn_single_task.state(['pressed', 'disabled'])
        self.btn_sichou.state(['!pressed', 'disabled'])
        self.btn_shilian.state(['!pressed', 'disabled'])
        self.btn_renwulian.state(['!pressed', 'disabled'])
        self.btn_shaxing.state(['!pressed', 'disabled'])
        self.btn_guaye.state(['!pressed', 'disabled'])
        self.btn_team_task.state(['!pressed', 'disabled'])
        self.btn_other.state(['!pressed', 'disabled'])
        self.btn_zudui.state(['!pressed', 'disabled'])
        self.btn_baoshi.state(['!pressed', 'disabled'])
        self.btn_qiangdao.state(['!pressed', 'disabled'])

        self.msglist.insert(END, "{}已开始。\n开始时间:{}\n".format(self.running, str(datetime.now())),
                            'important')
        self.msglist.see("end")

        if self.single_task.get() not in ["主线任务"]:
            if self.hwnd1 > 0:
                self.process1 = Process(target=single_task.task,
                                        args=(self.hwnd1, settings.x1, settings.y1, "hwnd1", self.single_task.get()))
                self.process1.daemon = True
                self.process1.start()
            if self.hwnd2 > 0:
                self.process2 = Process(target=single_task.task,
                                        args=(self.hwnd2, settings.x2, settings.y2, "hwnd2", self.single_task.get()))
                self.process2.daemon = True
                self.process2.start()
            if self.hwnd3 > 0:
                self.process3 = Process(target=single_task.task,
                                        args=(self.hwnd3, settings.x3, settings.y3, "hwnd3", self.single_task.get()))
                self.process3.daemon = True
                self.process3.start()
            if self.hwnd4 > 0:
                self.process4 = Process(target=single_task.task,
                                        args=(self.hwnd4, settings.x4, settings.y4, "hwnd4", self.single_task.get()))
                self.process4.daemon = True
                self.process4.start()
        if self.single_task.get() not in ["帮派宴会", "任务链", "桃来了", "科举答题"]:
            if self.hwnd5 > 0:
                self.process5 = Process(target=single_task.task,
                                        args=(self.hwnd5, settings.x5, settings.y5, "hwnd5", self.single_task.get()))
                self.process5.daemon = True
                self.process5.start()
            if self.hwnd6 > 0:
                self.process6 = Process(target=single_task.task,
                                        args=(self.hwnd6, settings.x6, settings.y6, "hwnd6", self.single_task.get()))
                self.process6.daemon = True
                self.process6.start()

    def run_team_task(self):
        self.running = self.team_task.get()
        self.btn_task2.state(['!pressed', 'disabled'])
        self.btn_task1.state(['!pressed', 'disabled'])
        self.btn_single_task.state(['!pressed', 'disabled'])
        self.btn_sichou.state(['!pressed', 'disabled'])
        self.btn_shilian.state(['!pressed', 'disabled'])
        self.btn_renwulian.state(['!pressed', 'disabled'])
        self.btn_shaxing.state(['!pressed', 'disabled'])
        self.btn_guaye.state(['!pressed', 'disabled'])
        self.btn_team_task.state(['pressed', 'disabled'])
        self.btn_other.state(['!pressed', 'disabled'])
        self.btn_zudui.state(['!pressed', 'disabled'])
        self.btn_baoshi.state(['!pressed', 'disabled'])
        self.btn_qiangdao.state(['!pressed', 'disabled'])

        self.msglist.insert(END, "{}已开始。\n开始时间:{}\n".format(self.running, str(datetime.now())),
                            'important')
        self.msglist.see("end")

        if self.team_task.get() in ["副本"]:
            if self.hwnd1 > 0:
                self.process1 = Process(target=team_task.task,
                                        args=(self.hwnd1, settings.x1, settings.y1, "hwnd1", self.team_task.get(), True))
                self.process1.daemon = True
                self.process1.start()
            if self.hwnd2 > 0:
                self.process2 = Process(target=team_task.task,
                                        args=(self.hwnd2, settings.x2, settings.y2, "hwnd2", self.team_task.get(), False))
                self.process2.daemon = True
                self.process2.start()
            if self.hwnd3 > 0:
                self.process3 = Process(target=team_task.task,
                                        args=(self.hwnd3, settings.x3, settings.y3, "hwnd3", self.team_task.get(), False))
                self.process3.daemon = True
                self.process3.start()
            if self.hwnd4 > 0:
                self.process4 = Process(target=team_task.task,
                                        args=(self.hwnd4, settings.x4, settings.y4, "hwnd4", self.team_task.get(), False))
                self.process4.daemon = True
                self.process4.start()
        elif self.team_task.get() in ["无启国", "魂石争夺战", "幻境寻宝"]:
            if self.hwnd1 > 0:
                self.process1 = Process(target=team_task.task,
                                        args=(self.hwnd1, settings.x1, settings.y1, "hwnd1", self.team_task.get()))
                self.process1.daemon = True
                self.process1.start()
        elif self.team_task.get() in ["帮派强盗"]:
            file_abs = os.path.join(os.path.dirname(os.path.abspath(__file__)), "together_qiangdao.py")
            # 至少三开
            if self.hwnd1 > 0 and self.hwnd2 > 0 and self.hwnd3:
                cmd = "pythonw " + file_abs + " {} {} {}".format(self.hwnd1, self.hwnd2, self.hwnd3)
                if self.hwnd4 > 0:
                    cmd = cmd + " {}".format(self.hwnd4)
                else:
                    # 窗口4启动，5、6不工作
                    if self.hwnd5 > 0:
                        cmd = cmd + " {}".format(self.hwnd5)
                        if self.hwnd6 > 0:
                            cmd = cmd + " {}".format(self.hwnd6)
            self.subprocess = subprocess.Popen(cmd, shell=True)
        elif self.team_task.get() in ["无限封妖"]:
            if self.hwnd5 > 0:
                self.process5 = Process(target=team_task.task,
                                        args=(self.hwnd5, settings.x5, settings.y5, "hwnd5", self.team_task.get()))
                self.process5.daemon = True
                self.process5.start()
            elif self.hwnd4 > 0:
                self.process4 = Process(target=team_task.task,
                                        args=(self.hwnd4, settings.x4, settings.y4, "hwnd4", self.team_task.get()))
                self.process4.daemon = True
                self.process4.start()
        else:
            if self.hwnd1 > 0:
                self.process1 = Process(target=team_task.task,
                                        args=(self.hwnd1, settings.x1, settings.y1, "hwnd1", self.team_task.get(), True))
                self.process1.daemon = True
                self.process1.start()
            if self.hwnd2 > 0:
                self.process2 = Process(target=team_task.task,
                                        args=(self.hwnd2, settings.x2, settings.y2, "hwnd2", self.team_task.get(), False))
                self.process2.daemon = True
                self.process2.start()
            if self.hwnd3 > 0:
                self.process3 = Process(target=team_task.task,
                                        args=(self.hwnd3, settings.x3, settings.y3, "hwnd3", self.team_task.get(), False))
                self.process3.daemon = True
                self.process3.start()
            if self.hwnd4 > 0:
                self.process4 = Process(target=team_task.task,
                                        args=(self.hwnd4, settings.x4, settings.y4, "hwnd4", self.team_task.get(), False))
                self.process4.daemon = True
                self.process4.start()
            if self.hwnd5 > 0:
                self.process5 = Process(target=team_task.task,
                                        args=(self.hwnd5, settings.x5, settings.y5, "hwnd5", self.team_task.get(), False))
                self.process5.daemon = True
                self.process5.start()
            if self.hwnd6 > 0:
                self.process6 = Process(target=team_task.task,
                                        args=(self.hwnd6, settings.x6, settings.y6, "hwnd6", self.team_task.get(), False))
                self.process6.daemon = True
                self.process6.start()
        
    def run_zudui(self):
        self.running = "组队离队"
        self.btn_task2.state(['!pressed', 'disabled'])
        self.btn_task1.state(['!pressed', 'disabled'])
        self.btn_single_task.state(['!pressed', 'disabled'])
        self.btn_sichou.state(['!pressed', 'disabled'])
        self.btn_shilian.state(['!pressed', 'disabled'])
        self.btn_renwulian.state(['!pressed', 'disabled'])
        self.btn_shaxing.state(['!pressed', 'disabled'])
        self.btn_guaye.state(['!pressed', 'disabled'])
        self.btn_team_task.state(['!pressed', 'disabled'])
        self.btn_other.state(['!pressed', 'disabled'])
        self.btn_zudui.state(['pressed', 'disabled'])
        self.btn_baoshi.state(['!pressed', 'disabled'])
        self.btn_qiangdao.state(['!pressed', 'disabled'])

        self.msglist.insert(END, "{}已开始。\n开始时间:{}\n".format(self.running, str(datetime.now())),
                            'important')
        self.msglist.see("end")

        if self.hwnd1 > 0:
            self.process1 = Process(target=zudui.zudui,
                                    args=(self.hwnd1, settings.x1, settings.y1, True))
            self.process1.daemon = True
            self.process1.start()
        if self.hwnd2 > 0:
            self.process2 = Process(target=zudui.zudui,
                                    args=(self.hwnd2, settings.x2, settings.y2, False))
            self.process2.daemon = True
            self.process2.start()
        if self.hwnd3 > 0:
            self.process3 = Process(target=zudui.zudui,
                                    args=(self.hwnd3, settings.x3, settings.y3, False))
            self.process3.daemon = True
            self.process3.start()
        if self.hwnd4 > 0:
            self.process4 = Process(target=zudui.zudui,
                                    args=(self.hwnd4, settings.x4, settings.y4, False))
            self.process4.daemon = True
            self.process4.start()
        if self.hwnd5 > 0:
            self.process5 = Process(target=zudui.zudui,
                                    args=(self.hwnd5, settings.x5, settings.y5, False))
            self.process5.daemon = True
            self.process5.start()
        if self.hwnd6 > 0:
            self.process6 = Process(target=zudui.zudui,
                                    args=(self.hwnd6, settings.x6, settings.y6, False))
            self.process6.daemon = True
            self.process6.start()

    def run_baoshi(self):
        self.running = "饱食补充"
        self.btn_task2.state(['!pressed', 'disabled'])
        self.btn_task1.state(['!pressed', 'disabled'])
        self.btn_single_task.state(['!pressed', 'disabled'])
        self.btn_sichou.state(['!pressed', 'disabled'])
        self.btn_shilian.state(['!pressed', 'disabled'])
        self.btn_renwulian.state(['!pressed', 'disabled'])
        self.btn_shaxing.state(['!pressed', 'disabled'])
        self.btn_guaye.state(['!pressed', 'disabled'])
        self.btn_team_task.state(['!pressed', 'disabled'])
        self.btn_other.state(['!pressed', 'disabled'])
        self.btn_zudui.state(['!pressed', 'disabled'])
        self.btn_baoshi.state(['pressed', 'disabled'])
        self.btn_qiangdao.state(['!pressed', 'disabled'])

        self.msglist.insert(END, "{}已开始。\n开始时间:{}\n".format(self.running, str(datetime.now())),
                            'important')
        self.msglist.see("end")

        if self.hwnd1 > 0:
            self.process1 = Process(target=baoshi.baoshi,
                                    args=(self.hwnd1, settings.x1, settings.y1))
            self.process1.daemon = True
            self.process1.start()
        if self.hwnd2 > 0:
            self.process2 = Process(target=baoshi.baoshi,
                                    args=(self.hwnd2, settings.x2, settings.y2))
            self.process2.daemon = True
            self.process2.start()
        if self.hwnd3 > 0:
            self.process3 = Process(target=baoshi.baoshi,
                                    args=(self.hwnd3, settings.x3, settings.y3))
            self.process3.daemon = True
            self.process3.start()
        if self.hwnd4 > 0:
            self.process4 = Process(target=baoshi.baoshi,
                                    args=(self.hwnd4, settings.x4, settings.y4))
            self.process4.daemon = True
            self.process4.start()
        if self.hwnd5 > 0:
            self.process5 = Process(target=baoshi.baoshi,
                                    args=(self.hwnd5, settings.x5, settings.y5))
            self.process5.daemon = True
            self.process5.start()
        if self.hwnd6 > 0:
            self.process6 = Process(target=baoshi.baoshi,
                                    args=(self.hwnd6, settings.x6, settings.y6))
            self.process6.daemon = True
            self.process6.start()

    def run_other(self):
        self.running = "其它任务"
        self.btn_task2.state(['!pressed', 'disabled'])
        self.btn_task1.state(['!pressed', 'disabled'])
        self.btn_single_task.state(['!pressed', 'disabled'])
        self.btn_sichou.state(['!pressed', 'disabled'])
        self.btn_shilian.state(['!pressed', 'disabled'])
        self.btn_renwulian.state(['!pressed', 'disabled'])
        self.btn_shaxing.state(['!pressed', 'disabled'])
        self.btn_guaye.state(['!pressed', 'disabled'])
        self.btn_team_task.state(['!pressed', 'disabled'])
        self.btn_other.state(['pressed', 'disabled'])
        self.btn_zudui.state(['!pressed', 'disabled'])
        self.btn_baoshi.state(['!pressed', 'disabled'])
        self.btn_qiangdao.state(['!pressed', 'disabled'])

        self.msglist.insert(END, "{}已开始。\n开始时间:{}\n".format(self.running, str(datetime.now())),
                            'important')
        self.msglist.see("end")

        if self.other_task.get() in ['无限战斗']:
            if self.hwnd4 > 0:
                self.process4 = Process(target=gongzhulianjie.main,
                                        args=(self.hwnd4, settings.x4, settings.y4, self.other_task.get()))
                self.process4.daemon = True
                self.process4.start()
        else:
            if self.hwnd1 > 0:
                self.process1 = Process(target=gongzhulianjie.main,
                                        args=(self.hwnd1, settings.x1, settings.y1, self.other_task.get()))
                self.process1.daemon = True
                self.process1.start()
            if self.hwnd2 > 0:
                self.process2 = Process(target=gongzhulianjie.main,
                                        args=(self.hwnd2, settings.x2, settings.y2, self.other_task.get()))
                self.process2.daemon = True
                self.process2.start()
            if self.hwnd3 > 0:
                self.process3 = Process(target=gongzhulianjie.main,
                                        args=(self.hwnd3, settings.x3, settings.y3, self.other_task.get()))
                self.process3.daemon = True
                self.process3.start()
            if self.hwnd4 > 0:
                self.process4 = Process(target=gongzhulianjie.main,
                                        args=(self.hwnd4, settings.x4, settings.y4, self.other_task.get()))
                self.process4.daemon = True
                self.process4.start()
            if self.hwnd5 > 0:
                self.process5 = Process(target=gongzhulianjie.main,
                                        args=(self.hwnd5, settings.x5, settings.y5, self.other_task.get()))
                self.process5.daemon = True
                self.process5.start()
            if self.hwnd6 > 0:
                self.process6 = Process(target=gongzhulianjie.main,
                                        args=(self.hwnd6, settings.x6, settings.y6, self.other_task.get()))
                self.process6.daemon = True
                self.process6.start()

    def run_shaxing(self):
        self.running = "杀星"
        self.btn_task2.state(['!pressed', 'disabled'])
        self.btn_task1.state(['!pressed', 'disabled'])
        self.btn_single_task.state(['!pressed', 'disabled'])
        self.btn_sichou.state(['!pressed', 'disabled'])
        self.btn_shilian.state(['!pressed', 'disabled'])
        self.btn_renwulian.state(['!pressed', 'disabled'])
        self.btn_shaxing.state(['pressed', 'disabled'])
        self.btn_guaye.state(['!pressed', 'disabled'])
        self.btn_team_task.state(['!pressed', 'disabled'])
        self.btn_other.state(['!pressed', 'disabled'])
        self.btn_zudui.state(['!pressed', 'disabled'])
        self.btn_baoshi.state(['!pressed', 'disabled'])
        self.btn_qiangdao.state(['!pressed', 'disabled'])

        self.msglist.insert(END, "{}已开始。\n开始时间:{}\n".format(self.running, str(datetime.now())),
                            'important')
        self.msglist.see("end")

        if self.hwnd1 > 0:
            self.process1 = Process(target=shaxing.shaxing,
                                    args=(self.hwnd1, settings.x1, settings.y1, self.shaxing_target.get()))
            self.process1.daemon = True
            self.process1.start()


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if __name__ == "__main__":
    # 需要管理员权限
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:
        AppUI()
