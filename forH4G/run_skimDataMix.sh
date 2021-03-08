#!/bin/bash
outDir=/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_22Jan2021/19Feb2021/H4G_PhoMVA_manyKinVars_aMass_fullRun2_DataMix_HighStat_kinWeight_dataSBScaling_MGPodd_bkgOdd_noCorrel/60/DataMix_Skim/
# for e in 0 1000 2000 3000 4000 5000 6000 7000 8000 9000 10000 12000 13000 14000 16000 17000 18000 19000 20000 30000 40000 60000 70000 90000 80000;
# do
#   for y in 2016 2017 2018;
#   do
#     echo python skimDataMix.py  -y ${y} -e ${e}
#     python skimDataMix.py  -y ${y} -e ${e}
#   done
#   echo ${outDir}hadd data_mix_run2_${e}.root  ${outDir}data_mix_2016_${e}.root ${outDir}data_mix_2017_${e}.root ${outDir}data_mix_2018_${e}.root
#   hadd ${outDir}data_mix_run2_${e}.root  ${outDir}data_mix_2016_${e}.root ${outDir}data_mix_2017_${e}.root ${outDir}data_mix_2018_${e}.root
# done
#


for num in {1..100};
do
    echo $num
    e=$(($num*20000))
    for y in 2016 2017 2018;
    do
      echo python skimDataMix.py  -y ${y} -e ${e}
      python skimDataMix.py  -y ${y} -e ${e}
    done
    echo ${outDir}hadd data_mix_run2_${e}.root  ${outDir}data_mix_2016_${e}.root ${outDir}data_mix_2017_${e}.root ${outDir}data_mix_2018_${e}.root
    hadd ${outDir}data_mix_run2_${e}.root  ${outDir}data_mix_2016_${e}.root ${outDir}data_mix_2017_${e}.root ${outDir}data_mix_2018_${e}.root

done
