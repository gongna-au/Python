#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Car:
    def __init__(self, manufacturer, year, country, money):
        self.manufacturer = manufacturer
        self.year = year
        self.country = country
        self.money = money

    def return_info(self):
        print(
            "这个车的生产商是："
            + self.manufacturer
            + "这个车的生产年份是："
            + "  "
            + self.year
            + "这个车的生产年地是："
            + self.country
            + "  "
            + "这个车的售价为"
            + self.money
            + "  "
            + str(self.mile)
        )

    def updata_mile(self, mile):
        """把里程设置为指定的值"""
        self.mile = mile

    def prohibit(self, newmile):
        """ 禁止把显示盘里所显示的已行路程往回改"""
        self.newmile = newmile
        if self.mile > self.newmile:
            print("警告：不可以把这个往回拨")
        else:
            self.mile = self.newmile
        print(self.mile)

    def increase(self, number):
        self.number = number
        self.mile = self.number + self.mile
        print(self.mile)


mycar = Car("奔驰", "2020-2-19", "中国", "三万")
mycar.updata_mile(10)

mycar.increase(100)
mycar.return_info()


class Eletric(Car):
    """电动车的独特之处"""

    def __init__(self, manufacturer, year, country, money):
        """初始化父类的属性"""
        super().__init__(manufacturer, year, country, money)
        """定义了一个电动车独特的属性"""
        self.eletric = 70
        self.battery = Battery()

    def print_ele(self):
        print(self.eletric)
        print(self.manufacturer)
        print(self.year)
        print(self.country)
        print(self.money)

    """重写父类"""

    def updata_mile(self):
        pass

    """重写父类"""

    def increase(self):
        pass


class Battery:
    def __init__(self, ele=0, time=0):
        self.ele = ele
        self.time = time
        print("距离充满还需要" + str(time) + "时间")
        print("剩余的电量是" + str(ele))


myelecar = Eletric("cs", "sa", "gera", "ewf")
myelecar.eletric = 100
myelecar.print_ele()
myelecar.updata_mile()
myelecar.increase()
myelecar.battery.__init__()
