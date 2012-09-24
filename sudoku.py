#coding=utf-8
# Filename : sudoku.py
import grid

# sudoku
class sudoku:
	def __init__(self) :
		self.__grid = grid.grid()
	def grid(self) :
		return self.__grid
	def sNakeSingle(self) :
		print " -- -- sNakeSingle Begin -- -- "
		count = 0
		for i in range(81) :
			if self.__grid.cell(i).value() == 0 :
				opt = self.__grid.cell(i).opt()
				if len(opt) == 1 :
					self.__grid.setValue(i, opt[0])	
					print "cell", i, "setValue :", opt[0], "by sNakeSingle"
					count += 1
		print " -- -- sNakeSingle Finished -- -- "
		print 
		return count 
	def sHideSingle(self) :
		print " -- -- sHideSingle Begin -- -- "
		count = 0
		for g_unit_id in range(27) :
			unit = self.__grid.allUnit(g_unit_id)
			for number in range(1,10) :
				opt = self.__grid.number(number).opt(unit.cell_id())
				if len(opt) == 1 :
					if self.__grid.cell(opt[0]).value() == 0 :
						self.__grid.setValue(opt[0], number)
						print "cell", opt[0], "setValue :", number, "by sHideSingle"
						count += 1
		print " -- -- sHideSingle Finished -- -- "
		print 
		return count
	def run(self) :
		while True :
			if self.__grid.check() :
				print " == == Puzzle Finished == == "
				break
			sign = self.sNakeSingle()
			if sign > 0 :
				continue
			sign = self.sHideSingle()
			if sign > 0 :
				continue
			print " == == Puzzle Unfinished == == "
			break



sud = sudoku()
# sud.grid().load("200400907030090025970100080002500604060800203703004500010006049680040050209007001")
# sud.grid().load("600900000008000000020410000008025000940000100000003000000003400002000000008000000")
# sud.grid().load("010200000000003060020100450003840090050000000009000010900000000020509040080002003")
# sud.grid().load("080000001600005900001002004060008090701004300020500080800700500003500008100000030")
sud.grid().load("792103800400270030013840070340218579100003628207050134481635927060017004700400360")
if False :
	print "Puzzle :"
	sud.grid().printGrid()
	for i in range(81) :
		sud.grid().printCell(i)
	for i in range(1,10) :
		sud.grid().printNumber(i)
	sud.grid().printAllOpt()
sud.grid().printGrid()
sud.run()
sud.grid().printGrid()
