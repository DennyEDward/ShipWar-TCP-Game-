from ShWr_GameMode import *
import os
import time
import random
from ShWr_game_setting import *


LOGO = '___________^____________\n|                       |\n<<<====  ShipWar  ====>>>\n|                       |\n___________v____________'


class ShWr_UI:
    def __init__(self):
        CL, IPGOT = game_setting()
        name = self.User_name(CL)
        self.UI_game_mode(name, CL,IPGOT)

    def User_name(self, CL):
        while True:
            os.system(CL)
            print(LOGO)
            print()
            user_name = input("请输入您的姓名:")
            if user_name == '':
                continue

            print("您将被称为[%s]舰长,确定使用此名字吗?\n1. 确定\n2. 重命名 " % (user_name))
            gamer_choose = input('>>>:')
            if gamer_choose == '2':
                os.system(CL)
                continue
            elif gamer_choose == '1' or gamer_choose == '':
                break
            else:
                print('输入有误,请重命名')
                time.sleep(1.5)
                os.system(CL)
                continue
        os.system(CL)
        print(LOGO)
        print()
        return user_name

    def UI_game_mode(self, user_name, CL,IPGOT):

        while True:
            print("您好,尊敬的[%s]舰长,请选择您的游戏模式" % (user_name))
            print('1键. 游戏说明\n2键. 双人模式\n3键. 关于游戏\n4键. 关于开发者\nn键. 退出游戏')
            try:
                gamer_choose = input('请选择:')
                # game_start = GameMode()

                if gamer_choose == '1':
                    os.system(CL)
                    print(LOGO)
                    print()
                    print('游戏说明:')
                    print()
                    print('该游戏是[双人联机]博弈的[益智类]游戏,\n您需要在游戏内合理的管理自己的[战舰群体]\n同时通过[计算与记忆],争取歼灭对方的舰队\n更多的游戏规则您可以在游戏中使用[阅读]\n希望您喜欢~')

                    time.sleep(2)
                    print()
                    input('回车确认')
                    os.system(CL)
                    print(LOGO)
                    print()
                    continue

                    # game_start.solo_game()
                elif gamer_choose == '2':
                    self.double_game_start(user_name, CL,IPGOT)
                elif gamer_choose == '3':
                    self.game_txt(CL)
                elif gamer_choose == '4':
                    self.about_game_writer(CL)
                elif gamer_choose == '':
                    os.system(CL)
                    print(LOGO)
                    continue
                else:
                    print('链接中断,再见,亲爱的舰长')
                    time.sleep(1)
                    return
            except BrokenPipeError :
                print('恭喜您,您获胜了!!!!')
                time.sleep(1)
                winner = '恭喜您获得称号'
                ran = random.randint(0,9)
                ranlist = ['[火力全开的舰长]','[沉着冷静的舰长]','[顾全大局的舰长]','[实力碾压的舰长]','[鱼雷达人]','[天雷滚滚]','[海军总司令]','[海军上将]','[海军统帅]','[蹦擦蹦擦擦]']
                winner += ranlist[ran]
                print(winner)
                time.sleep(1)
                print()
                print('游戏结束,辛苦了,[%s]舰长' % user_name)
                input('回车返回主界面')
                self.UI_game_mode( user_name, CL, IPGOT)
            except:
                print('游戏结束,正在断开链接,辛苦了,[%s]舰长'%user_name)
                time.sleep(1)
                return

    def double_game_start(self, user_name, CL,IPGOT):

        while True:
            os.system(CL)
            print(LOGO)
            print()
            print('1. 创建房间\n2. 加入游戏\n3.返回主画面')
            self.__gamer_choose = input('请选择:')
            if self.__gamer_choose == '1':
                Double_game().create_room(user_name, CL,IPGOT)
            elif self.__gamer_choose == '2':
                Double_game().join_room(user_name, CL,IPGOT)
            elif self.__gamer_choose == '3':
                os.system(CL)
                print(LOGO)
                return
            else:
                print("输入有误,请重新选择")
                time.sleep(1.5)
                continue

        pass

    def game_txt(self,CL):
        os.system(CL)
        print(LOGO)
        print()
        print('游戏版本 : 1.0.7 - 2019')
        print()
        print('游戏日志 : ')
        print('* 改进了联机中的准备机制,取消了房主优先准备\n -现在双方可以分别提前准备就绪,等待对方就绪\n* 追加对windows平台的支持\n* 调整鱼雷刷新频率,改为一局刷新\n* 船只血量从原本的1血升为3血\n -避免了鱼雷+坐标连击combo直接带走的情况\n* 为了双方友好竞争及个人安全问题,取消了游戏内嘲讽功能\n')
        print('改进计划 : ')
        print('* 预计增加[单人游戏功能],AI系统策划中...\n* 预计优化[界面UI]问题...\n* 预计找个对象...')
        time.sleep(2)
        print()
        input('回车确认')
        os.system(CL)
        print(LOGO)
        return

    def about_game_writer(self,CL):
        os.system(CL)
        print(LOGO)
        print()
        print('游戏作者      孙百韬(tao)')
        print('              Denny-Edward ')
        print()
        print('工具          python 3 - Ubuntu 12.0')
        print()
        print('特别鸣谢:')
        print('              充足的五一假期')
        print('              妈妈做的不怎么好吃的黄瓜')
        print('              身边的朋友')
        print('              酷狗音乐里的歌单')
        print('              半条巧克力,一瓶芒果汁')
        print('              两根泰山[平安]')
        print('              时好时坏的搜狗输入法')
        print('')
        print('注:           游戏内有一个关于[用户名]和[鱼雷]的彩蛋')
        print('              希望你能喜欢')
        time.sleep(2)
        print()
        input('回车确认')
        os.system(CL)
        print(LOGO)
        return


if __name__ == '__main__':
    ShWr_UI()
