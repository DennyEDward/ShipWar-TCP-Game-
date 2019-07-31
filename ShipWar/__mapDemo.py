list_num = [0,1,2,3,4,5,6,7,8,9]
list_word_s = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
             'n','o']
count = 0
for i in  range(10):
    if count == 0:
        print("    ",end='')

        for word in list_word_s:
            print(word,end='   ')
            count += 1
        print()
    print(list_num[i],'|',end='')
    for j in range(15):
        if i%2==0:
            print('   ',end='·')
        elif i == 9:
            print('____', end='')
        else:
            print('   ', end='')
    print()
    print()



    s = ''''
    
    a   b   c   d   e   f   g   h   i   j   k  l                                  
0 |   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·  |

1 |                                              |                     

2 |   ·   ·   ·   · < ·[3]· > ·   ·   ·   ·   ·  |

3 |                 O                            |

4 |   ·   ·   ·   ·   ·   ·   ·   · ^ ·   ·   ·  |

5 |                                [4]           |    

6 |   ·   · < ·[1]· > ·   ·   ·   · v ·   ·   ·  |

7 |                 ^                            |

8 |   ·   ·   ·   ·[2]·   ·   ·   ·   ·   ·   ·  |

9 |_________________v____________________________|
    
    
    '''