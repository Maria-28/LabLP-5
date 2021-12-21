#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Индивидуальное задание №16: Найти сумму аргументов, расположенных после последнего нуля

def args(*lst):
    t = 0
    list1 = list(lst)
    for i in range(len(list1) -1, -1, -1):
        if int(list1[i]) < 0:
            break
        t += int(list1[i])
    return t


print(args(1, -8, 0, 6, 3))
