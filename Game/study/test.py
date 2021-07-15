#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def print_score(**kw):
    print("    Name    Score     ")
    print("----------------------")
    for name, score in kw.items():
        print("    %s       %d     " % (name, score))


data = {
    "zhy": 89,
    "sdi": 99,
    "bdu": 78,
}
print_score(**data)


def print_info(name, *, gender, city="beijing", age):
    print("personnalInformation")
    print("--------------------")
    print("%s" % name)
    print("%s" % gender)
    print("%s" % city)
    print("%d" % age)


print_info("vsagh", gender="nu", age=18)
