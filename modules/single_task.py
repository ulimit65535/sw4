from . import sichou, yanhui, wabao, shilian, huoban, renwulian, keju, jianxueren, mingrifangzhou, taolaile, shimen, zhuxian
from etc import settings


def task(hwnd, x, y, hwndname, taskname):
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

    if taskname == "丝绸之路":
        sichou.sichou(hwnd, x, y)
    if taskname == "师门任务":
        shimen.shimen(hwnd, x, y)
    elif taskname == "帮派宴会":
        if hwndname == "hwnd1":
            yanhui.yanhui(hwnd, x, y, jianlihua=True)
        else:
            yanhui.yanhui(hwnd, x, y)
    elif taskname == "自动挖宝":
        wabao.wabao(hwnd, x, y)
    elif taskname == "英雄试炼":
        shilian.shilian(hwnd, x, y, skill.get('shilian'))
    elif taskname == "伙伴任务":
        huoban.huoban(hwnd, x, y, skill.get('huoban'))
    elif taskname == "任务链":
        renwulian.renwulian(hwnd, x, y)
    elif taskname == "科举答题":
        keju.keju(hwnd, x, y)
    elif taskname == "捡雪人":
        jianxueren.jianxueren(hwnd, x, y)
    elif taskname == "明日方舟":
        mingrifangzhou.mingrifangzhou(hwnd, x, y)
    elif taskname == "桃来了":
        taolaile.taolaile(hwnd, x, y)
    elif taskname == "主线任务":
        zhuxian.zhuxian(hwnd, x, y)
