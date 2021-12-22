#!/usr/bin/env python3
# -*- coding: utf-8 -*-
Задание. Вывести данные , переданные переменной.


def intro(**data):
    print("\nData type of argument: ",type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))

intro(Firstname="МАША", Lastname="СЕРИКОВА", Age=19, Phone=18938377890)
intro(Firstname="РАФИК", Lastname="ПИКАЧУ", Email="nhdhhdhdh@nomail.com", Country="Russia", Age=19, Phone=9876543210)
