#! /usr/bin/env bash
# create a GGA_PAW POTCAR file
# by bigbor ofcourse
# to use it: potcar.bash element element element element......

# define local potpaw_GGA pseudopotentialrepository:
repo="/home/cnzhang/bin/potpaw_PBE.54"

# check if older version of POTCAR is present:
if [ -f POTCAR ]; then
 mv -v POTCAR old_POTCAR
 echo " ** Warning: old POTCAR file found and renamed to 'old_POTCAR' "
fi

# Main loop -concatenate the appropriatePOTCARs (or archives)
for i in $*
do 
 if test -f $repo/$i/POTCAR ; then
  cat $repo/$i/POTCAR >> POTCAR
 else
 echo " ** Warning : No suitable POTCAR for element '$i' found! Skipped this eleent."
 fi
done
