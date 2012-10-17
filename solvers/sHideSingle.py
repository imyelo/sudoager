#coding=utf-8
# Filename: sHideSingle.py
from solver import solver

# sHideSingle 隐性唯一法
class sHideSingle(solver) :
	
	def __init__(self) :
		solver.__init__(self, complexity = 2, name = "sHideSingle", type = "cell", printChart = False)

	def solve(self, sudoku) :

		# for g_unit_id in range(27) :
		# 	unit = sudoku.grid().allUnit(g_unit_id)
		# 	for number in range(1,10) :
		# 		opt = sudoku.grid().number(number).opt(unit.cell_id())
		# 		if len(opt) == 1 :
		# 			if sudoku.grid().cell(opt[0]).value() == 0 :
		# 				sudoku.grid().setValue(opt[0], number)
		# 				self._matching(opt[0], number)
		# return self

		# for unit in sudoku.grid().allUnit() :
		# 	cells = unit.cell_id()
		# 	numbers = map( lambda n : sudoku.grid().number(n), range(1,10) )
		# 	for number in filter( lambda n : len(n.opt(cells)) == 1 and sudoku.grid().cell(n.opt(cells)[0]).value() == 0 , numbers ) :
		# 		sudoku.grid().setValue(number.opt(cells)[0], number.id())
		# 		self._matching(number.opt(cells)[0], number.id())
		# return self

		for unit in sudoku.grid().allUnit() :
			cells = unit.cell_id()
			for n in map( lambda n : sudoku.grid().number(n), range(1,10) ) :
				if len(n.opt(cells)) == 1 and sudoku.grid().cell(n.opt(cells)[0]).value() == 0 :
					sudoku.grid().setValue(n.opt(cells)[0], n.id())
					self._matching(n.opt(cells)[0], n.id())
		return self