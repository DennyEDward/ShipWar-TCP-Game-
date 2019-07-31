from socket import *
import os
from select import *
import signal
from ShWr_UI import *
from ShWr_map import *
from ShWr_ship_show import *
from ShWr_game_combo import *
import time
import json
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
import random


class Double_game:

    def run(self):
        pass



    def create_room(self,user_name,CL,IPGOT):
        ship_life_list=[['1号舰',3],['2号舰',3],['3号舰',3],['4号舰',3]]
        os.system(CL)
        for i in range(3):
            print('获取本机ip中', '.' * (i + 1))
            time.sleep(1)
            os.system(CL)
        while True:
            os.system(CL)
            os.system(IPGOT)
            print('**备注:ip号请以INET为主')

            INEIP = input('请输入本机ip:')
            if len(INEIP)<=7 :
                print('格式不对!请重新确认!')
                time.sleep(1)
                continue

            try:
                s = socket()

                s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
                s.settimeout(1.1)
                s.bind((INEIP,55055))
                s.listen(5)
                break
            except:
                print('ip设置有误！请检查是否与INET一致')
                input('回车返回')

        # fork_num = os.fork()
        # if fork_num == 0:
        #     self.wait_gamer(s)
        #     self.send_father(1)
        #     os._exit(0)
        #
        # else:
        #     self.send_father(INEIP,0)
        count = 0
        while True:
            # if count == 30:
            #     break
            count +=1
            os.system(CL)
            print(LOGO)
            print("报告[%s]舰长,您的房间已经创建完毕.\nip号为:"%user_name, INEIP,'      ',40-count)
            print('等待玩家链接','.'*(count%3+1))
            try:
                connfd, addr = s.accept()
                break
            except:
                if count==40:
                    os.system(CL)
                    print(LOGO)
                    print('连接超时!请重新创建链接!')
                    time.sleep(2)
                    return
                continue
        s.settimeout(2000)
        print('链接成功!')
        msg = connfd.recv(1024)
        enemy_name = msg.decode()
        os.system(CL)
        print(LOGO)
        print('[%s]舰长成功与你建立桥接' % (enemy_name))

        msg = user_name.encode()
        connfd.send(msg)
        time.sleep(3)
        my_list = self.place_ship(CL)
        os.system(CL)
        ShWr_map(my_list).show_self_map()
        print("<<====版图完成,请等待对方就绪====>>")

        msg = connfd.recv(1024)
        if msg == b'ok':
            connfd.send(b'ok')
        print('对方已就绪!')

        time.sleep(1.5)
        all_life_list = [['1', 3], ['2', 3], ['3', 3], ['4', 3]]
        view_list = [
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
        ]
        combo_number = random.randint(1,2)
        if combo_number == 1:
            connfd.send(b'enemy')
            print('>>==我方获得先手机会==<<')
            time.sleep(1.5)
            self.first_attack(connfd,view_list,all_life_list,CL)
            game_combo = Game_Combo(connfd, all_life_list, my_list,view_list, CL,1)

            while True:
                flag = 0
                while True:
                    result = game_combo.wait()
                    if result == 1:
                        flag = 1
                        connfd.close()
                        s.close()
                        print(' 您输了,正在退出游戏！')
                        s.send(b'win ')
                        time.sleep(3)
                        return
                    result = game_combo.move()
                    if result == 123:
                        continue
                    elif result == 1:
                        flag = 1
                        connfd.close()
                        s.close()
                        print(' 您输了,正在退出游戏！')
                        s.send(b'win ')
                        time.sleep(3)
                        return
                    else:
                        break
                result = game_combo.round_ship()
                if result == 1:
                    flag = 1
                    connfd.close()
                    s.close()
                    print(' 您输了,正在退出游戏！')
                    s.send(b'win ')
                    time.sleep(3)
                    return
                game_combo.put_boom()
                result = game_combo.attack()
                if flag == 1:
                    break
            connfd.close()
            s.close()
        else:
            connfd.send(b'my')
            print('>>==对方获得先手机会==<<')
            time.sleep(1.5)
            station_str = self.first_wait(connfd,my_list,all_life_list,CL)
            game_combo = Game_Combo(connfd, all_life_list, my_list,view_list, CL,2,station_str)
            while True:
                flag = 0
                while True:

                    result = game_combo.move()
                    if result == 123:
                        continue
                    elif result == 1:
                        flag = 1
                        connfd.close()
                        s.close()
                        print(' 您输了,正在退出游戏！')
                        s.send(b'win ')
                        time.sleep(3)
                        return
                    else:
                        break
                result = game_combo.round_ship()
                if result == 1:
                    flag = 1
                    connfd.close()
                    s.close()
                    print(' 您输了,正在退出游戏！')
                    s.send(b'win ')
                    time.sleep(3)
                    return
                game_combo.put_boom()
                game_combo.attack()
                result = game_combo.wait()
                if result == 1:
                    flag = 1
                    connfd.close()
                    s.close()
                    print(' 您输了,正在退出游戏！')
                    s.send(b'win ')
                    time.sleep(3)
                    return
                if flag == 1:
                    break



    def first_attack(self,s,view_list,ship_life_list,CL):
        while True:
            os.system(CL)
            ShWr_map(view_list).show_enemy_map()
            for i in ship_life_list:
                print(i[0], '号舰血量:[', i[-1], ']', end='--')
            print()
            print('<<=====我方回合=====>>')
            print()
            attack_top = input('请选择要打击的坐标\n格式为(数字和字母):')
            try:
                attack_num = int(attack_top[0])
                attack_word = attack_top[-1]
            except:
                print('格式错误!请重新输入!')
                time.sleep(1)
                continue
            if (attack_num not in list_num) or (attack_word not in list_word_s):
                print('输入有误!请注意数字的值以及区分大小写!')
                time.sleep(1)
                continue
            view_list[attack_num][dict_word_s[attack_word]] = ' X '
            os.system(CL)
            ShWr_map(view_list).show_enemy_map()
            print('打击坐标已在地图中以\'X\'标识!\n')
            time.sleep(1)
            s.send(attack_top.encode())
            msg = s.recv(1024).decode()
            print(msg)
            input('回车确认,结束回合')
            s.send(b'over')
            return







    def first_wait(self,s,my_list,all_life_list,CL) :
        os.system(CL)
        ShWr_map(my_list).show_self_map()
        for i in all_life_list:
            print(i[0],'号舰血量:[',i[-1],']',end='--')
        print()
        print('<<===对方回合,请等待===>>')
        print()

        attack_top = s.recv(1024).decode()
        attack_num = int(attack_top[0])
        attack_word = attack_top[-1]
        flag = 0
        if my_list[attack_num][dict_word_s[attack_word]] != '   ':

            flag = 1
            if my_list[attack_num][dict_word_s[attack_word]] == ' ^ ':
                hurt_num = my_list[attack_num+1][dict_word_s[attack_word]][1]
            elif my_list[attack_num][dict_word_s[attack_word]] == ' v ':
                hurt_num = my_list[attack_num-1][dict_word_s[attack_word]][1]
            elif my_list[attack_num][dict_word_s[attack_word]] == ' < ':
                hurt_num = my_list[attack_num][dict_word_s[attack_word]+1][1]
            elif my_list[attack_num][dict_word_s[attack_word]] == ' > ':
                hurt_num = my_list[attack_num][dict_word_s[attack_word]-1][1]
            else:
                hurt_num = my_list[attack_num][dict_word_s[attack_word]][1]
            all_life_list[int(hurt_num)-1][1] -=1
            station_str = my_list[attack_num][dict_word_s[attack_word]]
            my_list[attack_num][dict_word_s[attack_word]] = ' x '
        else:
            station_str = '   '
            my_list[attack_num][dict_word_s[attack_word]] = ' X '
        os.system(CL)
        ShWr_map(my_list).show_enemy_map()

        for i in all_life_list:
            print(i[0], '号舰血量:[', i[-1], ']', end='--')
        print()
        print('<<===对方回合,请等待===>>')
        print()
        if flag == 1:
            print('实时战报:\n对方击中了我方船只!\n已在地图中以\'x\'标识!\n')
            msg = '击中目标!对方船只行踪暴露!'
            s.send(msg.encode())
        else:
            print('实时战报:\n所幸对方没有击中我方船只!\n已在地图中以\'X\'标识!\n')
            msg = '没有击中目标!此地标暂时无对方行踪!'
            s.send(msg.encode())
        while True:
            msg = s.recv(1024)
            if msg == b'over':
                time.sleep(1)
                print('实时战报:\n对方回合结束!')
                input('按回车键开始回合')
                return station_str









        # recv_list = connfd.recv(2048)
        #
        # print('对方已就绪!')
        # enemy_list = json.loads(recv_list.decode())
        #
        # enemy_list,attack_list = self.first_attack(enemy_list,CL)
        # connfd.send(json.dumps(enemy_list).encode())
        # self.wait_enermy_combo(connfd,CL,my_list,ship_life_list)

    # def wait_enermy_combo(self,s,CL,my_list,ship_life_list):
    #
    #     os.system(CL)
    #     ShWr_map(my_list).show_self_map()
    #     print('<<=======对方回合,请等待=======>>')
    #     for i in ship_life_list:
    #         print(i[0], '血量:', i[1],'||', end=' ')
    #     count = 0
    #     while True:
    #         if len(ship_life_list) == 0:
    #             os.system(CL)
    #             ShWr_map(my_list).show_self_map()
    #             print('游戏结束!您的舰队以全部牺牲!')
    #             s.send(b'gameover')
    #             break
    #         count +=1
    #         msg = s.recv(2048).decode()
    #         try:
    #             get_list = json.loads(msg)
    #             for i in range(10):
    #                 for j in range(12):
    #                     if get_list[i][j] == ' O ' and count ==1:
    #                         my_list[i][j] = ' O '
    #                         os.system(CL)
    #                         ShWr_map(my_list).show_self_map()
    #                         print('<<=======对方回合,请等待=======>>')
    #                         print('实时战报:对方放置了鱼雷!\n请小心不要触碰到\n已在图中标示,符号为\'O\'')
    #                     if get_list[i][j] == '( )' and count ==1:
    #                         if my_list[i][j] == ' < ':
    #                             hurt_num = int(my_list[i][j + 1][1])
    #                         elif my_list[i][j] == ' > ':
    #                             hurt_num = int(my_list[i][j - 1][1])
    #                         elif my_list[i][j] == ' ^ ':
    #                             hurt_num = int(my_list[i + 1][j][1])
    #                         elif my_list[i][j] == ' v ':
    #                             hurt_num = int(my_list[i - 1][j][1])
    #                         else:
    #                             hurt_num = int(my_list[i][j][1])
    #                         ship_life_list[hurt_num - 1][1] -= 1
    #                         if ship_life_list[hurt_num - 1][1] == 0:
    #                             del ship_life_list[hurt_num - 1]
    #                             my_list[i][j] = '( )'
    #                             os.system(CL)
    #                             ShWr_map(my_list).show_self_map()
    #                             print('<<=======对方回合,请等待=======>>')
    #                             for i in ship_life_list:
    #                                 print(i[0], '血量:', i[1], '||', end=' ')
    #                             print('实时战报:对方放置了鱼雷!\n击中了您的船只,船只牺牲!\n已在图中标示,符号为\'( )\'')
    #                             continue
    #                         my_list[i][j] = '( )'
    #                         os.system(CL)
    #                         ShWr_map(my_list).show_self_map()
    #                         print('<<=======对方回合,请等待=======>>')
    #                         for i in ship_life_list:
    #                             print(i[0], '血量:', i[1], '||', end=' ')
    #                         print('实时战报:对方放置了鱼类!\n鱼类炸到了您的船只,船只位置暴露!\n已在图中标示,符号为\'( )\'')
    #                     if get_list[i][j] == ' X ':
    #                         if my_list[i][j] not in ('   ', ' X ', ' O ', '( )'):
    #                             if my_list[i][j] == ' < ':
    #                                 hurt_num = int(my_list[i][j + 1][1])
    #                             elif my_list[i][j] == ' > ':
    #                                 hurt_num = int(my_list[i][j - 1][1])
    #                             elif my_list[i][j] == ' ^ ':
    #                                 hurt_num = int(my_list[i + 1][j][1])
    #                             elif my_list[i][j] == ' v ':
    #                                 hurt_num = int(my_list[i - 1][j][1])
    #                             else:
    #                                 hurt_num = int(my_list[i][j][1])
    #                             ship_life_list[hurt_num - 1][1] -= 1
    #                             if ship_life_list[hurt_num - 1][1] == 0:
    #                                 del ship_life_list[hurt_num - 1]
    #                                 my_list[i][j] = ' X '
    #                                 os.system(CL)
    #                                 ShWr_map(my_list).show_self_map()
    #                                 print('<<=======对方回合,请等待=======>>')
    #                                 for i in ship_life_list:
    #                                     print(i[0], '血量:', i[1], '||', end=' ')
    #                                 print('实时战报:对方进行了地标打击!\n击中了您的船只,船只牺牲!\n已在图中标示,符号为\'X\'')
    #                                 continue
    #
    #
    #                             my_list[i][j] = ' X '
    #                             os.system(CL)
    #                             ShWr_map(my_list).show_self_map()
    #                             print('<<=======对方回合,请等待=======>>')
    #                             for i in ship_life_list:
    #                                 print(i[0], '血量:', i[1], '||', end=' ')
    #                             print('实时战报:对方进行了地标打击!\n击中了您的船只,船只位置暴露!\n已在图中标示,符号为\'X\'')
    #                         else:
    #                             my_list[i][j] = ' X '
    #                             os.system(CL)
    #                             ShWr_map(my_list).show_self_map()
    #                             print('<<=======对方回合,请等待=======>>')
    #                             for i in ship_life_list:
    #                                 print(i[0], '血量:', i[1], '||', end=' ')
    #                             print('实时战报:对方进行了地标打击!\n有惊无险!\n已在图中标示,符号为\'X\'')
    #
    #         except:
    #             if msg == 'over':
    #                 break







    def join_room(self,user_name,CL,IPGOT):

        os.system(CL)
        print(LOGO)
        s = socket()
        join_ip=input("请输入要加入的房间ip\n按r键返回:")
        if join_ip == 'r':
            return
        s.settimeout(1)
        count = 0
        while True:
            count +=1
            try:
                os.system(CL)
                print(LOGO)
                print('正在链接房间', '.' * (count % 3 + 1))
                s.connect((join_ip,55055))
                break

            except:
                if count == 10:
                    os.system(CL)
                    print(LOGO)
                    print('链接失败!\n请检查ip是否正确且房间存在')
                    print('您输入的ip:[%s]'%join_ip)
                    input('按[回车]返回')
                    return
                continue
        s.settimeout(2000)
        s.send(user_name.encode())
        data = s.recv(1024)
        os.system(CL)
        print(LOGO)
        print('链接成功!准备进入[%s]舰长的房间'%(data.decode()))
        time.sleep(2)
        print('正在载入...')
        time.sleep(3)
        for i in range(3):
            print()

        my_list = self.place_ship(CL)
        os.system(CL)
        ShWr_map(my_list).show_self_map()
        print("<<====版图完成,请等待对方就绪====>>")
        time.sleep(3)
        s.send(b'ok')
        msg = s.recv(1024)
        if msg == b'ok':
            print('对方已就绪!')
        time.sleep(1.5)
        all_life_list = [['1', 3], ['2', 3], ['3', 3], ['4', 3]]
        view_list = [
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
        ]
        msg = s.recv(1024)
        if msg == b'my':
            print('>>==我方获得先手机会==<<')
            time.sleep(1.5)
            self.first_attack(s, view_list, all_life_list,CL)
            game_combo = Game_Combo(s, all_life_list, my_list,view_list, CL,1)

            while True:
                flag = 0
                while True:
                    result = game_combo.wait()
                    if result == 1:
                        flag = 1

                        s.close()
                        print(' 您输了,正在退出游戏！')
                        s.send(b'win ')
                        time.sleep(3)
                        return

                    result = game_combo.move()
                    if result == 123:
                        continue
                    elif result == 1:
                        flag = 1
                        s.close()
                        print(' 您输了,正在退出游戏！')
                        s.send(b'win ')
                        time.sleep(3)

                        return
                    else:
                        break
                result = game_combo.round_ship()
                if result == 1:
                    flag = 1
                    s.close()
                    print(' 您输了,正在退出游戏！')
                    s.send(b'win ')
                    time.sleep(3)

                    return
                game_combo.put_boom()
                game_combo.attack()
                if flag == 1:
                    break
            s.close()



        else:
            print('>>==对方获得先手机会==<<')
            time.sleep(1.5)
            station_str = self.first_wait(s,my_list,all_life_list,CL)
            game_combo = Game_Combo(s, all_life_list, my_list,view_list, CL,2,station_str)
            while True:
                flag = 0
                while True:

                    result = game_combo.move()
                    if result == 123:
                        continue
                    elif result == 1:
                        flag = 1
                        s.close()
                        print(' 您输了,正在退出游戏！')
                        s.send(b'win ')
                        time.sleep(3)

                        return
                    else:
                        break
                result = game_combo.round_ship()
                if result == 1:
                    flag = 1
                    print(' 您输了,正在退出游戏！')
                    s.send(b'win ')
                    time.sleep(3)
                    s.close()
                    return
                game_combo.put_boom()
                game_combo.attack()
                result = game_combo.wait()
                if result == 1:
                    flag = 1
                    s.close()
                    print(' 您输了,正在退出游戏！')
                    s.send(b'win ')
                    time.sleep(3)

                    return
                if flag == 1:
                    break
            s.close()

        # s.send(json.dumps(my_list).encode())
        #
        # os.system(CL)
        # ShWr_map(my_list).show_self_map()
        # print('<<=======对方回合,请等待=======>>')
        # for i in ship_life_list:
        #     print(i[0], '血量:', i[1],'||', end=' ')
        # print()
        # msg = s.recv(2048)
        # recv_list = json.loads(msg.decode())
        # combo_time_test = 0
        # for i in range(10):
        #     for j in range(12):
        #         if recv_list[i][j] == ' X ':
        #             if my_list[i][j] not in ('   ', ' X ', ' O ', '( )'):
        #                 combo_time_test = 1
        #
        #                 if my_list[i][j] == ' < ':
        #                     hurt_num = int(my_list[i][j+1][1])
        #                 elif my_list[i][j] == ' > ':
        #                     hurt_num = int(my_list[i][j-1][1])
        #                 elif my_list[i][j] == ' ^ ':
        #                     hurt_num = int(my_list[i+1][j][1])
        #                 elif my_list[i][j] == ' v ':
        #                     hurt_num = int(my_list[i-1][j][1])
        #                 else:
        #                     hurt_num = int(my_list[i][j][1])
        #                 ship_life_list[hurt_num-1][1] -= 1
        #                 my_list[i][j] = ' X '
        #
        #
        # os.system(CL)
        # ShWr_map(my_list).show_self_map()
        # if combo_time_test == 0:
        #     print('战报:\n对方打击地标以\'X\'显示在图中')
        # else:
        #     print('战报:\n您的船只被击中了!\n对方打击地标以\'X\'显示在图中')
        # input('回车确认')
        # self.attack_combo(CL,ship_life_list,my_list)

    def attack_combo(self,CL,ship_life_list,my_list):
        pass








    def place_ship(self,CL):
        """
            船只初次摆放流程
        :param CL: 清屏指令
        :return: 地图列表
        """
        my_list = [
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
        ]
        self.__count = 1
        while self.__count <6:
            if self.__count !=5:
                os.system(CL)
                ShWr_map(my_list).show_self_map()
                ship_show(self.__count)
            else:
                os.system(CL)
                ShWr_map(my_list).show_self_map()


            if self.__count == 1:
                print("请选择横向放置或者纵向放置:\n1.横向放置\n2.纵向放置")
            elif self.__count <5:
                print("请选择横向放置或者纵向放置:\n1.横向放置\n2.纵向放置\n3.修改上一艘船")
            elif self.__count ==5:
                print("1.修改上一艘船\n2.确认全部放置")
                str_pos = input(">>>:")
                if str_pos == '1':
                    for i in range(10):
                        for j in range(12):
                            if my_list[i][j] == '[%d]' % (self.__count - 1):
                                my_list[i][j] = '   '
                                if my_list[i][j - 1] == ' < ':
                                    my_list[i][j - 1] = '   '
                                    my_list[i][j + 1] = '   '
                                elif my_list[i - 1][j] == ' ^ ':
                                    my_list[i - 1][j] = '   '
                                    my_list[i + 1][j] = '   '
                                break
                    self.__count -= 1
                    continue
                elif str_pos == '2' or str_pos == '':
                    return my_list

            str_pos = input(">>>:")
            if str_pos == '2' and self.__count !=5:
                my_list,self.__count = self.leng_ship(my_list,CL,self.__count)

            elif str_pos == '1'and self.__count !=5:
                my_list,self.__count = self.line_ship(my_list,CL,self.__count)
            elif str_pos == '3':
                for i in range(10):
                    for j in range(12):
                        if my_list[i][j] == '[%d]'%(self.__count-1):
                            my_list[i][j] = '   '
                            if my_list[i][j-1] == ' < ':
                                my_list[i][j - 1] = '   '
                                my_list[i][j + 1] = '   '
                            elif my_list[i-1][j] == ' ^ ':
                                my_list[i-1][j] = '   '
                                my_list[i+1][j] = '   '
                            break
                self.__count -= 1


            else:
                print("输入有误!注意格式(数字和小写字母)")
                time.sleep(1)






    def line_ship(self,list,CL,num):
        """
            横向船只摆放
        :return: 刷新列表
        """

        while True:
            os.system(CL)
            ShWr_map(list).show_self_map()
            ship_show_line(self.__count)
            pos= input('请输入船只放置坐标(格式为: 数字和小写字母)\n按r键重新调整方向:')
            if pos == 'r':
                return list,num


            try:
                pos_num = int(pos[0])
                pos_word = pos[-1]
                if (pos_num not in list_num)or(pos_word not in list_word_s):
                    print('参数错误,请重新输入')
                    time.sleep(1.5)
                    continue
                if pos_word == 'a' or pos_word== 'l':
                    print('船只长度溢出地图,请重新输入')
                    time.sleep(1.5)
                    continue
                if (list[pos_num][dict_word_s[pos_word]] != '   ') or (list[pos_num][dict_word_s[pos_word]-1] != '   ') or (list[pos_num][dict_word_s[pos_word]+1] != '   '):
                    print('船只重叠!请重新输入')
                    time.sleep(1.5)
                    continue

                list[pos_num][dict_word_s[pos_word]] = '[%d]'%num
                list[pos_num][dict_word_s[pos_word] - 1] = ' < '
                list[pos_num][dict_word_s[pos_word] + 1] = ' > '

                return list,num+1





            except:
                print('格式错误,请重新输入')
                time.sleep(1.5)
                continue




    def leng_ship(self,list,CL,num):
        """
            纵向船只摆放
        :return: 刷新列表
        """
        while True:
            os.system(CL)
            ShWr_map(list).show_self_map()
            ship_show_leng(self.__count)
            pos = input('请输入船只放置坐标(格式为: 数字和小写字母)\n按r键重新调整方向:')
            if pos == 'r':
                return list,num
            if len(pos) > 2:
                print('格式错误,请重新输入')
                time.sleep(1.5)
                continue

            try:
                pos_num = int(pos[0])
                pos_word = pos[-1]
                if (pos_num not in list_num) or (pos_word not in list_word_s):
                    print('参数错误,请重新输入')
                    time.sleep(1.5)
                    continue
                if pos_num == 0 or pos_num == 9:
                    print('船只长度溢出地图,请重新输入')
                    time.sleep(1.5)
                    continue
                if (list[pos_num][dict_word_s[pos_word]] != '   ') or (list[pos_num+1][dict_word_s[pos_word]] != '   ') or (list[pos_num-1][dict_word_s[pos_word]] != '   '):
                    print('船只重叠!请重新输入')
                    time.sleep(1.5)
                    continue

                list[pos_num][dict_word_s[pos_word]] = '[%d]'%num
                list[pos_num-1][dict_word_s[pos_word]] = ' ^ '
                list[pos_num+1][dict_word_s[pos_word]] = ' v '

                return list,num+1





            except:
                print('格式错误,请重新输入')
                time.sleep(1.5)
                continue
    # def first_attack(self,list,CL):
    #     attack_list = [
    #         ['   '] * 12,
    #         ['   '] * 12,
    #         ['   '] * 12,
    #         ['   '] * 12,
    #         ['   '] * 12,
    #         ['   '] * 12,
    #         ['   '] * 12,
    #         ['   '] * 12,
    #         ['   '] * 12,
    #         ['   '] * 12,
    #     ]
    #     while True:
    #
    #         os.system(CL)
    #         ShWr_map(attack_list).show_enemy_map()
    #         print('你的回合,请选择打击地标')
    #         attack_pos = input('(格式:数字和字母):')
    #         try:
    #             attack_num = int(attack_pos[0])
    #             attack_word = attack_pos[-1]
    #             if (attack_num not in list_num)or(attack_word not in list_word_s):
    #                 print('格式错误!请注意不要使用[大写]及格式问题!')
    #                 time.sleep(1.5)
    #                 continue
    #             if list[attack_num][dict_word_s[attack_word]] in ('   ',' X ',' O ','( )'):
    #                 os.system(CL)
    #                 list[attack_num][dict_word_s[attack_word]] = ' X '
    #                 attack_list[attack_num][dict_word_s[attack_word]] = ' X '
    #                 ShWr_map(attack_list).show_enemy_map()
    #                 print('未击中目标!此地标暂时没有船只经过')
    #                 input('回车确认')
    #
    #             else:
    #                 os.system(CL)
    #                 list[attack_num][dict_word_s[attack_word]] = ' X '
    #                 attack_list[attack_num][dict_word_s[attack_word]] = ' X '
    #                 ShWr_map(attack_list).show_enemy_map()
    #                 print('击中目标!此地标发现船只踪迹!')
    #                 input('回车确认')
    #
    #                 return list,attack_list
    #
    #
    #         except:
    #             print('格式错误!请注意使用[大写]及格式问题!')
    #             time.sleep(1.5)
    #             continue






        





if __name__ == '__main__':
    s = Double_game().place_ship('clear')
