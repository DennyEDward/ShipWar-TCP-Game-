from ShWr_map import *
from __shipDemo import *
import  time

class Solo_game:
    """
        单人游戏模式
    """
    def __init__(self):
        self.list = [
            ['   ']*15,
            ['   '] * 15,
            ['   '] * 15,
            ['   '] * 15,
            ['   '] * 15,
            ['   '] * 15,
            ['   '] * 15,
            ['   '] * 15,
            ['   '] * 15,
            ['   '] * 15,
           ]
    def run(self):
        self.place_ship()


    def show_map(self):
        map = ShWr_map(self.list)
        map.show_self_map()
    def place_ship(self):
        self.place_bigship()
        self.place_smallship(2)

    def place_bigship(self):
        pos_round = []
        print('地图初始化完成----开始摆放战舰')
        time.sleep(1)

        self.show_map()
        print('****1号母舰位置选择****')

        Show_ship.show_bigship()


        while True:
            print("请选择横向放置或者纵向放置:\n1.横向放置\n2.纵向放置")
            str_pos = input(">>>:")
            if str_pos == '1':
                pos_round = [2, 1]

            elif str_pos == '2':
                pos_round = [1, 2]

            else:
                print("请输入正确选择!")
                time.sleep(2)
                continue
            str = input("输入放置中心坐标(格式:'数字,小写字母'):")
            map = ShWr_map()
            demo_pos = str.split(',')
            list_pos = []
            try:

                list_pos.append((int(demo_pos[0])))
                list_pos.append(demo_pos[-1])
                if list_pos[0] not in map.list_num[pos_round[-1]:len(map.list_num)-pos_round[-1]]:
                    print("船只纵向边缘超出地图范围!")
                    continue
                if list_pos[-1] not in map.list_word_s[pos_round[0]:len(map.list_word_s)-pos_round[0]]:
                    print("船只横向边缘超出地图范围!")
                    continue
                if str_pos == '1':
                    # 横向画法
                    self.list[list_pos[0]][map.dict_word_s[list_pos[-1]]] = '[1]'
                    print(list_pos[0],map.dict_word_s[list_pos[-1]])
                    self.list[list_pos[0]][map.dict_word_s[list_pos[-1]] - 1] = '***'
                    print(list_pos[0], map.dict_word_s[list_pos[-1]] -1 )
                    self.list[list_pos[0]][map.dict_word_s[list_pos[-1]] + 1] = '***'
                    self.list[list_pos[0]][map.dict_word_s[list_pos[-1]] - 2] = ' | '
                    self.list[list_pos[0]][map.dict_word_s[list_pos[-1]] + 2] = ' | '
                    self.list[list_pos[0] - 1][map.dict_word_s[list_pos[-1]]] = ' - '
                    self.list[list_pos[0] - 1][map.dict_word_s[list_pos[-1]] - 1] =' - '
                    self.list[list_pos[0] - 1][map.dict_word_s[list_pos[-1]] + 1] = ' - '
                    self.list[list_pos[0] - 1][map.dict_word_s[list_pos[-1]] - 2] = ' / '
                    self.list[list_pos[0] - 1][map.dict_word_s[list_pos[-1]] + 2] = ' \\ '
                    self.list[list_pos[0] + 1][map.dict_word_s[list_pos[-1]]] = ' - '
                    self.list[list_pos[0] + 1][map.dict_word_s[list_pos[-1]] - 1] = ' - '
                    self.list[list_pos[0] + 1][map.dict_word_s[list_pos[-1]] + 1] = ' - '
                    self.list[list_pos[0] + 1][map.dict_word_s[list_pos[-1]] - 2] = ' \\ '
                    self.list[list_pos[0] + 1][map.dict_word_s[list_pos[-1]] + 2] = ' / '


                elif str_pos == '2':
                    # 纵向画法
                    self.list[list_pos[0]][map.dict_word_s[list_pos[-1]]] = '[1]'
                    self.list[list_pos[0] - 1][map.dict_word_s[list_pos[-1]]] = '***'
                    self.list[list_pos[0] + 1][map.dict_word_s[list_pos[-1]]] = '***'
                    self.list[list_pos[0] - 2][map.dict_word_s[list_pos[-1]]] = ' - '
                    self.list[list_pos[0] + 2][map.dict_word_s[list_pos[-1]]] = ' - '
                    self.list[list_pos[0]][map.dict_word_s[list_pos[-1]]-1] = ' | '
                    self.list[list_pos[0] - 1][map.dict_word_s[list_pos[-1]] - 1] = ' | '
                    self.list[list_pos[0] + 1][map.dict_word_s[list_pos[-1]] - 1] = ' | '
                    self.list[list_pos[0]][map.dict_word_s[list_pos[-1]] + 1] = ' | '
                    self.list[list_pos[0] - 1][map.dict_word_s[list_pos[-1]] + 1] = ' | '
                    self.list[list_pos[0] + 1][map.dict_word_s[list_pos[-1]] + 1] = ' | '
                    self.list[list_pos[0] - 2][map.dict_word_s[list_pos[-1]] - 1] = ' / '
                    self.list[list_pos[0] - 2][map.dict_word_s[list_pos[-1]] + 1] = ' \\ '
                    self.list[list_pos[0] + 2][map.dict_word_s[list_pos[-1]] + 1] = ' / '
                    self.list[list_pos[0] + 2][map.dict_word_s[list_pos[-1]] - 1] = ' \\ '
                self.show_map()
                if input("按r键重新摆放,回车键确认摆放") == 'r':
                    self.list = [
                        ['   '] * 15,
                        ['   '] * 15,
                        ['   '] * 15,
                        ['   '] * 15,
                        ['   '] * 15,
                        ['   '] * 15,
                        ['   '] * 15,
                        ['   '] * 15,
                        ['   '] * 15,
                        ['   '] * 15,
                    ]
                    continue

                break

            except:
                print("格式不对,请核对!")
                continue

    def place_smallship(self,num):
        self.show_map()
        print('****%d号巡洋舰位置选择****' % (num))
        print()
        Show_ship.show_smallship()
        while True:
            print("请选择横向放置或者纵向放置:\n1.横向放置\n2.纵向放置")
            str_pos = input(">>>:")
            if str_pos == '1':
                pos_round = [2,1]
                break
            elif str_pos == '2':
                pos_round = [1,2]
                break

    def second_place_ship(self):
        pass







if __name__ == '__main__':
    s = Solo_game()
    s.run()