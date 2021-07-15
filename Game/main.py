from collections import OrderedDict
from random import randint

list = OrderedDict()
list["gysudaf"] = "nfag"
list["baY"] = "buiSO"
list["gwqiug"] = "augsfu"
for key, value in list.items():
    print(key)
    print(value)

result = randint(1, 6)
print(result)
for i in range(1, 7):
    result = randint(1, 6)
    print(result)


filename = "1.txt"

with open(filename, "a") as file_object:
    file_object.write("5677868111144444443333333\n")
    file_object.write("5677868999999999999999999999999999\n")
    file_object.write("3428698317017000000000000000000000000000\n")
a=  int(input())
b= int(input())

try:
    c=a/b
except ZeroDivisionError:
    print("you can not input a zero")
else:
    print('hdfuifhu')