list_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_word_s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
list_word_S = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
dict_word_s = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11}
dict_word_S = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11}
class ShWr_map:
    def __init__(self,list = [
            ['   ']*12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
            ['   '] * 12,
           ]):
        self.list_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.list_word_s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
        self.list_word_S = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
        self.dict_word_s = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11}
        self.dict_word_S = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11}
        self.__list_map = list
    def show_self_map(self):
        print(' '*18,'[我方版图]')
        count = 0
        word_count = 0
        for i in self.list_word_s:
            if count == 0:
                print("   ",end='')

            print(i,end='')
        print()
        print()

        for i in self.__list_map:
            print(self.list_num[count],end=' ')
            count += 1
            for j in i:
                print(j,end="·")
            print("|")
            print()
        print("-"*50)
    def show_enemy_map(self):
        print(' '*18,'[敌方版图]')
        count = 0
        word_count = 0
        for i in self.list_word_s:
            if count == 0:
                print("   ",end='')

            print(i,end='')
        print()
        print()

        for i in self.__list_map:
            print(self.list_num[count],end=' ')
            count += 1
            for j in i:
                print(j,end="·")
            print("|")
            print()
        print("-" * 50)
    def show_demo_map(self):
        print(' '*18,'[版图示例]')
        count = 0
        word_count = 0
        for i in self.list_word_s:
            if count == 0:
                print("   ",end='')

            print(i,end='')
        print()
        print()

        for i in self.__list_map:
            print(self.list_num[count],end=' ')
            count += 1
            for j in i:
                print(j,end="·")
            print("|")
            print()
        print("-" * 50)








if __name__ == "__main__":
    list = [
            ['   ']*12
           ]*10
    s = ShWr_map()
    s.show_self_map()
    s.show_enemy_map()
    s.show_demo_map()
