# encoding = 'utf-8'

def deal():
    while len(string_list) != 0:
        if list_all[-1] == '#' and string_list[-1] == '#':
            break
        print("符号栈:" + str(list_all), end='')
        print("\t输入缓冲区:" + str(string_list))

        if list_all[-1] in list_intt:
            if list_all[-1] == string_list[0]:
                string_list.pop(0)
                list_all.pop()
        else:
            add = lists[list_int.index(list_all[-1])][list_intt.index(string_list[0])]

            print("所用产生式:" + list_all[-1] + '->' + add)

            if add == '0':
                list_all.pop()
            else:
                list_all.pop()
                for i in add[::-1]:
                    list_all.append(i)
        print()

    print('分析结束')
    print("输入缓冲区:" + str(string_list))
    print("符号栈:" + str(list_all))


if __name__ == '__main__':
    dict_s = {'S': ['aBc', 'bAB'], 'A': ['aAb', 'b'], 'B': 0}

    string = 'baabbb#'
    string_list = list(string)  # 缓冲区

    list_int = ['S', 'A', 'B']
    list_intt = ['a', 'b', 'c', '#']

    lists = [[] for i in range(3)]
    lists[0] = ['aBc', 'bAB', '', '']
    lists[1] = ['aAb', 'b', '', '']
    lists[2] = ['', 'b', '0', '0', '']

    list_all = ['#', 'S']  # 符号栈

    deal()
