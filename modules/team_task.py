from . import zhuogui, fengyao, guaye, qiangdao, menpai, wuqiguo, sanjie, fuben, hunshi, guixu, huanjing, huanjing_kaixiang
from etc import settings


def task(hwnd, x, y, hwndname, *args):
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

    taskname = args[0]
    if taskname == "捉鬼":
        is_leader = args[1]
        zhuogui.zhuogui(hwnd, x, y, is_leader, skill.get('zhuogui'))
    elif taskname == "封妖":
        is_leader = args[1]
        fengyao.fengyao(hwnd, x, y, is_leader, skill.get('fengyao'))
    elif taskname == "无限封妖":
        fengyao.fengyao_unlimited(hwnd, x, y)
    elif taskname == "挂野":
        is_leader = args[1]
        guaye.guaye(hwnd, x, y, is_leader, skill.get('guaye'))
    elif taskname == "帮派强盗":
        is_leader = args[1]
        qiangdao.qiangdao(hwnd, x, y, is_leader, skill.get('qiangdao'))
    elif taskname == "门派闯关":
        is_leader = args[1]
        menpai.menpai(hwnd, x, y, is_leader, skill.get('menpai'))
    elif taskname == "无启国":
        wuqiguo.wuqiguo(hwnd, x, y)
    elif taskname == "三界悬赏":
        is_leader = args[1]
        sanjie.sanjie(hwnd, x, y, is_leader, skill.get('sanjie'))
    elif taskname == "副本":
        is_leader = args[1]
        fuben.fuben(hwnd, x, y, is_leader, skill.get('fuben'))
    elif taskname == "魂石争夺战":
        hunshi.hunshi(hwnd, x, y)
    elif taskname == "归墟乱斗":
        is_leader = args[1]
        guixu.guixu(hwnd, x, y, is_leader)
    elif taskname == "幻境寻宝":
        huanjing.huanjing(hwnd, x, y)
    elif taskname == "幻境开箱":
        is_leader = args[1]
        huanjing_kaixiang.huanjing_kaixiang(hwnd, x, y, is_leader)

