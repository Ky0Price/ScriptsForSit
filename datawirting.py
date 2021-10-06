def datawirting_exe(datapath,idlist=None,compAndFElist=None,pressure=0,spacegrouplist=None,Enthalpylist=None):
    # 整理数据用
    # datapath写入你希望保存文件的目录
    # idlist传入结构的id，如EA123或者mp-1234
    # compAndFEdict传入最后的ref（refs，refs），他包含了结构和对应的分子形成焓
    # spacegrouplist是用其他库生成的,暂时先不整
    # pressure默认0Gpa
    # enthalpylist传入分子的总焓
    import csv
    with open(datapath,'w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        # 标题行
        head = ['id',
                'compsition',
                'pressure(GPa)',
                'enthalpy    (ev/atom)',
                'formation enthalpy    (ev/atom)']
        writer.writerow(head)
        for id,compAndFE,enthalpy in zip(idlist,compAndFElist,Enthalpylist):
            comp = compAndFE[0]
            FE = compAndFE[1]
            pressure = pressure
            row = [id]+[comp]+[pressure]+[enthalpy]+[FE]
            writer.writerow(row)