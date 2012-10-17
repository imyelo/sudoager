#coding=utf-8
# Filename: sNakeSingle.py
from solver import solver

# sNakeSingle 显性唯一法
class sNakeSingle(solver) :

	def __init__(self) :
		solver.__init__(self, complexity = 1, name = "sNakeSingle", type = "cell", printChart = False)
		
	def solve(self, sudoku) :

		# for i in range(81) :
		# 	if sudoku.grid().cell(i).value() == 0 :
		# 		opt = sudoku.grid().cell(i).opt()
		# 		if len(opt) == 1 :
		# 			sudoku.grid().setValue(i, opt[0])
		# 			self._matching(i, opt[0])
		# return self
		# 
		# for c in filter( lambda cell : cell.value() == 0 and len(cell.opt()) == 1 , sudoku.grid().cell() ) :
		# 	sudoku.grid().setValue( c.id(), c.opt()[0] )
		# 	self._matching( c.id() , c.opt()[0] )
		# return self
		# 
		for c in sudoku.grid().cell() :
			if c.value() == 0 and len(c.opt()) == 1 :
				sudoku.grid().setValue( c.id(), c.opt()[0] )
				self._matching( c.id() , c.opt()[0] )
		return self