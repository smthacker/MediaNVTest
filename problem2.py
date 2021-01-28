#// Customer bought stuff worth x rupees. She handed y rupees to the cashier. Hand the change back to the customer in the following coin denomination only. {1, 5, 10}. Please minimize number of coins so that the customer doesn't feel bulky in her pocket!
#
# // How to calculate
# // x is 65 & y is 100 then output
# // {"10 rs coin":3, "5 rs coin":1, "1 rs coin":0}
#
# // x is 45 & y is 50 then output
# // {"10 rs coin":0, "5 rs coin":1, "1 rs coin":0}
#
# // x is 12 & y is 20 then output
# // {"10 rs coin":0, "5 rs coin":1, "1 rs coin":3}
#


change_coins = [5, 10, 1]
def give_back_change(x,y):
    change_coins.sort(reverse=True)
    op_dict = dict.fromkeys(change_coins, 0)
    print(op_dict)
    if x < y:
        total_money_to_return = y - x
        for i in change_coins:
            if i <= total_money_to_return:
                coins = total_money_to_return // i
                remaining_money = total_money_to_return % i
                total_money_to_return = remaining_money
                op_dict[i] = coins
    else :
        print("There's nothing to return..........")
    print(op_dict)


if __name__ == '__main__':
    x = 65
    y = 100
    give_back_change(x,y)