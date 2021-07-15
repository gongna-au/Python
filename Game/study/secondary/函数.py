#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import 副本

uncomplete_design = ["wm", "ss", "ddhi", "siag"]

completed_design = []
uncomplete_design_copy = uncomplete_design[:]


def print_model(uncomplete_design_copy, completed_design):
    while uncomplete_design:
        new = uncomplete_design.pop()
        completed_design.append(new)
        print(uncomplete_design)


def print_commodel(completed_design):
    for new in completed_design:
        print(new)


print_model(uncomplete_design, completed_design)

print_commodel(completed_design)
print(completed_design)

print(uncomplete_design)

info = {"name": "gn", "age": "19", "city": "gansu", "sex": "nan"}
usr = 副本.print_userinfo(first="g", second="n", **info)

print(usr)
