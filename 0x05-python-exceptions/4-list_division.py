#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    count = 0
    new = []
    res = 0

    while count < list_length:
        try:
            a = my_list_1[count]
            b = my_list_2[count]
            if not (isinstance(a, (int, float)) and
                    isinstance(b, (int, float))):
                print("wrong type")
                res = 0
            else:
                res = a / b
        except IndexError:
            print("out of range")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        finally:
            new.append(res)
            count += 1
    return new
