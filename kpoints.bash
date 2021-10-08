#! /usr/bin/env bash

#to generate KPOINTS file
#written by bigbro XD
#to use it:kpoints.sh number1 number2 number3

echo K-POINTS > KPOINTS  # just a name,nothing special,but the first line should be occupied
echo 0 >> KPOINTS # 0 stands for auto-generating kpoints
echo Gamma-Centered >> KPOINTS  #Gamma centered MP grids,mostly used
echo $1 $2 $3 >> KPOINTS #subdivision for number1,n2,n3
echo 0 0 0 >> KPOINTS #optional shift of the mesh
