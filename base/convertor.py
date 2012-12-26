#coding=utf-8
# Filename: convertor.py
import math


# --Convertor--
# Decimal to Ternary
def getTer3(i, base=3):
    return int(math.floor(i / (base ** 3)) % base)


def getTer2(i, base=3):
    return int(math.floor(i / (base ** 2)) % base)


def getTer1(i, base=3):
    return int(math.floor(i / base) % base)


def getTer0(i, base=3):
    return int(i % base)


# id to R,C,B,A
def id2Row(id, base=3):
    return int(getTer3(id, base) * base + getTer1(id, base))


def id2Column(id, base=3):
    return int(getTer2(id, base) * base + getTer0(id, base))


def id2Box(id, base=3):
    return int(getTer3(id, base) * base + getTer2(id, base))


def id2Atom(id, base=3):
    return int(getTer1(id, base) * base + getTer0(id, base))


# B&A to id,R,C
def BA2id(box, atom, base=3):
    return int(getTer1(box, base) * (base ** 3) + getTer0(box, base) * (base ** 2) + getTer1(atom, base) * base + getTer0(atom, base))


def BA2Row(box, atom, base=3):
    return int(getTer1(box, base) * base + getTer1(atom, base))


def BA2Column(box, atom, base=3):
    return int(getTer0(box, base) * base + getTer0(atom, base))


# R&C to id,B,A
def RC2id(row, column, base=3):
    return int(getTer1(row, base) * (base ** 3) + getTer1(column, base) * (base ** 2) + getTer0(row, base) * base + getTer0(column, base))


def RC2Box(row, column, base=3):
    return int(getTer1(row, base) * base + getTer1(column, base))


def RC2Atom(row, column, base=3):
    return int(getTer0(row, base) * base + getTer0(column, base))

# --/Convertor--
