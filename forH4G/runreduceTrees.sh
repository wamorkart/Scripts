#!/bin/bash
#for i in 60 55 50 45 40 35 30 25 20 15;
for i in 60;
do
  echo ${i}
  python reduceTrees.py --i /eos/user/t/twamorka/16April2020_Ntuples_OldPairing/Signal/signal_m_${i} 
done
