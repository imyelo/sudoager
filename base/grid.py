#coding=utf-8
# Filename: grid.py
import convertor

# grid 
class grid :
	def __init__(self) :
		self.__cells = [cell(i) for i in range(81)]
		self.__numbers = [number(i+1) for i in range(9)]

	# load(data)载入谜题data
	def load(self, data) :
		self.__init__()
		data = list(data)
		cell_id = 0
		if len(data) == 81 :
			for v in data :
				value = int(v)
				if value != 0 :
					self.setValue(cell_id, value)
				cell_id += 1
		else :
			print "Wrong data : len=", len(data), "!"

	# unit(type,uintid)返回指定组
	def unit(self, type, unit_id) :
		if unit_id >= 0 and unit_id < 9 :
			if type != 2 and type >= 0 and type < 4 :
				return unit(self, type, unit_id)
	# allUnit(g_unit_id)由range(27)返回指定组, 不需要写type参数, 方便遍历
	def allUnit(self, g_unit_id = None) :
		if g_unit_id == None :
			units = []
			for i in range(27) :
				type = i / 9
				if type == 2 :
					type = 3
				unit_id = i % 9
				units.append(unit(self, type, unit_id))
			return units
		else :
			if g_unit_id in range(27) :
				type = g_unit_id / 9
				if type == 2 :
					type = 3
				unit_id = g_unit_id % 9
				return unit(self, type, unit_id)
	# cell()返回所有单元格[81]
	# cell(i)返回指定单元格
	def cell(self, cell_id = None) :
		if cell_id == None :	
			return self.__cells
		else :
			try :
				return self.__cells[cell_id]
			except :
				print "List index out of range!"
	# number(i)返回指定数字, 参数i为1至9(, 实际数组为0至8)。 
	# 为避免不同的编号习惯导致的错误, 不提供返回整个数组的方法。
	def number(self, number) :
		try :
			return self.__numbers[number-1]
		except :
			print "List index out of range!"

	# relationCell(cell_id)返回与单元格相关联的20个单元格
	def relationCell(self, cell_id) :
		row = convertor.id2Row(cell_id)
		column = convertor.id2Column(cell_id)
		box = convertor.id2Box(cell_id)
		relation = [convertor.RC2id(row, i) for i in range(9)]
		relation += [convertor.RC2id(i, column) for i in range(9)]
		relation += [convertor.BA2id(box, i) for i in range(9)]
		relation = list(set(relation))
		relation.remove(cell_id)
		relation.sort()
		return [self.cell(i) for i in relation]
	# cell_id(cells)由对象cells列表获得其id列表, 单个cell也可以用
	def cell_id(self, cells) :
		if isinstance(cells, list) :
			return [i.id() for i in cells]
		elif isinstance(cells, int) :
			return cells.id()

	## 用户进行的所有修改动作都应该从grid类执行
	## ---
	# setValue(cell, value) 为指定单元格确定值
	def setValue(self, cell_id, value) :
		# 为单元格(cell_id)设定值(value)
		self.cell(cell_id)._setValue(value)
		# -----
		for i in range(1,10) : 
			if i != value :
				# 为其余数字(非value)去除该格(cell_id)的可选标记
				self.number(i)._delOpt(cell_id)
				# 为单元格(cell_id)去除其余候选数(非value)
				self.cell(cell_id)._delOpt(i)
		# 为单元格(cell_id)所关联格去除该候选数(value)
		for i in self.relationCell(cell_id) :
			i._delOpt(value)
		# 为该候选数(value)去除单元格(cell_id)所关联格上的可选标记
		for i in self.cell_id(self.relationCell(cell_id)) :
			self.number(value)._delOpt(i)
	# delOpt(cells_id, numbers) 为指定单元格删除候选数, 并同步number的候选位置
	def delOpt(self, cell_id, number) :
		result = []
		if isinstance(cell_id, list) :
			for c_id in cell_id :
				res = self.cell(c_id)._delOpt(number)
				if res :
					result.append(res)
		elif isinstance(cell_id, int) :
			res = self.cell(cell_id)._delOpt(number)
			if res :
				result.append(res)
		if isinstance(number, list) :
			for num in number :
				res = self.number(num)._delOpt(cell_id)
				if res :
					result.append(res)
		elif isinstance(number, int) :
			res = self.number(number)._delOpt(cell_id)
			if res :
				result.append(res)
		if len(result) : 
			return result


	## 输出网格数据
	## ---
	# printGrid()输出总网格
	def printGrid(self) :
		lists = [i.value() for i in self.__cells]
		for i in range(9) :
			if i%3 == 0 :
				print " ----------------------- "
			for j in range(9) :
				if j%3 == 0 :
					print "|",
				v = lists[convertor.RC2id(i, j)]
				if v != 0 :
					print v,
				else :
					print "-",
				if j == 8 :
					print "|",
			print
			if i == 8 :
				print "-------------------------"
		print "-----"
	# printAllOpt()输出显示候选数的总网格
	def printAllOpt(self) :
		for row in range(9) :
			if row % 3 == 0 :
				print "  =========================================================================  "
			else :
				print "  -------------------------------------------------------------------------  "
			for row_in_box in range(3) :
				for column in range(9) :
					if column % 3 == 0 :
						print "||",
					else :
						print "|",
					cell_id = convertor.RC2id(row, column)
					for column_in_box in range(3) :
						opt = row_in_box * 3 + column_in_box + 1
						if opt in self.__cells[cell_id].opt() :
							print opt,
						else :
							print " ",
					if column == 8 :
						print "||",
				print
			if row == 8 :
				print "  =========================================================================  "
	# printCell(cell_id)输出单个单元格的数据
	def printCell(self, cell_id):
		print "cell id :", cell_id
		print "value :", 
		value = self.__cells[cell_id].value()
		if value != 0 :
			print value
		else :
			print "-"
		print "option :"
		opt = 0
		for i in range(3) :
			for j in range(3) :
				opt += 1
				if self.__cells[cell_id].hasOpt(opt) :
					print opt,
				else :
					print " ",
			print
		print "-----"
	# printNumber(number)输出某数字的数据
	def printNumber(self, number) :
		print "number :", number
		print "option :"
		for i in range(9) :
			if i%3 == 0 :
				print " ----------------------- "
			for j in range(9) :
				if j%3 == 0 :
					print "|",
				if 0 != self.__cells[convertor.RC2id(i, j)].value():
					print self.__cells[convertor.RC2id(i, j)].value(),
				elif self.__cells[convertor.RC2id(i, j)].hasOpt(number) :
					print "-",
				else :
					print "X",
				if j == 8 :
					print "|",
			print
			if i == 8 :
				print "-------------------------"
		print "-----"

	# 检查谜题是否已经完成
	def check(self) :
		for i in range(81) :
			if self.cell(i).value() == 0 :
				break
		else :
			return True
		return False

