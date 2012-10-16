#coding=utf-8
# Filename: sHideSingle.py
from solver import solver

# sHideSingle 隐性唯一法
class sHideSingle(solver) :
	
	def __init__(self) :
		solver.__init__(self, complexity = 2, name = "sHideSingle", type = "cell")

	def solve(self, sudoku) :
		for g_unit_id in range(27) :
			unit = sudoku.grid().allUnit(g_unit_id)
			for number in range(1,10) :
				opt = sudoku.grid().number(number).opt(unit.cell_id())
				if len(opt) == 1 :
					if sudoku.grid().cell(opt[0]).value() == 0 :
						sudoku.grid().setValue(opt[0], number)
						self._matching(opt[0], number)
		return self