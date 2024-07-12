#!/usr/bin/python3
print(", ".join("{:02}, {:02}".format(i // 10, i % 10) for i in range(10, 100) if i // 10 < i % 10))
