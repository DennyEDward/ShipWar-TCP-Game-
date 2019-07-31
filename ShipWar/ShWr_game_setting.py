def game_setting():
    game_word = ''
    print('请配置游戏环境\n1.Linux\n2.Windows')
    game_set = input('请选择:')

    if game_set == '2':
        game_word = 'CLR'
        ip_get ='ipconfig'
    else:
        game_word = 'clear'
        ip_get = 'ifconfig'
    return game_word,ip_get











if __name__ == '__main__':
    game_setting()