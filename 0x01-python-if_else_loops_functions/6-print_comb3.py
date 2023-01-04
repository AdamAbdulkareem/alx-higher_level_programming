#!/usr/bin/python3
for i in range(0, 10):
    for k in range(i + 1, 10):
        if i != k:
            if (int(str(i) + str(k))) == 89:
                print(str(i) + str(k), end="\n")
            else:
                print(str(i) + str(k), end=", ")
