from etc import settings
import sys, os
import random
import time

from lib.functions import window_mouse_move

try:
    darknet_dir = settings.darknet_dir

except:
    darknet_dir = None

if darknet_dir:
    sys.path.append(darknet_dir)
    from darknet import load_net, load_meta, detect

if __name__ == '__main__':
    lock_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "yanzheng.lock")

    is_lock = True
    for i in range(30):
        if os.path.exists(lock_file):
            time.sleep(1)
        else:
            is_lock = False
            break

    if is_lock:
        print("等待30秒后，文件锁依然存在，退出。")
        sys.exit(1)

    try:
        hwnd = int(sys.argv[1])
        image_file = sys.argv[2]
    except:
        print("未提供窗口句柄或图片地址.")
        sys.exit(1)

    # 创建文件锁
    open(lock_file,"w+").close()

    cfg_file = bytes(os.path.join(darknet_dir, "cfg/yolov3-sw.cfg_test"), encoding="utf8")
    weights_file = bytes(os.path.join(darknet_dir, "backup/yolov3-sw_5000.weights"), encoding="utf8")
    data_file = bytes(os.path.join(darknet_dir, "data/sw.data"), encoding="utf8")
    img = bytes(image_file, encoding="utf8")

    try:
        net = load_net(cfg_file, weights_file, 0)
        meta = load_meta(data_file)
        result = detect(net, meta, img)
        x, y, w, h = result[0][2]
        target_x = int(x)
    except:
        print("未找到target坐标.")
        # 删除文件锁
        os.remove(lock_file)
        sys.exit(1)

    # 删除文件锁
    os.remove(lock_file)

    # 验证截图x偏移坐标
    left = 230

    start_pos = (2190 - 1927, 559 - 156)
    end_pos = (left + target_x, 559 - 156)
    randint_x = random.randint(-2, 2)
    randint_y = random.randint(-2, 2)
    window_mouse_move(hwnd, start_pos, end_pos, randint_x, randint_y)