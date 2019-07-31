import os
import time
from ShWr_map import *


class Game_Combo:
    def __init__(self, socked, all_life_list, my_list, view_list, CL, boom = 0,station_str = '   '):
        self.s = socked
        self.CL = CL
        self.ship_life_list = all_life_list
        self.my_list = my_list
        self.view_list = view_list
        self.boom = boom
        self.pos_num_list = []
        self.station_str = station_str

    def move(self):
        while True:
            flag = 0
            while flag == 0:
                choose_ship_str = []
                for i in self.ship_life_list:
                    choose_ship_str.append(i[0])
                os.system(self.CL)
                ShWr_map(self.my_list).show_self_map()
                for i in self.ship_life_list:
                    print(i[0], '号舰血量:[', i[-1], ']', end='--')
                print()
                print('<<=====我方回合=====>>')
                print()
                self.choose_str = input('请输入[船只编号]选择要移动的船只:\n按r键阅读\'关于移动\':')
                if not self.choose_str:
                    continue
                if self.choose_str[0] == 'r':
                    os.system(self.CL)
                    ShWr_map(self.my_list).show_self_map()
                    for i in self.ship_life_list:
                        print(i[0], '号舰血量:[', i[-1], ']', end='--')
                    print()
                    print('<<=====我方回合=====>>')
                    print()
                    print('关于移动:\n每回合,玩家只能且必须选择一艘船只进行移动\n注意!!!\n横向船只只能水平移动,纵向船只只能上下移动\n您可以在移动结束后选择是否转向一次')
                    input('回车确认')
                    continue
                for i in choose_ship_str:
                    if self.choose_str == i:
                        flag = 1
                        break
                if flag == 0:
                    print('没有这艘船只!')
                    time.sleep(1)
                    continue
            self.pos_num_list = []
            for i in range(10):
                for j in range(12):
                    if self.my_list[i][j][1] == self.choose_str:
                        self.pos_num_list.append(i)
                        self.pos_num_list.append(j)
            if len(self.pos_num_list) < 2:
                for i in range(10):
                    for j in range(12):
                        if self.my_list[i][j] == ' x ':
                            self.pos_num_list.append(i)
                            self.pos_num_list.append(j)
            while True:
                os.system(self.CL)
                ShWr_map(self.my_list).show_self_map()
                for i in self.ship_life_list:
                    print(i[0], '号舰血量:[', i[-1], ']', end='--')
                print()
                print('<<=====我方回合=====>>')
                print('')
                print('确定移动[%s]号船只？？' % self.choose_str)
                s = input('r键重新选择--回车确认')
                if s == '':
                    s = '   '
                if s == 'r':
                    break
                if (self.my_list[self.pos_num_list[0]][self.pos_num_list[1] - 1] == ' < ') or (
                    self.my_list[self.pos_num_list[0]][self.pos_num_list[1] + 1] == ' > '):
                    os.system(self.CL)
                    ShWr_map(self.my_list).show_self_map()
                    for i in self.ship_life_list:
                        print(i[0], '号舰血量:[', i[-1], ']', end='--')
                    print()
                    print('<<=====我方回合=====>>')
                    print()
                    choose = input('注意:\n该船只为[横向]放置,请选择左右移动\n\'a\'键为左移,\'d\'键为右移\n\'其他\'键撤销:')
                    if choose == 'a':
                        flag = 0
                        if self.pos_num_list[1] == 1:
                            print('该船只不能行驶到地图外!请重新选择!')
                            time.sleep(1)
                            continue
                        if self.my_list[self.pos_num_list[0]][self.pos_num_list[1] - 2] == ' O ':
                            msg = 'getboom '
                            msg += str(self.pos_num_list[0])
                            msg += ' '
                            msg += str(self.pos_num_list[1] - 2)
                            self.s.send(msg.encode())
                            time.sleep(0.5)
                            print('触碰到鱼雷!船只踪迹暴露!\n')
                            for i in range(len(self.ship_life_list)):
                                if self.ship_life_list[i][0] == self.choose_str:
                                    self.ship_life_list[i][1] -= 1
                                    if self.ship_life_list[i][1] == 0:
                                        flag = 1
                                        del self.ship_life_list[i]
                                        self.my_list[self.pos_num_list[0]][self.pos_num_list[1] - 2] = '   '
                                        self.my_list[self.pos_num_list[0]][
                                            self.pos_num_list[1] - 1] = '   '
                                        self.my_list[self.pos_num_list[0]][self.pos_num_list[1]] = '   '
                                        self.my_list[self.pos_num_list[0]][self.pos_num_list[1] + 1] = '   '
                                        print('船只牺牲！\n')
                                        msg = 'died '
                                        self.s.send(msg.encode())
                                        time.sleep(0.5)
                                        if len(self.ship_life_list) == 0:
                                            return 1
                                        break

                            input('回车确认')
                        elif self.my_list[self.pos_num_list[0]][self.pos_num_list[1] - 2] != ' X ' and self.my_list[self.pos_num_list[0]][self.pos_num_list[1] - 2] != '   ':
                            input('船只位置重叠!按[回车]重新选择!')
                            continue
                        if flag == 0:
                            self.my_list[self.pos_num_list[0]][self.pos_num_list[1] - 2] = ' < '
                            self.my_list[self.pos_num_list[0]][self.pos_num_list[1] - 1] = '[%s]' % self.choose_str
                            self.my_list[self.pos_num_list[0]][self.pos_num_list[1]] = ' > '
                            self.my_list[self.pos_num_list[0]][self.pos_num_list[1] + 1] = '   '
                        self.pos_num_list[1] -= 1

                        return
                    if choose == 'd':
                        flag = 0
                        if self.pos_num_list[1] == 10:
                            os.system(self.CL)
                            ShWr_map(self.my_list).show_self_map()
                            for i in self.ship_life_list:
                                print(i[0], '号舰血量:[', i[-1], ']', end='--')
                            print()
                            print('<<=====我方回合=====>>')
                            print()
                            print('该船只不能行驶到地图外!请重新选择!')
                            time.sleep(1)
                            continue
                        if self.my_list[self.pos_num_list[0]][self.pos_num_list[1] + 2] == ' O ':
                            msg = 'getboom '
                            msg += str(self.pos_num_list[0])
                            msg += ' '
                            msg += str(self.pos_num_list[1] + 2)

                            self.s.send(msg.encode())
                            time.sleep(0.5)
                            print('触碰到鱼雷!船只踪迹暴露!\n')
                            for i in range(len(self.ship_life_list)):
                                if self.ship_life_list[i][0] == self.choose_str:
                                    self.ship_life_list[i][1] -= 1
                                    if self.ship_life_list[i][1] == 0:
                                        flag = 1
                                        del self.ship_life_list[i]
                                        self.my_list[self.pos_num_list[0]][self.pos_num_list[1] + 2] = '   '
                                        self.my_list[self.pos_num_list[0]][
                                            self.pos_num_list[1] + 1] = '   '
                                        self.my_list[self.pos_num_list[0]][self.pos_num_list[1]] = '   '
                                        self.my_list[self.pos_num_list[0]][self.pos_num_list[1] - 1] = '   '
                                        print('船只牺牲！\n')
                                        msg = 'died '
                                        self.s.send(msg.encode())
                                        time.sleep(0.5)
                                        if len(self.ship_life_list) == 0:
                                            return 1
                                        break
                            time.sleep(1)
                        elif self.my_list[self.pos_num_list[0]][self.pos_num_list[1] + 2] != ' X ' and self.my_list[self.pos_num_list[0]][self.pos_num_list[1] + 2] != '   ':
                            os.system(self.CL)
                            ShWr_map(self.my_list).show_self_map()
                            for i in self.ship_life_list:
                                print(i[0], '号舰血量:[', i[-1], ']', end='--')
                            print()
                            print('<<=====我方回合=====>>')
                            print()
                            print('船只位置重叠!请重新选择!')
                            time.sleep(1.5)
                            continue
                        if flag == 0:
                            self.my_list[self.pos_num_list[0]][self.pos_num_list[1] + 2] = ' > '
                            self.my_list[self.pos_num_list[0]][self.pos_num_list[1] + 1] = '[%s]' % self.choose_str
                            self.my_list[self.pos_num_list[0]][self.pos_num_list[1]] = ' < '
                            self.my_list[self.pos_num_list[0]][self.pos_num_list[1] - 1] = '   '
                        self.pos_num_list[1] += 1
                        return
                    else:

                        continue

                else:
                    os.system(self.CL)
                    ShWr_map(self.my_list).show_self_map()
                    for i in self.ship_life_list:
                        print(i[0], '号舰血量:[', i[-1], ']', end='--')
                    print()
                    print('<<=====我方回合=====>>')
                    print()
                    choose = input('注意:\n该船只为[纵向]放置,请选择上下移动\n\'w\'键为上移,\'s\'键为下移\n\'其他\'键撤销:')
                    if choose == 'w':
                        flag = 0
                        if self.pos_num_list[0] == 1:
                            os.system(self.CL)
                            ShWr_map(self.my_list).show_self_map()
                            for i in self.ship_life_list:
                                print(i[0], '号舰血量:[', i[-1], ']', end='--')
                            print()
                            print('<<=====我方回合=====>>')
                            print()
                            print('该船只不能行驶到地图外!请重新选择!')
                            time.sleep(1)
                            continue
                        if self.my_list[self.pos_num_list[0] - 2][self.pos_num_list[1]] == ' O ':
                            msg = 'getboom '
                            msg += str(self.pos_num_list[0] - 2)
                            msg += ' '
                            msg += str(self.pos_num_list[1])
                            self.s.send(msg.encode())
                            time.sleep(0.5)
                            print('触碰到鱼雷!船只踪迹暴露!\n')
                            for i in range(len(self.ship_life_list)):
                                if self.ship_life_list[i][0] == self.choose_str:
                                    self.ship_life_list[i][1] -= 1
                                    if self.ship_life_list[i][1] == 0:
                                        flag = 1
                                        del self.ship_life_list[i]
                                        self.my_list[self.pos_num_list[0] - 2][self.pos_num_list[1]] = '   '
                                        self.my_list[self.pos_num_list[0] - 1][
                                            self.pos_num_list[1]] = '   '
                                        self.my_list[self.pos_num_list[0]][self.pos_num_list[1]] = '   '
                                        self.my_list[self.pos_num_list[0] + 1][self.pos_num_list[1]] = '   '
                                        print('船只牺牲！\n')
                                        msg = 'died '
                                        self.s.send(msg.encode())
                                        time.sleep(0.5)
                                        if len(self.ship_life_list) == 0:
                                            return 1
                                        break
                            time.sleep(1)
                        elif self.my_list[self.pos_num_list[0] - 2][self.pos_num_list[1]] != ' X ' and self.my_list[self.pos_num_list[0] - 2][self.pos_num_list[1]] != '   ':
                            print('船只位置重叠!请重新选择!')
                            continue
                        if flag == 0:
                            self.my_list[self.pos_num_list[0] - 2][self.pos_num_list[1]] = ' ^ '
                            self.my_list[self.pos_num_list[0] - 1][self.pos_num_list[1]] = '[%s]' % self.choose_str
                            self.my_list[self.pos_num_list[0]][self.pos_num_list[1]] = ' v '
                            self.my_list[self.pos_num_list[0] + 1][self.pos_num_list[1]] = '   '
                        self.pos_num_list[0] -= 1
                        return
                    if choose == 's':
                        flag = 0
                        if self.pos_num_list[0] == 8:
                            print('该船只不能行驶到地图外!请重新选择!')
                            time.sleep(1)
                            continue

                        if self.my_list[self.pos_num_list[0] + 2][self.pos_num_list[1]] == ' O ':
                            msg = 'getboom '
                            msg += str(self.pos_num_list[0] + 2)
                            msg += ' '
                            msg += str(self.pos_num_list[1])
                            self.s.send(msg.encode())
                            time.sleep(0.5)
                            print('触碰到鱼雷!船只踪迹暴露!\n')
                            for i in range(len(self.ship_life_list)):
                                if self.ship_life_list[i][0] == self.choose_str:
                                    self.ship_life_list[i][1] -= 1
                                    if self.ship_life_list[i][1] == 0:
                                        flag = 1
                                        del self.ship_life_list[i]
                                        self.my_list[self.pos_num_list[0] + 2][self.pos_num_list[1]] = '   '
                                        self.my_list[self.pos_num_list[0] + 1][
                                            self.pos_num_list[1]] = '   '
                                        self.my_list[self.pos_num_list[0]][self.pos_num_list[1]] = '   '
                                        self.my_list[self.pos_num_list[0] - 1][self.pos_num_list[1]] = '   '
                                        print('船只牺牲！\n')
                                        msg = 'died '
                                        self.s.send(msg.encode())
                                        time.sleep(0.5)
                                        if len(self.ship_life_list) == 0:
                                            return 1
                                        break
                            time.sleep(1)
                        elif self.my_list[self.pos_num_list[0] + 2][self.pos_num_list[1]] != ' X ' and self.my_list[self.pos_num_list[0] + 2][self.pos_num_list[1]] != '   ':
                            print('船只位置重叠!请重新选择!')
                            continue
                        if flag == 0:
                            self.my_list[self.pos_num_list[0] + 2][self.pos_num_list[1]] = ' v '
                            self.my_list[self.pos_num_list[0] + 1][self.pos_num_list[1]] = '[%s]' % self.choose_str
                            self.my_list[self.pos_num_list[0]][self.pos_num_list[1]] = ' ^ '
                            self.my_list[self.pos_num_list[0] - 1][self.pos_num_list[1]] = '   '
                        self.pos_num_list[0] += 1

                        return
                    else:

                        continue


    def round_ship(self):



        for i in range(10):
            for j in range(12):
                if self.my_list[i][j] == ' x ':
                    self.my_list[i][j] = self.station_str
                if self.my_list[i][j][0] == '(':
                    if self.my_list[i][j][1] in('<','>','^','v') :
                        str_code = ''
                        for num in range(3):

                            if num == 1:
                                str_code += self.my_list[i][j][1]
                            else:
                                str_code += ' '
                        self.my_list[i][j] = str_code
                    else:
                        str_code = ''
                        for num in range(3):
                            if num == 0:
                                str_code += '['
                            if num == 1:
                                str_code += self.my_list[i][j][1]
                            if num == 2:
                                str_code += ']'
                        self.my_list[i][j] = str_code


        while True:
            os.system(self.CL)
            ShWr_map(self.my_list).show_self_map()
            for i in self.ship_life_list:
                print(i[0], '号舰血量:[', i[-1], ']', end='--')
            print()
            print('<<=====我方回合=====>>')
            print()
            if (self.pos_num_list[0] in (0, 9)) or (self.pos_num_list[1] in (0, 11)):
                input('该船只无法转向，按[回车]载入打击界面')

                break
            inp = input('是否转向?\ny键确认 n键跳过:')
            if inp == 'n':
                break
            elif inp == 'y':
                if self.my_list[self.pos_num_list[0]][self.pos_num_list[1] - 1] == ' < ':
                    flag = 0
                    if self.my_list[self.pos_num_list[0]+1][self.pos_num_list[1]] not in ('   ',' X ',' O ','( )') or self.my_list[self.pos_num_list[0]-1][self.pos_num_list[1]] not in ('   ',' X ',' O ','( )'):
                        os.system(self.CL)
                        ShWr_map(self.my_list).show_self_map()
                        for i in self.ship_life_list:
                            print(i[0], '号舰血量:[', i[-1], ']', end='--')
                        print()
                        print('<<=====我方回合=====>>')
                        print()
                        input('转向遭到船只阻碍，按[回车]载入攻击模块')

                        break
                    if self.my_list[self.pos_num_list[0] - 1][self.pos_num_list[1]] == ' O ':
                        msg = 'getboom '
                        msg += str(self.pos_num_list[0] - 1)
                        msg += ' '
                        msg += str(self.pos_num_list[1])
                        self.s.send(msg.encode())
                        os.system(self.CL)
                        ShWr_map(self.my_list).show_self_map()
                        for i in self.ship_life_list:
                            print(i[0], '号舰血量:[', i[-1], ']', end='--')
                        print()
                        print('<<=====我方回合=====>>')
                        print()
                        print('触碰到鱼雷!船只踪迹暴露!\n')
                        time.sleep(1.5)
                        for i in range(len(self.ship_life_list)):
                            if self.ship_life_list[i][0] == self.choose_str:
                                self.ship_life_list[i][1] -= 1
                                if self.ship_life_list[i][1] == 0:
                                    print('船只牺牲！\n')
                                    time.sleep(1)
                                    del self.ship_life_list[i]
                                    flag = 1
                                    self.my_list[self.pos_num_list[0]][self.pos_num_list[1] - 1] = '   '
                                    self.my_list[self.pos_num_list[0]][self.pos_num_list[1] + 1] = '   '
                                    self.my_list[self.pos_num_list[0] - 1][self.pos_num_list[1]] = '   '
                                    self.my_list[self.pos_num_list[0] + 1][self.pos_num_list[1]] = '   '
                                    self.my_list[self.pos_num_list[0]][self.pos_num_list[1]] = '   '
                                    msg = 'died '
                                    self.s.send(msg.encode())
                                    time.sleep(0.5)
                                    if len(self.ship_life_list) == 0:
                                        return 1
                        time.sleep(0.5)

                    if self.my_list[self.pos_num_list[0] + 1][self.pos_num_list[1]] == ' O ':
                        msg = 'getboom '
                        msg += str(self.pos_num_list[0] + 1)
                        msg += ' '
                        msg += str(self.pos_num_list[1])
                        self.s.send(msg.encode())
                        print('触碰到鱼雷!船只踪迹暴露!')
                        for i in range(len(self.ship_life_list)):
                            if self.ship_life_list[i][0] == self.choose_str:
                                self.ship_life_list[i][1] -= 1
                                if self.ship_life_list[i][1] == 0:
                                    print('船只牺牲！\n')
                                    time.sleep(1)
                                    del self.ship_life_list[i]
                                    flag = 1
                                    self.my_list[self.pos_num_list[0]][self.pos_num_list[1] - 1] = '   '
                                    self.my_list[self.pos_num_list[0]][self.pos_num_list[1] + 1] = '   '
                                    self.my_list[self.pos_num_list[0] - 1][self.pos_num_list[1]] = '   '
                                    self.my_list[self.pos_num_list[0] + 1][self.pos_num_list[1]] = '   '
                                    self.my_list[self.pos_num_list[0]][self.pos_num_list[1]] = '   '
                                    msg = 'died '
                                    self.s.send(msg.encode())
                                    time.sleep(0.5)
                                    if len(self.ship_life_list) == 0:
                                        return 1
                        time.sleep(0.5)
                    if flag == 0:
                        self.my_list[self.pos_num_list[0]][self.pos_num_list[1] - 1] = '   '
                        self.my_list[self.pos_num_list[0]][self.pos_num_list[1] + 1] = '   '
                        self.my_list[self.pos_num_list[0] - 1][self.pos_num_list[1]] = ' ^ '
                        self.my_list[self.pos_num_list[0] + 1][self.pos_num_list[1]] = ' v '
                    os.system(self.CL)
                    ShWr_map(self.my_list).show_self_map()
                    input('\n转向完成!按[回车]载入攻击模块')

                    break

                if self.my_list[self.pos_num_list[0] - 1][self.pos_num_list[1]] == ' ^ ':
                    flag = 0
                    if self.my_list[self.pos_num_list[0]][self.pos_num_list[1]-1] not in ('   ',' X ',' O ','( )') or self.my_list[self.pos_num_list[0]][self.pos_num_list[1]+1] not in ('   ',' X ',' O ','( )'):
                        input('该船只无法在地图边缘转向\n按[回车]载入攻击模块')

                        break
                    if self.my_list[self.pos_num_list[0]][self.pos_num_list[1] - 1] == ' O ':
                        msg = 'getboom '
                        msg += str(self.pos_num_list[0])
                        msg += ' '
                        msg += str(self.pos_num_list[1] - 1)
                        self.s.send(msg.encode())
                        print('\n触碰到鱼雷!船只踪迹暴露!')
                        for i in range(len(self.ship_life_list)):
                            if self.ship_life_list[i][0] == self.choose_str:
                                self.ship_life_list[i][1] -= 1
                                if self.ship_life_list[i][1] == 0:
                                    print('船只牺牲！\n')
                                    time.sleep(1)
                                    del self.ship_life_list[i]
                                    flag = 1
                                    self.my_list[self.pos_num_list[0]][self.pos_num_list[1] - 1] = '   '
                                    self.my_list[self.pos_num_list[0]][self.pos_num_list[1] + 1] = '   '
                                    self.my_list[self.pos_num_list[0] - 1][self.pos_num_list[1]] = '   '
                                    self.my_list[self.pos_num_list[0] + 1][self.pos_num_list[1]] = '   '
                                    msg = 'died '
                                    self.s.send(msg.encode())
                                    time.sleep(0.5)
                                    if len(self.ship_life_list) == 0:
                                        return 1
                        time.sleep(0.5)
                    if self.my_list[self.pos_num_list[0]][self.pos_num_list[1] + 1] == ' O ':
                        msg = 'getboom '
                        msg += str(self.pos_num_list[0])
                        msg += ' '
                        msg += str(self.pos_num_list[1] + 1)
                        self.s.send(msg.encode())
                        print('触碰到鱼雷!船只踪迹暴露!')
                        for i in range(len(self.ship_life_list)):
                            if self.ship_life_list[i][0] == self.choose_str:
                                self.ship_life_list[i][1] -= 1
                                if self.ship_life_list[i][1] == 0:
                                    print('船只牺牲！\n')
                                    time.sleep(1)
                                    del self.ship_life_list[i]
                                    flag = 1
                                    self.my_list[self.pos_num_list[0]][self.pos_num_list[1] - 1] = '   '
                                    self.my_list[self.pos_num_list[0]][self.pos_num_list[1] + 1] = '   '
                                    self.my_list[self.pos_num_list[0] - 1][self.pos_num_list[1]] = '   '
                                    self.my_list[self.pos_num_list[0] + 1][self.pos_num_list[1]] = '   '
                                    msg = 'died '
                                    self.s.send(msg.encode())
                                    time.sleep(0.5)
                                    if len(self.ship_life_list) == 0:
                                        return 1
                        time.sleep(0.5)
                    if flag == 0:
                        self.my_list[self.pos_num_list[0]][self.pos_num_list[1] - 1] = ' < '
                        self.my_list[self.pos_num_list[0]][self.pos_num_list[1] + 1] = ' > '
                        self.my_list[self.pos_num_list[0] - 1][self.pos_num_list[1]] = '   '
                        self.my_list[self.pos_num_list[0] + 1][self.pos_num_list[1]] = '   '
                    os.system(self.CL)
                    ShWr_map(self.my_list).show_self_map()
                    input('\n转向完成!按[回车]载入攻击模块')
                    break
            else:
                continue

        for i in range(10):
            for j in range(12):
                if self.my_list[i][j] == ' X ':
                    self.my_list[i][j] = '   '
                if self.my_list[i][j] == ' x ':
                    self.my_list[i][j] = '   '

    def put_boom(self):
        # if self.boom < 1:
        #     self.boom += 1
        #     return

        self.boom = 0
        while True:
            os.system(self.CL)
            ShWr_map(self.view_list).show_enemy_map()
            for i in self.ship_life_list:
                print(i[0], '号舰血量:[', i[-1], ']', end='--')
            print()
            print('<<=====我方回合=====>>')
            print()
            boom_top = input('输入坐标放置鱼雷 格式(数字和字母)\n按\'r\'键阅读\'关于鱼雷\':')
            if boom_top == '':
                continue
            if boom_top[0] == 'r':
                os.system(self.CL)
                ShWr_map(self.view_list).show_enemy_map()
                for i in self.ship_life_list:
                    print(i[0], '号舰血量:[', i[-1], ']', end='--')
                print()
                print('<<=====我方回合=====>>')
                print()
                print('关于鱼雷:\n每回合补充一个鱼雷,玩家可以在对方地图放置\n鱼雷会被永久放置,直到被对方船只触碰到')
                input('回车确认')
                continue
            try:
                boom_num = int(boom_top[0])
                boom_word = boom_top[-1]
                if (boom_num not in list_num) or (boom_word not in list_word_s):
                    print('请填写合理范围内的坐标！')
                    continue
                break
            except:
                print('输入参数有误!请重新输入!')
                time.sleep(1)
                continue

        msg = 'putboom ' + str(boom_num) + ' ' + boom_word
        self.s.send(msg.encode())
        time.sleep(0.5)
        msg = self.s.recv(1024)
        if '鱼雷击中了船只' in msg.decode():
            self.view_list[boom_num][dict_word_s[boom_word]] = '( )'

        else:
            self.view_list[boom_num][dict_word_s[boom_word]] = ' O '
        os.system(self.CL)
        ShWr_map(self.view_list).show_enemy_map()
        for i in self.ship_life_list:
            print(i[0], '号舰血量:[', i[-1], ']', end='--')
        print()
        print('<<=====我方回合=====>>')
        print()
        print(msg.decode())
        input('回车确认')


    def attack(self):
        while True:
            os.system(self.CL)
            ShWr_map(self.view_list).show_enemy_map()
            for i in self.ship_life_list:
                print(i[0], '号舰血量:[', i[-1], ']', end='--')
            print()
            print('<<=====我方回合=====>>')
            print()
            boom_top = input('输入坐标进行打击 格式(数字和字母):')
            try:
                boom_num = int(boom_top[0])
                boom_word = boom_top[-1]
                if (boom_num not in list_num) or (boom_word not in list_word_s):
                    print('请填写合理范围内的坐标！')
                    continue

            except:
                print('输入参数有误!请重新输入!')
                time.sleep(1)
                continue
            if self.view_list[boom_num][dict_word_s[boom_word]] == ' O ':
                print('这里是您布置好的鱼雷...')
                time.sleep(1)
                print('您不能这么愚钝...')
                time.sleep(1)
                print('我就当做什么都没看见,您重新选择地标吧...')
                time.sleep(1.5)
                continue

            msg = 'attack ' + str(boom_num) + ' ' + boom_word
            self.s.send(msg.encode())

            time.sleep(0.5)
            msg = self.s.recv(1024)
            for i in range(10):
                for j in range(12):
                    if self.view_list[i][j] == ' X ':
                        self.view_list[i][j] = '   '
                    if self.view_list[i][j][0] == '(':
                        self.view_list[i][j] = '   '

            self.view_list[boom_num][dict_word_s[boom_word]] = ' X '
            os.system(self.CL)
            ShWr_map(self.view_list).show_enemy_map()
            for i in self.ship_life_list:
                print(i[0], '号舰血量:[', i[-1], ']', end='--')
            print()
            print('<<=====我方回合=====>>\n')
            print(msg.decode())
            time.sleep(0.5)
            input('\n回车确认,结束回合')
            self.s.send(b'over')
            return

    def wait(self):

        msg_s = '<<===对方回合,请等待===>>\n'
        while True:

            os.system(self.CL)
            ShWr_map(self.my_list).show_self_map()
            for i in self.ship_life_list:
                print(i[0], '号舰血量:[', i[-1], ']', end='--')
            print()
            print(msg_s)

            r_msg = self.s.recv(1024)

            msg_list_before = r_msg.decode()
            msg = msg_list_before.split(' ')
            if msg[0] == 'win':
                print('游戏结束,您获胜了!')
                time.sleep(3)
                self.s.close()
                break


            msg_s += '\n实时战报:'
            if msg[0] == 'getboom':

                self.view_list[int(msg[1])][int(msg[2])] = '( )'
                os.system(self.CL)
                ShWr_map(self.view_list).show_enemy_map()
                # for i in self.ship_life_list:
                #     print(i[0], '号舰血量:[', i[-1], ']', end='--')
                msg_s += '\n对方触碰了鱼雷!'
                print(msg_s)
                time.sleep(2.5)
                msg_s += '\n下回合将在[敌方地图]上以\'( )\'显示\n'
                continue
            if msg[0] == 'died':
                msg_s += '\n对方牺牲了一条船只！'
                continue
            if msg[0] == 'putboom':
                boom_num = int(msg[1])
                boom_word = msg[2]
                msg_s += '\n对方放置了鱼雷!'
                sendmsg = '鱼雷已被放置\n'
                if self.my_list[boom_num][dict_word_s[boom_word]] == '   ':
                    msg_s+='\n已在地图中以\'O\'标识\n'
                    self.my_list[boom_num][dict_word_s[boom_word]] = ' O '
                else:

                    sendmsg += '鱼雷击中了船只!\n'
                    msg_s += '鱼雷击中船只!船只行踪暴露!\n'
                    station_str = ''
                    for i in range(3):
                        if i == 0:
                            station_str += '('
                        elif i == 1:
                            station_str += self.my_list[boom_num][dict_word_s[boom_word]][i]
                        else:
                            station_str += ')'
                    self.station_str = self.my_list[boom_num][dict_word_s[boom_word]]
                    self.my_list[boom_num][dict_word_s[boom_word]] = station_str
                    hurt_num = 0
                    hurt_word = 0

                    if self.my_list[boom_num][dict_word_s[boom_word]][1] == '<':
                        self.choose_ship = self.my_list[boom_num][dict_word_s[boom_word] + 1][1]
                        hurt_num = boom_num
                        hurt_word = dict_word_s[boom_word] + 1
                    elif self.my_list[boom_num][dict_word_s[boom_word]][1] == '>':
                        self.choose_ship = self.my_list[boom_num][dict_word_s[boom_word] - 1][1]
                        hurt_num = boom_num
                        hurt_word = dict_word_s[boom_word] - 1
                    elif self.my_list[boom_num][dict_word_s[boom_word]][1] == '^':
                        self.choose_ship = self.my_list[boom_num + 1][dict_word_s[boom_word]][1]
                        hurt_num = boom_num+1
                        hurt_word = dict_word_s[boom_word]
                    elif self.my_list[boom_num][dict_word_s[boom_word]][1] == 'v':
                        self.choose_ship = self.my_list[boom_num - 1][dict_word_s[boom_word]][1]
                        hurt_num = boom_num-1
                        hurt_word = dict_word_s[boom_word]
                    else:
                        self.choose_ship = self.my_list[boom_num][dict_word_s[boom_word]][1]
                        hurt_num = boom_num
                        hurt_word = dict_word_s[boom_word]

                    for i in range(len(self.ship_life_list)):
                        if self.ship_life_list[i][0] == self.choose_ship:
                            self.ship_life_list[i][1] -= 1
                            if self.ship_life_list[i][1] == 0:
                                del self.ship_life_list[i]
                                self.my_list[hurt_num][hurt_word] = '   '
                                if self.my_list[hurt_num - 1][hurt_word] == ' ^ ':
                                    self.my_list[hurt_num - 1][hurt_word] = '   '
                                    self.my_list[hurt_num + 1][hurt_word] = '   '
                                else:
                                    self.my_list[hurt_num][hurt_word - 1] = '   '
                                    self.my_list[hurt_num][hurt_word + 1] = '   '
                                msg_s += '船只牺牲!\n'
                                sendmsg += '对方损失一艘船只!'
                                self.s.send(sendmsg.encode())
                                time.sleep(0.5)
                                if len(self.ship_life_list) == 0:
                                    return 1
                                break
                sendmsg += '已在图中标识!\n'
                self.s.send(sendmsg.encode())
                time.sleep(0.1)
                continue
            if msg[0] == 'attack':

                boom_num = int(msg[1])
                boom_word = msg[-1]
                msg_s += '\n对方进行了地标轰炸，已在图中以\'X\'标识!'
                sendmsg = '\n轰炸完成!\n'
                # print(boom_num,type(boom_num),boom_word,type(boom_word))# #　#
                if self.my_list[boom_num][dict_word_s[boom_word]] == '   ':
                    msg_s += '\n所幸没有伤亡...'
                    sendmsg += '没有击中目标！此地标暂时无对方行踪!\n'
                    self.station_str = '   '
                    self.my_list[boom_num][dict_word_s[boom_word]] = ' X '
                else:
                    self.station_str = self.my_list[boom_num][dict_word_s[boom_word]]
                    sendmsg += '轰炸击中了船只!\n'
                    msg_s += '轰炸击中船只!船只行踪暴露!\n'
                    small_flag = 0
                    hurt_num = 0
                    hurt_word = 0

                    if self.my_list[boom_num][dict_word_s[boom_word]][1] == '<':
                        self.choose_ship = self.my_list[boom_num][dict_word_s[boom_word] + 1][1]
                        hurt_num = boom_num
                        hurt_word = dict_word_s[boom_word] + 1
                    elif self.my_list[boom_num][dict_word_s[boom_word]][1] == '>':
                        self.choose_ship = self.my_list[boom_num][dict_word_s[boom_word] - 1][1]
                        hurt_num = boom_num
                        hurt_word = dict_word_s[boom_word] - 1
                    elif self.my_list[boom_num][dict_word_s[boom_word]][1] == '^':
                        self.choose_ship = self.my_list[boom_num + 1][dict_word_s[boom_word]][1]
                        hurt_num = boom_num + 1
                        hurt_word = dict_word_s[boom_word]
                    elif self.my_list[boom_num][dict_word_s[boom_word]][1] == 'v':
                        self.choose_ship = self.my_list[boom_num - 1][dict_word_s[boom_word]][1]
                        hurt_num = boom_num - 1
                        hurt_word = dict_word_s[boom_word]
                    else:
                        self.choose_ship = self.my_list[boom_num][dict_word_s[boom_word]][1]
                        hurt_num = boom_num
                        hurt_word = dict_word_s[boom_word]

                    for i in range(len(self.ship_life_list)):
                        if self.ship_life_list[i][0] == self.choose_ship:
                            self.ship_life_list[i][1] -= 1
                            if self.ship_life_list[i][1] == 0:
                                del self.ship_life_list[i]
                                self.my_list[hurt_num][hurt_word] = '   '
                                if self.my_list[hurt_num - 1][hurt_word] == ' ^ ':
                                    self.my_list[hurt_num - 1][hurt_word] = '   '
                                    self.my_list[hurt_num + 1][hurt_word] = '   '
                                else:
                                    self.my_list[hurt_num][hurt_word - 1] = '   '
                                    self.my_list[hurt_num][hurt_word + 1] = '   '
                                msg_s += '船只牺牲!\n'
                                sendmsg += '对方损失一艘船只!'
                                self.my_list[boom_num][dict_word_s[boom_word]] = ' X '
                                small_flag = 1
                                if len(self.ship_life_list) == 0:
                                    return 1
                                break
                    self.station_str = self.my_list[boom_num][dict_word_s[boom_word]]
                    if small_flag == 0:
                        self.my_list[boom_num][dict_word_s[boom_word]] = ' x '
                self.s.send(sendmsg.encode())
                time.sleep(0.1)
                data = self.s.recv(1024)
                if data == b'over':
                    os.system(self.CL)
                    ShWr_map(self.my_list).show_self_map()
                    for i in self.ship_life_list:
                        print(i[0], '号舰血量:[', i[-1], ']', end='--')
                    print()
                    print(msg_s)
                    print()
                    input('对方回合结束,回车确认:')
                    return
            if msg[0] == 'bye':
                print('游戏结束!您获胜了')
                return 1