# unittype
UNITTYPE = ('row', 'box', 'atom', 'column')


#unit 
class unit :

	# __init__
	def __init__(self, grid, type, unit_id):
		if unit_id >= 0 and unit_id < 9 :
			self.__unit_id = unit_id
			self.__type = type
			# 初始化组内格子的引用
			if self.__type == 0 :	#row
				self.__cells = [grid.cell(i) for i in range(81) if convertor.id2Row(i)==self.__unit_id]
			elif self.__type == 1 : #box
				self.__cells = [grid.cell(i) for i in range(81) if convertor.id2Box(i)==self.__unit_id]
			elif self.__type == 3 : #column
				self.__cells = [grid.cell(i) for i in range(81) if convertor.id2Column(i)==self.__unit_id]
			else :
				self.__cells = []
				print "UNITTYPE is not defined!"
				del self
		else :
			print "The unit_id is not exist!"
			del self

	# unit_id()返回组号
	def unit_id(self) :
		return self.__unit_id
	# type()返回分组类型的描述
	def type(self) :
		return UNITTYPE[self.__type]
	# __itype()返回分组下类型的id, 如0(r)对应-1(c)
	def __itype(self) :
		return -self.__type-1
	# itype()返回分组下类型的描述
	def itype(self) 	:
		return UNITTYPE[self.__itype()]

	# cell()返回组内所有单元格[9]
	# cell(id_in_unit)返回组内指定单元格
	# id_in_unit为组内的id, 不等于cell类的id属性
	def cell(self, id_in_unit = None) :
		if len(self.__cells)==9 :
			if id_in_unit == None :
				return self.__cells
			else :
				try : 
					return self.__cells[id_in_unit]
				except :
					print "List index out of range!"
		else :
			print "The unit is undefined!"
	# cell_id()返回组内单元格的真实id
	def cell_id(self) :
		return [i.id() for i in self.cell()]
	# hasCell(cell_id)根据cell的id检查指定cell是否在当前unit中, 返回布尔值
	def hasCell(self, cell_id) :
		if cell_id in self.cell_id() :
			return True
		else :
			return False


