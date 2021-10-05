# 需要和read_ConvexHull中（以下简称rC）产生的数据结构联动
def FormationEnCalc(idlist,moleEn,system,atomEn):
    # idlist对应rC中getID()返回的结构ID列表
    # moleEn指分子总焓，对应的是rC中getEnthalpies()返回的总焓列表
    # system指体系的组成向量，对应rC中getTotalEnt()返回的组成向量列表
    # atomEn指的是组成分子前每个原子的基态能量，需要自己手动写个字典传入，比如{Li:-2,C:-9}
    # 形成焓计算公式deltaE(mAnB) = E(mAnB)-m*E(A)-n*E(B)
    FEdict = {} #存放最终的ID-生成焓的对应字典
    for id,comp,en in zip(idlist,system,moleEn):
        # 计算体系中原子种类数和各原子种类对应的原子数目
        FormationEn = en
        complist = comp.split('_') # 按元素切割一下
        #testlist.append(complist)
        totalAtomNumber = 0
        composition = ''  # 用于生成方便输入ASE的组成格式
        for ele in complist:
            element = ''  # 记录元素种类
            number = ''  # 记录原子个数
            for i in ele:
                if i.isalpha():
                    element += i
                else:
                    number += i
            totalAtomNumber += eval(number)
            composition += element+number
            FormationEn -= atomEn[element]*eval(number)  #减去对应原子的基态能量
        FEdict[composition]=FormationEn/totalAtomNumber
    return FEdict

