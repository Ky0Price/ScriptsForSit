# 需要和read_ConvexHull中（以下简称rC）产生的数据结构联动
def FormationEnCalc(idlist,system,moleEn,atomEn,op):
    # idlist对应rC中getID()返回的结构ID列表,没发现有什么用，但是删掉会出问题，就给他留着吧
    # moleEn指分子总焓，对应的是rC中getEnthalpies()返回的总焓列表
    # system指体系的组成向量，对应rC中getTotalEnt()返回的组成向量列表
    # atomEn指的是组成分子前每个原子的基态能量，需要自己手动写个字典传入，比如{Li:-2,C:-9}
    # 形成焓计算公式deltaE(mAnB) = E(mAnB)-m*E(A)-n*E(B)
    FElist=[] #存放最终的ID-生成焓的对应字典的列表
    for id,comp,en in zip(idlist,system,moleEn):
        # 计算体系中原子种类数和各原子种类对应的原子数目
        FEdict = {}
        FormationEn = en
        complist = comp.split('_') # 按元素切割一下
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
            FormationEn -= atomEn[element]*eval(number) # 减去对应原子的基态能量
        #print(composition)
        if op==1:
            FEdict['composition']=composition # ASE要求输入的是分子总生成焓，如果想要得到分子中每原子的平均生成焓，请把这一项改为“FEdict[composition]=FormationEn/totalAtomNumber”
            FEdict['FE']=FormationEn
            FEdict['id']=id
            #print(FEdict)
        else:
            FEdict['composition'] = composition
            FEdict['FE'] = FormationEn/totalAtomNumber
            FEdict['id'] = id
        FElist.append(FEdict)
    return FElist

def FE2refs(FElist):
    refs=[]
    for entry in FElist:
        ref=(entry['composition'],entry['FE'])
        refs.append(ref)
    return refs