# cell
class cell:
	def __init__(self, id) :
		self.__id = id
		self.__value = 0
		self.__couldBe = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	# id()返回单元格在grid中的id
	def id(self) :
		return self.__id
	# value()返回单元格的值
	def value(self) :
		return self.__value
	# _setValue(value)设置单元格的值
	def _setValue(self, value):
		if value > 0 and value <=9 :
			self.__value = value

	# opt()返回候选数列表
	def opt(self) :
		return self.__couldBe
	# hasOpt(opt)根据单元格是否含有指定候选数返回布尔值
	def hasOpt(self, opt) :
		if opt in self.__couldBe :
			return True
		else :
			return False
	# len()返回可选候选数个数
	def len(self) :
		return len(self.__couldBe)
	# _delOpt(opt)删除候选数
	# opt可以为列表或单个int数值
	def _delOpt(self, opt) :
		result = []
		if isinstance(opt, list) :
			for i in opt :
				if self.hasOpt(i) :
					self.__couldBe.remove(i)
					result.append([self.__id, i])
		elif isinstance(opt, int) :
			if self.hasOpt(opt) :
				self.__couldBe.remove(opt)
				result.append([self.__id, opt])
		else :
			print "type(opt) should be 'list' or 'int' !"
		if len(result) :
			return result

	# getUnitDict() 返回单元格所属组
	def getUnitDict(self) :
		row = convertor.id2Row(self.__id)
		box = convertor.id2Box(self.__id)
		column = convertor.id2Column(self.__id)
		return {UNITTYPE[0]: row, UNITTYPE[3]: column, UNITTYPE[1]: box}


# number
class number:
	def __init__(self, id) :
		self.__id = id
		self.__couldAt = [i for i in range(81)]
	# id()返回真实代表的数字
	def id(self) :
		return self.__id
	# opt(in_cells)返回候选位置列表
	# in_cells为位置范围, 默认为整grid个
	def opt(self, in_cells = [i for i in range(81)]) :
		opts = (self.__couldAt + in_cells)
		opts = list(set([opt for opt in opts if opts.count(opt)>1]))
		opts.sort()
		return opts
	# hasOpt(in_cell)根据数字是否可以在指定单元格返回布尔值
	def hasOpt(self, in_cell) :
		if in_cell in self.__couldAt :
			return True
		else :
			return False
	# len()返回可选位置个数
	def len(self) :
		return len(self.__couldAt)
	# _delOpt(in_cells)删除指定候选位置
	# opt可以为列表或单个int数值
	def _delOpt(self, in_cells) :
		result = []
		if isinstance(in_cells, list) :
			for i in in_cells :
				if self.hasOpt(i) :
					self.__couldAt.remove(i)
					result.append([i, self.__id])
		elif isinstance(in_cells, int) :
			if self.hasOpt(in_cells) :
				self.__couldAt.remove(in_cells)
				result.append([in_cells, self.__id])
		else :
			print "type(in_cells) should be 'list' or 'int' !"
		if len(result) :
			return result


#try:
# grid = grid()
# unit = grid.unit(3,2)
# units = unit.cell()
# unit.cell(2)._setValue(7)
# for i in unit.cell():
# 	print i.value(),
# print 
# for i in grid.cell():
# 	print i.value(),
# print 
# print grid.cell(0).value()
# print unit.cell(2).opt()
# unit.cell(2)._delOpt([3,4])
# unit.cell(2)._delOpt(10)
# print unit.cell(2).hasOpt(1)
# print unit.hasCell(60)
# grid.number(5)._delOpt(5)
# print grid.number(5).opt(unit.cell_id())
# grid.number(5)._delOpt(29)
# print grid.number(5).opt()
# print grid.number(5).opt(unit.cell_id())
# ral = grid.relationCell(5)
# print grid.cell_id(ral)
# print grid.number(3).opt()
#except:
#	print "catch a error!"