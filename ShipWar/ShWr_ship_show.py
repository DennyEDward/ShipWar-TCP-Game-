def ship_show(num):
    print('''%d号巡洋舰横向展示:  %d号巡洋舰纵向展示:\n
                           ^\n
        <  [%d]  >         [%d]\n
                           v'''%(num,num,num,num))
    print()


def ship_show_line(num):
    print('''%d号巡洋舰横向展示: 
                               
 <  [%d]  >         
                               ''' % (num,num))
    print()

def ship_show_leng(num):
    print('''%d号巡洋舰纵向展示:\n
    ^\n
   [%d]\n
    v'''%(num,num))
    print()

if __name__ == '__main__':
    ship_show_line(1)
    ship_show_leng(1)
