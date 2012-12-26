#coding=utf-8
# Filename: sNakePair.py
from solver import solver
import grid


# sNakePair 显性对数法
class sNakePair(solver):

    def __init__(self):
        solver.__init__(self, complexity=3, name="sNakePair", type="opt", printChart=True)

    def solve(self, sudoku):
        cell_with_two_opt = [sudoku.grid().cell(i) for i in range(81) if sudoku.grid().cell(i).len() == 2]
        cell_with_two_opt.sort()
        if len(cell_with_two_opt) > 1:
            for i, cell_A in enumerate(cell_with_two_opt[:-2]):
            # TODO 改进遍历效率
                for cell_B in cell_with_two_opt[i + 1:]:
                    if cell_B.opt() == cell_A.opt():
                        for type in [0, 1, 3]:
                            if cell_A.getUnitDict()[grid.UNITTYPE[type]] == cell_B.getUnitDict()[grid.UNITTYPE[type]]:
                                unit = sudoku.grid().unit(type, cell_A.getUnitDict()[grid.UNITTYPE[type]])
                                otherCellInUnit_id = [cell.id() for cell in unit.cell() if cell != cell_A and cell != cell_B]
                                res = sudoku.grid().delOpt(otherCellInUnit_id, cell_B.opt())
                                if res:
                                    for r in res[0]:
                                        self._matching(r[0], r[1])
        return self
