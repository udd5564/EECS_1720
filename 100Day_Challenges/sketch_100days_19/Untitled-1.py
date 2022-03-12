class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1
while (True):
    try:
        print("[Leftover Chicken : {0}]".format(chicken))3
        order = int(input("How many chickens would you like to order?"))
        if order > chicken:
            print("We don't have enough ingredients.")
        elif order <= 0:
            raise ValueError
        else:
            print("[Waiting Number {0}] {1} order(s) have(s) been placed. "\
                .format(waiting, order))
            waiting += 1
            chicken -= order
        
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("Wrong Value.")
    except SoldOutError:
        print("Sold Out. We don't get more order.")
        break
