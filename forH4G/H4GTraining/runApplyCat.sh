#!/bin/bash

mass='60 45 35 25 15'
# mass='60'

year='2016 2017 2018'

bkg='QCD_30to40 QCD_30toInf QCD_40toInf GJet_20to40 GJet_20toInf GJet_40toInf DiPho_40to80 DiPho_80toInf'
training='dataset_PhoMVA_manyKinVars_fullRun2_datamix_old_kinWeight_dataSBScaling_m'

# for m in ${mass};
# do
#   echo ${m}
#   t1='dataset_PhoMVA_manyKinVars_fullRun2_datamix_v10_dataSBScaling_m'
#   for y in ${year};
#   do
#     for b in ${bkg};
#     do
#       echo 'Running on Background MC: ' ${b} ${y}
#       echo python ApplyBDT.py -i /eos/user/t/twamorka/h4g_forPreApp_Nov2020/${y}/hadd/${b}.root  -m ${m} -y ${y}  -W /eos/user/b/bmarzocc/H4G/${t1}${m}/weights/TMVAClassification_BDTG.weights.xml -o /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_19Nov2020/${t1}${m}_17Nov2020_Final/${b}_${m}_${y}.root
#       python ApplyBDT.py -i /eos/user/t/twamorka/h4g_forPreApp_Nov2020/${y}/hadd/${b}.root  -m ${m} -y ${y}  -W /eos/user/b/bmarzocc/H4G/${t1}${m}/weights/TMVAClassification_BDTG.weights.xml -o /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_19Nov2020/${t1}${m}_17Nov2020_Final/${b}_${m}_${y}.root
#     done
#   done
# done
# for m in ${mass};
# do
#   echo ${m}
#   t1='dataset_PhoMVA_manyKinVars_fullRun2_datamix_v10_dataSBScaling_m'
#   for y in ${year};
#   do
#     echo 'Running on Signal'
#     echo python ApplyCatBDT.py -f /eos/user/t/twamorka/h4g_fullRun2/withSystematics/${y}/hadd/signal_m_${m}.root  -m ${m} -y ${y} -t ${t1}${m} -W /eos/user/b/bmarzocc/H4G/${t1}${m}/weights/TMVAClassification_BDTG.weights.xml -O /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_19Nov2020/${t1}${m}_17Nov2020_Final/signal_m_${m}_${y}_wSyst.root
#     python ApplyCatBDT.py -f /eos/user/t/twamorka/h4g_fullRun2/withSystematics/${y}/hadd/signal_m_${m}.root  -m ${m} -y ${y} -t ${t1}${m} -W /eos/user/b/bmarzocc/H4G/${t1}${m}/weights/TMVAClassification_BDTG.weights.xml -O /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_19Nov2020/${t1}${m}_17Nov2020_Final/signal_m_${m}_${y}_wSyst.root
#
#   done
# done
# training_type='Standard'
# training='dataset_PhoMVA_KinVars_fullRun2_datamix_phoMVA_dataSBScaling_m15_v3'
# training='dataset_PhoMVA_manyKinVars_fullRun2_datamix_v10_dataSBScaling_m'
# training='dataset_PhoMVA_KinVars_final_fullRun2_datamix_v10_dataSBScaling'
# training='dataset_PhoMVA_KinVars_final_fullRun2_datamix_v11_dataSBScaling_addCuts_v2
#training='dataset_PhoMVA_fullRun2_datamix_v10_dataSBScaling_EVEN'
# training='dataset_PhoMVA_KinVars_fullRun2_datamix_v4_dataSBScaling_v2'
# training='dataset_PhoMVA_KinVars_fullRun2_datamix_v8_dataSBScaling_addCuts dataset_PhoMVA_KinVars_fullRun2_datamix_v8_lumiScaling_addCuts'
# training='dataset_PhoMVA_KinVars_fullRun2_datamix_v8_dataSBScaling_addCuts_v2 dataset_PhoMVA_KinVars_fullRun2_datamix_v8_dataSBScaling_signalToo_addCuts_v2 dataset_PhoMVA_KinVars_fullRun2_datamix_v8_dataSBScaling_v2 dataset_PhoMVA_KinVars_fullRun2_datamix_v8_lumiScaling_addCuts_v2 dataset_PhoMVA_KinVars_fullRun2_datamix_v8_lumiScaling_v2'
# training='CatTrain_GenMass_AllMasses'
# trainingyear='Run2'
# dirName='CatTrain_Standard_M45_on_M60_PerYear'
# outDir='/eos/user/t/twamorka/h4g_fullRun2/withSystematics/'
# Bkg='QCD_30to40 QCD_30toInf QCD_40toInf GJet_20to40 GJet_20toInf GJet_40toInf DiPho_40to80 DiPho_80toInf'

