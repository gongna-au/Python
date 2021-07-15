#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def print_userinfo(first, second, **list):
    user = {}
    user["first"] = first
    user["second"] = second
    for key, value in list.items():
        print(key)
        print(value)
        user[key] = value
    return user



