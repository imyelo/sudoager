#coding=utf-8
# Filename: link.py
from solver import solver


# 强弱链交替寻路
class sLink(solver):
    def __init__(self):
        solver.__init__(self, complexity=9, name="sLink", type="opt", printChart=False)

    def start(self, id):
        self.__milestone = []                 # 栈结构路径
        self.__count = 0
        self.__tryed = []                     # 已尝试删减的结束点列表
        self.__loadStrongLink(id)

    # 进行强链操作
    def __loadStrongLink(self, id):
        if self.__checkMilestone(id):     # 检查路径是否回环
            self.__addMilestone(id)                     # 加入路径
            for i in self.__getStrongLink(id):            # 遍历与指定点的强关系点(强链列表)
                self.__trySubtractive(self.__milestone[0], i)          # 使用指定点尝试删减动作
                self.__loadWeekLink(i)                                # 继续寻路(弱链)
            self.__removeMilestone(id)                     # 撤销路径
        return self

    # 进行弱链操作
    def __loadWeekLink(self, id):
        if self.__checkMilestone(id):     # 检查是否回环
            self.__addMilestone(id)                     # 加入路径
            for i in self.__getWeekLink(id):             # 遍历与指定点的弱关系点(弱链列表)
                self.__loadStrongLink(i)                # 继续寻路(强链)
            self.__removeMilestone(id)                     # 撤销路径
        return self

    # 获取强链列表
    def __getStrongLink(self, id):
        return filter(lambda x: x < 30, [id + 3, id + 5])

    # 获取弱链列表
    def __getWeekLink(self, id):
        return filter(lambda x: x < 30, [id + 2, id + 7])

    # 增加路径点
    def __addMilestone(self, id):
        self.__milestone.append(id)
        return self.__milestone

    # 撤销路径点
    def __removeMilestone(self, id):
        return self.__milestone.pop()

    # 检查是否绕回了已经经过的路径点
    def __checkMilestone(self, id):
        return not id in self.__milestone

    # 两点的组区域是否有重叠部分
    def __isOverlap(self, start, id):
        return True

    # 结束点是否已经尝试过删减
    def __isTryed(self, id):
        return id in self.__tryed

    # 增加尝试点历史记录(结束点)
    def __addTryed(self, id):
        self.__tryed.append(id)
        return self.__tryed

    # 尝试进行删减动作
    def __trySubtractive(self, start, id):
        # 条件:     1. 没有出现在历史路径中 checkMilestone
        #             2. 没有出现在历史检查中 isTryed
        #             3. 两点的组区域有重叠部分 isOverlap
        #             4. 重叠部分含有可消除候选数
        if self.__isOverlap(start, id) and self.__checkMilestone(id) and not self.__isTryed(id):
            print self.__milestone, id
            self.__addTryed(id)
            return True
        return False


test = sLink()
test.start(1)
