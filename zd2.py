#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def harmon_mid(*args):
    if args and 0 not in args:
        ans = 0
        for item in args:
            ans += 1/item
        return len(args) / ans
    else:
        return None

if __name__ == "__main__":
    print(harmon_mid())
    print(harmon_mid(3, 7, 1, 6, 9))
    print(harmon_mid(3, 2, 9, 5, 7, 8))