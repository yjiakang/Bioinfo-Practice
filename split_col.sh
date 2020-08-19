#!bin/bash
help(){
cat <<- EOF
'''Split a file by column per file
   author jkyin
   2019-9-14
[usage]:[col_per_file] [file]'''
EOF
exit 0
}
while [ -n "$1" ];do
case $1 in
-h) help;;
esac
done

col_per=$1
file=$2
ncol=$(head -n 1 $file | awk "{print NF}")
for((i=0;i*col_per<ncol;i++))
do
awk -v c=$i -v n=$col_per '{{printf $1"\t"}for(j=c*n+2;j<(c+1)*n+2;j++){printf $j"\t"}{print ""}}' $file > split_col_${i}
done

