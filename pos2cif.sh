#! /usr/bin/env

for i in *;do mkdir POS_${i} | mv ${i} POS_${i}/POSCAR;done
for i in E*;do mkdir POS_${i} | mv ${i} POS_${i}/POSCAR;done
for i in POSCAR_*;do mkdir POS_${i} | mv ${i} POS_${i}/POSCAR;done
# 三重保险
# 因为vaspkit只能识别名称为POSCAR的文件，所以有了这一步操作（我假定你把一大堆结构的POSCAR文件放在了同一个文件夹里，如果不是，请注释掉这一步）
for i in *E*;
    do cd ${i};
        (echo 4;echo 413;echo 1) | vaspkit
        cd ${OLDPWD}
    done
# 批量调用VASPKIT的413功能生成cif文件
for i in POS_POSCAR*;
    do cd ${i};
        (echo 4;echo 413;echo 2) | vaspkit
        cd ${OLDPWD}
    done
#for those which we got by ourselves, they are usually contcars,so we use function 4-413-2 here.

mkdir CIFS

for i in *; do mv ${i}/POSCAR.cif ./CIFS/${i}.cif;done 
# 批量提取CIF文件