#whichEvents='odd'
# for t1 in $training;
# do
#      mkdir /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/${t1}_DFReweighting_18Nov2020/
#      # for y in $year;
#      # do
#        for m in $mass;
#        do
#          echo 'Running on data mix'
#          echo python ApplyCatBDT.py -f /eos/user/t/twamorka/h4g_fullRun2/withSystematics/data_mix_weight_FullRun2_dataFrame.root -gm ${m}  -t ${t1} -W /eos/user/b/bmarzocc/H4G/${t1}/weights/TMVAClassification_BDTG.weights.xml -O /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/${t1}_DFReweighting_18Nov2020/data_mix_${m}_Run2.root
#          python ApplyCatBDT.py -f /eos/user/t/twamorka/h4g_fullRun2/withSystematics/data_mix_weight_FullRun2_dataFrame.root -gm ${m}  -t ${t1} -W /eos/user/b/bmarzocc/H4G/${t1}/weights/TMVAClassification_BDTG.weights.xml -O /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/${t1}_DFReweighting_18Nov2020/data_mix_${m}_Run2.root
#
#          # echo 'Running on '
#          # echo 'Running on data mix'
#          # echo python ApplyCatBDT.py -f /eos/user/t/twamorka/h4g_fullRun2/withSystematics/${y}/hadd/data_mix_weight_v10.root -gm ${m} -y ${y} -t ${t1} -W /eos/user/b/bmarzocc/H4G/${t1}/weights/TMVAClassification_BDTG.weights.xml -O /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/${t1}_17Nov2020_Final/data_mix_${m}_${y}.root
#          # python ApplyCatBDT.py -f /eos/user/t/twamorka/h4g_fullRun2/withSystematics/${y}/hadd/data_mix_weight_v10.root -gm ${m} -y ${y} -t ${t1} -W /eos/user/b/bmarzocc/H4G/${t1}/weights/TMVAClassification_BDTG.weights.xml -O /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/${t1}_17Nov2020_Final/data_mix_${m}_${y}.root
#
#          # echo 'Running on data'
#          # echo python ApplyCatBDT.py -f /eos/user/t/twamorka/h4g_fullRun2/withSystematics/${y}/hadd/data_${y}.root -gm ${m} -y ${y} -t ${t1} -W /eos/user/b/bmarzocc/H4G/${t1}/weights/TMVAClassification_BDTG.weights.xml -O /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/${t1}_17Nov2020_Final/data_${m}_${y}.root
#          # python ApplyCatBDT.py -f /eos/user/t/twamorka/h4g_fullRun2/withSystematics/${y}/hadd/data_${y}.root -gm ${m} -y ${y} -t ${t1} -W /eos/user/b/bmarzocc/H4G/${t1}/weights/TMVAClassification_BDTG.weights.xml -O /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/${t1}_17Nov2020_Final/data_${m}_${y}.root
#          #
#          # echo 'Running on Signal'
#          # echo python ApplyCatBDT.py -f /eos/user/t/twamorka/h4g_fullRun2/withSystematics/${y}/hadd/signal_m_${m}.root -gm ${m} -m ${m} -y ${y} -t ${t1} -W /eos/user/b/bmarzocc/H4G/${t1}/weights/TMVAClassification_BDTG.weights.xml -O /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/${t1}_17Nov2020_Final/signal_m_${m}_${y}.root
#          # python ApplyCatBDT.py -f /eos/user/t/twamorka/h4g_fullRun2/withSystematics/${y}/hadd/signal_m_${m}.root -gm ${m} -m ${m} -y ${y} -t ${t1} -W /eos/user/b/bmarzocc/H4G/${t1}/weights/TMVAClassification_BDTG.weights.xml -O /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/${t1}_17Nov2020_Final/signal_m_${m}_${y}.root
#
#        done
#      # done
# done
for m in $mass;
do

     for t1 in $training;

     do
       mkdir /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_9Dec2020/${t1}${m}/
       for y in $year;


       do


         echo 'Running on data mix'
         echo python ApplyCatBDT.py -f /eos/user/t/twamorka/h4g_fullRun2/withSystematics/${y}/hadd/data_mix_${y}_kinWeight.root  -y ${y} -t ${t1}${m} -W /eos/user/b/bmarzocc/H4G/${t1}${m}/weights/TMVAClassification_BDTG.weights.xml -O /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_9Dec2020/${t1}${m}/data_mix_${y}_kinWeight.root
         python ApplyCatBDT.py -f /eos/user/t/twamorka/h4g_fullRun2/withSystematics/${y}/hadd/data_mix_${y}_kinWeight.root  -y ${y} -t ${t1}${m} -W /eos/user/b/bmarzocc/H4G/${t1}${m}/weights/TMVAClassification_BDTG.weights.xml -O /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_9Dec2020/${t1}${m}/data_mix_${y}_kinWeight.root

         echo 'Running on data'
         echo python ApplyCatBDT.py -f /eos/user/t/twamorka/h4g_fullRun2/withSystematics/${y}/hadd/data_${y}.root  -y ${y} -t ${t1}${m} -W /eos/user/b/bmarzocc/H4G/${t1}${m}/weights/TMVAClassification_BDTG.weights.xml -O /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_9Dec2020/${t1}${m}/data_${m}_${y}.root
         python ApplyCatBDT.py -f /eos/user/t/twamorka/h4g_fullRun2/withSystematics/${y}/hadd/data_${y}.root  -y ${y} -t ${t1}${m} -W /eos/user/b/bmarzocc/H4G/${t1}${m}/weights/TMVAClassification_BDTG.weights.xml -O /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_9Dec2020/${t1}${m}/data_${m}_${y}.root

         echo 'Running on Signal'
         echo python ApplyCatBDT.py -f /eos/user/t/twamorka/h4g_fullRun2/withSystematics/${y}/hadd/signal_m_${m}.root  -m ${m} -y ${y} -t ${t1}${m} -W /eos/user/b/bmarzocc/H4G/${t1}${m}/weights/TMVAClassification_BDTG.weights.xml -O /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_9Dec2020/${t1}${m}/signal_m_${m}_${y}.root
         python ApplyCatBDT.py -f /eos/user/t/twamorka/h4g_fullRun2/withSystematics/${y}/hadd/signal_m_${m}.root  -m ${m} -y ${y} -t ${t1}${m} -W /eos/user/b/bmarzocc/H4G/${t1}${m}/weights/TMVAClassification_BDTG.weights.xml -O /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_9Dec2020/${t1}${m}/signal_m_${m}_${y}.root

       done
     done
done


# for y in ${year};
# do
#   for b in ${Bkg};
#   do
#     echo 'Running on ' ${b}
#     echo python ApplyBDT.py -i /eos/user/t/twamorka/h4g_forPreApp_Nov2020/${y}/hadd/${b}.root -y ${y} -m ${mass} -s 0 -W /afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_6_8/src/flashgg/Scripts/Training/dataset/weights/TMVAClassification_BDTG.weights.xml -o /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/PerMass_FullRun2_DataMix_v8_SignalDataMix_NormalizedToDataSideband/${b}_${mass}_${y}.root
#     python ApplyBDT.py -i /eos/user/t/twamorka/h4g_forPreApp_Nov2020/${y}/hadd/${b}.root -y ${y} -m ${mass} -s 0 -W /afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_6_8/src/flashgg/Scripts/Training/dataset/weights/TMVAClassification_BDTG.weights.xml -o /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/PerMass_FullRun2_DataMix_v8_SignalDataMix_NormalizedToDataSideband/${b}_${mass}_${y}.root
#   done
# done
