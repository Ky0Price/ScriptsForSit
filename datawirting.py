def datawirting_exe(datapath,comp_FE_id_list=[],pressure=0,spacegrouplist=[],Enthalpylist=[]):
    # 整理数据用
    # datapath写入你希望保存文件的位置
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
                'spacegroup',
                'pressure(GPa)',
                'enthalpy    (ev/atom)',
                'formation enthalpy    (ev/atom)']
        writer.writerow(head)
        for comp_FE_id,enthalpy in zip(comp_FE_id_list,Enthalpylist):
            comp = comp_FE_id['composition']
            FE = comp_FE_id['FE']
            id = comp_FE_id['id']
            #print(id)
            pressure = '0'
            sg = 0
            for sgdict in spacegrouplist:
                if sgdict['id'] == id:
                    #print(sgdict['number'])
                    sg += sgdict['number']
            #print(sg)
            row = [id]+[comp]+[sg]+[pressure]+[enthalpy]+[FE]
            writer.writerow(row)