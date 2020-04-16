#!/bin/bash

for i in 260 500 1200 2000;
do
  echo $i
  python genAnalyzer.py -i /eos/user/t/twamorka/newCatalog_fixVtx_3Oct2019/hadd_Tree/signal_hh_Grav_${i}.root -o /eos/user/t/twamorka/newCatalog_fixVtx_3Oct2019/hadd_Tree/genOutputTrees/signal_hh_Grav_gen_${i}.root


done
