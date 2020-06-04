# sw

#### 介绍
自己写的神武手游脚本，需要使用雷电模拟器运行游戏，需要进行如下设置:
1. 模拟器分辨率选择 960x540(dpi 160)
2. 登陆神武手游，打开“省流量减少同屏人数和“迷你坐骑模式”

#### 软件架构
使用opencv的match_template进行图像对比，使用win32api后台发送鼠标操作。


#### 安装教程

1.  下载安装python 3.7.x：https://www.python.org/downloads/
2.  在项目文件夹下，按shift+鼠标右键，打开Powershell，安装依赖：pip install -r requirements.txt
3.  双击main.pyw，运行程序

#### 使用说明
使用编辑器打开项目etc/settings.py，进行相关配置

1.  corpid、corpsecret、wechat_user为微信企业号发送消息配置，需要自己先申请微信企业号，如不配置，将不会发送任何微信通知。
2.  darknet_dir需要另行安装darknet，项目地址:https://github.com/AlexeyAB/darknet。配置后，将使用深度学习自动过验证码。


#### darknet安装使用说明
项目地址:https://github.com/AlexeyAB/darknet。darknet安装步骤网上有很多，请使用GPU版本编译。  
安装完成后，将本项目darknet文件夹下的三个子文件夹，复制到darknet安装目录，并修改darknet/data/sw.data文件中配置的地址为实际安装地址。

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request
