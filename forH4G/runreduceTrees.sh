#!/bin/bash
python reduceTrees.py -y 2016 -e B
python reduceTrees.py -y 2016 -e C
python reduceTrees.py -y 2016 -e D
python reduceTrees.py -y 2016 -e E
python reduceTrees.py -y 2016 -e F
python reduceTrees.py -y 2016 -e G
python reduceTrees.py -y 2016 -e H

python reduceTrees.py -y 2017 -e B
python reduceTrees.py -y 2017 -e C
python reduceTrees.py -y 2017 -e D
python reduceTrees.py -y 2017 -e E
python reduceTrees.py -y 2017 -e F

python reduceTrees.py -y 2018 -e A
python reduceTrees.py -y 2018 -e B
python reduceTrees.py -y 2018 -e C
python reduceTrees.py -y 2018 -e D
#year='2016 2017 2018'
#for y in ${year};
#do
#  if [["$y" -eq  2016]];then
#  era='B C D E F G H'

#  fi
#  if [$y==2017];then
#  era='B C D E F'
#  fi
#  if [$y==2018];then
#  era='A B C D'
#  fi
#  echo $era
#  for e in era;
#  do
#    echo 
     #python reduceTrees.py -y ${y} -e ${e} #  done
#  done

#done
