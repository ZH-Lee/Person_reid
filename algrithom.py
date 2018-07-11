#!/usr/bin/env python
# -*- coding_utf-8 -*-
"""
    Author: Zhenghan Lee
    Date:
"""
def is_bianxing(str1,str2):
    dic = {}
    for i in str1:
        if i in dic:

            dic[i] += 1
        else:
            dic[i] = 1
    for j in str2:
        dic[j] -= 1
        if dic[j]<0:
            return False
    return True

def add_(str1):
    sign = 0
    sum = 0
    num = ''
    for i in str1:
        if ord(i) == ord('-'):
            sign += 1
        else:
            n = ord(i) - ord('0')
            if n <= 9 and n >=0:
                num += i
            else:
                if num == '':
                    pass
                else:
                    sum = (-1) ** sign * int(num) + sum
                    num =''
                    sign = 0
                    #print(sum)
    if num != '':
        sum += (-1) ** sign * int(num)


if __name__ == '__main__':
    #print(is_bianxing('123','2331'))
    add_('A-1B--2c--D6E33')
    add_('012c-1')