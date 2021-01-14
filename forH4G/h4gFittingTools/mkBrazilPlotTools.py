mass = [15,20,25,30,40,45,50,55,60]
# mass = [15,25,45,60]
mode = 'LimitOverSM'

outDir = '/eos/user/t/twamorka/www/Training_forPreApp_HighStat_oldfggfinalfit/'
outName = 'Limit_WithVtxSplit_OverSM'

inDir = '/afs/cern.ch/work/t/twamorka/fggfinalfit_h4g_run2/CMSSW_10_2_13/src/flashggFinalFit/Datacard/'
inDir_denom = '/afs/cern.ch/work/t/twamorka/fggfinalfit_h4g_run2/CMSSW_10_2_13/src/flashggFinalFit/Datacard/'
tag_1 = 'higgsCombine_HighStat_withsyst_wTheorySyst_noQCDSyst_M'
tag_2 = ''
# tag_2 = '_ManyKinVars_aMassCuts_1CatOnly_18Dec2020_wSyst'
tag_1_num = 'higgsCombine_HighStat_NoVtxSplit_withsyst_wTheorySyst_noQCDSyst_M'
tag_2_num = ''
# tag_1_denom = 'higgsCombineDataMix_Old_KinWeight_M'
# tag_2_denom = '_ManyKinVars_aMass_1CatOnly_29Dec2020_wSyst'
tag_1_denom = 'higgsCombine_HighStat_withsyst_wTheorySyst_noQCDSyst_M'
tag_2_denom = ''

sample = []
sample_num = []
sample_denom = []
for m in mass:
    sample.append([inDir+tag_1+str(m)+tag_2+'.AsymptoticLimits.mH125.root',m])
    sample_num.append([inDir+tag_1_num+str(m)+tag_2_num+'.AsymptoticLimits.mH125.root',m])
    sample_denom.append([inDir_denom+tag_1_denom+str(m)+tag_2_denom+'.AsymptoticLimits.mH125.root',m])
