#coding=utf-8
# Filename: solver.py
import convertor
import grid

# solver
class solver:
	
	def __init__(self, complexity = 0, name = "sOlver", type = "opt") :
		self.__complexity = complexity
		self.__name = name
		self.__type = type
		self.__count = 0
		
	def name(self) :
		return self.__name

	def complexity(self) :
		return self.__complexity

	def __begin(self) :
		print " -- --", self.__name, "Begin -- -- "

	def __finished(self) :
		print " -- --", self.__name, "Finished -- -- "
		print

	def _matching(self, cell, number) :
		try :
			a = { 'cell' : 'cell', 'opt' : ' .. cell'}[self.__type]
			b = self.gCP(cell)
			c = { 'cell' : 'setValue', 'opt' : 'delOpt :'}[self.__type]
			d = number
			e = "by " + self.__name
			print a, b, c, d, e
			self.__count += 1
		except KeyError :
			print "Check the Type"

	def run(self, sudoku) :
		self.__begin()
		self.__count = 0
		self.solve(sudoku)
		self.__finished()
		return self.__count

	def solve(self, sudoku) :
		return self

	# gCP getCellPostion 将cell_id输出为更好的样式
	def gCP(self, cell_id) :
		row = str(convertor.id2Row(cell_id)+1)
		column = str(convertor.id2Column(cell_id)+1)
		id = str(cell_id)
		return id + "( R" + row + " C" + column+" )"