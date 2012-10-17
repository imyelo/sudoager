#coding=utf-8
# Filename: solver.py
# import sys
# sys.path.append("..")
# sys.path.append("../base")
import convertor
import grid

# solver
class solver:
	
	def __init__(self, complexity = 0, name = "sOlver", type = "opt", printChart = False) :
		self.__complexity = complexity
		self.__name = name
		self.__type = type
		self.__count = 0
		self.__hash = []
		self.__printChart = printChart
		
	def name(self) :
		return self.__name

	def complexity(self) :
		return self.__complexity

	def __begin(self) :
		print " -- --", self.__name, "Begin -- -- "

	def __finished(self) :
		print " -- --", self.__name, "Finished -- -- "
		print
	def __doPrintChart(self, sudoku) :
		try : 
			if self.__printChart :
				print 
				{ 'cell' : lambda :sudoku.grid().printGrid() , 'opt' : lambda :sudoku.grid().printAllOpt() }[self.__type]()
				print 
		except KeyError :
			print "Check the Type"
		return None

	def _matching(self, cell, number) :
		try :
			a = { 'cell' : 'cell', 'opt' : ' .. cell'}[self.__type]
			b = self.gCP(cell)
			c = { 'cell' : 'setValue', 'opt' : 'delOpt :'}[self.__type]
			d = number
			e = "by " + self.__name
			print a, b, c, d, e
			self.__count += 1
			self.hash(cell, number)
		except KeyError :
			print "Check the Type"

	def run(self, sudoku) :
		self.__begin()
		self.__doPrintChart(sudoku)
		self.__count = 0
		self.solve(sudoku)
		self.__doPrintChart(sudoku)
		self.__finished()
		return { 'count' : self.__count , 'hash' : self.__hash }

	def solve(self, sudoku) :
		return self

	# gCP getCellPostion 将cell_id输出为更好的样式
	def gCP(self, cell_id) :
		row = str(convertor.id2Row(cell_id)+1)
		column = str(convertor.id2Column(cell_id)+1)
		id = str(cell_id)
		return id + "( R" + row + " C" + column+" )"

	# hash 计算解题特征码
	def hash(self, cell, number) :
		hash = [str(self.__complexity), self.__type, str(cell), str(number)]
		self.__hash.append('-'.join(hash))
		return self.__hash