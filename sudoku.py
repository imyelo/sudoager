#coding=utf-8
# Filename : sudoku.py
import grid

# sudoku
class sudoku:
	def __init__(self) :
		self.__grid = grid.grid()
	def grid(self) :
		return self.__grid

	# sNakeSingle 显性唯一法
	def sNakeSingle(self) :
		print " -- -- sNakeSingle Begin -- -- "
		count = 0
		for i in range(81) :
			if self.__grid.cell(i).value() == 0 :
				opt = self.__grid.cell(i).opt()
				if len(opt) == 1 :
					self.__grid.setValue(i, opt[0])	
					print "cell", self.gCP(i), "setValue :", opt[0], "by sNakeSingle"
					count += 1
		print " -- -- sNakeSingle Finished -- -- "
		print 
		return count 

	# sHideSingle 隐形唯一法
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
						print "cell", self.gCP(opt[0]), "setValue :", number, "by sHideSingle"
						count += 1
		print " -- -- sHideSingle Finished -- -- "
		print 
		return count

	# sNakePair 显性对数法
	def sNakePair(self) :
		print " .. -- sNakePair Begin -- .. " 
		self.__grid.printAllOpt()
		count = 0
		cell_with_two_opt = [ self.__grid.cell(i) for i in range(81) if self.__grid.cell(i).len() == 2 ]
		cell_with_two_opt.sort()
		if len(cell_with_two_opt) > 1 :
			for cell_A in cell_with_two_opt[:-2] :
			# TODO 改进遍历效率
				for cell_B in [ cell for cell in cell_with_two_opt if cell > cell_A ] :
					if cell_B.opt() == cell_A.opt() :
						for type in [0,1,3] :
							if cell_A.getUnitDict()[grid.UNITTYPE[type]] == cell_B.getUnitDict()[grid.UNITTYPE[type]] :
								unit = self.__grid.unit(type, cell_A.getUnitDict()[grid.UNITTYPE[type]])
								otherCellInUnit_id = [ cell.id() for cell in unit.cell() if cell != cell_A and cell != cell_B ]
								res = self.__grid.delOpt(otherCellInUnit_id, cell_B.opt())
								if res :
									for r in res[0] :
										print " .. cell", self.gCP(r[0]), "delOpt :", r[1], "by sNakePair"
										count += 1
		self.__grid.printAllOpt()
		print " .. -- sNakePair Finished -- .. "
		print 
		return count

	# gCP getCellPostion 将cell_id输出为更好的样式
	def gCP(self, cell_id) :
		row = str(grid.convertor.id2Row(cell_id)+1)
		column = str(grid.convertor.id2Column(cell_id)+1)
		id = str(cell_id)
		return id + "( R" + row + " C" + column+" )"

	# run 循环调用方法解题
	def run(self) :
		complexity = 0;
		while True :
			if self.__grid.check() :
				print " == == Puzzle Finished == == "
				break
			if complexity < 1 : complexity = 1;
			sign = self.sNakeSingle()
			if sign > 0 :
				continue
			# if complexity < 2 : complexity = 2;
			# sign = self.sHideSingle()
			# if sign > 0 :
			# 	continue
			if complexity < 3 : complexity = 3;
			sign = self.sNakePair()
			if sign > 0 :
				continue
			print " == == Puzzle Unfinished == == "
			break
		print "Complexity Level :", complexity



sud = sudoku()
puzzle = []

# puzzle.append("010200000000003060020100450003840090050000000009000010900000000020509040080002003")
# puzzle.append("600900000008000000020410000008025000940000100000003000000003400002000000008000000")
# puzzle.append("080000001600005900001002004060008090701004300020500080800700500003500008100000030")
puzzle.append("792103800400270030013840070340218579100003628207050134481635927060017004700400360")
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
	sud.grid().printGrid()
	print
	print