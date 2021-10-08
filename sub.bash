for i in *; do cd $i; qsub mysub; cd $OLDPWD; done
# mysub为自己的提交脚本名字
# 使用该脚本需要在对应的上级文件夹