# print sample_num
# print sample_denom
# FullRun2_DataMix_Old_KinWeight_ManyKinVars_aMass_1CatOnly_15Dec2020_wSyst = []
# for m in mass:
#     FullRun2_DataMix_Old_KinWeight_ManyKinVars_aMass_1CatOnly_15Dec2020_wSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineDataMix_Old_KinWeight_M'+str(m)+'_ManyKinVars_aMass_1CatOnly_15Dec2020_wSyst.AsymptoticLimits.mH125.root',m])
#
# FullRun2_DataMix_Old_KinWeight_ManyKinVars_1CatOnly_12Dec2020_wSyst = []
# for m in mass:
#     FullRun2_DataMix_Old_KinWeight_ManyKinVars_1CatOnly_12Dec2020_wSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineDataMix_Old_KinWeight_M'+str(m)+'_ManyKinVars_1CatOnly_12Dec2020_wSyst.AsymptoticLimits.mH125.root',m])
# CutBased_MVACuts_12Dec2020_wSyst = []
# for m in mass:
#     CutBased_MVACuts_12Dec2020_wSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineCutBased_MVACuts_M'+str(m)+'_12Dec2020_wSyst.AsymptoticLimits.mH125.root',m])
#
# FullRun2_DataMix_Old_KinWeight_ManyKinVars_5Cats_10Dec2020_wSyst = []
# FullRun2_DataMix_Old_KinWeight_ManyKinVars_5Cats_10Dec2020_wSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineDataMix_Old_KinWeight_M15_ManyKinVars_5Cats_10Dec2020_wSyst.AsymptoticLimits.mH125.root',15])
# FullRun2_DataMix_Old_KinWeight_ManyKinVars_5Cats_10Dec2020_wSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineDataMix_Old_KinWeight_M25_ManyKinVars_5Cats_10Dec2020_wSyst.AsymptoticLimits.mH125.root',25])
# FullRun2_DataMix_Old_KinWeight_ManyKinVars_5Cats_10Dec2020_wSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineDataMix_Old_KinWeight_M35_ManyKinVars_5Cats_10Dec2020_wSyst.AsymptoticLimits.mH125.root',35])
# FullRun2_DataMix_Old_KinWeight_ManyKinVars_5Cats_10Dec2020_wSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineDataMix_Old_KinWeight_M45_ManyKinVars_5Cats_10Dec2020_wSyst.AsymptoticLimits.mH125.root',45])
# FullRun2_DataMix_Old_KinWeight_ManyKinVars_5Cats_10Dec2020_wSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineDataMix_Old_KinWeight_M60_ManyKinVars_5Cats_10Dec2020_wSyst.AsymptoticLimits.mH125.root',60])
#
# FullRun2_DataMix_Old_KinWeight_ManyKinVars_5Cats_10Dec2020_noSyst = []
# FullRun2_DataMix_Old_KinWeight_ManyKinVars_5Cats_10Dec2020_noSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineDataMix_Old_KinWeight_M15_ManyKinVars_5Cats_10Dec2020_noSyst.AsymptoticLimits.mH125.root',15])
# FullRun2_DataMix_Old_KinWeight_ManyKinVars_5Cats_10Dec2020_noSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineDataMix_Old_KinWeight_M25_ManyKinVars_5Cats_10Dec2020_noSyst.AsymptoticLimits.mH125.root',25])
# FullRun2_DataMix_Old_KinWeight_ManyKinVars_5Cats_10Dec2020_noSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineDataMix_Old_KinWeight_M35_ManyKinVars_5Cats_10Dec2020_noSyst.AsymptoticLimits.mH125.root',35])
# FullRun2_DataMix_Old_KinWeight_ManyKinVars_5Cats_10Dec2020_noSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineDataMix_Old_KinWeight_M45_ManyKinVars_5Cats_10Dec2020_noSyst.AsymptoticLimits.mH125.root',45])
# FullRun2_DataMix_Old_KinWeight_ManyKinVars_5Cats_10Dec2020_noSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineDataMix_Old_KinWeight_M60_ManyKinVars_5Cats_10Dec2020_noSyst.AsymptoticLimits.mH125.root',60])
#
# FullRun2_DataMixv10_KinVars_ReWeighted_21Nov2020_wSyst = []
# FullRun2_DataMixv10_KinVars_ReWeighted_21Nov2020_wSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineM15_FullRun2_DataMixv10_KinVarsReweighted_21Nov2020_wSyst.AsymptoticLimits.mH125.root',15])
# FullRun2_DataMixv10_KinVars_ReWeighted_21Nov2020_wSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineM25_FullRun2_DataMixv10_KinVarsReweighted_21Nov2020_wSyst.AsymptoticLimits.mH125.root',25])
# FullRun2_DataMixv10_KinVars_ReWeighted_21Nov2020_wSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineM35_FullRun2_DataMixv10_KinVarsReweighted_21Nov2020_wSyst.AsymptoticLimits.mH125.root',35])
# FullRun2_DataMixv10_KinVars_ReWeighted_21Nov2020_wSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineM45_FullRun2_DataMixv10_KinVarsReweighted_21Nov2020_wSyst.AsymptoticLimits.mH125.root',45])
# FullRun2_DataMixv10_KinVars_ReWeighted_21Nov2020_wSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineM60_FullRun2_DataMixv10_KinVarsReweighted_21Nov2020_wSyst.AsymptoticLimits.mH125.root',60])
#
# FullRun2_DataMixv10_KinVars_ReWeighted_21Nov2020_noSyst = []
# FullRun2_DataMixv10_KinVars_ReWeighted_21Nov2020_noSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineM15_FullRun2_DataMixv10_KinVarsReweighted_21Nov2020.AsymptoticLimits.mH125.root',15])
# FullRun2_DataMixv10_KinVars_ReWeighted_21Nov2020_noSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineM25_FullRun2_DataMixv10_KinVarsReweighted_21Nov2020.AsymptoticLimits.mH125.root',25])
# FullRun2_DataMixv10_KinVars_ReWeighted_21Nov2020_noSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineM35_FullRun2_DataMixv10_KinVarsReweighted_21Nov2020.AsymptoticLimits.mH125.root',35])
# FullRun2_DataMixv10_KinVars_ReWeighted_21Nov2020_noSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineM45_FullRun2_DataMixv10_KinVarsReweighted_21Nov2020.AsymptoticLimits.mH125.root',45])
# FullRun2_DataMixv10_KinVars_ReWeighted_21Nov2020_noSyst.append(['/eos/user/t/twamorka/H4G_Limits/higgsCombineM60_FullRun2_DataMixv10_KinVarsReweighted_21Nov2020.AsymptoticLimits.mH125.root',60])
#
# Training_CombinedMasses_GenInfor_PerYear_FullRun2_26_09_2020 = []
# Training_CombinedMasses_GenInfor_PerYear_FullRun2_26_09_2020.append(['/eos/user/t/twamorka/H4G_Limits/Training_CombinedMasses_GenInfor_PerYear_FullRun2_26_09_2020/higgsCombineTraining_CombinedMasses_GenInfor_PerYear_m15_FullRun2.AsymptoticLimits.mH125.root',15])
# Training_CombinedMasses_GenInfor_PerYear_FullRun2_26_09_2020.append(['/eos/user/t/twamorka/H4G_Limits/Training_CombinedMasses_GenInfor_PerYear_FullRun2_26_09_2020/higgsCombineTraining_CombinedMasses_GenInfor_PerYear_m25_FullRun2.AsymptoticLimits.mH125.root',25])
# Training_CombinedMasses_GenInfor_PerYear_FullRun2_26_09_2020.append(['/eos/user/t/twamorka/H4G_Limits/Training_CombinedMasses_GenInfor_PerYear_FullRun2_26_09_2020/higgsCombineTraining_CombinedMasses_GenInfor_PerYear_m35_FullRun2.AsymptoticLimits.mH125.root',35])
# Training_CombinedMasses_GenInfor_PerYear_FullRun2_26_09_2020.append(['/eos/user/t/twamorka/H4G_Limits/Training_CombinedMasses_GenInfor_PerYear_FullRun2_26_09_2020/higgsCombineTraining_CombinedMasses_GenInfor_PerYear_m45_FullRun2.AsymptoticLimits.mH125.root',45])
# Training_CombinedMasses_GenInfor_PerYear_FullRun2_26_09_2020.append(['/eos/user/t/twamorka/H4G_Limits/Training_CombinedMasses_GenInfor_PerYear_FullRun2_26_09_2020/higgsCombineTraining_CombinedMasses_GenInfor_PerYear_m60_FullRun2.AsymptoticLimits.mH125.root',60])
#
# Training_CombinedMasses_PerYear_FullRun2_26_09_2020 = []
# Training_CombinedMasses_PerYear_FullRun2_26_09_2020.append(['/eos/user/t/twamorka/H4G_Limits/Training_CombinedMasses_PerYear_FullRun2_26_09_2020/higgsCombineTraining_CombinedMasses_PerYear_m15_FullRun2.AsymptoticLimits.mH125.root',15])
# Training_CombinedMasses_PerYear_FullRun2_26_09_2020.append(['/eos/user/t/twamorka/H4G_Limits/Training_CombinedMasses_PerYear_FullRun2_26_09_2020/higgsCombineTraining_CombinedMasses_PerYear_m25_FullRun2.AsymptoticLimits.mH125.root',25])
# Training_CombinedMasses_PerYear_FullRun2_26_09_2020.append(['/eos/user/t/twamorka/H4G_Limits/Training_CombinedMasses_PerYear_FullRun2_26_09_2020/higgsCombineTraining_CombinedMasses_PerYear_m35_FullRun2.AsymptoticLimits.mH125.root',35])
# Training_CombinedMasses_PerYear_FullRun2_26_09_2020.append(['/eos/user/t/twamorka/H4G_Limits/Training_CombinedMasses_PerYear_FullRun2_26_09_2020/higgsCombineTraining_CombinedMasses_PerYear_m45_FullRun2.AsymptoticLimits.mH125.root',45])
# Training_CombinedMasses_PerYear_FullRun2_26_09_2020.append(['/eos/user/t/twamorka/H4G_Limits/Training_CombinedMasses_PerYear_FullRun2_26_09_2020/higgsCombineTraining_CombinedMasses_PerYear_m60_FullRun2.AsymptoticLimits.mH125.root',60])
#
# Training_CombinedMasses_PerYear_FullRun2_25_09_2020 = []
# Training_CombinedMasses_PerYear_FullRun2_25_09_2020.append(['/eos/user/t/twamorka/H4G_Limits/Training_CombinedMasses_PerYear_FullRun2_25_09_2020/higgsCombineTraining_CombinedMasses_PerYear_m15_FullRun2.AsymptoticLimits.mH125.root',15])
# Training_CombinedMasses_PerYear_FullRun2_25_09_2020.append(['/eos/user/t/twamorka/H4G_Limits/Training_CombinedMasses_PerYear_FullRun2_25_09_2020/higgsCombineTraining_CombinedMasses_PerYear_m25_FullRun2.AsymptoticLimits.mH125.root',25])
# Training_CombinedMasses_PerYear_FullRun2_25_09_2020.append(['/eos/user/t/twamorka/H4G_Limits/Training_CombinedMasses_PerYear_FullRun2_25_09_2020/higgsCombineTraining_CombinedMasses_PerYear_m35_FullRun2.AsymptoticLimits.mH125.root',35])
# Training_CombinedMasses_PerYear_FullRun2_25_09_2020.append(['/eos/user/t/twamorka/H4G_Limits/Training_CombinedMasses_PerYear_FullRun2_25_09_2020/higgsCombineTraining_CombinedMasses_PerYear_m45_FullRun2.AsymptoticLimits.mH125.root',45])
# Training_CombinedMasses_PerYear_FullRun2_25_09_2020.append(['/eos/user/t/twamorka/H4G_Limits/Training_CombinedMasses_PerYear_FullRun2_25_09_2020/higgsCombineTraining_CombinedMasses_PerYear_m60_FullRun2.AsymptoticLimits.mH125.root',60])
#
#
# masses_FullRun2_bdtVar = []
# masses_FullRun2_bdtVar.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_Run2_minEvents8_5_bdt.AsymptoticLimits.mH125.root',15])
# masses_FullRun2_bdtVar.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_Run2_minEvents8_5_bdt.AsymptoticLimits.mH125.root',25])
# masses_FullRun2_bdtVar.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_Run2_minEvents8_5_bdt.AsymptoticLimits.mH125.root',35])
# masses_FullRun2_bdtVar.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_Run2_minEvents8_5_bdt.AsymptoticLimits.mH125.root',45])
# masses_FullRun2_bdtVar.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_Run2_minEvents8_5_bdt.AsymptoticLimits.mH125.root',60])
#
# masses_FullRun2_bdtVar_wSyst = []
# masses_FullRun2_bdtVar_wSyst.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombine15.AsymptoticLimits.mH125.root',15])
# masses_FullRun2_bdtVar_wSyst.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombine25.AsymptoticLimits.mH125.root',25])
# masses_FullRun2_bdtVar_wSyst.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombine35.AsymptoticLimits.mH125.root',35])
# masses_FullRun2_bdtVar_wSyst.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombine45.AsymptoticLimits.mH125.root',45])
# masses_FullRun2_bdtVar_wSyst.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombine60.AsymptoticLimits.mH125.root',60])
#
# masses_FullRun2_bdtVar_noSyst = []
# masses_FullRun2_bdtVar_noSyst.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombine15_noSyst.AsymptoticLimits.mH125.root',15])
# masses_FullRun2_bdtVar_noSyst.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombine25_noSyst.AsymptoticLimits.mH125.root',25])
# masses_FullRun2_bdtVar_noSyst.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombine35_noSyst.AsymptoticLimits.mH125.root',35])
# masses_FullRun2_bdtVar_noSyst.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombine45_noSyst.AsymptoticLimits.mH125.root',45])
# masses_FullRun2_bdtVar_noSyst.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombine60_noSyst.AsymptoticLimits.mH125.root',60])
#
#
# # masses_FullRun2 = []
# # masses_FullRun2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_Run2_all_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',15])
# # masses_FullRun2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_Run2_all_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',25])
# # masses_FullRun2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_Run2_all_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',35])
# # masses_FullRun2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_Run2_all_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',45])
# # masses_FullRun2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_Run2_all_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',60])
#
# masses_FullRun2_CombinedMassTraining = []
# masses_FullRun2_CombinedMassTraining.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_Run2_m15.AsymptoticLimits.mH125.root',15])
# masses_FullRun2_CombinedMassTraining.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_Run2_m25.AsymptoticLimits.mH125.root',25])
# masses_FullRun2_CombinedMassTraining.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_Run2_m35.AsymptoticLimits.mH125.root',35])
# masses_FullRun2_CombinedMassTraining.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_Run2_m45.AsymptoticLimits.mH125.root',45])
# masses_FullRun2_CombinedMassTraining.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_Run2_m60.AsymptoticLimits.mH125.root',60])
#
# # masses_FullRun2_CombinedTraining_2016 = []
# # masses_FullRun2_CombinedTraining_2016.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_Run2_2016_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',15])
# # masses_FullRun2_CombinedTraining_2016.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_Run2_2016_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',25])
# # masses_FullRun2_CombinedTraining_2016.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_Run2_2016_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',35])
# # masses_FullRun2_CombinedTraining_2016.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_Run2_2016_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',45])
# # masses_FullRun2_CombinedTraining_2016.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_Run2_2016_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',60])
# #
# # masses_FullRun2_CombinedTraining_2017 = []
# # masses_FullRun2_CombinedTraining_2017.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_Run2_2017_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',15])
# # masses_FullRun2_CombinedTraining_2017.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_Run2_2017_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',25])
# # masses_FullRun2_CombinedTraining_2017.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_Run2_2017_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',35])
# # masses_FullRun2_CombinedTraining_2017.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_Run2_2017_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',45])
# # masses_FullRun2_CombinedTraining_2017.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_Run2_2017_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',60])
# #
# # masses_FullRun2_CombinedTraining_2018 = []
# # masses_FullRun2_CombinedTraining_2018.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_Run2_2018_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',15])
# # masses_FullRun2_CombinedTraining_2018.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_Run2_2018_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',25])
# # masses_FullRun2_CombinedTraining_2018.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_Run2_2018_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',35])
# # masses_FullRun2_CombinedTraining_2018.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_Run2_2018_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',45])
# # masses_FullRun2_CombinedTraining_2018.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_Run2_2018_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',60])
#
# masses_CombinedTraining_2016 = []
# masses_CombinedTraining_2016.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_2016_m15.AsymptoticLimits.mH125.root',15])
# masses_CombinedTraining_2016.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_2016_m25.AsymptoticLimits.mH125.root',25])
# masses_CombinedTraining_2016.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_2016_m35.AsymptoticLimits.mH125.root',35])
# masses_CombinedTraining_2016.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_2016_m45.AsymptoticLimits.mH125.root',45])
# masses_CombinedTraining_2016.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_2016_m60.AsymptoticLimits.mH125.root',60])
#
# masses_CombinedTraining_2017 = []
# masses_CombinedTraining_2017.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_2017_m15.AsymptoticLimits.mH125.root',15])
# masses_CombinedTraining_2017.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_2017_m25.AsymptoticLimits.mH125.root',25])
# masses_CombinedTraining_2017.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_2017_m35.AsymptoticLimits.mH125.root',35])
# masses_CombinedTraining_2017.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_2017_m45.AsymptoticLimits.mH125.root',45])
# masses_CombinedTraining_2017.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_2017_m60.AsymptoticLimits.mH125.root',60])
#
# masses_CombinedTraining_2018 = []
# masses_CombinedTraining_2018.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_2018_m15.AsymptoticLimits.mH125.root',15])
# masses_CombinedTraining_2018.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_2018_m25.AsymptoticLimits.mH125.root',25])
# masses_CombinedTraining_2018.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_2018_m35.AsymptoticLimits.mH125.root',35])
# masses_CombinedTraining_2018.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_2018_m45.AsymptoticLimits.mH125.root',45])
# masses_CombinedTraining_2018.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_2018_m60.AsymptoticLimits.mH125.root',60])
#
# masses_CombinedTraining_FullRun2 = []
# masses_CombinedTraining_FullRun2.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_FullRun2_m15.AsymptoticLimits.mH125.root',15])
# masses_CombinedTraining_FullRun2.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_FullRun2_m25.AsymptoticLimits.mH125.root',25])
# masses_CombinedTraining_FullRun2.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_FullRun2_m35.AsymptoticLimits.mH125.root',35])
# masses_CombinedTraining_FullRun2.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_FullRun2_m45.AsymptoticLimits.mH125.root',45])
# masses_CombinedTraining_FullRun2.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_FullRun2_m60.AsymptoticLimits.mH125.root',60])
#
# masses_CombinedTraining_FullRun2_FIX = []
# masses_CombinedTraining_FullRun2_FIX.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_FullRun2_17_09_2020_FIX_m15.AsymptoticLimits.mH125.root',15])
# masses_CombinedTraining_FullRun2_FIX.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_FullRun2_17_09_2020_FIX_m25.AsymptoticLimits.mH125.root',25])
# masses_CombinedTraining_FullRun2_FIX.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_FullRun2_17_09_2020_FIX_m35.AsymptoticLimits.mH125.root',35])
# masses_CombinedTraining_FullRun2_FIX.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_FullRun2_17_09_2020_FIX_m45.AsymptoticLimits.mH125.root',45])
# masses_CombinedTraining_FullRun2_FIX.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_FullRun2_17_09_2020_FIX_m60.AsymptoticLimits.mH125.root',60])
#
#
#
# masses_CombinedTraining_CombinedatWSLevel_FullRun2 = []
# masses_CombinedTraining_CombinedatWSLevel_FullRun2.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_CombinedatWSLevel_16_09_2020_m15.AsymptoticLimits.mH125.root',15])
# masses_CombinedTraining_CombinedatWSLevel_FullRun2.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_CombinedatWSLevel_16_09_2020_m25.AsymptoticLimits.mH125.root',25])
# masses_CombinedTraining_CombinedatWSLevel_FullRun2.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_CombinedatWSLevel_16_09_2020_m35.AsymptoticLimits.mH125.root',35])
# masses_CombinedTraining_CombinedatWSLevel_FullRun2.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_CombinedatWSLevel_16_09_2020_m45.AsymptoticLimits.mH125.root',45])
# masses_CombinedTraining_CombinedatWSLevel_FullRun2.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_CombinedatWSLevel_16_09_2020_m60.AsymptoticLimits.mH125.root',60])
#
# masses_CombinedTraining_CombinedatWSLevel_FullRun2_RateParamFix = []
# masses_CombinedTraining_CombinedatWSLevel_FullRun2_RateParamFix.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_CombinedatWSLevel_17_09_2020_RateParamFIX_m15.AsymptoticLimits.mH125.root',15])
# masses_CombinedTraining_CombinedatWSLevel_FullRun2_RateParamFix.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_CombinedatWSLevel_17_09_2020_RateParamFIX_m25.AsymptoticLimits.mH125.root',25])
# masses_CombinedTraining_CombinedatWSLevel_FullRun2_RateParamFix.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_CombinedatWSLevel_17_09_2020_RateParamFIX_m35.AsymptoticLimits.mH125.root',35])
# masses_CombinedTraining_CombinedatWSLevel_FullRun2_RateParamFix.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_CombinedatWSLevel_17_09_2020_RateParamFIX_m45.AsymptoticLimits.mH125.root',45])
# masses_CombinedTraining_CombinedatWSLevel_FullRun2_RateParamFix.append(['/afs/cern.ch/work/t/twamorka/flashgg_16aug2020/CMSSW_10_2_13/src/flashggFinalFit/Datacard/higgsCombineCombinedMassTraining_peryear_CombinedatWSLevel_17_09_2020_RateParamFIX_m60.AsymptoticLimits.mH125.root',60])
#
# # masses_FullRun2_CombinedTraining_CombinedYear = []
# # masses_FullRun2_CombinedTraining_CombinedYear.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_Run2_CombinedYear_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',15])
# # masses_FullRun2_CombinedTraining_CombinedYear.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_Run2_CombinedYear_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',25])
# # masses_FullRun2_CombinedTraining_CombinedYear.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_Run2_CombinedYear_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',35])
# # masses_FullRun2_CombinedTraining_CombinedYear.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_Run2_CombinedYear_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',45])
# # masses_FullRun2_CombinedTraining_CombinedYear.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_Run2_CombinedYear_minEvents8_5_bdtTransformed.AsymptoticLimits.mH125.root',60])
#
# # masses_2016_Only_Min6Events = []
# # masses_2016_Only_Min6Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_PhoMVA_KinVars_v2_2016_minEvents6_bdt_1Cat.AsymptoticLimits.mH125.root',15])
# # masses_2016_Only_Min6Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_PhoMVA_KinVars_v2_2016_minEvents6_bdt_1Cat.AsymptoticLimits.mH125.root',25])
# # masses_2016_Only_Min6Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_PhoMVA_KinVars_v2_2016_minEvents6_bdt_1Cat.AsymptoticLimits.mH125.root',35])
# # masses_2016_Only_Min6Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_PhoMVA_KinVars_v2_2016_minEvents6_bdt_1Cat.AsymptoticLimits.mH125.root',45])
# # masses_2016_Only_Min6Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_PhoMVA_KinVars_v2_2016_minEvents6_bdt_1Cat.AsymptoticLimits.mH125.root',60])
# #
# # masses_2017_Only_Min6Events = []
# # masses_2017_Only_Min6Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_PhoMVA_KinVars_v2_2017_minEvents6_bdt_1Cat.AsymptoticLimits.mH125.root',15])
# # masses_2017_Only_Min6Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_PhoMVA_KinVars_v2_2017_minEvents6_bdt_1Cat.AsymptoticLimits.mH125.root',25])
# # masses_2017_Only_Min6Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_PhoMVA_KinVars_v2_2017_minEvents6_bdt_1Cat.AsymptoticLimits.mH125.root',35])
# # masses_2017_Only_Min6Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_PhoMVA_KinVars_v2_2017_minEvents6_bdt_1Cat.AsymptoticLimits.mH125.root',45])
# # masses_2017_Only_Min6Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_PhoMVA_KinVars_v2_2017_minEvents6_bdt_1Cat.AsymptoticLimits.mH125.root',60])
# #
# # masses_2018_Only_Min6Events = []
# # masses_2018_Only_Min6Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_PhoMVA_KinVars_v2_2018_minEvents6_bdt_1Cat.AsymptoticLimits.mH125.root',15])
# # masses_2018_Only_Min6Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_PhoMVA_KinVars_v2_2018_minEvents6_bdt_1Cat.AsymptoticLimits.mH125.root',25])
# # masses_2018_Only_Min6Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_PhoMVA_KinVars_v2_2018_minEvents6_bdt_1Cat.AsymptoticLimits.mH125.root',35])
# # masses_2018_Only_Min6Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_PhoMVA_KinVars_v2_2018_minEvents6_bdt_1Cat.AsymptoticLimits.mH125.root',45])
# # masses_2018_Only_Min6Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_PhoMVA_KinVars_v2_2018_minEvents6_bdt_1Cat.AsymptoticLimits.mH125.root',60])
# #
# #
# # masses_2016_Only_Min10Events = []
# # masses_2016_Only_Min10Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_PhoMVA_KinVars_v2_2016_minEvents10_bdt_1Cat.AsymptoticLimits.mH125.root',15])
# # masses_2016_Only_Min10Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_PhoMVA_KinVars_v2_2016_minEvents10_bdt_1Cat.AsymptoticLimits.mH125.root',25])
# # masses_2016_Only_Min10Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_PhoMVA_KinVars_v2_2016_minEvents10_bdt_1Cat.AsymptoticLimits.mH125.root',35])
# # masses_2016_Only_Min10Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_PhoMVA_KinVars_v2_2016_minEvents10_bdt_1Cat.AsymptoticLimits.mH125.root',45])
# # masses_2016_Only_Min10Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_PhoMVA_KinVars_v2_2016_minEvents10_bdt_1Cat.AsymptoticLimits.mH125.root',60])
# #
# # masses_2017_Only_Min10Events = []
# # masses_2017_Only_Min10Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_PhoMVA_KinVars_v2_2017_minEvents10_bdt_1Cat.AsymptoticLimits.mH125.root',15])
# # masses_2017_Only_Min10Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_PhoMVA_KinVars_v2_2017_minEvents10_bdt_1Cat.AsymptoticLimits.mH125.root',25])
# # masses_2017_Only_Min10Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_PhoMVA_KinVars_v2_2017_minEvents10_bdt_1Cat.AsymptoticLimits.mH125.root',35])
# # masses_2017_Only_Min10Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_PhoMVA_KinVars_v2_2017_minEvents10_bdt_1Cat.AsymptoticLimits.mH125.root',45])
# # masses_2017_Only_Min10Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_PhoMVA_KinVars_v2_2017_minEvents10_bdt_1Cat.AsymptoticLimits.mH125.root',60])
# #
# # masses_2018_Only_Min10Events = []
# # masses_2018_Only_Min10Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_PhoMVA_KinVars_v2_2018_minEvents10_bdt_1Cat.AsymptoticLimits.mH125.root',15])
# # masses_2018_Only_Min10Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_PhoMVA_KinVars_v2_2018_minEvents10_bdt_1Cat.AsymptoticLimits.mH125.root',25])
# # masses_2018_Only_Min10Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_PhoMVA_KinVars_v2_2018_minEvents10_bdt_1Cat.AsymptoticLimits.mH125.root',35])
# # masses_2018_Only_Min10Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_PhoMVA_KinVars_v2_2018_minEvents10_bdt_1Cat.AsymptoticLimits.mH125.root',45])
# # masses_2018_Only_Min10Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_PhoMVA_KinVars_v2_2018_minEvents10_bdt_1Cat.AsymptoticLimits.mH125.root',60])
# #
# #
# # masses_FullRun2_Min6Events = []
# # masses_FullRun2_Min6Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_PhoMVA_KinVars_v2_minEvents6_bdt_1Cat.AsymptoticLimits.mH125.root',15])
# # masses_FullRun2_Min6Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_PhoMVA_KinVars_v2_minEvents6_bdt_1Cat.AsymptoticLimits.mH125.root',25])
# # masses_FullRun2_Min6Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_PhoMVA_KinVars_v2_minEvents6_bdt_1Cat.AsymptoticLimits.mH125.root',35])
# # masses_FullRun2_Min6Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_PhoMVA_KinVars_v2_minEvents6_bdt_1Cat.AsymptoticLimits.mH125.root',45])
# # masses_FullRun2_Min6Events .append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_PhoMVA_KinVars_v2_minEvents6_bdt_1Cat.AsymptoticLimits.mH125.root',60])
# #
# #
# #
# #
# #
# #
# # masses_PhoMVA_Only_cat2 = []
# # masses_PhoMVA_Only_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m10_PhoMVA_Only_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',10])
# # masses_PhoMVA_Only_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_PhoMVA_Only_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',15])
# # masses_PhoMVA_Only_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_PhoMVA_Only_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',20])
# # masses_PhoMVA_Only_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_PhoMVA_Only_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',25])
# # masses_PhoMVA_Only_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_PhoMVA_Only_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',30])
# # masses_PhoMVA_Only_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_PhoMVA_Only_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',35])
# # masses_PhoMVA_Only_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_PhoMVA_Only_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',40])
# # masses_PhoMVA_Only_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_PhoMVA_Only_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',45])
# # masses_PhoMVA_Only_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_PhoMVA_Only_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',50])
# # masses_PhoMVA_Only_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_PhoMVA_Only_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',55])
# # masses_PhoMVA_Only_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_PhoMVA_Only_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',60])
# #
# # masses_PhoMVA_Only_cat3 = []
# # masses_PhoMVA_Only_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m10_PhoMVA_Only_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',10])
# # masses_PhoMVA_Only_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_PhoMVA_Only_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',15])
# # masses_PhoMVA_Only_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_PhoMVA_Only_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',20])
# # masses_PhoMVA_Only_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_PhoMVA_Only_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',25])
# # masses_PhoMVA_Only_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_PhoMVA_Only_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',30])
# # masses_PhoMVA_Only_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_PhoMVA_Only_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',35])
# # masses_PhoMVA_Only_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_PhoMVA_Only_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',40])
# # masses_PhoMVA_Only_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_PhoMVA_Only_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',45])
# # masses_PhoMVA_Only_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_PhoMVA_Only_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',50])
# # masses_PhoMVA_Only_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_PhoMVA_Only_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',55])
# # masses_PhoMVA_Only_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_PhoMVA_Only_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',60])
# #
# #
# # masses_PhoMVA_Only_cat4 = []
# # masses_PhoMVA_Only_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m10_PhoMVA_Only_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',10])
# # masses_PhoMVA_Only_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_PhoMVA_Only_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',15])
# # masses_PhoMVA_Only_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_PhoMVA_Only_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',20])
# # masses_PhoMVA_Only_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_PhoMVA_Only_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',25])
# # masses_PhoMVA_Only_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_PhoMVA_Only_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',30])
# # masses_PhoMVA_Only_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_PhoMVA_Only_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',35])
# # masses_PhoMVA_Only_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_PhoMVA_Only_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',40])
# # masses_PhoMVA_Only_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_PhoMVA_Only_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',45])
# # masses_PhoMVA_Only_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_PhoMVA_Only_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',50])
# # masses_PhoMVA_Only_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_PhoMVA_Only_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',55])
# # masses_PhoMVA_Only_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_PhoMVA_Only_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',60])
# #
# #
# # masses_PhoMVA_KinVars_cat2 = []
# # masses_PhoMVA_KinVars_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m10_PhoMVA_KinVars_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',10])
# # masses_PhoMVA_KinVars_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_PhoMVA_KinVars_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',15])
# # masses_PhoMVA_KinVars_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_PhoMVA_KinVars_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',20])
# # masses_PhoMVA_KinVars_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_PhoMVA_KinVars_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',25])
# # masses_PhoMVA_KinVars_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_PhoMVA_KinVars_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',30])
# # masses_PhoMVA_KinVars_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_PhoMVA_KinVars_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',35])
# # masses_PhoMVA_KinVars_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_PhoMVA_KinVars_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',40])
# # masses_PhoMVA_KinVars_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_PhoMVA_KinVars_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',45])
# # masses_PhoMVA_KinVars_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_PhoMVA_KinVars_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',50])
# # masses_PhoMVA_KinVars_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_PhoMVA_KinVars_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',55])
# # masses_PhoMVA_KinVars_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_PhoMVA_KinVars_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',60])
# #
# # masses_PhoMVA_KinVars_cat3 = []
# # masses_PhoMVA_KinVars_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m10_PhoMVA_KinVars_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',10])
# # masses_PhoMVA_KinVars_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_PhoMVA_KinVars_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',15])
# # masses_PhoMVA_KinVars_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_PhoMVA_KinVars_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',20])
# # masses_PhoMVA_KinVars_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_PhoMVA_KinVars_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',25])
# # masses_PhoMVA_KinVars_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_PhoMVA_KinVars_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',30])
# # masses_PhoMVA_KinVars_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_PhoMVA_KinVars_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',35])
# # masses_PhoMVA_KinVars_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_PhoMVA_KinVars_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',40])
# # masses_PhoMVA_KinVars_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_PhoMVA_KinVars_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',45])
# # masses_PhoMVA_KinVars_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_PhoMVA_KinVars_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',50])
# # masses_PhoMVA_KinVars_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_PhoMVA_KinVars_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',55])
# # masses_PhoMVA_KinVars_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_PhoMVA_KinVars_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',60])
# #
# #
# # masses_PhoMVA_KinVars_cat4 = []
# # masses_PhoMVA_KinVars_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m10_PhoMVA_KinVars_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',10])
# # masses_PhoMVA_KinVars_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_PhoMVA_KinVars_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',15])
# # masses_PhoMVA_KinVars_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_PhoMVA_KinVars_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',20])
# # masses_PhoMVA_KinVars_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_PhoMVA_KinVars_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',25])
# # masses_PhoMVA_KinVars_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_PhoMVA_KinVars_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',30])
# # masses_PhoMVA_KinVars_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_PhoMVA_KinVars_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',35])
# # masses_PhoMVA_KinVars_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_PhoMVA_KinVars_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',40])
# # masses_PhoMVA_KinVars_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_PhoMVA_KinVars_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',45])
# # masses_PhoMVA_KinVars_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_PhoMVA_KinVars_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',50])
# # masses_PhoMVA_KinVars_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_PhoMVA_KinVars_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',55])
# # masses_PhoMVA_KinVars_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_PhoMVA_KinVars_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',60])
# #
# #
# # masses_PhoMVA_KinVars_Many_cat2 = []
# # masses_PhoMVA_KinVars_Many_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m10_PhoMVA_KinVars_Many_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',10])
# # masses_PhoMVA_KinVars_Many_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_PhoMVA_KinVars_Many_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',15])
# # masses_PhoMVA_KinVars_Many_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_PhoMVA_KinVars_Many_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',20])
# # masses_PhoMVA_KinVars_Many_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_PhoMVA_KinVars_Many_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',25])
# # masses_PhoMVA_KinVars_Many_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_PhoMVA_KinVars_Many_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',30])
# # masses_PhoMVA_KinVars_Many_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_PhoMVA_KinVars_Many_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',35])
# # masses_PhoMVA_KinVars_Many_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_PhoMVA_KinVars_Many_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',40])
# # masses_PhoMVA_KinVars_Many_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_PhoMVA_KinVars_Many_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',45])
# # masses_PhoMVA_KinVars_Many_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_PhoMVA_KinVars_Many_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',50])
# # masses_PhoMVA_KinVars_Many_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_PhoMVA_KinVars_Many_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',55])
# # masses_PhoMVA_KinVars_Many_cat2.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_PhoMVA_KinVars_Many_cat2_minEvents6_bdt.AsymptoticLimits.mH125.root',60])
# #
# # masses_PhoMVA_KinVars_Many_cat3 = []
# # masses_PhoMVA_KinVars_Many_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m10_PhoMVA_KinVars_Many_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',10])
# # masses_PhoMVA_KinVars_Many_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_PhoMVA_KinVars_Many_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',15])
# # masses_PhoMVA_KinVars_Many_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_PhoMVA_KinVars_Many_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',20])
# # masses_PhoMVA_KinVars_Many_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_PhoMVA_KinVars_Many_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',25])
# # masses_PhoMVA_KinVars_Many_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_PhoMVA_KinVars_Many_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',30])
# # masses_PhoMVA_KinVars_Many_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_PhoMVA_KinVars_Many_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',35])
# # masses_PhoMVA_KinVars_Many_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_PhoMVA_KinVars_Many_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',40])
# # masses_PhoMVA_KinVars_Many_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_PhoMVA_KinVars_Many_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',45])
# # masses_PhoMVA_KinVars_Many_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_PhoMVA_KinVars_Many_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',50])
# # masses_PhoMVA_KinVars_Many_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_PhoMVA_KinVars_Many_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',55])
# # masses_PhoMVA_KinVars_Many_cat3.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_PhoMVA_KinVars_Many_cat3_minEvents6_bdt.AsymptoticLimits.mH125.root',60])
# #
# #
# # masses_PhoMVA_KinVars_Many_cat4 = []
# # masses_PhoMVA_KinVars_Many_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m10_PhoMVA_KinVars_Many_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',10])
# # masses_PhoMVA_KinVars_Many_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_PhoMVA_KinVars_Many_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',15])
# # masses_PhoMVA_KinVars_Many_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_PhoMVA_KinVars_Many_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',20])
# # masses_PhoMVA_KinVars_Many_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_PhoMVA_KinVars_Many_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',25])
# # masses_PhoMVA_KinVars_Many_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_PhoMVA_KinVars_Many_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',30])
# # masses_PhoMVA_KinVars_Many_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_PhoMVA_KinVars_Many_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',35])
# # masses_PhoMVA_KinVars_Many_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_PhoMVA_KinVars_Many_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',40])
# # masses_PhoMVA_KinVars_Many_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_PhoMVA_KinVars_Many_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',45])
# # masses_PhoMVA_KinVars_Many_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_PhoMVA_KinVars_Many_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',50])
# # masses_PhoMVA_KinVars_Many_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_PhoMVA_KinVars_Many_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',55])
# # masses_PhoMVA_KinVars_Many_cat4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_PhoMVA_KinVars_Many_cat4_minEvents6_bdt.AsymptoticLimits.mH125.root',60])
# #
# #
# #
# # masses_PhoMVA_KinVars = []
# # masses_PhoMVA_KinVars.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m10_NCat2_PhoMVA_KinVars.AsymptoticLimits.mH125',10])
# # masses_PhoMVA_KinVars.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_NCat2_PhoMVA_KinVars.AsymptoticLimits.mH125',15])
# # masses_PhoMVA_KinVars.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_NCat2_PhoMVA_KinVars.AsymptoticLimits.mH125',20])
# # masses_PhoMVA_KinVars.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_NCat2_PhoMVA_KinVars.AsymptoticLimits.mH125',25])
# # masses_PhoMVA_KinVars.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_NCat2_PhoMVA_KinVars.AsymptoticLimits.mH125',30])
# # masses_PhoMVA_KinVars.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_NCat2_PhoMVA_KinVars.AsymptoticLimits.mH125',35])
# # masses_PhoMVA_KinVars.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_NCat2_PhoMVA_KinVars.AsymptoticLimits.mH125',40])
# # masses_PhoMVA_KinVars.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_NCat2_PhoMVA_KinVars.AsymptoticLimits.mH125',45])
# # masses_PhoMVA_KinVars.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_NCat2_PhoMVA_KinVars.AsymptoticLimits.mH125',50])
# # masses_PhoMVA_KinVars.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_NCat2_PhoMVA_KinVars.AsymptoticLimits.mH125',55])
# # masses_PhoMVA_KinVars.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_NCat2_PhoMVA_KinVars.AsymptoticLimits.mH125',60])
# #
# # masses_PhoMVA_KinVars_Many = []
# # masses_PhoMVA_KinVars_Many.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m10_NCat2_PhoMVA_KinVars_Many.AsymptoticLimits.mH125',10])
# # masses_PhoMVA_KinVars_Many.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_NCat2_PhoMVA_KinVars_Many.AsymptoticLimits.mH125',15])
# # masses_PhoMVA_KinVars_Many.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_NCat2_PhoMVA_KinVars_Many.AsymptoticLimits.mH125',20])
# # masses_PhoMVA_KinVars_Many.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_NCat2_PhoMVA_KinVars_Many.AsymptoticLimits.mH125',25])
# # masses_PhoMVA_KinVars_Many.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_NCat2_PhoMVA_KinVars_Many.AsymptoticLimits.mH125',30])
# # masses_PhoMVA_KinVars_Many.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_NCat2_PhoMVA_KinVars_Many.AsymptoticLimits.mH125',35])
# # masses_PhoMVA_KinVars_Many.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_NCat2_PhoMVA_KinVars_Many.AsymptoticLimits.mH125',40])
# # masses_PhoMVA_KinVars_Many.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_NCat2_PhoMVA_KinVars_Many.AsymptoticLimits.mH125',45])
# # masses_PhoMVA_KinVars_Many.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_NCat2_PhoMVA_KinVars_Many.AsymptoticLimits.mH125',50])
# # masses_PhoMVA_KinVars_Many.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_NCat2_PhoMVA_KinVars_Many.AsymptoticLimits.mH125',55])
# # masses_PhoMVA_KinVars_Many.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_NCat2_PhoMVA_KinVars_Many.AsymptoticLimits.mH125',60])
# #
# # masses_PhoMVA_Only_noBlind = []
# # masses_PhoMVA_Only_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m10_NCat2_PhoMVA_Only_noBlind.AsymptoticLimits.mH125',10])
# # masses_PhoMVA_Only_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_NCat2_PhoMVA_Only_noBlind.AsymptoticLimits.mH125',15])
# # masses_PhoMVA_Only_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_NCat2_PhoMVA_Only_noBlind.AsymptoticLimits.mH125',20])
# # masses_PhoMVA_Only_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_NCat2_PhoMVA_Only_noBlind.AsymptoticLimits.mH125',25])
# # masses_PhoMVA_Only_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_NCat2_PhoMVA_Only_noBlind.AsymptoticLimits.mH125',30])
# # masses_PhoMVA_Only_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_NCat2_PhoMVA_Only_noBlind.AsymptoticLimits.mH125',35])
# # masses_PhoMVA_Only_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_NCat2_PhoMVA_Only_noBlind.AsymptoticLimits.mH125',40])
# # masses_PhoMVA_Only_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_NCat2_PhoMVA_Only_noBlind.AsymptoticLimits.mH125',45])
# # masses_PhoMVA_Only_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_NCat2_PhoMVA_Only_noBlind.AsymptoticLimits.mH125',50])
# # masses_PhoMVA_Only_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_NCat2_PhoMVA_Only_noBlind.AsymptoticLimits.mH125',55])
# # masses_PhoMVA_Only_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_NCat2_PhoMVA_Only_noBlind.AsymptoticLimits.mH125',60])
# #
# # masses_PhoMVA_KinVars_noBlind = []
# # masses_PhoMVA_KinVars_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m10_NCat2_PhoMVA_KinVars_noBlind.AsymptoticLimits.mH125',10])
# # masses_PhoMVA_KinVars_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_NCat2_PhoMVA_KinVars_noBlind.AsymptoticLimits.mH125',15])
# # masses_PhoMVA_KinVars_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_NCat2_PhoMVA_KinVars_noBlind.AsymptoticLimits.mH125',20])
# # masses_PhoMVA_KinVars_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_NCat2_PhoMVA_KinVars_noBlind.AsymptoticLimits.mH125',25])
# # masses_PhoMVA_KinVars_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_NCat2_PhoMVA_KinVars_noBlind.AsymptoticLimits.mH125',30])
# # masses_PhoMVA_KinVars_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_NCat2_PhoMVA_KinVars_noBlind.AsymptoticLimits.mH125',35])
# # masses_PhoMVA_KinVars_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_NCat2_PhoMVA_KinVars_noBlind.AsymptoticLimits.mH125',40])
# # masses_PhoMVA_KinVars_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_NCat2_PhoMVA_KinVars_noBlind.AsymptoticLimits.mH125',45])
# # masses_PhoMVA_KinVars_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_NCat2_PhoMVA_KinVars_noBlind.AsymptoticLimits.mH125',50])
# # masses_PhoMVA_KinVars_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_NCat2_PhoMVA_KinVars_noBlind.AsymptoticLimits.mH125',55])
# # masses_PhoMVA_KinVars_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_NCat2_PhoMVA_KinVars_noBlind.AsymptoticLimits.mH125',60])
# #
# # masses_PhoMVA_KinVars_Many_noBlind = []
# # masses_PhoMVA_KinVars_Many_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m10_NCat2_PhoMVA_KinVars_Many_noBlind.AsymptoticLimits.mH125',10])
# # masses_PhoMVA_KinVars_Many_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_NCat2_PhoMVA_KinVars_Many_noBlind.AsymptoticLimits.mH125',15])
# # masses_PhoMVA_KinVars_Many_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_NCat2_PhoMVA_KinVars_Many_noBlind.AsymptoticLimits.mH125',20])
# # masses_PhoMVA_KinVars_Many_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_NCat2_PhoMVA_KinVars_Many_noBlind.AsymptoticLimits.mH125',25])
# # masses_PhoMVA_KinVars_Many_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_NCat2_PhoMVA_KinVars_Many_noBlind.AsymptoticLimits.mH125',30])
# # masses_PhoMVA_KinVars_Many_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_NCat2_PhoMVA_KinVars_Many_noBlind.AsymptoticLimits.mH125',35])
# # masses_PhoMVA_KinVars_Many_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_NCat2_PhoMVA_KinVars_Many_noBlind.AsymptoticLimits.mH125',40])
# # masses_PhoMVA_KinVars_Many_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_NCat2_PhoMVA_KinVars_Many_noBlind.AsymptoticLimits.mH125',45])
# # masses_PhoMVA_KinVars_Many_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_NCat2_PhoMVA_KinVars_Many_noBlind.AsymptoticLimits.mH125',50])
# # masses_PhoMVA_KinVars_Many_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_NCat2_PhoMVA_KinVars_Many_noBlind.AsymptoticLimits.mH125',55])
# # masses_PhoMVA_KinVars_Many_noBlind.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_NCat2_PhoMVA_KinVars_Many_noBlind.AsymptoticLimits.mH125',60])
# #
# #
# # masses = []
# # masses.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_CombinedTraining_phoMVA_vLooseMVACut.AsymptoticLimits.mH125.root',15])
# # masses.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_CombinedTraining_phoMVA_vLooseMVACut.AsymptoticLimits.mH125.root',20])
# # masses.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_CombinedTraining_phoMVA_vLooseMVACut.AsymptoticLimits.mH125.root',25])
# # masses.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_CombinedTraining_phoMVA_vLooseMVACut.AsymptoticLimits.mH125.root',30])
# # masses.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_CombinedTraining_phoMVA_vLooseMVACut.AsymptoticLimits.mH125.root',35])
# # masses.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_CombinedTraining_phoMVA_vLooseMVACut.AsymptoticLimits.mH125.root',40])
# # masses.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_CombinedTraining_phoMVA_vLooseMVACut.AsymptoticLimits.mH125.root',45])
# # masses.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_CombinedTraining_phoMVA_vLooseMVACut.AsymptoticLimits.mH125.root',50])
# # masses.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_CombinedTraining_phoMVA_vLooseMVACut.AsymptoticLimits.mH125.root',55])
# # masses.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_CombinedTraining_phoMVA_vLooseMVACut.AsymptoticLimits.mH125.root',60])
# #
# #
# # masses_compare = []
# # masses_compare.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_CutBased_Common.AsymptoticLimits.mH125.root',15])
# # masses_compare.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_CutBased_Common.AsymptoticLimits.mH125.root',20])
# # masses_compare.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_CutBased_Common.AsymptoticLimits.mH125.root',25])
# # masses_compare.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_CutBased_Common.AsymptoticLimits.mH125.root',30])
# # masses_compare.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_CutBased_Common.AsymptoticLimits.mH125.root',35])
# # masses_compare.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_CutBased_Common.AsymptoticLimits.mH125.root',40])
# # masses_compare.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_CutBased_Common.AsymptoticLimits.mH125.root',45])
# # masses_compare.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_CutBased_Common.AsymptoticLimits.mH125.root',50])
# # masses_compare.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_CutBased_Common.AsymptoticLimits.mH125.root',55])
# # masses_compare.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_CutBased_Common.AsymptoticLimits.mH125.root',60])
# #
# # masses_cb_zerovtx = []
# # masses_cb_zerovtx.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_CutBased_ZeroVtx.AsymptoticLimits.mH125.root',15])
# # masses_cb_zerovtx.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_CutBased_ZeroVtx.AsymptoticLimits.mH125.root',20])
# # masses_cb_zerovtx.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_CutBased_ZeroVtx.AsymptoticLimits.mH125.root',25])
# # masses_cb_zerovtx.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_CutBased_ZeroVtx.AsymptoticLimits.mH125.root',30])
# # masses_cb_zerovtx.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_CutBased_ZeroVtx.AsymptoticLimits.mH125.root',35])
# # masses_cb_zerovtx.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_CutBased_ZeroVtx.AsymptoticLimits.mH125.root',40])
# # masses_cb_zerovtx.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_CutBased_ZeroVtx.AsymptoticLimits.mH125.root',45])
# # masses_cb_zerovtx.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_CutBased_ZeroVtx.AsymptoticLimits.mH125.root',50])
# # masses_cb_zerovtx.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_CutBased_ZeroVtx.AsymptoticLimits.mH125.root',55])
# # masses_cb_zerovtx.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_CutBased_ZeroVtx.AsymptoticLimits.mH125.root',60])
# #
# #
# #
# # masses_zerovtx = []
# # masses_zerovtx.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_CombinedTraining_phoMVA_vLooseMVACut_ZeroVtx.AsymptoticLimits.mH125.root',15])
# # masses_zerovtx.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_CombinedTraining_phoMVA_vLooseMVACut_ZeroVtx.AsymptoticLimits.mH125.root',20])
# # masses_zerovtx.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_CombinedTraining_phoMVA_vLooseMVACut_ZeroVtx.AsymptoticLimits.mH125.root',25])
# # masses_zerovtx.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_CombinedTraining_phoMVA_vLooseMVACut_ZeroVtx.AsymptoticLimits.mH125.root',30])
# # masses_zerovtx.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_CombinedTraining_phoMVA_vLooseMVACut_ZeroVtx.AsymptoticLimits.mH125.root',35])
# # masses_zerovtx.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_CombinedTraining_phoMVA_vLooseMVACut_ZeroVtx.AsymptoticLimits.mH125.root',40])
# # masses_zerovtx.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_CombinedTraining_phoMVA_vLooseMVACut_ZeroVtx.AsymptoticLimits.mH125.root',45])
# # masses_zerovtx.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_CombinedTraining_phoMVA_vLooseMVACut_ZeroVtx.AsymptoticLimits.mH125.root',50])
# # masses_zerovtx.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_CombinedTraining_phoMVA_vLooseMVACut_ZeroVtx.AsymptoticLimits.mH125.root',55])
# # masses_zerovtx.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_CombinedTraining_phoMVA_vLooseMVACut_ZeroVtx.AsymptoticLimits.mH125.root',60])
# #
# # masses_3Events = []
# # masses_3Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_CombinedTraining_phoMVA_vLooseMVACut_3Events.AsymptoticLimits.mH125.root',15])
# # masses_3Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_CombinedTraining_phoMVA_vLooseMVACut_3Events.AsymptoticLimits.mH125.root',20])
# # masses_3Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_CombinedTraining_phoMVA_vLooseMVACut_3Events.AsymptoticLimits.mH125.root',25])
# # masses_3Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_CombinedTraining_phoMVA_vLooseMVACut_3Events.AsymptoticLimits.mH125.root',30])
# # masses_3Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_CombinedTraining_phoMVA_vLooseMVACut_3Events.AsymptoticLimits.mH125.root',35])
# # masses_3Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_CombinedTraining_phoMVA_vLooseMVACut_3Events.AsymptoticLimits.mH125.root',40])
# # masses_3Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_CombinedTraining_phoMVA_vLooseMVACut_3Events.AsymptoticLimits.mH125.root',45])
# # masses_3Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_CombinedTraining_phoMVA_vLooseMVACut_3Events.AsymptoticLimits.mH125.root',50])
# # masses_3Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_CombinedTraining_phoMVA_vLooseMVACut_3Events.AsymptoticLimits.mH125.root',55])
# # masses_3Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_CombinedTraining_phoMVA_vLooseMVACut_3Events.AsymptoticLimits.mH125.root',60])
# #
# # masses_2Events = []
# # masses_2Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_CombinedTraining_phoMVA_vLooseMVACut_2Events.AsymptoticLimits.mH125.root',15])
# # masses_2Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_CombinedTraining_phoMVA_vLooseMVACut_2Events.AsymptoticLimits.mH125.root',20])
# # masses_2Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_CombinedTraining_phoMVA_vLooseMVACut_2Events.AsymptoticLimits.mH125.root',25])
# # masses_2Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_CombinedTraining_phoMVA_vLooseMVACut_2Events.AsymptoticLimits.mH125.root',30])
# # masses_2Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_CombinedTraining_phoMVA_vLooseMVACut_2Events.AsymptoticLimits.mH125.root',35])
# # masses_2Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_CombinedTraining_phoMVA_vLooseMVACut_2Events.AsymptoticLimits.mH125.root',40])
# # masses_2Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_CombinedTraining_phoMVA_vLooseMVACut_2Events.AsymptoticLimits.mH125.root',45])
# # masses_2Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_CombinedTraining_phoMVA_vLooseMVACut_2Events.AsymptoticLimits.mH125.root',50])
# # masses_2Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_CombinedTraining_phoMVA_vLooseMVACut_2Events.AsymptoticLimits.mH125.root',55])
# # masses_2Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_CombinedTraining_phoMVA_vLooseMVACut_2Events.AsymptoticLimits.mH125.root',60])
# #
# #
# # masses_5Events = []
# # masses_5Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_CombinedTraining_phoMVA_vLooseMVACut_5Events.AsymptoticLimits.mH125.root',15])
# # masses_5Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_CombinedTraining_phoMVA_vLooseMVACut_5Events.AsymptoticLimits.mH125.root',20])
# # masses_5Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_CombinedTraining_phoMVA_vLooseMVACut_5Events.AsymptoticLimits.mH125.root',25])
# # masses_5Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_CombinedTraining_phoMVA_vLooseMVACut_5Events.AsymptoticLimits.mH125.root',30])
# # masses_5Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_CombinedTraining_phoMVA_vLooseMVACut_5Events.AsymptoticLimits.mH125.root',35])
# # masses_5Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_CombinedTraining_phoMVA_vLooseMVACut_5Events.AsymptoticLimits.mH125.root',40])
# # masses_5Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_CombinedTraining_phoMVA_vLooseMVACut_5Events.AsymptoticLimits.mH125.root',45])
# # masses_5Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_CombinedTraining_phoMVA_vLooseMVACut_5Events.AsymptoticLimits.mH125.root',50])
# # masses_5Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_CombinedTraining_phoMVA_vLooseMVACut_5Events.AsymptoticLimits.mH125.root',55])
# # masses_5Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_CombinedTraining_phoMVA_vLooseMVACut_5Events.AsymptoticLimits.mH125.root',60])
# #
# # masses_9Events = []
# # masses_9Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_CombinedTraining_phoMVA_vLooseMVACut_9Events.AsymptoticLimits.mH125.root',15])
# # masses_9Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_CombinedTraining_phoMVA_vLooseMVACut_9Events.AsymptoticLimits.mH125.root',20])
# # masses_9Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_CombinedTraining_phoMVA_vLooseMVACut_9Events.AsymptoticLimits.mH125.root',25])
# # masses_9Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_CombinedTraining_phoMVA_vLooseMVACut_9Events.AsymptoticLimits.mH125.root',30])
# # masses_9Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_CombinedTraining_phoMVA_vLooseMVACut_9Events.AsymptoticLimits.mH125.root',35])
# # masses_9Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_CombinedTraining_phoMVA_vLooseMVACut_9Events.AsymptoticLimits.mH125.root',40])
# # masses_9Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_CombinedTraining_phoMVA_vLooseMVACut_9Events.AsymptoticLimits.mH125.root',45])
# # masses_9Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_CombinedTraining_phoMVA_vLooseMVACut_9Events.AsymptoticLimits.mH125.root',50])
# # masses_9Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_CombinedTraining_phoMVA_vLooseMVACut_9Events.AsymptoticLimits.mH125.root',55])
# # masses_9Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_CombinedTraining_phoMVA_vLooseMVACut_9Events.AsymptoticLimits.mH125.root',60])
# #
# # masses_6Events = []
# # masses_6Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_CombinedTraining_phoMVA_vLooseMVACut_6Events.AsymptoticLimits.mH125.root',15])
# # masses_6Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_CombinedTraining_phoMVA_vLooseMVACut_6Events.AsymptoticLimits.mH125.root',20])
# # masses_6Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_CombinedTraining_phoMVA_vLooseMVACut_6Events.AsymptoticLimits.mH125.root',25])
# # masses_6Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_CombinedTraining_phoMVA_vLooseMVACut_6Events.AsymptoticLimits.mH125.root',30])
# # masses_6Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_CombinedTraining_phoMVA_vLooseMVACut_6Events.AsymptoticLimits.mH125.root',35])
# # masses_6Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_CombinedTraining_phoMVA_vLooseMVACut_6Events.AsymptoticLimits.mH125.root',40])
# # masses_6Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_CombinedTraining_phoMVA_vLooseMVACut_6Events.AsymptoticLimits.mH125.root',45])
# # masses_6Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_CombinedTraining_phoMVA_vLooseMVACut_6Events.AsymptoticLimits.mH125.root',50])
# # masses_6Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_CombinedTraining_phoMVA_vLooseMVACut_6Events.AsymptoticLimits.mH125.root',55])
# # masses_6Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_CombinedTraining_phoMVA_vLooseMVACut_6Events.AsymptoticLimits.mH125.root',60])
# #
# # masses_7Events = []
# # masses_7Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_CombinedTraining_phoMVA_vLooseMVACut_7Events.AsymptoticLimits.mH125.root',15])
# # masses_7Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_CombinedTraining_phoMVA_vLooseMVACut_7Events.AsymptoticLimits.mH125.root',20])
# # masses_7Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_CombinedTraining_phoMVA_vLooseMVACut_7Events.AsymptoticLimits.mH125.root',25])
# # masses_7Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_CombinedTraining_phoMVA_vLooseMVACut_7Events.AsymptoticLimits.mH125.root',30])
# # masses_7Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_CombinedTraining_phoMVA_vLooseMVACut_7Events.AsymptoticLimits.mH125.root',35])
# # masses_7Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_CombinedTraining_phoMVA_vLooseMVACut_7Events.AsymptoticLimits.mH125.root',40])
# # masses_7Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_CombinedTraining_phoMVA_vLooseMVACut_7Events.AsymptoticLimits.mH125.root',45])
# # masses_7Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_CombinedTraining_phoMVA_vLooseMVACut_7Events.AsymptoticLimits.mH125.root',50])
# # masses_7Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_CombinedTraining_phoMVA_vLooseMVACut_7Events.AsymptoticLimits.mH125.root',55])
# # masses_7Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_CombinedTraining_phoMVA_vLooseMVACut_7Events.AsymptoticLimits.mH125.root',60])
# #
# # masses_8Events = []
# # masses_8Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_CombinedTraining_phoMVA_vLooseMVACut_8Events.AsymptoticLimits.mH125.root',15])
# # masses_8Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_CombinedTraining_phoMVA_vLooseMVACut_8Events.AsymptoticLimits.mH125.root',20])
# # masses_8Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_CombinedTraining_phoMVA_vLooseMVACut_8Events.AsymptoticLimits.mH125.root',25])
# # masses_8Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_CombinedTraining_phoMVA_vLooseMVACut_8Events.AsymptoticLimits.mH125.root',30])
# # masses_8Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_CombinedTraining_phoMVA_vLooseMVACut_8Events.AsymptoticLimits.mH125.root',35])
# # masses_8Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_CombinedTraining_phoMVA_vLooseMVACut_8Events.AsymptoticLimits.mH125.root',40])
# # masses_8Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_CombinedTraining_phoMVA_vLooseMVACut_8Events.AsymptoticLimits.mH125.root',45])
# # masses_8Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_CombinedTraining_phoMVA_vLooseMVACut_8Events.AsymptoticLimits.mH125.root',50])
# # masses_8Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_CombinedTraining_phoMVA_vLooseMVACut_8Events.AsymptoticLimits.mH125.root',55])
# # masses_8Events.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_CombinedTraining_phoMVA_vLooseMVACut_8Events.AsymptoticLimits.mH125.root',60])
# #
# #
# # masses_allVars_minEvt4 = []
# # # masses_allVars_minEvt4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m10_allVars_minEvt4.AsymptoticLimits.mH125.root',10])
# # masses_allVars_minEvt4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_allVars_minEvt4.AsymptoticLimits.mH125.root',15])
# # masses_allVars_minEvt4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_allVars_minEvt4.AsymptoticLimits.mH125.root',20])
# # masses_allVars_minEvt4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_allVars_minEvt4.AsymptoticLimits.mH125.root',25])
# # masses_allVars_minEvt4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_allVars_minEvt4.AsymptoticLimits.mH125.root',30])
# # masses_allVars_minEvt4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_allVars_minEvt4.AsymptoticLimits.mH125.root',35])
# # masses_allVars_minEvt4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_allVars_minEvt4.AsymptoticLimits.mH125.root',40])
# # masses_allVars_minEvt4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_allVars_minEvt4.AsymptoticLimits.mH125.root',45])
# # masses_allVars_minEvt4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_allVars_minEvt4.AsymptoticLimits.mH125.root',50])
# # masses_allVars_minEvt4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_allVars_minEvt4.AsymptoticLimits.mH125.root',55])
# # masses_allVars_minEvt4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_allVars_minEvt4.AsymptoticLimits.mH125.root',60])
# #
# # masses_allVars_minEvt5 = []
# # # masses_allVars_minEvt5.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m10_allVars_minEvt5.AsymptoticLimits.mH125.root',10])
# # masses_allVars_minEvt5.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_allVars_minEvt5.AsymptoticLimits.mH125.root',15])
# # masses_allVars_minEvt5.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_allVars_minEvt5.AsymptoticLimits.mH125.root',20])
# # masses_allVars_minEvt5.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_allVars_minEvt5.AsymptoticLimits.mH125.root',25])
# # masses_allVars_minEvt5.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_allVars_minEvt5.AsymptoticLimits.mH125.root',30])
# # masses_allVars_minEvt5.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_allVars_minEvt5.AsymptoticLimits.mH125.root',35])
# # masses_allVars_minEvt5.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_allVars_minEvt5.AsymptoticLimits.mH125.root',40])
# # masses_allVars_minEvt5.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_allVars_minEvt5.AsymptoticLimits.mH125.root',45])
# # masses_allVars_minEvt5.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_allVars_minEvt5.AsymptoticLimits.mH125.root',50])
# # masses_allVars_minEvt5.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_allVars_minEvt5.AsymptoticLimits.mH125.root',55])
# # masses_allVars_minEvt5.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_allVars_minEvt5.AsymptoticLimits.mH125.root',60])
# #
# #
# # masses_allVars_minEvt7 = []
# # # masses_allVars_minEvt7.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m10_allVars_minEvt7.AsymptoticLimits.mH125.root',10])
# # masses_allVars_minEvt7.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_allVars_minEvt7.AsymptoticLimits.mH125.root',15])
# # masses_allVars_minEvt7.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_allVars_minEvt7.AsymptoticLimits.mH125.root',20])
# # masses_allVars_minEvt7.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_allVars_minEvt7.AsymptoticLimits.mH125.root',25])
# # masses_allVars_minEvt7.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_allVars_minEvt7.AsymptoticLimits.mH125.root',30])
# # masses_allVars_minEvt7.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_allVars_minEvt7.AsymptoticLimits.mH125.root',35])
# # masses_allVars_minEvt7.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_allVars_minEvt7.AsymptoticLimits.mH125.root',40])
# # masses_allVars_minEvt7.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_allVars_minEvt7.AsymptoticLimits.mH125.root',45])
# # masses_allVars_minEvt7.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_allVars_minEvt7.AsymptoticLimits.mH125.root',50])
# # masses_allVars_minEvt7.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_allVars_minEvt7.AsymptoticLimits.mH125.root',55])
# # masses_allVars_minEvt7.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_allVars_minEvt7.AsymptoticLimits.mH125.root',60])
# #
# # masses_onlyPhoMVA_minEvt4 = []
# # # masses_onlyPhoMVA_minEvt4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m10_onlyPhoMVA_minEvt4.AsymptoticLimits.mH125.root',10])
# # masses_onlyPhoMVA_minEvt4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m15_onlyPhoMVA_minEvt4.AsymptoticLimits.mH125.root',15])
# # masses_onlyPhoMVA_minEvt4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m20_onlyPhoMVA_minEvt4.AsymptoticLimits.mH125.root',20])
# # masses_onlyPhoMVA_minEvt4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m25_onlyPhoMVA_minEvt4.AsymptoticLimits.mH125.root',25])
# # masses_onlyPhoMVA_minEvt4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m30_onlyPhoMVA_minEvt4.AsymptoticLimits.mH125.root',30])
# # masses_onlyPhoMVA_minEvt4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m35_onlyPhoMVA_minEvt4.AsymptoticLimits.mH125.root',35])
# # masses_onlyPhoMVA_minEvt4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m40_onlyPhoMVA_minEvt4.AsymptoticLimits.mH125.root',40])
# # masses_onlyPhoMVA_minEvt4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m45_onlyPhoMVA_minEvt4.AsymptoticLimits.mH125.root',45])
# # masses_onlyPhoMVA_minEvt4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m50_onlyPhoMVA_minEvt4.AsymptoticLimits.mH125.root',50])
# # masses_onlyPhoMVA_minEvt4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m55_onlyPhoMVA_minEvt4.AsymptoticLimits.mH125.root',55])
# # masses_onlyPhoMVA_minEvt4.append(['/afs/cern.ch/work/t/twamorka/5Sep2019/fits/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/higgsCombineh4g_m60_onlyPhoMVA_minEvt4.AsymptoticLimits.mH125.root',60])
W = 800
H  = 600
T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.04*W

lumi = '131.78'
