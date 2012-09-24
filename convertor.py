#coding=utf-8
# Filename: convertor.py

import math

# --Convertor--
# Decimal to Ternary
def getTer3(i) :
	return int(math.floor(i/27)%3)
def getTer2(i) :
	return int(math.floor(i/9)%3)
def getTer1(i) :
	return int(math.floor(i/3)%3)
def getTer0(i) :
	return int(i%3)
# id to R,C,B,A
def id2Row(id) :
	return int(getTer3(id)*3+getTer1(id))
def id2Column(id) :
	return int(getTer2(id)*3+getTer0(id))
def id2Box(id) :
	return int(getTer3(id)*3+getTer2(id))
def id2Atom(id) :
	return int(getTer1(id)*3+getTer0(id))
# B&A to id,R,C
def BA2id(box, atom) :
	return int(getTer1(box)*27 + getTer0(box)*9 + getTer1(atom)*3 + getTer0(atom))
def BA2Row(box, atom) :
	return int(getTer1(box)*3 + getTer1(atom))
def BA2Column(box, atom) :
	return int(getTer0(box)*3 + getTer0(atom))
# R&C to id,B,A
def RC2id(row, column) :
	return int(getTer1(row)*27 + getTer1(column)*9 + getTer0(row)*3 +getTer0(column))
def RC2Box(row, column) :
	return int(getTer1(row)*3 + getTer1(column))
def RC2Atom(row, column) :
	return int(getTer0(row)*3 + getTer0(column))
# --/Convertor--