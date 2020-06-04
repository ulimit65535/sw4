from etc import settings
from . import shimen, baotu, jingji, huoban, sichou, shilian, public, keju


def task(hwnd, x, y, hwndname, *tasks):
    if hwndname == "hwnd1":
        skill = settings.hwnd1_skill
    elif hwndname == "hwnd2":
        skill = settings.hwnd2_skill
    elif hwndname == "hwnd3":
        skill = settings.hwnd3_skill
    elif hwndname == "hwnd4":
        skill = settings.hwnd4_skill
    elif hwndname == "hwnd5":
        skill = settings.hwnd5_skill
    elif hwndname == "hwnd6":
        skill = settings.hwnd6_skill

    # 若锁屏，则解锁
    public.jiesuo(hwnd, x, y)

    undo_task_list = public.get_undo_tasks(hwnd, x, y)

    for task in tasks:
        if task in undo_task_list:
            if task == "shimen":
                shimen.shimen(hwnd, x, y, skill.get('shimen'))
            elif task == "baotu":
                baotu.baotu(hwnd, x, y, skill.get('baotu'), True)
            elif task == "sichou":
                sichou.sichou(hwnd, x, y, True)
            elif task == "jingji":
                jingji.jingji(hwnd, x, y, skill.get('jingji'), True)
            elif task == "huoban":
                huoban.huoban(hwnd, x, y, skill.get('huoban'))
            elif task == "shilian":
                shilian.shilian(hwnd, x, y, skill.get('shilian'), True)
        elif task == "keju":
            keju.keju(hwnd, x, y)
