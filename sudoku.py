#coding=utf-8
# Filename : sudoku.py
import sys
sys.path.append("base")
import grid
import solvers

# sudoku
class sudoku:
	def __init__(self) :
		self.__grid = grid.grid()
		self.loadSolver()
	def grid(self) :
		return self.__grid

	# run 遍历方法解题
	def run(self) :
		complexity = 0
		solvers = sorted(self.solver, key = lambda x : x.complexity())	
		while True :
			if self.grid().check() :
				print " == == Puzzle Finished == == "
				break			

			for solver in solvers :
				if complexity < solver.complexity() : complexity = solver.complexity()
				sign = solver.run(self)
				if sign > 0 :
					break
			if sign > 0 :
				continue

			print " == == Puzzle Unfinished == == "
			break
		print "Complexity Level :", complexity
		return self

	# loadSolver 载入解题方法
	def loadSolver(self) :
		self.solver = solvers.classes
		return self


sud = sudoku()
puzzle = []

# puzzle.append("010200000000003060020100450003840090050000000009000010900000000020509040080002003")
# puzzle.append("600900000008000000020410000008025000940000100000003000000003400002000000008000000")
puzzle.append("080000001600005900001002004060008090701004300020500080800700500003500008100000030")
# puzzle.append("792103800400270030013840070340218579100003628207050134481635927060017004700400360")
# puzzle.append("670004001040500706903200500309500002201900007400008306008006703305008090600700051")
# puzzle.append("820009030100020540007083002408002500010780030009400708200710900071050004060800071")
# puzzle.append("200400907030090025970100080002500604060800203703004500010006049680040050209007001")

for p in puzzle :
	sud.grid().load(p)
	if False :
		print "Puzzle :"
		sud.grid().printGrid()
		for i in range(81) :
			sud.grid().printCell(i)
		for i in range(1,10) :
			sud.grid().printNumber(i)
		sud.grid().printAllOpt()
	sud.grid().printGrid()
	# sud.grid().printAllOpt()
	# sud.sNakePair()
	sud.run()
	# sud.test()
	sud.grid().printGrid()
	print
	print