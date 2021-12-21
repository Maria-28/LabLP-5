#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def geometric_mid(*args):
    if args:
        ans = 1
        for item in args:
            ans *= item
        return pow(ans, 1/len(args))
    else:
        return None


if __name__ == "__main__":
    print(geometric_mid())
    print(geometric_mid(4, 3, 1, 7, 8))
    print(geometric_mid(2, 6, 5, 8, 3, 1))