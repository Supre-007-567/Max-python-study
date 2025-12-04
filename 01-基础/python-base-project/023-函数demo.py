"""
银行demo
"""

money = 1000
name = None


def check_money():
    """
    查询余额
    :return:
    """
    global money
    global name
    print(f"目前账户: {name}\n余额为: {money}")


def menu_save():
    """
    存钱
    :return:
    """
    global money
    global name
    save_money = int(input("请输入要存的金额"))
    money += save_money
    print(f"存入成功\n")
    check_money()


def draw_money():
    """
    取钱
    :return:
    """
    global money
    global name
    check_money()
    ded_money = int(input("请输入要取出的金额"))
    if money - ded_money > 0:
        money -= ded_money
    else:
        print("余额不足")
        return
    print(f"取出成功")
    check_money()


def main_menu():
    global name
    name = input("请输入用户名")
    while True:
        print("----------------主菜单----------------")
        print("余额查询\t[输入1]")
        print("存款\t\t[输入2]")
        print("取款\t\t[输入3]")
        print("退出\t\t[输入4]")
        option = int(input("请选择:"))
        if option == 1:
            check_money()
        elif option == 2:
            menu_save()
        elif option == 3:
            draw_money()
        else:
            print("已退出")
            return


main_menu()





