for i in *; do echo -e $i "\t" $(grep '  without' $i/OUTCAR | tail -n 1| awk '{print $7}');  done > data
# \t 为分隔符，表示一个tab,也可以设为逗号，方便以csv格式读取
