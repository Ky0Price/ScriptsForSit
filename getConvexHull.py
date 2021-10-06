import os

class read_convexhull:
    # 功能列表；[读取文件extended_convex_hull文件，按要求选取结构，获得结构对应的POSCAR文件，获得结构对应的ID、组成、FIT、总焓（每原子和每分子）]
    def __init__(self, filepath, POSpath, fitreq=0.0000, idlenth=4, datastart=3):
        # 默认第3行开始正式有数据
        # 行数请根据实际文件进行设置
        # 我自己把extended_convex_hull的前几行文字说明都删了
        # 后期建议改一下这里，一个个去文件里面删东西太麻烦
        # 读取ID并格式化
        self.filename = filepath  # 数据文件的目录
        self.pospath = POSpath
        self.fitreq = fitreq  # 获取的fitness的最大值
        self.idlenth = idlenth  # id的最大长度
        self.datastart = datastart  # 数据开始的行数
        self.id = []
        self.compositions = []
        self.enthalpies = []
        self.fitness = []
        self.selected = []
        self.compositions_ini = []
        self.totalEnergy = []

    # def speak(self):
    #    print('')
    # 打印出输入的条件限制，日后再写

    # 读取数据文件
    def readfile(self, ):
        data_ini = []
        for line in open(self.filename, "r"):
            data_ini.append(line)
        return data_ini

    # 读取poscar文件,返回列表
    def readPOSCAR(self):
        pos_ini = []
        for line in open(self.pospath, 'r'):
            pos_ini.append(line)
        return pos_ini

    # 根据fitness大小来筛选所需行
    def selectByFitness(self):
        for line in self.readfile()[self.datastart - 1:]:
            fit = line[51:57]
            if eval(fit) <= self.fitreq:
                self.selected.append(line)
            else:
                break
        return self.selected

    # 取得目标结构的ID，返回列表
    def getID(self):
        for line in self.selected:
            ID = 'EA' + line[0:self.idlenth].strip()  # 加上'EA'后方面后续与POSCAR文件对照与抓取
            self.id.append(ID)
        return self.id

    # 获取ID对应的POSCAR文件,返回字典，键为ID，值为对应的POSCAR，并写入到指定路径（rootpath=）的文件夹中
    def getPOSCARbyID(self,rootpath='.'):
        pos_dict = {}
        l = 0
        strloc = []
        endloc = []
        idlist = []
        idlist_e = []
        structurestart = []
        for ids in self.id:
            idlist.append(ids[2:])
        for i in idlist:
            i = eval(i)+1
            i = str(i)
            idlist_e.append(i)
        for line in self.readPOSCAR():
            start = 0
            end = 0
            for i in line:
                if i == 'E':
                    structurestart.append(l)
                    break
                else:
                    start += 1
            for i in line:
                if i == ' ':
                    break
                else:
                    end += 1
            l += 1
            for i in idlist:
                if line[start+2:end] == i:
                    strloc.append(structurestart[eval(i)-1])
            for i in idlist_e:
                if line[start+2:end] == i:
                    endloc.append(structurestart[eval(i)-1])
        for strat, end, id in zip(strloc, endloc, self.id):
            pos_dict[id] = self.readPOSCAR()[strat:end]
        os.mkdir(rootpath)  # 创建用于保存摘取出的POSCAR文件的文件夹,如果文件夹已存在，需要手动删除
        filepath = rootpath
        pathlist = []
        # 写入POSCAR，每一条结构对应一个文件，文件名格式[ID]+组成
        for comp,id,poscar in zip(self.getCompositions(),pos_dict.keys(),pos_dict.values()):
            filepath = filepath+"["+id+"]"+comp
            with open (filepath,'w') as f:
                for line in poscar:
                    f.write(line)
            pathlist.append(filepath)
            filepath = rootpath
        return pos_dict

    # 取得每个结构的焓，以原子为单位，返回列表
    def getEnthalpies(self):
        for line in self.selected:
            enthalpy = line[24:32] + "(eV/atom)"
            self.enthalpies.append(enthalpy)
        return self.enthalpies

    # 取得每个结构的fitness，返回列表
    def getFitness(self):
        for line in self.selected:
            Fit = line[50:56] + "(ev/block)"
            self.fitness.append(Fit)
        return self.fitness

    # 取得每个结构的组分
    def getCompositions(self):
        for line in self.selected:
            comp_ini = line[7:18].strip().split(' ')
            for i in range(len(comp_ini) - 1, -1, -1):
                if comp_ini[i] == '':
                    comp_ini.remove('')
            self.compositions_ini.append(comp_ini)
            comp_str = 'Li' + comp_ini[0] + '_C' + comp_ini[1] + '_N' + comp_ini[2]  # LiCN特供,其他体系自己搞定
            self.compositions.append(comp_str)
        return self.compositions

    # 计算每个结构的总焓（分子式为单位）,再用这个之前必须运行一次getEnthalpies()
    def getTotalEnt(self):
        for line in self.selected:
            comp_ini = line[7:18].strip().split(' ')
            for i in range(len(comp_ini) - 1, -1, -1):
                if comp_ini[i] == '':
                    comp_ini.remove('')
            self.compositions_ini.append(comp_ini)
        for compini, en in zip(self.compositions_ini, self.enthalpies):
            energy = eval(en[0:6])
            atom_num = 0
            for i in compini:
                atom_num += eval(i)
            # totalenergy = str(atom_num * energy)[0:8] + '(ev/block)'
            totalenergy = atom_num * energy
            self.totalEnergy.append(totalenergy)
        return self.totalEnergy

#使用示例
#传入convexhull文件和对应的poscar文件
data_big = read_convexhull('./extended_convexhull_dir_big/extended_convexhull_LiCN-0GPa',
                           './extended_convexhull_dir_big/gatheredPOSCARS-0GPa')
data_small = read_convexhull('./extended_convexhull_dir_small/extended_convexhull_LiCN-0GPa',
                           './extended_convexhull_dir_small/gatheredPOSCARS-0GPa')

data_big.readPOSCAR() #写入poscar
data_small.readPOSCAR()
data_big.selectByFitness() #筛选结构
data_small.selectByFitness()
data_big.getID() #返回结构对应的ID
data_small.getID()
#print(ids_b)
data_big.getCompositions()
data_small.getCompositions()
sele_poscars_b = data_big.getPOSCARbyID(rootpath='./extended_convexhull_dir_big/poscar_selectedByid_0GPa_big/') #返回对应的poscar字典并写入一个新的文件
sele_poscars_s = data_small.getPOSCARbyID(rootpath='./extended_convexhull_dir_small/poscar_selectedByid_0GPa_small/')
print(sele_poscars_b)
#print(sele_poscars_b)

