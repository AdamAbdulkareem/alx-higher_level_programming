#!/usr/bin/python3
import dis
def magic_calculation(a, b):
    const = 98
    return a + a ** b;
dis.dis(magic_calculation)
