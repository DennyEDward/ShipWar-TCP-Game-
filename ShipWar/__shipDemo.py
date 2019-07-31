class Show_ship:
    @staticmethod
    def show_bigship():
        print('''1号母舰横向展示:     1号母舰纵向展示:\n
                    /  -  \\\n
 /  -   -   -  \\   |  ***  |\n
 | *** [1] *** |   |  [1]  |\n
 \\  -   -   -  /   |  ***  |\n
                    \\  -  /
 ''')
    @staticmethod
    def show_smallship():
        print('''巡洋舰横向展示:  巡洋舰纵向展示:\n
                       ^\n
    <  [ ]  >         [ ]\n
                       v''')


if __name__ == "__main__":
    s = Show_ship()
    s.show_bigship()
    s.show_smallship()
